#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, os
from psychopy import visual, core, event
from math import pi, atan


# set a few constants
scrWidth=65
scrHeight=45
scnSize = [1920, 1080]
viewDist=60
deg2pix = int((scnSize[0]/2.0) / (atan(scrWidth/2.0 /viewDist) * 180.0 / pi)) #弧度=角度×π/180​
fontSize=2*deg2pix

####get subj info
def getSubjInfo():
    ID = str(input('Subject ID: '))
    Name = str(input('Subject Name: '))
    Gender = str(input('Subject Gender: '))
    Age = str(input('Age: '))
    return [ID, Name, Gender, Age]
subjInfo = getSubjInfo()

#### set wd
os.chdir('D:\project4')
#### Data manipulation functions #################################################
def init_data_file(SUBJ_INFO):
    """ define a function that initializes the data file"""
    if not os.path.exists('Data'): os.mkdir('Data')
    file_name = 'Data/' + SUBJ_INFO[0] + '_' + SUBJ_INFO[2] + '.csv'
    data_file = open(file_name, 'w')
    header = ['subj', 'trial',  'dir',  'cond', 'resp', 'RT']
    data_file.write(','.join(header) + '\n')
    return data_file
# initialize the data files
DATA_FILE = init_data_file(subjInfo)

# Design mat
def shuju ():
 Design=[[1, 1], [2, 1], [1, 2], [2, 2]]*1
 random.shuffle(Design)
 return Design
# setup a display
win = visual.Window(scnSize, fullscr=True, units='pix')
event.Mouse(visible=False)
timer = core.Clock()

def display_clear():
    """ clear up the screen """
    win.color=[0.5,0.5,0.5]
    win.flip()
      
def put_txt(txt, loc,font_size=3*deg2pix,color='black', win=win):
    """ Put text on display """
    text_1 = visual.TextStim(win, text = txt,
    pos = loc,
    height=font_size,
    color = color,
    bold = True)
    text_1.draw()
    win.flip()
 
def instructions(MODE):
    """ Presenting the instructions"""
    if MODE == 'prac':
        put_txt("现在请您练习下。\n\n请判断中央箭头朝向\n\n请判断朝左边还是右边\n\n如果在左边请按 z 键，在右边按 m 键。\n\n明白后按空格键开始", (0,0))
        event.waitKeys(keyList =['space'])
    if MODE == 'formal':
        put_txt("下面开始正式实验\n\n请判断中央箭头朝向\n\n请判断朝左边还是右边\n\n如果在左边请按 z 键，在右边按 m 键。\n\n明白后按空格键开始", (0,0))
        event.waitKeys(keyList =['space'])
    if MODE == 'continue':
        put_txt("请按空格进入正式实验阶段", (0,0))
        event.waitKeys(keyList =['space'])

    if MODE == 'end':
        put_txt("按空格结束，谢谢参与！", (0,0))
        event.waitKeys(keyList =['space'])

def drawSti(type, trial_info):
    """ define a function to draw stimulus on display'"""
    if type == 'fix':
        put_txt('+', (0,0), fontSize)
    elif type == 'stim':
        dir, cond= trial_info
        if dir==1 and cond ==1:
            stim_text='<<<<<'
        elif dir==1 and cond ==2:
            stim_text='>><>>'
        elif dir==2 and cond ==1:
            stim_text='>>>>>'
        else:
            stim_text='<<><<'
        put_txt(stim_text, (0,0), fontSize)


def wait4key(maxWait=3, keyList =['z', 'm','q']):
    timer.reset()
    resp=event.waitKeys(maxWait=maxWait, keyList =keyList)
    RT = timer.getTime()
    if resp is None:
        resp=['nan']
        RT='nan'
    if resp==['q']:
        win.close()
        core.quit()
    return [resp[0], RT]

def runTrial(subjInfo, pars, datafile):
    """ define a function to run a single trial '"""
    trial_info=pars
    drawSti('fix', trial_info) # 画注视点
    core.wait(random.uniform(0.8, 1.2))
    drawSti('stim', trial_info) # 画刺激
    resp,RT=wait4key(maxWait=5, keyList =['z', 'm','q']) #反应
    core.wait(5-RT)
    display_clear() # 空屏
    trial_data = [subjInfo[0]] + [trial] + trial_info + [resp, RT]
    trial_data = [str(item) for item in trial_data]
    datafile.write(','.join(trial_data) + '\n')
def trueif(resp,dir):
    if resp[0]=='z' and dir==1:
     return 1
    if resp[0]=='m' and dir==2:
     return 1
    if resp=='nan':
     return -1
    else:
     return 0


def runprac(pars):
    trial_info=pars
    drawSti('fix', trial_info)
    core.wait(random.uniform(0.8, 1.2))
    drawSti('stim', trial_info)
    resp,RT=wait4key(maxWait=3, keyList =['z', 'm','q'])
    dir,cond=trial_info
    i=trueif(resp,dir)

    if i==1:
       put_txt('V', (0,0), fontSize,color='green')
       core.wait(3)
       return 1
    if i==0:
       put_txt('X', (0, 0), fontSize, color='red')
       core.wait(3)
       return 0
    if i==-1:
        put_txt('反应慢了', (0, 0), fontSize, color='blue')
        core.wait(3)
        return 0

def run_experiment(mode):
    """ define a function to run blocks/exp '"""
    global trial
    trial = 0
    if mode=='prac':
     instructions('prac')
     sum=0
     while True:
        if sum<4:
         display_clear()
         for t1 in shuju():
             trial = trial + 1
             i=runprac(t1)
             if i == 1:
              sum += 1
        elif sum>=4:
            break
     instructions('continue')
    if mode == 'formal':
        instructions('formal')
        display_clear()
        #### run the trials
        i=0
        for i in range(0,6):
         for t2 in shuju():
            trial = trial + 1
            runTrial(subjInfo, t2, DATA_FILE)
         i+=1
        instructions('end')


run_experiment('prac')
run_experiment('formal') 
# Close the DATA file
DATA_FILE.close()
# Close the experiment graphics
win.close()
#core.quit()


