#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 一月 26, 2025, at 01:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = '刘雅暄期末作业、'  # from the Builder filename that created this script
expInfo = {'participantID': '', 'gender(f=female,m=male)': '', 'age': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participantID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Administrator\\Desktop\\实心实\\ZUOYE\\刘雅暄202311998325期末大作业\\刘雅暄期末作业、_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1707, 1067], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='欢迎参加本实验，\n请按空格键继续\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=1.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp1 = keyboard.Keyboard()

# Initialize components for Routine "ins1"
ins1Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='pics/inst1.png', mask=None,
    ori=0.0, pos=(0, 0), size=[1.7,1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "pra1"
pra1Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "pra1re"
pra1reClock = core.Clock()
image_22 = visual.ImageStim(
    win=win,
    name='image_22', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "ins2"
ins2Clock = core.Clock()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='pics/inst2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "pra2"
pra2Clock = core.Clock()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(-0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='22%',
    font='Open Sans',
    pos=(0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
button = visual.ButtonStim(win, 
    text='Final choose', font='simhei',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=(0.4,0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button'
)
button.buttonClock = core.Clock()

# Initialize components for Routine "prachoose2"
prachoose2Clock = core.Clock()
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_5 = visual.TextStim(win=win, name='text_5',
    text='84%',
    font='Open Sans',
    pos=(-0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='40%',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='22%',
    font='Open Sans',
    pos=(0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "prare2"
prare2Clock = core.Clock()
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "ins3"
ins3Clock = core.Clock()
image_20 = visual.ImageStim(
    win=win,
    name='image_20', 
    image='pics/inst3.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "pra3"
pra3Clock = core.Clock()
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(-0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='12%',
    font='Open Sans',
    pos=(0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
button_2 = visual.ButtonStim(win, 
    text='Final choose', font='simhei',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=(0.4,0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_2'
)
button_2.buttonClock = core.Clock()

# Initialize components for Routine "prachose3"
prachose3Clock = core.Clock()
image_26 = visual.ImageStim(
    win=win,
    name='image_26', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_27 = visual.ImageStim(
    win=win,
    name='image_27', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_28 = visual.ImageStim(
    win=win,
    name='image_28', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_11 = visual.TextStim(win=win, name='text_11',
    text='50%',
    font='Open Sans',
    pos=(-0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='24%',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='12%',
    font='Open Sans',
    pos=(0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "prare3"
prare3Clock = core.Clock()
image_29 = visual.ImageStim(
    win=win,
    name='image_29', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_30 = visual.ImageStim(
    win=win,
    name='image_30', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_31 = visual.ImageStim(
    win=win,
    name='image_31', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "ins4"
ins4Clock = core.Clock()
image_21 = visual.ImageStim(
    win=win,
    name='image_21', 
    image='pics/inst4.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "ins5"
ins5Clock = core.Clock()
image_41 = visual.ImageStim(
    win=win,
    name='image_41', 
    image='pics/inst5.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "ins6"
ins6Clock = core.Clock()
image_51 = visual.ImageStim(
    win=win,
    name='image_51', 
    image='pics/inst6.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "ins7"
ins7Clock = core.Clock()
image_64 = visual.ImageStim(
    win=win,
    name='image_64', 
    image='pics/inst7.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "setp"
setpClock = core.Clock()



# Initialize components for Routine "pra6"
pra6Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='',
    font='Open Sans',
    pos=(0.25, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='剩余派遣侦察兵次数：',
    font='Open Sans',
    pos=(-0.1,0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_52 = visual.ImageStim(
    win=win,
    name='image_52', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_53 = visual.ImageStim(
    win=win,
    name='image_53', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_54 = visual.ImageStim(
    win=win,
    name='image_54', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()
button1 = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=[0.4,0.1], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button1'
)
button1.buttonClock = core.Clock()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()

# Initialize components for Routine "prare6_1"
prare6_1Clock = core.Clock()
image_55 = visual.ImageStim(
    win=win,
    name='image_55', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_56 = visual.ImageStim(
    win=win,
    name='image_56', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_57 = visual.ImageStim(
    win=win,
    name='image_57', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "pra6chose"
pra6choseClock = core.Clock()
image_58 = visual.ImageStim(
    win=win,
    name='image_58', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_59 = visual.ImageStim(
    win=win,
    name='image_59', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_60 = visual.ImageStim(
    win=win,
    name='image_60', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()

# Initialize components for Routine "prare6_2"
prare6_2Clock = core.Clock()
image_61 = visual.ImageStim(
    win=win,
    name='image_61', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_62 = visual.ImageStim(
    win=win,
    name='image_62', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_63 = visual.ImageStim(
    win=win,
    name='image_63', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "ins8"
ins8Clock = core.Clock()
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='pics/inst8.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "setp"
setpClock = core.Clock()



# Initialize components for Routine "pra7"
pra7Clock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='',
    font='Open Sans',
    pos=(0.25, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='剩余派遣侦察兵次数：',
    font='Open Sans',
    pos=(-0.1,0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_65 = visual.ImageStim(
    win=win,
    name='image_65', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_66 = visual.ImageStim(
    win=win,
    name='image_66', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_67 = visual.ImageStim(
    win=win,
    name='image_67', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()
button1_2 = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=[0.4,0.1], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button1_2'
)
button1_2.buttonClock = core.Clock()

# Initialize components for Routine "feedback2"
feedback2Clock = core.Clock()

# Initialize components for Routine "prare7_1"
prare7_1Clock = core.Clock()
image_68 = visual.ImageStim(
    win=win,
    name='image_68', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_69 = visual.ImageStim(
    win=win,
    name='image_69', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_70 = visual.ImageStim(
    win=win,
    name='image_70', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "pra7chose"
pra7choseClock = core.Clock()
image_71 = visual.ImageStim(
    win=win,
    name='image_71', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_72 = visual.ImageStim(
    win=win,
    name='image_72', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_73 = visual.ImageStim(
    win=win,
    name='image_73', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()

# Initialize components for Routine "confidence"
confidenceClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.4, 0.3)[0], height=(0.4, 0.3)[1],
    ori=0.0, pos=[0,0],
    lineWidth=20.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=1.0, depth=-1.0, interpolate=True)
image_77 = visual.ImageStim(
    win=win,
    name='image_77', 
    image='pics/1.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_78 = visual.ImageStim(
    win=win,
    name='image_78', 
    image='pics/2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_79 = visual.ImageStim(
    win=win,
    name='image_79', 
    image='pics/3.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.25), units=None,
    labels=[0,50,100], ticks=(1, 2,3), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-6, readOnly=False)
button_3 = visual.ButtonStim(win, 
    text='My confidence', font='Arvo',
    pos=(0, -0.45),
    letterHeight=0.05,
    size=[0.5,0.1], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_3'
)
button_3.buttonClock = core.Clock()

# Initialize components for Routine "prare7__"
prare7__Clock = core.Clock()
image_74 = visual.ImageStim(
    win=win,
    name='image_74', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_75 = visual.ImageStim(
    win=win,
    name='image_75', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_76 = visual.ImageStim(
    win=win,
    name='image_76', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "ins9"
ins9Clock = core.Clock()
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='pics/inst9.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_9 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp1.keys = []
key_resp1.rt = []
_key_resp1_allKeys = []
# keep track of which components have finished
instructionComponents = [text, key_resp1]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp1* updates
    waitOnFlip = False
    if key_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp1.frameNStart = frameN  # exact frame index
        key_resp1.tStart = t  # local t and not account for scr refresh
        key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
        key_resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp1.getKeys(keyList=['space'], waitRelease=False)
        _key_resp1_allKeys.extend(theseKeys)
        if len(_key_resp1_allKeys):
            key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
            key_resp1.rt = _key_resp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp1.keys in ['', [], None]:  # No response was made
    key_resp1.keys = None
thisExp.addData('key_resp1.keys',key_resp1.keys)
if key_resp1.keys != None:  # we had a response
    thisExp.addData('key_resp1.rt', key_resp1.rt)
thisExp.addData('key_resp1.started', key_resp1.tStartRefresh)
thisExp.addData('key_resp1.stopped', key_resp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ins1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
ins1Components = [image, key_resp]
for thisComponent in ins1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins1"-------
while continueRoutine:
    # get current time
    t = ins1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins1"-------
for thisComponent in ins1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "ins1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pra1"-------
    continueRoutine = True
    # update component parameters for each repeat
    import random
    p3 = random.random() 
    p4 = random.random()
    p5 = random.random()
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    pra1Components = [image_2, image_3, image_4, mouse]
    for thisComponent in pra1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pra1"-------
    while continueRoutine:
        # get current time
        t = pra1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            image_4.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image_2,image_3,image_4])
                        clickableList = [image_2,image_3,image_4]
                    except:
                        clickableList = [[image_2,image_3,image_4]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra1"-------
    for thisComponent in pra1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('image_2.started', image_2.tStartRefresh)
    trials_3.addData('image_2.stopped', image_2.tStopRefresh)
    trials_3.addData('image_3.started', image_3.tStartRefresh)
    trials_3.addData('image_3.stopped', image_3.tStopRefresh)
    trials_3.addData('image_4.started', image_4.tStartRefresh)
    trials_3.addData('image_4.stopped', image_4.tStopRefresh)
    # store data for trials_3 (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([image_2,image_3,image_4])
            clickableList = [image_2,image_3,image_4]
        except:
            clickableList = [[image_2,image_3,image_4]]
        for obj in clickableList:
            if obj.contains(mouse):
                gotValidClick = True
                mouse.clicked_name.append(obj.name)
    trials_3.addData('mouse.x', x)
    trials_3.addData('mouse.y', y)
    trials_3.addData('mouse.leftButton', buttons[0])
    trials_3.addData('mouse.midButton', buttons[1])
    trials_3.addData('mouse.rightButton', buttons[2])
    if len(mouse.clicked_name):
        trials_3.addData('mouse.clicked_name', mouse.clicked_name[0])
    trials_3.addData('mouse.started', mouse.tStart)
    trials_3.addData('mouse.stopped', mouse.tStop)
    # the Routine "pra1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pra1re"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    import random
    pic2='pics/1.png'
    pic3='pics/2.png'
    pic4='pics/3.png'
    if mouse.getPressed():
     if mouse.isPressedIn(image_2):
            clickresult=random.random()
            if clickresult<p3:
                pic2='pics/empty.png' 
            else:
                pic2='pics/gift.png' 
     elif mouse.isPressedIn(image_3):
            clickresult=random.random()
            if clickresult<p4:
                pic3='pics/empty.png'
            else:
                pic3='pics/gift.png' 
     elif mouse.isPressedIn(image_4):
            clickresult=random.random()
            if clickresult<p5:
                pic4='pics/empty.png' 
            else:
                pic4='pics/gift.png' 
    continueRoutine=True
    image_22.setImage(pic2)
    image_5.setImage(pic3)
    image_6.setImage(pic4)
    # keep track of which components have finished
    pra1reComponents = [image_22, image_5, image_6]
    for thisComponent in pra1reComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra1reClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pra1re"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pra1reClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra1reClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_22* updates
        if image_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_22.frameNStart = frameN  # exact frame index
            image_22.tStart = t  # local t and not account for scr refresh
            image_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_22, 'tStartRefresh')  # time at next scr refresh
            image_22.setAutoDraw(True)
        if image_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_22.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                image_22.tStop = t  # not accounting for scr refresh
                image_22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_22, 'tStopRefresh')  # time at next scr refresh
                image_22.setAutoDraw(False)
        
        # *image_5* updates
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            image_5.setAutoDraw(True)
        if image_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_5.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                image_5.tStop = t  # not accounting for scr refresh
                image_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
                image_5.setAutoDraw(False)
        
        # *image_6* updates
        if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            image_6.setAutoDraw(True)
        if image_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_6.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                image_6.tStop = t  # not accounting for scr refresh
                image_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
                image_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra1reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra1re"-------
    for thisComponent in pra1reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('image_22.started', image_22.tStartRefresh)
    trials_3.addData('image_22.stopped', image_22.tStopRefresh)
    trials_3.addData('image_5.started', image_5.tStartRefresh)
    trials_3.addData('image_5.stopped', image_5.tStopRefresh)
    trials_3.addData('image_6.started', image_6.tStartRefresh)
    trials_3.addData('image_6.stopped', image_6.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "ins2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
ins2Components = [image_7, key_resp_2]
for thisComponent in ins2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins2"-------
while continueRoutine:
    # get current time
    t = ins2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins2"-------
for thisComponent in ins2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_7.started', image_7.tStartRefresh)
thisExp.addData('image_7.stopped', image_7.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "ins2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pra2"-------
continueRoutine = True
# update component parameters for each repeat
text_2.setText('84%')
text_3.setText('40%')
# keep track of which components have finished
pra2Components = [image_8, image_9, image_10, text_2, text_3, text_4, button]
for thisComponent in pra2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pra2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pra2"-------
while continueRoutine:
    # get current time
    t = pra2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pra2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_8* updates
    if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_8.frameNStart = frameN  # exact frame index
        image_8.tStart = t  # local t and not account for scr refresh
        image_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
        image_8.setAutoDraw(True)
    
    # *image_9* updates
    if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_9.frameNStart = frameN  # exact frame index
        image_9.tStart = t  # local t and not account for scr refresh
        image_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
        image_9.setAutoDraw(True)
    
    # *image_10* updates
    if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_10.frameNStart = frameN  # exact frame index
        image_10.tStart = t  # local t and not account for scr refresh
        image_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
        image_10.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *button* updates
    if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
            else:
                button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = True  # if button is still clicked next frame, it is not a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button.wasClicked = False  # if button is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pra2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pra2"-------
for thisComponent in pra2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_8.started', image_8.tStartRefresh)
thisExp.addData('image_8.stopped', image_8.tStopRefresh)
thisExp.addData('image_9.started', image_9.tStartRefresh)
thisExp.addData('image_9.stopped', image_9.tStopRefresh)
thisExp.addData('image_10.started', image_10.tStartRefresh)
thisExp.addData('image_10.stopped', image_10.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('button.started', button.tStartRefresh)
thisExp.addData('button.stopped', button.tStopRefresh)
thisExp.addData('button.numClicks', button.numClicks)
if button.numClicks:
   thisExp.addData('button.timesOn', button.timesOn)
   thisExp.addData('button.timesOff', button.timesOff)
else:
   thisExp.addData('button.timesOn', "")
   thisExp.addData('button.timesOff', "")
# the Routine "pra2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prachoose2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
prachoose2Components = [image_17, image_18, image_19, text_5, text_6, text_7, mouse_2]
for thisComponent in prachoose2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prachoose2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prachoose2"-------
while continueRoutine:
    # get current time
    t = prachoose2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prachoose2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_17* updates
    if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_17.frameNStart = frameN  # exact frame index
        image_17.tStart = t  # local t and not account for scr refresh
        image_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
        image_17.setAutoDraw(True)
    
    # *image_18* updates
    if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_18.frameNStart = frameN  # exact frame index
        image_18.tStart = t  # local t and not account for scr refresh
        image_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
        image_18.setAutoDraw(True)
    
    # *image_19* updates
    if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_19.frameNStart = frameN  # exact frame index
        image_19.tStart = t  # local t and not account for scr refresh
        image_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
        image_19.setAutoDraw(True)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_17)
                    clickableList = image_17
                except:
                    clickableList = [image_17]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prachoose2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prachoose2"-------
for thisComponent in prachoose2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_17.started', image_17.tStartRefresh)
thisExp.addData('image_17.stopped', image_17.tStopRefresh)
thisExp.addData('image_18.started', image_18.tStartRefresh)
thisExp.addData('image_18.stopped', image_18.tStopRefresh)
thisExp.addData('image_19.started', image_19.tStartRefresh)
thisExp.addData('image_19.stopped', image_19.tStopRefresh)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(image_17)
        clickableList = image_17
    except:
        clickableList = [image_17]
    for obj in clickableList:
        if obj.contains(mouse_2):
            gotValidClick = True
            mouse_2.clicked_name.append(obj.name)
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
if len(mouse_2.clicked_name):
    thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
# the Routine "prachoose2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prare2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
pic2='pics/1.png'
pic3='pics/2.png'
pic4='pics/3.png'
if mouse.getPressed():
   if mouse.isPressedIn(image_17):
    pic2='pics/gift.png' 
image_11.setImage(pic2)
image_12.setImage(pic3)
image_13.setImage(pic4)
# keep track of which components have finished
prare2Components = [image_11, image_12, image_13]
for thisComponent in prare2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prare2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prare2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = prare2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prare2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_11* updates
    if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_11.frameNStart = frameN  # exact frame index
        image_11.tStart = t  # local t and not account for scr refresh
        image_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
        image_11.setAutoDraw(True)
    if image_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_11.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_11.tStop = t  # not accounting for scr refresh
            image_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_11, 'tStopRefresh')  # time at next scr refresh
            image_11.setAutoDraw(False)
    
    # *image_12* updates
    if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_12.frameNStart = frameN  # exact frame index
        image_12.tStart = t  # local t and not account for scr refresh
        image_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
        image_12.setAutoDraw(True)
    if image_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_12.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_12.tStop = t  # not accounting for scr refresh
            image_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_12, 'tStopRefresh')  # time at next scr refresh
            image_12.setAutoDraw(False)
    
    # *image_13* updates
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        image_13.setAutoDraw(True)
    if image_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_13.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_13.tStop = t  # not accounting for scr refresh
            image_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
            image_13.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prare2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prare2"-------
for thisComponent in prare2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_11.started', image_11.tStartRefresh)
thisExp.addData('image_11.stopped', image_11.tStopRefresh)
thisExp.addData('image_12.started', image_12.tStartRefresh)
thisExp.addData('image_12.stopped', image_12.tStopRefresh)
thisExp.addData('image_13.started', image_13.tStartRefresh)
thisExp.addData('image_13.stopped', image_13.tStopRefresh)

# ------Prepare to start Routine "ins3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
ins3Components = [image_20, key_resp_3]
for thisComponent in ins3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins3"-------
while continueRoutine:
    # get current time
    t = ins3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_20* updates
    if image_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_20.frameNStart = frameN  # exact frame index
        image_20.tStart = t  # local t and not account for scr refresh
        image_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_20, 'tStartRefresh')  # time at next scr refresh
        image_20.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins3"-------
for thisComponent in ins3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_20.started', image_20.tStartRefresh)
thisExp.addData('image_20.stopped', image_20.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "ins3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pra3"-------
continueRoutine = True
# update component parameters for each repeat
text_8.setText('50%')
text_9.setText('24%')
# keep track of which components have finished
pra3Components = [image_23, image_24, image_25, text_8, text_9, text_10, button_2]
for thisComponent in pra3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pra3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pra3"-------
while continueRoutine:
    # get current time
    t = pra3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pra3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_23* updates
    if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_23.frameNStart = frameN  # exact frame index
        image_23.tStart = t  # local t and not account for scr refresh
        image_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
        image_23.setAutoDraw(True)
    
    # *image_24* updates
    if image_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_24.frameNStart = frameN  # exact frame index
        image_24.tStart = t  # local t and not account for scr refresh
        image_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
        image_24.setAutoDraw(True)
    
    # *image_25* updates
    if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_25.frameNStart = frameN  # exact frame index
        image_25.tStart = t  # local t and not account for scr refresh
        image_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
        image_25.setAutoDraw(True)
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *button_2* updates
    if button_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_2.frameNStart = frameN  # exact frame index
        button_2.tStart = t  # local t and not account for scr refresh
        button_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
        button_2.setAutoDraw(True)
    if button_2.status == STARTED:
        # check whether button_2 has been pressed
        if button_2.isClicked:
            if not button_2.wasClicked:
                button_2.timesOn.append(button_2.buttonClock.getTime()) # store time of first click
                button_2.timesOff.append(button_2.buttonClock.getTime()) # store time clicked until
            else:
                button_2.timesOff[-1] = button_2.buttonClock.getTime() # update time clicked until
            if not button_2.wasClicked:
                continueRoutine = False  # end routine when button_2 is clicked
                None
            button_2.wasClicked = True  # if button_2 is still clicked next frame, it is not a new click
        else:
            button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
    else:
        button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pra3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pra3"-------
for thisComponent in pra3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_23.started', image_23.tStartRefresh)
thisExp.addData('image_23.stopped', image_23.tStopRefresh)
thisExp.addData('image_24.started', image_24.tStartRefresh)
thisExp.addData('image_24.stopped', image_24.tStopRefresh)
thisExp.addData('image_25.started', image_25.tStartRefresh)
thisExp.addData('image_25.stopped', image_25.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
thisExp.addData('button_2.started', button_2.tStartRefresh)
thisExp.addData('button_2.stopped', button_2.tStopRefresh)
thisExp.addData('button_2.numClicks', button_2.numClicks)
if button_2.numClicks:
   thisExp.addData('button_2.timesOn', button_2.timesOn)
   thisExp.addData('button_2.timesOff', button_2.timesOff)
else:
   thisExp.addData('button_2.timesOn', "")
   thisExp.addData('button_2.timesOff', "")
# the Routine "pra3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prachose3"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
prachose3Components = [image_26, image_27, image_28, text_11, text_12, text_13, mouse_3]
for thisComponent in prachose3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prachose3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prachose3"-------
while continueRoutine:
    # get current time
    t = prachose3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prachose3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_26* updates
    if image_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_26.frameNStart = frameN  # exact frame index
        image_26.tStart = t  # local t and not account for scr refresh
        image_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
        image_26.setAutoDraw(True)
    
    # *image_27* updates
    if image_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_27.frameNStart = frameN  # exact frame index
        image_27.tStart = t  # local t and not account for scr refresh
        image_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_27, 'tStartRefresh')  # time at next scr refresh
        image_27.setAutoDraw(True)
    
    # *image_28* updates
    if image_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_28.frameNStart = frameN  # exact frame index
        image_28.tStart = t  # local t and not account for scr refresh
        image_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_28, 'tStartRefresh')  # time at next scr refresh
        image_28.setAutoDraw(True)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    # *mouse_3* updates
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_26)
                    clickableList = image_26
                except:
                    clickableList = [image_26]
                for obj in clickableList:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prachose3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prachose3"-------
for thisComponent in prachose3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_26.started', image_26.tStartRefresh)
thisExp.addData('image_26.stopped', image_26.tStopRefresh)
thisExp.addData('image_27.started', image_27.tStartRefresh)
thisExp.addData('image_27.stopped', image_27.tStopRefresh)
thisExp.addData('image_28.started', image_28.tStartRefresh)
thisExp.addData('image_28.stopped', image_28.tStopRefresh)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(image_26)
        clickableList = image_26
    except:
        clickableList = [image_26]
    for obj in clickableList:
        if obj.contains(mouse_3):
            gotValidClick = True
            mouse_3.clicked_name.append(obj.name)
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
if len(mouse_3.clicked_name):
    thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
# the Routine "prachose3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prare3"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
pic2='pics/1.png'
pic3='pics/2.png'
pic4='pics/3.png'
if mouse.getPressed():
   if mouse.isPressedIn(image_17):
    pic2='pics/empty.png' 
image_29.setImage(pic2)
image_30.setImage(pic3)
image_31.setImage(pic4)
# keep track of which components have finished
prare3Components = [image_29, image_30, image_31]
for thisComponent in prare3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prare3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prare3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = prare3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prare3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_29* updates
    if image_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_29.frameNStart = frameN  # exact frame index
        image_29.tStart = t  # local t and not account for scr refresh
        image_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_29, 'tStartRefresh')  # time at next scr refresh
        image_29.setAutoDraw(True)
    if image_29.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_29.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_29.tStop = t  # not accounting for scr refresh
            image_29.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_29, 'tStopRefresh')  # time at next scr refresh
            image_29.setAutoDraw(False)
    
    # *image_30* updates
    if image_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_30.frameNStart = frameN  # exact frame index
        image_30.tStart = t  # local t and not account for scr refresh
        image_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_30, 'tStartRefresh')  # time at next scr refresh
        image_30.setAutoDraw(True)
    if image_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_30.tStop = t  # not accounting for scr refresh
            image_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_30, 'tStopRefresh')  # time at next scr refresh
            image_30.setAutoDraw(False)
    
    # *image_31* updates
    if image_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_31.frameNStart = frameN  # exact frame index
        image_31.tStart = t  # local t and not account for scr refresh
        image_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_31, 'tStartRefresh')  # time at next scr refresh
        image_31.setAutoDraw(True)
    if image_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_31.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_31.tStop = t  # not accounting for scr refresh
            image_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_31, 'tStopRefresh')  # time at next scr refresh
            image_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prare3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prare3"-------
for thisComponent in prare3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_29.started', image_29.tStartRefresh)
thisExp.addData('image_29.stopped', image_29.tStopRefresh)
thisExp.addData('image_30.started', image_30.tStartRefresh)
thisExp.addData('image_30.stopped', image_30.tStopRefresh)
thisExp.addData('image_31.started', image_31.tStartRefresh)
thisExp.addData('image_31.stopped', image_31.tStopRefresh)

# ------Prepare to start Routine "ins4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
ins4Components = [image_21, key_resp_4]
for thisComponent in ins4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins4"-------
while continueRoutine:
    # get current time
    t = ins4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_21* updates
    if image_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_21.frameNStart = frameN  # exact frame index
        image_21.tStart = t  # local t and not account for scr refresh
        image_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_21, 'tStartRefresh')  # time at next scr refresh
        image_21.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins4"-------
for thisComponent in ins4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_21.started', image_21.tStartRefresh)
thisExp.addData('image_21.stopped', image_21.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "ins4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ins5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
ins5Components = [image_41, key_resp_5]
for thisComponent in ins5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins5"-------
while continueRoutine:
    # get current time
    t = ins5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_41* updates
    if image_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_41.frameNStart = frameN  # exact frame index
        image_41.tStart = t  # local t and not account for scr refresh
        image_41.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_41, 'tStartRefresh')  # time at next scr refresh
        image_41.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins5"-------
for thisComponent in ins5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_41.started', image_41.tStartRefresh)
thisExp.addData('image_41.stopped', image_41.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "ins5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ins6"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
ins6Components = [image_51, key_resp_6]
for thisComponent in ins6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins6"-------
while continueRoutine:
    # get current time
    t = ins6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_51* updates
    if image_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_51.frameNStart = frameN  # exact frame index
        image_51.tStart = t  # local t and not account for scr refresh
        image_51.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_51, 'tStartRefresh')  # time at next scr refresh
        image_51.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins6"-------
for thisComponent in ins6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_51.started', image_51.tStartRefresh)
thisExp.addData('image_51.stopped', image_51.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "ins6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ins7"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
ins7Components = [image_64, key_resp_7]
for thisComponent in ins7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins7"-------
while continueRoutine:
    # get current time
    t = ins7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_64* updates
    if image_64.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_64.frameNStart = frameN  # exact frame index
        image_64.tStart = t  # local t and not account for scr refresh
        image_64.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_64, 'tStartRefresh')  # time at next scr refresh
        image_64.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins7"-------
for thisComponent in ins7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_64.started', image_64.tStartRefresh)
thisExp.addData('image_64.stopped', image_64.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "ins7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "setp"-------
    continueRoutine = True
    # update component parameters for each repeat
    import random
    p3 = random.random()
    p4 = random.random()
    p5 = random.random()
    
    # keep track of which components have finished
    setpComponents = []
    for thisComponent in setpComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    setpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "setp"-------
    while continueRoutine:
        # get current time
        t = setpClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=setpClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setp"-------
    for thisComponent in setpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    num=10
    # the Routine "setp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=11.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=99.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "pra6"-------
            continueRoutine = True
            # update component parameters for each repeat
            text_14.setText(num
)
            # setup some python lists for storing info about the mouse_7
            mouse_7.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_7.mouseClock.reset()
            # keep track of which components have finished
            pra6Components = [text_14, text_15, image_52, image_53, image_54, mouse_7, button1]
            for thisComponent in pra6Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            pra6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "pra6"-------
            while continueRoutine:
                # get current time
                t = pra6Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=pra6Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_14* updates
                if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_14.frameNStart = frameN  # exact frame index
                    text_14.tStart = t  # local t and not account for scr refresh
                    text_14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
                    text_14.setAutoDraw(True)
                
                # *text_15* updates
                if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_15.frameNStart = frameN  # exact frame index
                    text_15.tStart = t  # local t and not account for scr refresh
                    text_15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                    text_15.setAutoDraw(True)
                
                # *image_52* updates
                if image_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_52.frameNStart = frameN  # exact frame index
                    image_52.tStart = t  # local t and not account for scr refresh
                    image_52.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_52, 'tStartRefresh')  # time at next scr refresh
                    image_52.setAutoDraw(True)
                
                # *image_53* updates
                if image_53.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_53.frameNStart = frameN  # exact frame index
                    image_53.tStart = t  # local t and not account for scr refresh
                    image_53.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_53, 'tStartRefresh')  # time at next scr refresh
                    image_53.setAutoDraw(True)
                
                # *image_54* updates
                if image_54.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_54.frameNStart = frameN  # exact frame index
                    image_54.tStart = t  # local t and not account for scr refresh
                    image_54.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_54, 'tStartRefresh')  # time at next scr refresh
                    image_54.setAutoDraw(True)
                # *mouse_7* updates
                if mouse_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_7.frameNStart = frameN  # exact frame index
                    mouse_7.tStart = t  # local t and not account for scr refresh
                    mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
                    mouse_7.status = STARTED
                    prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
                if mouse_7.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_7.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([image_52,image_53,image_54])
                                clickableList = [image_52,image_53,image_54]
                            except:
                                clickableList = [[image_52,image_53,image_54]]
                            for obj in clickableList:
                                if obj.contains(mouse_7):
                                    gotValidClick = True
                                    mouse_7.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *button1* updates
                if button1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button1.frameNStart = frameN  # exact frame index
                    button1.tStart = t  # local t and not account for scr refresh
                    button1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button1, 'tStartRefresh')  # time at next scr refresh
                    button1.setAutoDraw(True)
                if button1.status == STARTED:  # only update if drawing
                    button1.setText('Final Choose', log=False)
                if button1.status == STARTED:
                    # check whether button1 has been pressed
                    if button1.isClicked:
                        if not button1.wasClicked:
                            button1.timesOn.append(button1.buttonClock.getTime()) # store time of first click
                            button1.timesOff.append(button1.buttonClock.getTime()) # store time clicked until
                        else:
                            button1.timesOff[-1] = button1.buttonClock.getTime() # update time clicked until
                        if not button1.wasClicked:
                            continueRoutine = False  # end routine when button1 is clicked
                            trials.finished=True
                            
                        button1.wasClicked = True  # if button1 is still clicked next frame, it is not a new click
                    else:
                        button1.wasClicked = False  # if button1 is clicked next frame, it is a new click
                else:
                    button1.wasClicked = False  # if button1 is clicked next frame, it is a new click
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pra6Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "pra6"-------
            for thisComponent in pra6Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('text_14.started', text_14.tStartRefresh)
            trials_2.addData('text_14.stopped', text_14.tStopRefresh)
            trials_2.addData('text_15.started', text_15.tStartRefresh)
            trials_2.addData('text_15.stopped', text_15.tStopRefresh)
            trials_2.addData('image_52.started', image_52.tStartRefresh)
            trials_2.addData('image_52.stopped', image_52.tStopRefresh)
            trials_2.addData('image_53.started', image_53.tStartRefresh)
            trials_2.addData('image_53.stopped', image_53.tStopRefresh)
            trials_2.addData('image_54.started', image_54.tStartRefresh)
            trials_2.addData('image_54.stopped', image_54.tStopRefresh)
            # store data for trials_2 (TrialHandler)
            x, y = mouse_7.getPos()
            buttons = mouse_7.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([image_52,image_53,image_54])
                    clickableList = [image_52,image_53,image_54]
                except:
                    clickableList = [[image_52,image_53,image_54]]
                for obj in clickableList:
                    if obj.contains(mouse_7):
                        gotValidClick = True
                        mouse_7.clicked_name.append(obj.name)
            trials_2.addData('mouse_7.x', x)
            trials_2.addData('mouse_7.y', y)
            trials_2.addData('mouse_7.leftButton', buttons[0])
            trials_2.addData('mouse_7.midButton', buttons[1])
            trials_2.addData('mouse_7.rightButton', buttons[2])
            if len(mouse_7.clicked_name):
                trials_2.addData('mouse_7.clicked_name', mouse_7.clicked_name[0])
            trials_2.addData('mouse_7.started', mouse_7.tStartRefresh)
            trials_2.addData('mouse_7.stopped', mouse_7.tStopRefresh)
            trials_2.addData('button1.started', button1.tStartRefresh)
            trials_2.addData('button1.stopped', button1.tStopRefresh)
            trials_2.addData('button1.numClicks', button1.numClicks)
            if button1.numClicks:
               trials_2.addData('button1.timesOn', button1.timesOn)
               trials_2.addData('button1.timesOff', button1.timesOff)
            else:
               trials_2.addData('button1.timesOn', "")
               trials_2.addData('button1.timesOff', "")
            # the Routine "pra6" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "feedback"-------
            continueRoutine = True
            # update component parameters for each repeat
            if num>0:
                trials_2.finished=True
                if mouse.isPressedIn(image_52):
                    result=1
                if mouse.isPressedIn(image_53):
                    result=2
                if mouse.isPressedIn(image_54):
                    result=3    
            if num==0:
                if button1.isClicked:
                    trials_2.finished=True
                    trials.finished=True
                else:
                    trials_2.finished=False
            continueRoutine=False
            # keep track of which components have finished
            feedbackComponents = []
            for thisComponent in feedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "feedback"-------
            while continueRoutine:
                # get current time
                t = feedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "feedback"-------
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 99.0 repeats of 'trials_2'
        
        
        # ------Prepare to start Routine "prare6_1"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        if button1.isClicked:
            continueRoutine=False
        else:
            continueRoutine=True
        import random
        pic2='pics/1.png'
        pic3='pics/2.png'
        pic4='pics/3.png'
        if result==1:
                clickresult=random.random()
                if clickresult<p3:
                    pic2='pics/empty.png' 
                else:
                    pic2='pics/gift.png' 
        elif result==2:
                clickresult=random.random()
                if clickresult<p4:
                    pic3='pics/empty.png'
                else:
                    pic3='pics/gift.png' 
        elif result==3:
                clickresult=random.random()
                if clickresult<p5:
                    pic4='pics/empty.png' 
                else:
                    pic4='pics/gift.png' 
        
        image_55.setImage(pic2)
        image_56.setImage(pic3)
        image_57.setImage(pic4)
        # keep track of which components have finished
        prare6_1Components = [image_55, image_56, image_57]
        for thisComponent in prare6_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        prare6_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prare6_1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = prare6_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prare6_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            
            # *image_55* updates
            if image_55.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_55.frameNStart = frameN  # exact frame index
                image_55.tStart = t  # local t and not account for scr refresh
                image_55.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_55, 'tStartRefresh')  # time at next scr refresh
                image_55.setAutoDraw(True)
            if image_55.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_55.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_55.tStop = t  # not accounting for scr refresh
                    image_55.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_55, 'tStopRefresh')  # time at next scr refresh
                    image_55.setAutoDraw(False)
            
            # *image_56* updates
            if image_56.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_56.frameNStart = frameN  # exact frame index
                image_56.tStart = t  # local t and not account for scr refresh
                image_56.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_56, 'tStartRefresh')  # time at next scr refresh
                image_56.setAutoDraw(True)
            if image_56.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_56.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_56.tStop = t  # not accounting for scr refresh
                    image_56.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_56, 'tStopRefresh')  # time at next scr refresh
                    image_56.setAutoDraw(False)
            
            # *image_57* updates
            if image_57.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_57.frameNStart = frameN  # exact frame index
                image_57.tStart = t  # local t and not account for scr refresh
                image_57.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_57, 'tStartRefresh')  # time at next scr refresh
                image_57.setAutoDraw(True)
            if image_57.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_57.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_57.tStop = t  # not accounting for scr refresh
                    image_57.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_57, 'tStopRefresh')  # time at next scr refresh
                    image_57.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prare6_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prare6_1"-------
        for thisComponent in prare6_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('image_55.started', image_55.tStartRefresh)
        trials.addData('image_55.stopped', image_55.tStopRefresh)
        trials.addData('image_56.started', image_56.tStartRefresh)
        trials.addData('image_56.stopped', image_56.tStopRefresh)
        trials.addData('image_57.started', image_57.tStartRefresh)
        trials.addData('image_57.stopped', image_57.tStopRefresh)
        num-=1
        thisExp.nextEntry()
        
    # completed 11.0 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "pra6chose"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_8
    mouse_8.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    pra6choseComponents = [image_58, image_59, image_60, mouse_8]
    for thisComponent in pra6choseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra6choseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pra6chose"-------
    while continueRoutine:
        # get current time
        t = pra6choseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra6choseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_58* updates
        if image_58.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_58.frameNStart = frameN  # exact frame index
            image_58.tStart = t  # local t and not account for scr refresh
            image_58.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_58, 'tStartRefresh')  # time at next scr refresh
            image_58.setAutoDraw(True)
        
        # *image_59* updates
        if image_59.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_59.frameNStart = frameN  # exact frame index
            image_59.tStart = t  # local t and not account for scr refresh
            image_59.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_59, 'tStartRefresh')  # time at next scr refresh
            image_59.setAutoDraw(True)
        
        # *image_60* updates
        if image_60.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_60.frameNStart = frameN  # exact frame index
            image_60.tStart = t  # local t and not account for scr refresh
            image_60.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_60, 'tStartRefresh')  # time at next scr refresh
            image_60.setAutoDraw(True)
        # *mouse_8* updates
        if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_8.frameNStart = frameN  # exact frame index
            mouse_8.tStart = t  # local t and not account for scr refresh
            mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
            mouse_8.status = STARTED
            mouse_8.mouseClock.reset()
            prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
        if mouse_8.status == STARTED:  # only update if started and not finished!
            buttons = mouse_8.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image_58,image_59,image_60])
                        clickableList = [image_58,image_59,image_60]
                    except:
                        clickableList = [[image_58,image_59,image_60]]
                    for obj in clickableList:
                        if obj.contains(mouse_8):
                            gotValidClick = True
                            mouse_8.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra6choseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra6chose"-------
    for thisComponent in pra6choseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('image_58.started', image_58.tStartRefresh)
    trials_4.addData('image_58.stopped', image_58.tStopRefresh)
    trials_4.addData('image_59.started', image_59.tStartRefresh)
    trials_4.addData('image_59.stopped', image_59.tStopRefresh)
    trials_4.addData('image_60.started', image_60.tStartRefresh)
    trials_4.addData('image_60.stopped', image_60.tStopRefresh)
    # store data for trials_4 (TrialHandler)
    x, y = mouse_8.getPos()
    buttons = mouse_8.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([image_58,image_59,image_60])
            clickableList = [image_58,image_59,image_60]
        except:
            clickableList = [[image_58,image_59,image_60]]
        for obj in clickableList:
            if obj.contains(mouse_8):
                gotValidClick = True
                mouse_8.clicked_name.append(obj.name)
    trials_4.addData('mouse_8.x', x)
    trials_4.addData('mouse_8.y', y)
    trials_4.addData('mouse_8.leftButton', buttons[0])
    trials_4.addData('mouse_8.midButton', buttons[1])
    trials_4.addData('mouse_8.rightButton', buttons[2])
    if len(mouse_8.clicked_name):
        trials_4.addData('mouse_8.clicked_name', mouse_8.clicked_name[0])
    trials_4.addData('mouse_8.started', mouse_8.tStart)
    trials_4.addData('mouse_8.stopped', mouse_8.tStop)
    # the Routine "pra6chose" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "prare6_2"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    import random
    pic2='pics/1.png'
    pic3='pics/2.png'
    pic4='pics/3.png'
    if mouse.getPressed():
     if mouse.isPressedIn(image_58):
            clickresult=random.random()
            if clickresult<p3:
                pic2='pics/empty.png' 
            else:
                pic2='pics/gift.png' 
     elif mouse.isPressedIn(image_59):
            clickresult=random.random()
            if clickresult<p4:
                pic3='pics/empty.png'
            else:
                pic3='pics/gift.png' 
     elif mouse.isPressedIn(image_60):
            clickresult=random.random()
            if clickresult<p5:
                pic4='pics/empty.png' 
            else:
                pic4='pics/gift.png' 
    continueRoutine=True
    image_61.setImage(pic2)
    image_62.setImage(pic3)
    image_63.setImage(pic4)
    # keep track of which components have finished
    prare6_2Components = [image_61, image_62, image_63]
    for thisComponent in prare6_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prare6_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prare6_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prare6_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prare6_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_61* updates
        if image_61.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_61.frameNStart = frameN  # exact frame index
            image_61.tStart = t  # local t and not account for scr refresh
            image_61.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_61, 'tStartRefresh')  # time at next scr refresh
            image_61.setAutoDraw(True)
        if image_61.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_61.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_61.tStop = t  # not accounting for scr refresh
                image_61.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_61, 'tStopRefresh')  # time at next scr refresh
                image_61.setAutoDraw(False)
        
        # *image_62* updates
        if image_62.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_62.frameNStart = frameN  # exact frame index
            image_62.tStart = t  # local t and not account for scr refresh
            image_62.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_62, 'tStartRefresh')  # time at next scr refresh
            image_62.setAutoDraw(True)
        if image_62.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_62.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_62.tStop = t  # not accounting for scr refresh
                image_62.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_62, 'tStopRefresh')  # time at next scr refresh
                image_62.setAutoDraw(False)
        
        # *image_63* updates
        if image_63.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_63.frameNStart = frameN  # exact frame index
            image_63.tStart = t  # local t and not account for scr refresh
            image_63.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_63, 'tStartRefresh')  # time at next scr refresh
            image_63.setAutoDraw(True)
        if image_63.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_63.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_63.tStop = t  # not accounting for scr refresh
                image_63.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_63, 'tStopRefresh')  # time at next scr refresh
                image_63.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prare6_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prare6_2"-------
    for thisComponent in prare6_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('image_61.started', image_61.tStartRefresh)
    trials_4.addData('image_61.stopped', image_61.tStopRefresh)
    trials_4.addData('image_62.started', image_62.tStartRefresh)
    trials_4.addData('image_62.stopped', image_62.tStopRefresh)
    trials_4.addData('image_63.started', image_63.tStartRefresh)
    trials_4.addData('image_63.stopped', image_63.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_4'

# get names of stimulus parameters
if trials_4.trialList in ([], [None], None):
    params = []
else:
    params = trials_4.trialList[0].keys()
# save data for this loop
trials_4.saveAsExcel(filename + '.xlsx', sheetName='trials_4',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "ins8"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
ins8Components = [image_14, key_resp_8]
for thisComponent in ins8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins8"-------
while continueRoutine:
    # get current time
    t = ins8Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins8Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_14* updates
    if image_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_14.frameNStart = frameN  # exact frame index
        image_14.tStart = t  # local t and not account for scr refresh
        image_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
        image_14.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins8"-------
for thisComponent in ins8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_14.started', image_14.tStartRefresh)
thisExp.addData('image_14.stopped', image_14.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "ins8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "setp"-------
    continueRoutine = True
    # update component parameters for each repeat
    import random
    p3 = random.random()
    p4 = random.random()
    p5 = random.random()
    
    # keep track of which components have finished
    setpComponents = []
    for thisComponent in setpComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    setpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "setp"-------
    while continueRoutine:
        # get current time
        t = setpClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=setpClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setp"-------
    for thisComponent in setpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    num=10
    # the Routine "setp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials77 = data.TrialHandler(nReps=11.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials77')
    thisExp.addLoop(trials77)  # add the loop to the experiment
    thisTrials77 = trials77.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials77.rgb)
    if thisTrials77 != None:
        for paramName in thisTrials77:
            exec('{} = thisTrials77[paramName]'.format(paramName))
    
    for thisTrials77 in trials77:
        currentLoop = trials77
        # abbreviate parameter names if possible (e.g. rgb = thisTrials77.rgb)
        if thisTrials77 != None:
            for paramName in thisTrials77:
                exec('{} = thisTrials77[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials66 = data.TrialHandler(nReps=99.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials66')
        thisExp.addLoop(trials66)  # add the loop to the experiment
        thisTrials66 = trials66.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials66.rgb)
        if thisTrials66 != None:
            for paramName in thisTrials66:
                exec('{} = thisTrials66[paramName]'.format(paramName))
        
        for thisTrials66 in trials66:
            currentLoop = trials66
            # abbreviate parameter names if possible (e.g. rgb = thisTrials66.rgb)
            if thisTrials66 != None:
                for paramName in thisTrials66:
                    exec('{} = thisTrials66[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "pra7"-------
            continueRoutine = True
            # update component parameters for each repeat
            text_16.setText(num
)
            # setup some python lists for storing info about the mouse_9
            mouse_9.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            pra7Components = [text_16, text_17, image_65, image_66, image_67, mouse_9, button1_2]
            for thisComponent in pra7Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            pra7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "pra7"-------
            while continueRoutine:
                # get current time
                t = pra7Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=pra7Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_16* updates
                if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_16.frameNStart = frameN  # exact frame index
                    text_16.tStart = t  # local t and not account for scr refresh
                    text_16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
                    text_16.setAutoDraw(True)
                
                # *text_17* updates
                if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_17.frameNStart = frameN  # exact frame index
                    text_17.tStart = t  # local t and not account for scr refresh
                    text_17.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
                    text_17.setAutoDraw(True)
                
                # *image_65* updates
                if image_65.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_65.frameNStart = frameN  # exact frame index
                    image_65.tStart = t  # local t and not account for scr refresh
                    image_65.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_65, 'tStartRefresh')  # time at next scr refresh
                    image_65.setAutoDraw(True)
                
                # *image_66* updates
                if image_66.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_66.frameNStart = frameN  # exact frame index
                    image_66.tStart = t  # local t and not account for scr refresh
                    image_66.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_66, 'tStartRefresh')  # time at next scr refresh
                    image_66.setAutoDraw(True)
                
                # *image_67* updates
                if image_67.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_67.frameNStart = frameN  # exact frame index
                    image_67.tStart = t  # local t and not account for scr refresh
                    image_67.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_67, 'tStartRefresh')  # time at next scr refresh
                    image_67.setAutoDraw(True)
                # *mouse_9* updates
                if mouse_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_9.frameNStart = frameN  # exact frame index
                    mouse_9.tStart = t  # local t and not account for scr refresh
                    mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
                    mouse_9.status = STARTED
                    mouse_9.mouseClock.reset()
                    prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
                if mouse_9.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_9.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([image_65,image_66,image_67])
                                clickableList = [image_65,image_66,image_67]
                            except:
                                clickableList = [[image_65,image_66,image_67]]
                            for obj in clickableList:
                                if obj.contains(mouse_9):
                                    gotValidClick = True
                                    mouse_9.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *button1_2* updates
                if button1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button1_2.frameNStart = frameN  # exact frame index
                    button1_2.tStart = t  # local t and not account for scr refresh
                    button1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button1_2, 'tStartRefresh')  # time at next scr refresh
                    button1_2.setAutoDraw(True)
                if button1_2.status == STARTED:  # only update if drawing
                    button1_2.setText('Final Choose', log=False)
                if button1_2.status == STARTED:
                    # check whether button1_2 has been pressed
                    if button1_2.isClicked:
                        if not button1_2.wasClicked:
                            button1_2.timesOn.append(button1_2.buttonClock.getTime()) # store time of first click
                            button1_2.timesOff.append(button1_2.buttonClock.getTime()) # store time clicked until
                        else:
                            button1_2.timesOff[-1] = button1_2.buttonClock.getTime() # update time clicked until
                        if not button1_2.wasClicked:
                            continueRoutine = False  # end routine when button1_2 is clicked
                            
                            trials77.finished=True
                            
                        button1_2.wasClicked = True  # if button1_2 is still clicked next frame, it is not a new click
                    else:
                        button1_2.wasClicked = False  # if button1_2 is clicked next frame, it is a new click
                else:
                    button1_2.wasClicked = False  # if button1_2 is clicked next frame, it is a new click
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pra7Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "pra7"-------
            for thisComponent in pra7Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials66.addData('text_16.started', text_16.tStartRefresh)
            trials66.addData('text_16.stopped', text_16.tStopRefresh)
            trials66.addData('text_17.started', text_17.tStartRefresh)
            trials66.addData('text_17.stopped', text_17.tStopRefresh)
            trials66.addData('image_65.started', image_65.tStartRefresh)
            trials66.addData('image_65.stopped', image_65.tStopRefresh)
            trials66.addData('image_66.started', image_66.tStartRefresh)
            trials66.addData('image_66.stopped', image_66.tStopRefresh)
            trials66.addData('image_67.started', image_67.tStartRefresh)
            trials66.addData('image_67.stopped', image_67.tStopRefresh)
            # store data for trials66 (TrialHandler)
            x, y = mouse_9.getPos()
            buttons = mouse_9.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([image_65,image_66,image_67])
                    clickableList = [image_65,image_66,image_67]
                except:
                    clickableList = [[image_65,image_66,image_67]]
                for obj in clickableList:
                    if obj.contains(mouse_9):
                        gotValidClick = True
                        mouse_9.clicked_name.append(obj.name)
            trials66.addData('mouse_9.x', x)
            trials66.addData('mouse_9.y', y)
            trials66.addData('mouse_9.leftButton', buttons[0])
            trials66.addData('mouse_9.midButton', buttons[1])
            trials66.addData('mouse_9.rightButton', buttons[2])
            if len(mouse_9.clicked_name):
                trials66.addData('mouse_9.clicked_name', mouse_9.clicked_name[0])
            trials66.addData('mouse_9.started', mouse_9.tStartRefresh)
            trials66.addData('mouse_9.stopped', mouse_9.tStopRefresh)
            trials66.addData('button1_2.started', button1_2.tStartRefresh)
            trials66.addData('button1_2.stopped', button1_2.tStopRefresh)
            trials66.addData('button1_2.numClicks', button1_2.numClicks)
            if button1_2.numClicks:
               trials66.addData('button1_2.timesOn', button1_2.timesOn)
               trials66.addData('button1_2.timesOff', button1_2.timesOff)
            else:
               trials66.addData('button1_2.timesOn', "")
               trials66.addData('button1_2.timesOff', "")
            # the Routine "pra7" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "feedback2"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            feedback2Components = []
            for thisComponent in feedback2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            feedback2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "feedback2"-------
            while continueRoutine:
                # get current time
                t = feedback2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=feedback2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if num>0:
                    trials66.finished=True
                    if mouse.isPressedIn(image_65):
                        result=1
                    if mouse.isPressedIn(image_66):
                        result=2
                    if mouse.isPressedIn(image_67):
                        result=3    
                if num==0:
                    if button1_2.isClicked:
                        trials66.finished=True
                        trials77.finished=True
                    else:
                        trials66.finished=False
                continueRoutine=False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "feedback2"-------
            for thisComponent in feedback2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "feedback2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 99.0 repeats of 'trials66'
        
        
        # ------Prepare to start Routine "prare7_1"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        if button1_2.isClicked:
            continueRoutine=False
        else:
            continueRoutine=True
        import random
        pic2='pics/1.png'
        pic3='pics/2.png'
        pic4='pics/3.png'
        if result==1:
                clickresult=random.random()
                if clickresult<p3:
                    pic2='pics/empty.png' 
                else:
                    pic2='pics/gift.png' 
        elif result==2:
                clickresult=random.random()
                if clickresult<p4:
                    pic3='pics/empty.png'
                else:
                    pic3='pics/gift.png' 
        elif result==3:
                clickresult=random.random()
                if clickresult<p5:
                    pic4='pics/empty.png' 
                else:
                    pic4='pics/gift.png' 
        
        image_68.setImage(pic2)
        image_69.setImage(pic3)
        image_70.setImage(pic4)
        # keep track of which components have finished
        prare7_1Components = [image_68, image_69, image_70]
        for thisComponent in prare7_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        prare7_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prare7_1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = prare7_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prare7_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_68* updates
            if image_68.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_68.frameNStart = frameN  # exact frame index
                image_68.tStart = t  # local t and not account for scr refresh
                image_68.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_68, 'tStartRefresh')  # time at next scr refresh
                image_68.setAutoDraw(True)
            if image_68.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_68.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_68.tStop = t  # not accounting for scr refresh
                    image_68.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_68, 'tStopRefresh')  # time at next scr refresh
                    image_68.setAutoDraw(False)
            
            # *image_69* updates
            if image_69.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_69.frameNStart = frameN  # exact frame index
                image_69.tStart = t  # local t and not account for scr refresh
                image_69.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_69, 'tStartRefresh')  # time at next scr refresh
                image_69.setAutoDraw(True)
            if image_69.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_69.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_69.tStop = t  # not accounting for scr refresh
                    image_69.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_69, 'tStopRefresh')  # time at next scr refresh
                    image_69.setAutoDraw(False)
            
            # *image_70* updates
            if image_70.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_70.frameNStart = frameN  # exact frame index
                image_70.tStart = t  # local t and not account for scr refresh
                image_70.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_70, 'tStartRefresh')  # time at next scr refresh
                image_70.setAutoDraw(True)
            if image_70.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_70.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_70.tStop = t  # not accounting for scr refresh
                    image_70.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_70, 'tStopRefresh')  # time at next scr refresh
                    image_70.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prare7_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prare7_1"-------
        for thisComponent in prare7_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials77.addData('image_68.started', image_68.tStartRefresh)
        trials77.addData('image_68.stopped', image_68.tStopRefresh)
        trials77.addData('image_69.started', image_69.tStartRefresh)
        trials77.addData('image_69.stopped', image_69.tStopRefresh)
        trials77.addData('image_70.started', image_70.tStartRefresh)
        trials77.addData('image_70.stopped', image_70.tStopRefresh)
        num-=1
    # completed 11.0 repeats of 'trials77'
    
    
    # ------Prepare to start Routine "pra7chose"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_10
    mouse_10.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    pra7choseComponents = [image_71, image_72, image_73, mouse_10]
    for thisComponent in pra7choseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra7choseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pra7chose"-------
    while continueRoutine:
        # get current time
        t = pra7choseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra7choseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_71* updates
        if image_71.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_71.frameNStart = frameN  # exact frame index
            image_71.tStart = t  # local t and not account for scr refresh
            image_71.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_71, 'tStartRefresh')  # time at next scr refresh
            image_71.setAutoDraw(True)
        
        # *image_72* updates
        if image_72.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_72.frameNStart = frameN  # exact frame index
            image_72.tStart = t  # local t and not account for scr refresh
            image_72.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_72, 'tStartRefresh')  # time at next scr refresh
            image_72.setAutoDraw(True)
        
        # *image_73* updates
        if image_73.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_73.frameNStart = frameN  # exact frame index
            image_73.tStart = t  # local t and not account for scr refresh
            image_73.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_73, 'tStartRefresh')  # time at next scr refresh
            image_73.setAutoDraw(True)
        # *mouse_10* updates
        if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_10.frameNStart = frameN  # exact frame index
            mouse_10.tStart = t  # local t and not account for scr refresh
            mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
            mouse_10.status = STARTED
            mouse_10.mouseClock.reset()
            prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
        if mouse_10.status == STARTED:  # only update if started and not finished!
            buttons = mouse_10.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image_71,image_72,image_73])
                        clickableList = [image_71,image_72,image_73]
                    except:
                        clickableList = [[image_71,image_72,image_73]]
                    for obj in clickableList:
                        if obj.contains(mouse_10):
                            gotValidClick = True
                            mouse_10.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra7choseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra7chose"-------
    for thisComponent in pra7choseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('image_71.started', image_71.tStartRefresh)
    trials_5.addData('image_71.stopped', image_71.tStopRefresh)
    trials_5.addData('image_72.started', image_72.tStartRefresh)
    trials_5.addData('image_72.stopped', image_72.tStopRefresh)
    trials_5.addData('image_73.started', image_73.tStartRefresh)
    trials_5.addData('image_73.stopped', image_73.tStopRefresh)
    # store data for trials_5 (TrialHandler)
    x, y = mouse_10.getPos()
    buttons = mouse_10.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([image_71,image_72,image_73])
            clickableList = [image_71,image_72,image_73]
        except:
            clickableList = [[image_71,image_72,image_73]]
        for obj in clickableList:
            if obj.contains(mouse_10):
                gotValidClick = True
                mouse_10.clicked_name.append(obj.name)
    trials_5.addData('mouse_10.x', x)
    trials_5.addData('mouse_10.y', y)
    trials_5.addData('mouse_10.leftButton', buttons[0])
    trials_5.addData('mouse_10.midButton', buttons[1])
    trials_5.addData('mouse_10.rightButton', buttons[2])
    if len(mouse_10.clicked_name):
        trials_5.addData('mouse_10.clicked_name', mouse_10.clicked_name[0])
    trials_5.addData('mouse_10.started', mouse_10.tStart)
    trials_5.addData('mouse_10.stopped', mouse_10.tStop)
    # the Routine "pra7chose" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "confidence"-------
    continueRoutine = True
    # update component parameters for each repeat
    if mouse.getPressed():
     if mouse.isPressedIn(image_71):
        result=1
     if mouse.isPressedIn(image_72):
        result=2
     if mouse.isPressedIn(image_73):
        result=3
    slider.reset()
    # keep track of which components have finished
    confidenceComponents = [polygon, image_77, image_78, image_79, slider, button_3]
    for thisComponent in confidenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    confidenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "confidence"-------
    while continueRoutine:
        # get current time
        t = confidenceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=confidenceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:  # only update if drawing
            polygon.setPos((x, 0), log=False)
        if mouse.getPressed():
         if mouse.isPressedIn(image_71):
                x=-0.5
         elif mouse.isPressedIn(image_72):
                x=0 
         elif mouse.isPressedIn(image_73):
                x=0.5
        
        # *image_77* updates
        if image_77.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_77.frameNStart = frameN  # exact frame index
            image_77.tStart = t  # local t and not account for scr refresh
            image_77.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_77, 'tStartRefresh')  # time at next scr refresh
            image_77.setAutoDraw(True)
        
        # *image_78* updates
        if image_78.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_78.frameNStart = frameN  # exact frame index
            image_78.tStart = t  # local t and not account for scr refresh
            image_78.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_78, 'tStartRefresh')  # time at next scr refresh
            image_78.setAutoDraw(True)
        
        # *image_79* updates
        if image_79.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_79.frameNStart = frameN  # exact frame index
            image_79.tStart = t  # local t and not account for scr refresh
            image_79.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_79, 'tStartRefresh')  # time at next scr refresh
            image_79.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *button_3* updates
        if button_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_3.frameNStart = frameN  # exact frame index
            button_3.tStart = t  # local t and not account for scr refresh
            button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
            button_3.setAutoDraw(True)
        if button_3.status == STARTED:
            # check whether button_3 has been pressed
            if button_3.isClicked:
                if not button_3.wasClicked:
                    button_3.timesOn.append(button_3.buttonClock.getTime()) # store time of first click
                    button_3.timesOff.append(button_3.buttonClock.getTime()) # store time clicked until
                else:
                    button_3.timesOff[-1] = button_3.buttonClock.getTime() # update time clicked until
                if not button_3.wasClicked:
                    continueRoutine = False  # end routine when button_3 is clicked
                    None
                button_3.wasClicked = True  # if button_3 is still clicked next frame, it is not a new click
            else:
                button_3.wasClicked = False  # if button_3 is clicked next frame, it is a new click
        else:
            button_3.wasClicked = False  # if button_3 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "confidence"-------
    for thisComponent in confidenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('polygon.started', polygon.tStartRefresh)
    trials_5.addData('polygon.stopped', polygon.tStopRefresh)
    trials_5.addData('image_77.started', image_77.tStartRefresh)
    trials_5.addData('image_77.stopped', image_77.tStopRefresh)
    trials_5.addData('image_78.started', image_78.tStartRefresh)
    trials_5.addData('image_78.stopped', image_78.tStopRefresh)
    trials_5.addData('image_79.started', image_79.tStartRefresh)
    trials_5.addData('image_79.stopped', image_79.tStopRefresh)
    trials_5.addData('slider.response', slider.getRating())
    trials_5.addData('slider.rt', slider.getRT())
    trials_5.addData('slider.started', slider.tStartRefresh)
    trials_5.addData('slider.stopped', slider.tStopRefresh)
    trials_5.addData('button_3.started', button_3.tStartRefresh)
    trials_5.addData('button_3.stopped', button_3.tStopRefresh)
    trials_5.addData('button_3.numClicks', button_3.numClicks)
    if button_3.numClicks:
       trials_5.addData('button_3.timesOn', button_3.timesOn)
       trials_5.addData('button_3.timesOff', button_3.timesOff)
    else:
       trials_5.addData('button_3.timesOn', "")
       trials_5.addData('button_3.timesOff', "")
    # the Routine "confidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "prare7__"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    import random
    pic2='pics/1.png'
    pic3='pics/2.png'
    pic4='pics/3.png'
    if result==1:
            clickresult=random.random()
            if clickresult<p3:
                pic2='pics/empty.png' 
            else:
                pic2='pics/gift.png' 
    elif result==2:
            clickresult=random.random()
            if clickresult<p4:
                pic3='pics/empty.png'
            else:
                pic3='pics/gift.png' 
    elif result==3:
            clickresult=random.random()
            if clickresult<p5:
                pic4='pics/empty.png' 
            else:
                pic4='pics/gift.png' 
    continueRoutine=True
    image_74.setImage(pic2)
    image_75.setImage(pic3)
    image_76.setImage(pic4)
    # keep track of which components have finished
    prare7__Components = [image_74, image_75, image_76]
    for thisComponent in prare7__Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prare7__Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prare7__"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prare7__Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prare7__Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_74* updates
        if image_74.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_74.frameNStart = frameN  # exact frame index
            image_74.tStart = t  # local t and not account for scr refresh
            image_74.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_74, 'tStartRefresh')  # time at next scr refresh
            image_74.setAutoDraw(True)
        if image_74.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_74.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_74.tStop = t  # not accounting for scr refresh
                image_74.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_74, 'tStopRefresh')  # time at next scr refresh
                image_74.setAutoDraw(False)
        
        # *image_75* updates
        if image_75.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_75.frameNStart = frameN  # exact frame index
            image_75.tStart = t  # local t and not account for scr refresh
            image_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_75, 'tStartRefresh')  # time at next scr refresh
            image_75.setAutoDraw(True)
        if image_75.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_75.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_75.tStop = t  # not accounting for scr refresh
                image_75.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_75, 'tStopRefresh')  # time at next scr refresh
                image_75.setAutoDraw(False)
        
        # *image_76* updates
        if image_76.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_76.frameNStart = frameN  # exact frame index
            image_76.tStart = t  # local t and not account for scr refresh
            image_76.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_76, 'tStartRefresh')  # time at next scr refresh
            image_76.setAutoDraw(True)
        if image_76.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_76.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_76.tStop = t  # not accounting for scr refresh
                image_76.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_76, 'tStopRefresh')  # time at next scr refresh
                image_76.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prare7__Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prare7__"-------
    for thisComponent in prare7__Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('image_74.started', image_74.tStartRefresh)
    trials_5.addData('image_74.stopped', image_74.tStopRefresh)
    trials_5.addData('image_75.started', image_75.tStartRefresh)
    trials_5.addData('image_75.stopped', image_75.tStopRefresh)
    trials_5.addData('image_76.started', image_76.tStartRefresh)
    trials_5.addData('image_76.stopped', image_76.tStopRefresh)
# completed 5.0 repeats of 'trials_5'


# ------Prepare to start Routine "ins9"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
ins9Components = [image_15, key_resp_9]
for thisComponent in ins9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins9"-------
while continueRoutine:
    # get current time
    t = ins9Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins9Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_15* updates
    if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_15.frameNStart = frameN  # exact frame index
        image_15.tStart = t  # local t and not account for scr refresh
        image_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
        image_15.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins9"-------
for thisComponent in ins9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_15.started', image_15.tStartRefresh)
thisExp.addData('image_15.stopped', image_15.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "ins9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
