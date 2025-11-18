clear; % clear existing variables
close all; % close all open figures

main();

function main()
% subject information
prompt = {'subject ID' 'age' 'gender(m = male, f = female)'};
name = 'subject info';
info = inputdlg(prompt, name);

% open window
Screen('Preference', 'SkipSyncTests', 1); % shorten sync test
ScrNum = Screen('Screens'); % read screen number
[w, rect] = Screen('OpenWindow', max(ScrNum), 255); % open window
Screen('TextFont',w,'Microsoft YaHei'); % choose a Chinese font type
Screen('TextSize',w,50); % set font size

[centerX, centerY] = RectCenter(rect); % coordinate of window center
lenth_box = centerX/2;
width_box = 500/695*lenth_box;
box1 = [centerX/2-lenth_box/2, centerY-width_box/2, centerX/2+lenth_box/2, centerY+width_box/2];
box2 = [centerX-lenth_box/2, centerY-width_box/2, centerX+lenth_box/2, centerY+width_box/2];
box3= [3*centerX/2-lenth_box/2, centerY-width_box/2, 3*centerX/2+lenth_box/2, centerY+width_box/2];
frame_box = [10, 30, -10, -30];
box_choice = [centerX-lenth_box/4, 3*centerY/2, centerX+lenth_box/4, 7*centerY/4];
box_confidence = [centerX-lenth_box/8, 7*centerY/4, centerX+lenth_box/8, 15*centerY/8];
Priority(MaxPriority(w)); % set maximum priority for the window
% HideCursor; % hide cursor
ListenChar(2); % characters typed do not show up in command window
KbName('UnifyKeyNames'); % cross-platform compatibility of keynaming

% generate condition
ntrials = 50;
rng('shuffle'); % change random seed

% generate stim
condition = rand(ntrials,3);

% pre-experiment
filename = fullfile(pwd,'./pics/1.png');
c1 = imread(filename);
t1 = Screen('MakeTexture', w, c1);
filename = fullfile(pwd,'./pics/2.png');
c2 = imread(filename);
t2 = Screen('MakeTexture', w, c2);
filename = fullfile(pwd,'./pics/3.png');
c3 = imread(filename);
t3 = Screen('MakeTexture', w, c3);
filename = fullfile(pwd,'./pics/gift.png');
gift = imread(filename);
t_gift = Screen('MakeTexture', w, gift);
filename = fullfile(pwd,'./pics/empty.png');
empty = imread(filename);
t_empty = Screen('MakeTexture', w, empty);

%exp_date = datetime("now");
%exp_date = string(exp_date);
filename = ['gorilla_',info{1},'.mat'];
filename = fullfile(pwd,'data',filename);
results = struct;%create a structure
results.info = info;

Trial = 1:ntrials;
learn_time = zeros(ntrials,1);
choice_learn_list = cell(ntrials,1);
choice_learn_time_list = cell(ntrials,1);
properties_list = cell(ntrials,1);
resp_time = zeros(ntrials,1);
choice_list = zeros(ntrials,1);
confidence_list = zeros(ntrials,1);
conftime_list = zeros(ntrials,1);
scores_list = zeros(ntrials,1);

show_instruct('./pics/inst1.png');
pureClick();

show_instruct('./pics/inst2.png');
choice_Prob([20, 90, 60], 0, 1);
desgined_final([20, 90, 60], 2, 1);

show_instruct('./pics/inst3.png');
choice_Prob([50, 40, 15], 0, 1);
desgined_final([50, 40, 15], 1, 0);

show_instruct('./pics/inst4.png');
trial = 1;
points = 0;
ntrials = 5;
for trial = 1:ntrials
    prob = [];
    while length(prob) < 3
        prob = randi(100, 1, 3);
        prob = unique(prob);
    end
    choice_Prob(prob, 1, 1);
    prob_final(prob, 1);
    show_reward(choice);
end

show_instruct('./pics/inst5.png');
trial = 1;
points = 0;
ntrials = 5;
for trial = 1:ntrials
    prob = [];
    while length(prob) < 3
        prob = randi(100, 1, 3);
        prob = unique(prob);
    end
    choice_Prob(prob, 1, 0);
    prob_final(prob, 0);
    show_reward(choice);
end

trial = 1;
points = 0;
ntrials = 5;
show_instruct('./pics/inst6.png');
for trial = 1:ntrials
    zanki = 999;
    [~,~,~] = choice_learn();
    [~,choice] = choice_final();
    show_reward(choice);
end

trial = 1;
points = 0;
show_instruct('./pics/inst7.png');
for trial = 1:ntrials
    zanki = 10;
    [~,~,~] = choice_learn();
    [~,choice] = choice_final();
    show_reward(choice);
end

trial = 1;
points = 0;
show_instruct('./pics/inst8.png');
for trial = 1:ntrials
    zanki = 10;
    [~,~,~] = choice_learn();
    [~,choice] = choice_final();
    [~,~] = resp_confidence(choice);
    show_reward(choice);
end

trial = 1;
points = 0;
ntrials = 50;
show_instruct('./pics/inst9.png');
for trial = 1:ntrials
    if trial == 26
        show_instruct('./pics/rest.png');
    end

    zanki = 10;
    [resp_time_learn,choices_list,choice_time_list,properties] = choice_learn();
    [resp_time_final,choice] = choice_final();
    [confidence,conf_time] = resp_confidence(choice);
    show_reward(choice);

    learn_time(trial) = resp_time_learn;
    choice_learn_list{trial} = num2cell(choices_list);
    choice_learn_time_list{trial} = num2cell(choice_time_list);
    properties_list{trial} = num2cell(properties);
    resp_time(trial) = resp_time_final;
    choice_list(trial) = choice;
    confidence_list(trial) = confidence;
    conftime_list(trial) = conf_time;
    scores_list(trial) = points;

    results.dataMat = [num2cell(Trial'),num2cell(condition),num2cell(learn_time),...
        choice_learn_list,choice_learn_time_list,properties_list,num2cell(resp_time),num2cell(choice_list),num2cell(confidence_list),num2cell(conftime_list),num2cell(scores_list)];
    save(filename,'results');
end

%% Ending
show_instruct('./pics/end.png');
% close window
close_ptb();

    function [resp_time,choice_list,choice_time_list,properties] = choice_learn()
        t0=GetSecs();choice=9;t0_tmp = GetSecs();
        choice_list = [];choice_time_list = [];properties = [];property = zeros(1,6);
        while choice
            show_all();show_points();
            if zanki < 100
                show_zanki();
            end
            Screen('FillRect',w,[128,128,128],box_choice)
            DrawFormattedText(w,double('最终选择'),'center',13.14*centerY/8,0);
            Screen('Flip', w);
            [x,y,button] = GetMouse(w);
            if x>box1(1) && x<box1(3) && y>box1(2) && y<box1(4)
                if button(1) && zanki > 0
                    choice_time = GetSecs();
                    choice_time = choice_time - t0_tmp;
                    choice = 1;
                    gift = rand_sample(choice);
                    show_gift(gift,box1);
                    if gift
                        index_property = 1;
                    else
                        index_property = 2;
                    end
                    %points = points-0.5;
                    zanki = zanki - 1;
                    choice_list = [choice_list,choice];
                    choice_time_list = [choice_time_list,choice_time];
                    property(index_property) = property(index_property) + 1;
                    properties = [properties;property];
                    t0_tmp = GetSecs();
                end
            elseif x>box2(1) && x<box2(3) && y>box2(2) && y<box2(4)
                if button(1) && zanki > 0
                    choice_time = GetSecs();
                    choice_time = choice_time - t0_tmp;
                    choice = 2;
                    gift = rand_sample(choice);
                    show_gift(gift,box2);
                    if gift
                        index_property = 3;
                    else
                        index_property = 4;
                    end
                    %points = points-0.5;
                    zanki = zanki - 1;
                    choice_list = [choice_list,choice];
                    choice_time_list = [choice_time_list,choice_time];
                    property(index_property) = property(index_property) + 1;
                    properties = [properties;property];
                    t0_tmp = GetSecs();
                end
            elseif x>box3(1) && x<box3(3) && y>box3(2) && y<box3(4)
                if button(1) && zanki > 0
                    choice_time = GetSecs();
                    choice_time = choice_time - t0_tmp;
                    choice = 3;
                    gift = rand_sample(choice);
                    show_gift(gift,box3);
                    if gift
                        index_property = 5;
                    else
                        index_property = 6;
                    end
                    %points = points-0.5;
                    zanki = zanki - 1;
                    choice_list = [choice_list,choice];
                    choice_time_list = [choice_time_list,choice_time];
                    property(index_property) = property(index_property) + 1;
                    properties = [properties;property];
                    t0_tmp = GetSecs();
                end
            elseif (x>box_choice(1) && x<box_choice(3) && y>box_choice(2) && y<box_choice(4))
                if button(1)
                    choice = 0;
                    t = GetSecs;
                    resp_time  = t-t0;
                    break;
                end
            end
            % if ~zanki
            %     choice = 0;
            %     t = GetSecs;
            %     resp_time  = t-t0;
            %     break;
            % end

        end
    end

    function pureClick()
        maxClick = 6;
        nClick = 0;
        while nClick < maxClick
            show_all();
            Screen('Flip', w);
            [x, y, button] = GetMouse(w);
            if x>box1(1) && x<box1(3) && y>box1(2) && y<box1(4)
                if button(1)
                    gift = rand()<=0.5;
                    show_all();
                    if gift
                        show_all();
                        Screen('DrawTexture', w, t_gift, [], box1);
                    else
                        show_all();
                        Screen('DrawTexture', w, t_empty, [], box1);
                    end
                    Screen('Flip',w);
                    WaitSecs(1);
                    nClick = nClick+1;
                end
            elseif x>box2(1) && x<box2(3) && y>box2(2) && y<box2(4)
                if button(1)
                    gift = rand()<=0.5;
                    if gift
                        show_all();
                        Screen('DrawTexture', w, t_gift, [], box2);
                    else
                        show_all();
                        Screen('DrawTexture', w, t_empty, [], box2);
                    end
                    Screen('Flip',w);
                    WaitSecs(1);
                    nClick = nClick+1;
                end
            elseif x>box3(1) && x<box3(3) && y>box3(2) && y<box3(4)
                if button(1)
                    gift = rand()<=0.5;
                    if gift
                        show_all();
                        Screen('DrawTexture', w, t_gift, [], box3);
                    else
                        show_all();
                        Screen('DrawTexture', w, t_empty, [], box3);
                    end
                    Screen('Flip',w);
                    WaitSecs(1);
                    nClick = nClick+1;
                end
            end
        end
    end

    function choice_Prob(prob, showScore, showProb)
        choice = 9;
        while choice
            show_all();
            if showProb
                show_prob(prob);
            end
            if showScore
                show_points();
            end
            Screen('FillRect',w,[128,128,128],box_choice)
            DrawFormattedText(w,double('最终选择'),'center',13.14*centerY/8,0);
            Screen('Flip', w);
            [x,y,button] = GetMouse(w);
            if (x>box_choice(1) && x<box_choice(3) && y>box_choice(2) && y<box_choice(4))
                if button(1)
                    choice = 0;
                    break;
                end
            end
        end
    end

    function [resp_time,choice] = choice_final()
        % show_all();show_points();
        t0=GetSecs;t=0;choice=0;
        while ~choice
            % [~,x,y,button,~] = GetClicks(w);
            [x,y,button] = GetMouse(w);
            show_all();
            if x>box1(1) && x<box1(3) && y>box1(2) && y<box1(4)
                Screen('FrameRect', w, 0, box1+frame_box, 15);
                if button(1)
                    choice = 1;
                    t = GetSecs;
                    break;
                end
            elseif x>box2(1) && x<box2(3) && y>box2(2) && y<box2(4)
                Screen('FrameRect', w, 0, box2+frame_box, 15);
                if button(1)
                    choice = 2;
                    t = GetSecs;
                    break;
                end
            elseif x>box3(1) && x<box3(3) && y>box3(2) && y<box3(4)
                Screen('FrameRect', w, 0, box3+frame_box, 15);
                if button(1)
                    choice = 3;
                    t = GetSecs;
                    break;
                end
            else
                choice = 0;
            end
            DrawFormattedText(w,double('请做出最终选择'),'center',300,0);
            Screen('Flip', w);
        end
        resp_time  = t-t0;
        gift = rand_sample(choice);
        if gift
            points = points + 20;
        end

    end

    function desgined_final(prob, iBox, isGift)
        allBox = {box1, box2, box3};
        iBox = allBox{iBox};
        while 1
            [x,y,button] = GetMouse(w);
            show_all();
            show_prob(prob);
            if x>box1(1) && x<box1(3) && y>box1(2) && y<box1(4)
                Screen('FrameRect', w, 0, box1+frame_box, 15);
            elseif x>box2(1) && x<box2(3) && y>box2(2) && y<box2(4)
                Screen('FrameRect', w, 0, box2+frame_box, 15);
            elseif x>box3(1) && x<box3(3) && y>box3(2) && y<box3(4)
                Screen('FrameRect', w, 0, box3+frame_box, 15);
            end
            if x>iBox(1) && x<iBox(3) && y>iBox(2) && y<iBox(4)
                if button(1)
                    break
                end
            end
            DrawFormattedText(w,double('请做出最终选择'),'center',300,0);
            Screen('Flip', w); 
        end
        show_all();
        if isGift
            Screen('DrawTexture', w, t_gift, [], iBox);
        else
            Screen('DrawTexture', w, t_empty, [], iBox);
        end
        Screen('Flip',w);
        WaitSecs(1);
    end

    function prob_final(prob, showProb)
        choice = 0;
        while ~choice
            [x,y,button] = GetMouse(w);
            show_all();
            if showProb
                show_prob(prob);
            end
            if x>box1(1) && x<box1(3) && y>box1(2) && y<box1(4)
                Screen('FrameRect', w, 0, box1+frame_box, 15);
                if button(1)
                    choice = 1;
                    break;
                end
            elseif x>box2(1) && x<box2(3) && y>box2(2) && y<box2(4)
                Screen('FrameRect', w, 0, box2+frame_box, 15);
                if button(1)
                    choice = 2;
                    break;
                end
            elseif x>box3(1) && x<box3(3) && y>box3(2) && y<box3(4)
                Screen('FrameRect', w, 0, box3+frame_box, 15);
                if button(1)
                    choice = 3;
                    break;
                end
            end
            DrawFormattedText(w,double('请做出最终选择'),'center',300,0);
            Screen('Flip', w); 
        end
        gift = rand()<(prob(choice)/100);
        if gift
            points = points+20;
        end
    end

    function [confidence,t] = resp_confidence(choice)
        instruct = '请选择您的自信程度:';
        t0=GetSecs;t=0;
        x_dot = centerX + 0.15*(1-2*rand(1))*centerX;
        while 1
            [x,y,button]= GetMouse(w);
            show_all();
            draw_triangle(x_dot);
            Screen('DrawLine', w, 0, centerX/2, 13*centerY/8, 3*centerX/2, 13*centerY/8, 4);
            Screen('FillRect',w,[128,128,128],box_confidence);
            DrawFormattedText(w,double('确认'),'center',58.5*centerY/32,0);

            if x > centerX/2 && x < 3*centerX/2 && y > 12*centerY/8 && y < 14*centerY/8 && button(1)
                x_dot = x;
                draw_triangle(x_dot);
            end
            confidence_tmp = round(100*(x_dot-centerX/2)/centerX);
            ins_tmp = [instruct,num2str(confidence_tmp)];
            DrawFormattedText(w,double(ins_tmp),'center',3*centerY/2,0)

            if choice == 1
                Screen('FrameRect', w, 0, box1+frame_box, 15);
            elseif choice == 2
                Screen('FrameRect', w, 0, box2+frame_box, 15);
            elseif choice == 3
                Screen('FrameRect', w, 0, box3+frame_box, 15);
            end

            Screen('Flip',w);

            if x > box_confidence(1) && x < box_confidence(3) && y > box_confidence(2) && y < box_confidence(4) && button(1)
                t_tmp = GetSecs;
                t=t_tmp-t0;
                confidence = confidence_tmp;
                break;
            end
        end
    end

    function show_reward(choice)
        show_all();show_points();
        if gift
            text = '+20';
        else
            text = '+0';
        end
        if choice == 1
            DrawFormattedText(w,double(text),(box1(1)+box1(3))/2,centerY/2,0);
            show_gift(gift,box1)
        elseif choice == 2
            DrawFormattedText(w,double(text),'center',centerY/2,0);
            show_gift(gift,box2)
        elseif choice == 3
            DrawFormattedText(w,double(text),(box3(1)+box3(3))/2,centerY/2,0);
            show_gift(gift,box3)
        end
    end

    function gift = rand_sample(box_i)
        current_box = condition(trial,box_i);
        tmp = rand();
        if current_box >= tmp
            gift = 1;
        else
            gift = 0;
        end
    end

    function show_gift(gift,box)
        show_all();
        if gift
            show_all();
            Screen('DrawTexture', w, t_gift, [], box);
        else
            show_all();
            Screen('DrawTexture', w, t_empty, [], box);
        end
        show_points();
        Screen('Flip',w);
        WaitSecs(1);
    end

    function show_prob(prob)
        normBoundsRect = Screen('TextBounds', w, sprintf('%d%%', prob(1)));
        textWidth = normBoundsRect(3) - normBoundsRect(1);
        DrawFormattedText(w,sprintf('%d%%', prob(1)),centerX/2-0.5*textWidth,centerY+0.6*width_box,0);

        normBoundsRect = Screen('TextBounds', w, sprintf('%d%%', prob(2)));
        textWidth = normBoundsRect(3) - normBoundsRect(1);
        DrawFormattedText(w,sprintf('%d%%', prob(2)),centerX-0.5*textWidth,centerY+0.6*width_box,0);

        normBoundsRect = Screen('TextBounds', w, sprintf('%d%%', prob(3)));
        textWidth = normBoundsRect(3) - normBoundsRect(1);
        DrawFormattedText(w,sprintf('%d%%', prob(3)),centerX*3/2-0.5*textWidth,centerY+0.6*width_box,0);



        % DrawFormattedText2(sprintf('%d%%', prob(1)), 'win', w, 'baseColor', [0 0 0], 'sx', centerX/2, ...
        %     'sy', centerY+0.6*width_box, 'xalign', 'center', 'yalign', 'center');
        % DrawFormattedText2(sprintf('%d%%', prob(2)), 'win', w, 'baseColor', [0 0 0], 'sx', centerX, ...
        %     'sy', centerY+0.6*width_box, 'xalign', 'center', 'yalign', 'center');
        % DrawFormattedText2(sprintf('%d%%', prob(3)), 'win', w, 'baseColor', [0 0 0], 'sx', centerX*3/2, ...
        %     'sy', centerY+0.6*width_box, 'xalign', 'center', 'yalign', 'center');
    end

    function show_points()
        DrawFormattedText(w,double(['轮次：',num2str(trial),'/',num2str(ntrials)]),100,100,0);
        DrawFormattedText(w,double(['总运输物资：',num2str(points)]),12*centerX/8,100,0);
    end

    function show_zanki()
        DrawFormattedText(w,double(['剩余派遣次数：',num2str(zanki)]),'center',300,0);
    end

    function show_all()
        Screen('DrawTexture', w, t1, [], box1);
        Screen('DrawTexture', w, t2, [], box2);
        Screen('DrawTexture', w, t3, [], box3);
    end

    function draw_triangle(x_dot)
        Screen('DrawLine', w, 0, x_dot, 13*centerY/8, x_dot+20, 13*centerY/8+20*sqrt(3), 5);
        Screen('DrawLine', w, 0, x_dot-20, 13*centerY/8+20*sqrt(3), x_dot+20, 13*centerY/8+20*sqrt(3), 5);
        Screen('DrawLine', w, 0, x_dot-20, 13*centerY/8+20*sqrt(3), x_dot, 13*centerY/8, 5);
    end

    function show_instruct(file_path)
        filename_tmp = fullfile(pwd,file_path);
        c_tmp = imread(filename_tmp);
        t_tmp = Screen('MakeTexture', w, c_tmp);
        Screen('DrawTexture', w, t_tmp, [], [0,0,2*centerX,2*centerY]);
        Screen('Flip',w);
        WaitPress(KbName('space'));
    end

    function close_ptb()
        ListenChar(0); % characters typed do show up in command window
        Priority(0); % reset window priority
        ShowCursor; % show cursor
        Screen('CloseAll'); % close window
    end

    function [responseTime, keyCode] = WaitPress(keys, timeOut, timeMode)
        t0=GetSecs;
        t=0;
        responseTime=nan;

        while KbCheck;end % clear keypress information in cache

        if nargin < 3
            timeMode = 0;
        end
        if nargin < 2
            timeOut = Inf;
        end
        if nargin < 1
            keys=[];
        end

        if timeOut == Inf
            timeMode = 0;
        end
        if timeMode ~= 0 && timeMode ~= 1
            error('timeMode must be 0 or 1');
        end

        if isempty(keys)
            % Not accepting mouse buttons (from 1 to 7)
            keys =  8:256 ;
        end
        if any(keys<1)
            error('Can''t map keys below 1');
        end
        keyCode=zeros(1,256);

        if timeMode == 0 % stop waiting after pressing a key
            while ~any(keyCode(keys)) && ((t-t0) < timeOut)
                [~,t,keyCode] = KbCheck;
            end
        elseif timeMode == 1 % wait until timeout after pressing a key
            keyPressed = 0;
            t_tmp = 0;
            while (t_tmp-t0) < timeOut
                [~,t_tmp,keyCode_tmp] = KbCheck;
                if keyPressed == 0
                    if any(keyCode_tmp(keys))
                        keyPressed = 1;
                        t = t_tmp;
                        keyCode = keyCode_tmp;
                    end
                end
            end
        end

        if any(keyCode(keys))
            responseTime = t-t0;
        end
    end
end

