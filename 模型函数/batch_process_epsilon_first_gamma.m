function batch_process_epsilon_first_gamma()
    [filenames, pathname] = uigetfile('*.mat', '选择数据文件', 'MultiSelect', 'on');
    
    if ~iscell(filenames)
        if filenames == 0
            error('未选择文件');
        end
        filenames = {filenames};
    end
    
    n_subjects = length(filenames);
    results = struct();
    results.subject_numbers = zeros(n_subjects, 1);
    results.epsilon_values = zeros(n_subjects, 1);
    results.gamma_values = zeros(n_subjects, 1);
    results.nll_values = zeros(n_subjects, 1);
    results.filenames = filenames';
    
    for i = 1:n_subjects
        filename = filenames{i};
        subject_match = regexp(filename, 'gorilla_(\d+)', 'tokens', 'once');
        if isempty(subject_match)
            subject_number = i;
        else
            subject_number = str2double(subject_match{1});
        end
        
        try
            [epsilon, gamma, nll] = epsilon_first_gamma_estimation_internal(fullfile(pathname, filename));
            results.subject_numbers(i) = subject_number;
            results.epsilon_values(i) = epsilon;
            results.gamma_values(i) = gamma;
            results.nll_values(i) = nll;
            fprintf('被试 %d 的epsilon值为: %.4f, gamma值为: %.4f, NLL: %.2f\n', subject_number, epsilon, gamma, nll);
        catch ME
            fprintf('警告: 处理被试 %d 时出错: %s\n', subject_number, ME.message);
            results.subject_numbers(i) = subject_number;
            results.epsilon_values(i) = NaN;
            results.gamma_values(i) = NaN;
            results.nll_values(i) = NaN;
        end
    end
    
    % 保存结果
    save('epsilon_first_gamma_results.mat', 'results');
end

function [epsilon, gamma, best_nll] = epsilon_first_gamma_estimation_internal(fullpath)
    % 加载数据
    data = load(fullpath);
    dataMat = data.results.dataMat;
    n_rounds = 50;
    max_trials = 10;
    choices = nan(n_rounds, max_trials);
    feedback = nan(n_rounds, max_trials);
    
    % 提取选择和反馈数据
    for round = 1:n_rounds
        trial_choices = cell2mat(dataMat{round, 6});
        actual_trials = length(trial_choices);
        choices(round, 1:actual_trials) = trial_choices;
        
        result_matrix = cell2mat(dataMat{round, 8});
        for trial = 1:actual_trials
            choice = choices(round, trial);
            if trial == 1
                feedback(round, trial) = (result_matrix(1, 2*choice-1) == 1);
            else
                prev_correct = result_matrix(trial-1, 2*choice-1);
                curr_correct = result_matrix(trial, 2*choice-1);
                feedback(round, trial) = (curr_correct > prev_correct);
            end
        end
    end
    
    % ε-first和γ参数的似然函数
    likelihood_function = @(params) compute_epsilon_first_likelihood(params(1), params(2), choices, feedback);
    
    % 优化参数
    options = optimoptions('simulannealbnd', ...
        'Display', 'off', ...
        'InitialTemperature', 100, ...
        'ReannealInterval', 100, ...
        'MaxIterations', 1000);
    
    n_starts = 5;
    best_params = [NaN, NaN];
    best_nll = Inf;
    
    for start = 1:n_starts
        % 随机初始化epsilon和gamma
        init_epsilon = 0.1 + 0.8 * rand();
        init_gamma = 0.5 + 0.5 * rand();
        init_params = [init_epsilon, init_gamma];
        
        % 设置参数边界
        lb = [0.01, 0.5];
        ub = [0.99, 1.0];
        
        [params, fval] = simulannealbnd(likelihood_function, init_params, lb, ub, options);
        
        if fval < best_nll
            best_params = params;
            best_nll = fval;
        end
    end
    
    epsilon = best_params(1);
    gamma = best_params(2);
end

function total_ll = compute_epsilon_first_likelihood(epsilon, gamma, choices, feedback)
    total_ll = 0;
    [n_rounds, ~] = size(choices);
    
    for round = 1:n_rounds
        round_choices = choices(round, :);
        round_feedback = feedback(round, :);
        actual_trials = sum(~isnan(round_choices));
        
        if actual_trials == 0
            continue;
        end
        
        % 计算探索阶段的试次数
        explore_trials = ceil(epsilon * actual_trials);
        
        for trial = 1:actual_trials
            % ε-first模型中，判断当前是探索阶段还是利用阶段
            if trial <= explore_trials  % 探索阶段
                % 根据ε-first理论，探索阶段应该是纯随机选择
                intended_probs = [1/3, 1/3, 1/3];
            else  % 利用阶段
                % 利用阶段中，应该选择已知最优的选项
                % 通过计算每个臂到目前为止的获胜频率来确定最优选项
                arm_wins = zeros(1, 3);
                arm_plays = zeros(1, 3);
                
                for t = 1:trial-1
                    if ~isnan(round_choices(t)) && ~isnan(round_feedback(t))
                        choice = round_choices(t);
                        arm_plays(choice) = arm_plays(choice) + 1;
                        if round_feedback(t) == 1
                            arm_wins(choice) = arm_wins(choice) + 1;
                        end
                    end
                end
                
                % 根据ε-first理论，使用纯频率而不是贝叶斯估计
                win_rates = zeros(1, 3);
                for arm = 1:3
                    if arm_plays(arm) > 0
                        win_rates(arm) = arm_wins(arm) / arm_plays(arm);
                    else
                        win_rates(arm) = 0; % 未探索的臂，胜率假设为0
                    end
                end
                
                % 找出胜率最高的臂
                max_rate = max(win_rates);
                best_arms = find(win_rates == max_rate);
                
                % 如果有多个最优选项，均匀分布在这些选项上
                intended_probs = zeros(1, 3);
                intended_probs(best_arms) = 1/length(best_arms);
            end
            
            % 应用执行准确性(γ)参数
            choice_probs = gamma * intended_probs + (1-gamma) * [1/3, 1/3, 1/3];
            
            % 计算对数似然
            actual_choice = round_choices(trial);
            if ~isnan(actual_choice) && actual_choice >= 1 && actual_choice <= 3
                total_ll = total_ll - log(choice_probs(actual_choice));
            end
        end
    end
end