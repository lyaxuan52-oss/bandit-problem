function batch_process_epsilon()
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
    results.epsilons0 = zeros(n_subjects, 1);
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
            [epsilon] = epsilon0_estimation_internal(fullfile(pathname, filename));
            results.subject_numbers(i) = subject_number;
            results.epsilons0(i) = epsilon;
            fprintf('被试 %d 的epsilon值为: %.4f\n', subject_number, epsilon);
        catch ME
            fprintf('警告: 处理被试 %d 时出错: %s\n', subject_number, ME.message);
            results.subject_numbers(i) = subject_number;
            results.epsilons0(i) = NaN;
        end
    end
end

function [epsilon0] = epsilon0_estimation_internal(fullpath)
    data = load(fullpath);
    dataMat = data.results.dataMat;
    n_rounds = 50;
    max_trials = 10;
    choices = nan(n_rounds, max_trials);
    feedback = nan(n_rounds, max_trials);
    
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
    
    likelihood_function = @(eps0) compute_total_likelihood(eps0, choices, feedback);
    
    options = optimoptions('simulannealbnd', ...
        'Display', 'off', ...
        'InitialTemperature', 100, ...
        'ReannealInterval', 100, ...
        'MaxIterations', 1000);
    
    n_starts = 5;
    best_epsilon0 = NaN;
    best_fval = Inf;
    
    for start = 1:n_starts
        init_point = 0.1 + 0.8 * rand();
        [eps0, fval] = simulannealbnd(likelihood_function, init_point, 0.01, 0.99, options);
        
        if fval < best_fval
            best_epsilon0 = eps0;
            best_fval = fval;
        end
    end
    
    epsilon0 = best_epsilon0;
end

function total_ll = compute_total_likelihood(epsilon0, choices, feedback)
    total_ll = 0;
    [n_rounds, ~] = size(choices);
    
    for round = 1:n_rounds
        round_choices = choices(round, :);
        round_feedback = feedback(round, :);
        actual_trials = sum(~isnan(round_choices));
        
        for trial = 1:actual_trials
            actual_epsilon = epsilon0 - 0.016398*trial;  % 线性衰减
            prev_choices = round_choices(1:trial-1);
            prev_feedback = round_feedback(1:trial-1);
            
            counts_success = zeros(1, 3);
            counts_total = zeros(1, 3);
            
            for i = 1:trial-1
                choice = prev_choices(i);
                counts_total(choice) = counts_total(choice) + 1;
                if prev_feedback(i) == 1
                    counts_success(choice) = counts_success(choice) + 1;
                end
            end
            
            probs = zeros(1, 3);
            for opt = 1:3
                alpha = 1;
                beta = 1;
                probs(opt) = (counts_success(opt) + alpha) / (counts_total(opt) + alpha + beta);
            end
            
            max_prob = max(probs);
            best_options = find(probs == max_prob);
            n_best_options = length(best_options);
            
            choice_probs = zeros(1, 3);
            choice_probs = choice_probs + actual_epsilon/3;
            choice_probs(best_options) = choice_probs(best_options) + (1-actual_epsilon)/n_best_options;
            
            choice_probs = choice_probs + 1e-10;
            choice_probs = choice_probs / sum(choice_probs);
            
            actual_choice = round_choices(trial);
            total_ll = total_ll - log(choice_probs(actual_choice));
        end
    end
end