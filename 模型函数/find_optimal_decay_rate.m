function find_optimal_decay_rate()
    % 选择数据文件
    [filenames, pathname] = uigetfile('*.mat', '选择数据文件', 'MultiSelect', 'on');
    
    if ~iscell(filenames)
        if filenames == 0
            error('未选择文件');
        end
        filenames = {filenames};
    end
    
    % 加载所有被试数据
    fprintf('正在加载数据...\n');
    all_subjects_data = load_all_subjects_data(filenames, pathname);
    
    % 搜索最优衰减率
    fprintf('开始搜索最佳全局衰减率...\n');
    [best_decay_rate, best_total_nll, all_epsilons] = search_optimal_decay_rate(all_subjects_data);
    
    % 输出结果
    fprintf('\n===== 最终结果 =====\n');
    fprintf('全局最优衰减率: %.6f\n', best_decay_rate);
    fprintf('总负对数似然: %.2f\n\n', best_total_nll);
    
    % 保存结果
    results = struct();
    results.decay_rate = best_decay_rate;
    results.total_nll = best_total_nll;
    results.epsilons0 = all_epsilons;
    results.filenames = filenames';
    
    save('optimal_decay_results.mat', 'results');
    fprintf('结果已保存到 optimal_decay_results.mat\n');
    
    % 绘制衰减曲线图
    figure;
    trials = 1:10;
    decayed_epsilon = zeros(size(trials));
    
    % 假设平均epsilon0为0.5
    avg_epsilon0 = nanmean(all_epsilons);
    if isnan(avg_epsilon0)
        avg_epsilon0 = 0.5;
    end
    
    for i = 1:length(trials)
        decayed_epsilon(i) = max(0.001, avg_epsilon0 - best_decay_rate * trials(i));
    end
    
    plot(trials, decayed_epsilon, 'r-o', 'LineWidth', 2);
    xlabel('试次');
    ylabel('平均 Epsilon 值');
    title(sprintf('最优衰减率: %.4f', best_decay_rate));
    grid on;
    ylim([0, max(avg_epsilon0*1.1, 0.1)]);
    
    fprintf('分析完成。\n');
end
function all_data = load_all_subjects_data(filenames, pathname)
    n_subjects = length(filenames);
    all_data = cell(n_subjects, 1);
    
    for i = 1:n_subjects
        try
            data = load(fullfile(pathname, filenames{i}));
            all_data{i} = extract_subject_data(data);
            fprintf('成功加载被试数据: %s\n', filenames{i});
        catch ME
            fprintf('警告: 加载文件 %s 时出错: %s\n', filenames{i}, ME.message);
            all_data{i} = [];
        end
    end
    
    % 检查是否有成功加载的数据
    valid_data_count = sum(~cellfun(@isempty, all_data));
    if valid_data_count == 0
        error('没有成功加载任何有效数据，请检查文件格式');
    else
        fprintf('成功加载 %d/%d 个被试数据\n', valid_data_count, n_subjects);
    end
end
function subject_data = extract_subject_data(data)
    % 从原始数据中提取选择和反馈
    dataMat = data.results.dataMat;
    n_rounds = 50;
    max_trials = 10;
    choices = nan(n_rounds, max_trials);
    feedback = nan(n_rounds, max_trials);
    
    for round = 1:n_rounds
        if round <= size(dataMat, 1)  % 确保round不超过dataMat大小
            % 安全地获取选择数据
            if ~isempty(dataMat{round, 6}) && iscell(dataMat{round, 6})
                try
                    trial_choices = cell2mat(dataMat{round, 6});
                    actual_trials = length(trial_choices);
                    choices(round, 1:actual_trials) = trial_choices;
                catch
                    fprintf('警告: 处理第 %d 轮选择数据时出错\n', round);
                    continue;
                end
            else
                continue;
            end
            
            % 安全地获取结果数据
            if ~isempty(dataMat{round, 8}) && iscell(dataMat{round, 8})
                try
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
                catch
                    fprintf('警告: 处理第 %d 轮反馈数据时出错\n', round);
                end
            end
        end
    end
    
    % 检查数据有效性
    valid_choices = sum(sum(~isnan(choices)));
    if valid_choices == 0
        error('没有有效的选择数据');
    end
    
    subject_data.choices = choices;
    subject_data.feedback = feedback;
end
function [best_decay_rate, best_total_nll, all_epsilons] = search_optimal_decay_rate(all_subjects_data)
    % 使用网格搜索找到大致最优值
    decay_rates = linspace(0.0001, 0.05, 20);
    nll_values = zeros(length(decay_rates), 1);  % 确保大小正确
    
    % 显示搜索进度
    fprintf('开始网格搜索最优衰减率...\n');
    fprintf('共需测试 %d 个衰减率点\n', length(decay_rates));
    
    for i = 1:length(decay_rates)
        fprintf('测试第 %d/%d 个点, 衰减率 = %.5f: ', i, length(decay_rates), decay_rates(i));
        try
            [current_nll, ~] = compute_global_nll(decay_rates(i), all_subjects_data);
            nll_values(i) = current_nll;
            fprintf('NLL = %.2f\n', current_nll);
        catch ME
            fprintf('出错: %s\n', ME.message);
            nll_values(i) = Inf;  % 出错时将似然值设为无穷大
        end
    end
    
    % 找到有效的最小NLL值
    valid_indices = ~isinf(nll_values);
    if sum(valid_indices) == 0
        error('所有衰减率点的计算都失败了，请检查数据');
    end
    
    valid_decay_rates = decay_rates(valid_indices);
    valid_nll_values = nll_values(valid_indices);
    [~, best_idx] = min(valid_nll_values);
    initial_decay = valid_decay_rates(best_idx);
    
    fprintf('\n粗略最优衰减率: %.5f (NLL = %.2f)\n', initial_decay, valid_nll_values(best_idx));
    
    % 使用精细优化进一步优化
    fprintf('开始精细搜索...\n');
    options = optimset('Display', 'iter', 'TolX', 1e-6, 'TolFun', 1e-6);
    
    try
        [best_decay_rate, ~] = fminbnd(@(d) safe_global_nll(d, all_subjects_data), ...
                                max(0.0001, initial_decay*0.5), min(0.05, initial_decay*1.5), options);
        
        % 获取最终结果
        [best_total_nll, all_epsilons] = compute_global_nll(best_decay_rate, all_subjects_data);
        
        fprintf('精细搜索完成\n');
    catch ME
        fprintf('精细搜索失败: %s\n', ME.message);
        % 如果精细搜索失败，使用粗略搜索的结果
        best_decay_rate = initial_decay;
        [best_total_nll, all_epsilons] = compute_global_nll(best_decay_rate, all_subjects_data);
    end
end

% 安全的全局似然计算，防止错误导致优化中断
function [nll, eps] = safe_global_nll(decay_rate, all_subjects_data)
    try
        [nll, eps] = compute_global_nll(decay_rate, all_subjects_data);
    catch ME
        fprintf('警告: 计算衰减率 %.5f 的似然时出错: %s\n', decay_rate, ME.message);
        nll = Inf;
        eps = [];
    end
end
function [total_nll, all_eps] = compute_global_nll(decay_rate, all_subjects_data)
    n_subjects = length(all_subjects_data);
    total_nll = 0;
    all_eps = zeros(n_subjects, 1);
    
    valid_subjects = 0;  % 计数有效的被试数量
    
    for i = 1:n_subjects
        if ~isempty(all_subjects_data{i})
            try
                % 优化单个被试的epsilon0
                [eps0, subj_nll] = optimize_epsilon0(decay_rate, all_subjects_data{i});
                
                % 检查结果是否有效
                if isfinite(eps0) && isfinite(subj_nll)
                    all_eps(i) = eps0;
                    total_nll = total_nll + subj_nll;
                    valid_subjects = valid_subjects + 1;
                else
                    all_eps(i) = NaN;
                    fprintf('警告: 被试 %d 的优化结果无效\n', i);
                end
            catch ME
                all_eps(i) = NaN;
                fprintf('警告: 优化被试 %d 时出错: %s\n', i, ME.message);
            end
        else
            all_eps(i) = NaN;
        end
    end
    
    % 如果没有有效被试，返回无穷大
    if valid_subjects == 0
        total_nll = Inf;
        fprintf('警告: 衰减率 %.5f 没有有效的被试结果\n', decay_rate);
    end
end
function [best_epsilon0, best_nll] = optimize_epsilon0(decay_rate, subject_data)
    % 对单个被试优化epsilon0
    likelihood_func = @(epsilon0) compute_subject_likelihood(epsilon0, decay_rate, subject_data.choices, subject_data.feedback);
    
    % 多次随机初始化搜索
    n_starts = 5;
    best_epsilon0 = NaN;
    best_nll = Inf;
    
    for start = 1:n_starts
        try
            init_point = 0.1 + 0.8 * rand();  % 随机初始点
            [eps0, fval] = fminbnd(likelihood_func, 0.01, 0.99);
            
            if fval < best_nll && isfinite(fval)
                best_epsilon0 = eps0;
                best_nll = fval;
            end
        catch ME
            fprintf('优化尝试 %d 失败: %s\n', start, ME.message);
        end
    end
    
    % 如果所有尝试都失败
    if isinf(best_nll)
        error('无法找到有效的epsilon0值');
    end
end
function nll = compute_subject_likelihood(epsilon0, decay_rate, choices, feedback)
    nll = 0;
    [n_rounds, ~] = size(choices);
    
    for round = 1:n_rounds
        round_choices = choices(round, :);
        round_feedback = feedback(round, :);
        actual_trials = sum(~isnan(round_choices));
        
        for trial = 1:actual_trials
            % 使用给定的衰减率计算实际epsilon
            actual_epsilon = max(0.001, min(0.999, epsilon0 - decay_rate*trial));
            
            % 确保实际选择和反馈值有效
            if isnan(round_choices(trial)) || isnan(round_feedback(trial))
                continue;
            end
            
            prev_choices = round_choices(1:trial-1);
            prev_feedback = round_feedback(1:trial-1);
            
            % 确保没有NaN值
            valid_trials = ~isnan(prev_choices) & ~isnan(prev_feedback);
            prev_choices = prev_choices(valid_trials);
            prev_feedback = prev_feedback(valid_trials);
            
            % 计算每个选项的成功/总尝试次数
            counts_success = zeros(1, 3);
            counts_total = zeros(1, 3);
            
            for i = 1:length(prev_choices)
                choice = prev_choices(i);
                if choice >= 1 && choice <= 3  % 确保选择在有效范围内
                    counts_total(choice) = counts_total(choice) + 1;
                    if prev_feedback(i) == 1
                        counts_success(choice) = counts_success(choice) + 1;
                    end
                end
            end
            
            % 计算每个选项的期望价值
            probs = zeros(1, 3);
            for opt = 1:3
                alpha = 1;
                beta = 1;
                probs(opt) = (counts_success(opt) + alpha) / (counts_total(opt) + alpha + beta);
            end
            
            % 识别最佳选项
            max_prob = max(probs);
            best_options = find(probs == max_prob);
            n_best_options = length(best_options);
            
            % 计算选择概率
            choice_probs = zeros(1, 3);
            choice_probs = choice_probs + actual_epsilon/3;
            choice_probs(best_options) = choice_probs(best_options) + (1-actual_epsilon)/n_best_options;
            
            choice_probs = max(choice_probs, 1e-10);
            choice_probs = choice_probs / sum(choice_probs);
            
            % 计算对数似然
            actual_choice = round_choices(trial);
            if actual_choice >= 1 && actual_choice <= 3  % 确保选择在有效范围内
                nll = nll - log(choice_probs(actual_choice));
            end
        end
    end
    
    % 如果没有有效数据，返回无穷大
    if nll == 0
        nll = Inf;
    end
end