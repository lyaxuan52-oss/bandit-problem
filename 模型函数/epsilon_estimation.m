function batch_process_epsilon()

    [filenames, pathname] = uigetfile('*.mat', '选择数据文件', 'MultiSelect', 'on');
    
    
    if ~iscell(filenames)
        if filenames == 0
            error('未选择文件');
        end
        filenames = {filenames};
    end
    
   
    [save_path] = uigetdir('', '选择结果保存位置');
    if save_path == 0
        save_path = pwd;  % 如果用户取消选择，使用当前目录
    end
    
   
    n_subjects = length(filenames);
    results = struct();
    results.subject_numbers = zeros(n_subjects, 1);
    results.epsilons = zeros(n_subjects, 1);
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
           
            epsilon = epsilon_estimation_internal(fullfile(pathname, filename));
          
            results.subject_numbers(i) = subject_number;
            results.epsilons(i) = epsilon;
            
            fprintf('被试 %d (文件: %s) 的epsilon值为: %.4f\n', subject_number, filename, epsilon);
        catch ME
            fprintf('警告: 处理被试 %d (文件: %s) 时出错\n', subject_number, filename);
            fprintf('错误信息: %s\n', ME.message);
            results.subject_numbers(i) = subject_number;
            results.epsilons(i) = NaN;
        end
    end
   
    save_results(results, save_path);
end

function save_results(results, save_path)

    timestamp = datestr(now, 'yyyymmdd_HHMMSS');
    filename = fullfile(save_path, sprintf('epsilon_results_%s.mat', timestamp));
    

    save(filename, 'results');
    fprintf('\n结果已保存到文件: %s\n', filename);
    

    txt_filename = fullfile(save_path, sprintf('epsilon_results_%s.txt', timestamp));
    fid = fopen(txt_filename, 'w');
    fprintf(fid, '被试编号\tEpsilon值\t文件名\n');
    for i = 1:length(results.subject_numbers)
        fprintf(fid, '%d\t%.4f\t%s\n', ...
            results.subject_numbers(i), ...
            results.epsilons(i), ...
            results.filenames{i});
    end
    fclose(fid);
    fprintf('结果摘要已保存到文件: %s\n', txt_filename);
end

function epsilon = epsilon_estimation_internal(fullpath)
   
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
    
    
    likelihood = @(eps) compute_total_likelihood(eps, choices, feedback);
    
   
    options = optimset('Display', 'off');
    epsilon = fmincon(likelihood, 0.5, [], [], [], [], 0, 1, [], options);
end

function total_ll = compute_total_likelihood(epsilon, choices, feedback)
    total_ll = 0;
    [n_rounds, ~] = size(choices);
    
    for round = 1:n_rounds
        round_choices = choices(round, :);
        round_feedback = feedback(round, :);
        
        actual_trials = sum(~isnan(round_choices));
        
     
        for trial = 1:actual_trials
           
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
                probs(opt) = (counts_success(opt) + 1) / (counts_total(opt) + 2);
            end
            
           
            max_prob = max(probs);
            best_options = find(probs == max_prob);
            n_best_options = length(best_options);
        
            choice_probs = zeros(1, 3);
         
            choice_probs = choice_probs + epsilon/3;
         
            choice_probs(best_options) = choice_probs(best_options) + (1-epsilon)/n_best_options;
       
            actual_choice = round_choices(trial);
            total_ll = total_ll - log(choice_probs(actual_choice));
        end
    end
end