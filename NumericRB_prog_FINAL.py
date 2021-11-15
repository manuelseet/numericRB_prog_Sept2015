#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), August 29, 2016, at 08:49
"""


"""
######################################################################
Manuel Seet - September 2015 - Talented Student Programme Research Component
#####################################################################

Programme Scaffold was designed and initially created via Psychopy experiment builder
Modified code of specific stimuli below to fine tune experimental display parameters 
and restructure sequence flow based on literature recommendations and best practices


Tested and verified effect of forward and backwards visual masking of similar visual spatial frequency 
Tested and verified presence of RB effect with repetition as experimental baseline
RSVP frame rate was iteratively calibrated with a sample of participants prior to testing
-- currently 

TRIAL SEQUENCE
Each trial began with a blank screen for 585 ms (50 frames) 
before a mask was displayed for approximately 1170 ms (100 frames). 
Four test stimuli were then presented one after the other, 
lasting 106 ms (9 frames) apiece. 
Another mask marking the end of the RSVP stream was presented for 1170 ms (100 frames). 

PRACTICE TRIALS
Fifteen practice trials were presented at the beginning of the testing session. 
The first five trials were conducted at 471 ms (40 frames) apiece, 
next five at approximately 129 ms (11 frames) apiece  
last five at approximately 106 (9 frames) apiece. 
In all practice trials, duration of forward and backward masks was kept at 1170 (100 frames) each


NOTE:
All pictures and picture masks were presented centrally on screen, 
with a maximum height and width having a visual angle of 7.4 degrees subtended at the eye, 
viewed at approximately 50 cm from the screen

All words and masks were presented centrally on screen in Arial, 
with the height of all words kept at approximately 2.0 degrees of visual angle

Experimental Procedure
Participants were individually tested in a room under normal lighting conditions
Stimuli were displayed on a Trinitron G520 CRT monitor (Sony Corporation, Tokyo, Japan), 
set to a spatial resolution of 1024 × 768 and a screen refresh rate of 85 Hz
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'semantic experiment'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Manuel\\Desktop\\Psychopy\\Numbers experimenttr.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions = visual.TextStim(win=win, ori=0, name='instructions',
    text=u'Welcome to the experiment.\n\nPlease press the spacebar to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instrc_2"
instrc_2Clock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=u'You will be presented with a series of words or images. Immediately after the end of each trial, please report the words or pictures to the experimenter in order you saw them.\n\nPress the spacebar to begin your practice trials.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "prac1"
prac1Clock = core.Clock()
text_31 = visual.TextStim(win=win, ori=0, name='text_31',
    text=u'%%%%%%%',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_32 = visual.TextStim(win=win, ori=0, name='text_32',
    text=u'>>>>>',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_33 = visual.TextStim(win=win, ori=0, name='text_33',
    text=u'*****',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
dist1a = visual.TextStim(win=win, ori=0, name='dist1a',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)
crit1a = visual.TextStim(win=win, ori=0, name='crit1a',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
dist2a = visual.TextStim(win=win, ori=0, name='dist2a',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)
crit2a = visual.TextStim(win=win, ori=0, name='crit2a',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0)
dist3a = visual.TextStim(win=win, ori=0, name='dist3a',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-7.0)
endmaska = visual.TextStim(win=win, ori=0, name='endmaska',
    text=u'%%%%%%%',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-8.0)
text_34 = visual.TextStim(win=win, ori=0, name='text_34',
    text=u'Please report the items in the order you saw them. \n\nSay the item twice if you saw it twice.\n\n\nPress the spacebar to continue after reporting',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-9.0)

# Initialize components for Routine "instrc_3"
instrc_3Clock = core.Clock()
text_35 = visual.TextStim(win=win, ori=0, name='text_35',
    text=u'The stream will now be presented at a faster rate.\n\nPress the spacebar to begin the practice.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "prac2"
prac2Clock = core.Clock()
text_16 = visual.TextStim(win=win, ori=0, name='text_16',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_17 = visual.TextStim(win=win, ori=0, name='text_17',
    text=')))))',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_18 = visual.TextStim(win=win, ori=0, name='text_18',
    text='*****',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_19 = visual.TextStim(win=win, ori=0, name='text_19',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
text_20 = visual.TextStim(win=win, ori=0, name='text_20',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
text_21 = visual.TextStim(win=win, ori=0, name='text_21',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
text_22 = visual.TextStim(win=win, ori=0, name='text_22',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
text_23 = visual.TextStim(win=win, ori=0, name='text_23',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
text_24 = visual.TextStim(win=win, ori=0, name='text_24',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0)
text_25 = visual.TextStim(win=win, ori=0, name='text_25',
    text='Please report the items in the order you saw them. \n\nSay the item twice if you saw it twice.\n\n\nPress the spacebar to continue after reporting',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)

# Initialize components for Routine "instrc_4"
instrc_4Clock = core.Clock()
text_36 = visual.TextStim(win=win, ori=0, name='text_36',
    text=u'The stream will be presented at an even faster rate. This is will be the rate for the entire experiment.\n\nPress the spacebar to begin the practice.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "prac3_2"
prac3_2Clock = core.Clock()
text_26 = visual.TextStim(win=win, ori=0, name='text_26',
    text=u'%%%%%%%',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_27 = visual.TextStim(win=win, ori=0, name='text_27',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_28 = visual.TextStim(win=win, ori=0, name='text_28',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
dist1 = visual.TextStim(win=win, ori=0, name='dist1',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)
crit1 = visual.TextStim(win=win, ori=0, name='crit1',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
dist2 = visual.TextStim(win=win, ori=0, name='dist2',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)
crit2 = visual.TextStim(win=win, ori=0, name='crit2',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0)
dist3 = visual.TextStim(win=win, ori=0, name='dist3',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-7.0)
text_29 = visual.TextStim(win=win, ori=0, name='text_29',
    text=u'%%%%%%%',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-8.0)
text_30 = visual.TextStim(win=win, ori=0, name='text_30',
    text=u'Please report the items in the order you saw them. \n\nSay the item twice if you saw it twice.\n\n\nPress the spacebar to continue after reporting',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-9.0)

# Initialize components for Routine "instr_real"
instr_realClock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text=u'This marks the end of your practice trials.\n\nPress the spacebar to begin the experiment.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
fixmask1 = visual.TextStim(win=win, ori=0, name='fixmask1',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='#####',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='******',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
d1 = visual.TextStim(win=win, ori=0, name='d1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
c1 = visual.TextStim(win=win, ori=0, name='c1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
d2 = visual.TextStim(win=win, ori=0, name='d2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
c2 = visual.TextStim(win=win, ori=0, name='c2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
d3 = visual.TextStim(win=win, ori=0, name='d3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0)
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text=u'Please report the items in the order you saw them. \n\nSay the item twice if you saw it twice.\n\n\nPress the spacebar to continue after reporting',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'This marks the end of the experiment. \n\nThank you for your participation.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_start = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_start.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(instructions)
InstructionsComponents.append(key_resp_start)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if t >= 0.0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t  # underestimates by a little under one frame
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)
    
    # *key_resp_start* updates
    if t >= 0.0 and key_resp_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_start.tStart = t  # underestimates by a little under one frame
        key_resp_start.frameNStart = frameN  # exact frame index
        key_resp_start.status = STARTED
        # keyboard checking is just starting
        key_resp_start.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_start.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_start.keys = theseKeys[-1]  # just the last key pressed
            key_resp_start.rt = key_resp_start.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_start.keys in ['', [], None]:  # No response was made
   key_resp_start.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_start.keys',key_resp_start.keys)
if key_resp_start.keys != None:  # we had a response
    thisExp.addData('key_resp_start.rt', key_resp_start.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instrc_2"-------
t = 0
instrc_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
instrc_2Components = []
instrc_2Components.append(text_4)
instrc_2Components.append(key_resp_5)
for thisComponent in instrc_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrc_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrc_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrc_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrc_2"-------
for thisComponent in instrc_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "instrc_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\Manuel\\Desktop\\Psychopy\\Numbers experimenttr.psyexp',
    trialList=data.importConditions(u'Prac.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4.keys():
        exec(paramName + '= thisTrial_4.' + paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    #------Prepare to start Routine "prac1"-------
    t = 0
    prac1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    dist1a.setText(D1a)
    crit1a.setText(C1a)
    dist2a.setText(D2a)
    crit2a.setText(C2a)
    dist3a.setText(D3a)
    key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_10.status = NOT_STARTED
    # keep track of which components have finished
    prac1Components = []
    prac1Components.append(text_31)
    prac1Components.append(text_32)
    prac1Components.append(text_33)
    prac1Components.append(dist1a)
    prac1Components.append(crit1a)
    prac1Components.append(dist2a)
    prac1Components.append(crit2a)
    prac1Components.append(dist3a)
    prac1Components.append(endmaska)
    prac1Components.append(text_34)
    prac1Components.append(key_resp_10)
    for thisComponent in prac1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "prac1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = prac1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_31* updates
        if t >= 1 and text_31.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_31.tStart = t  # underestimates by a little under one frame
            text_31.frameNStart = frameN  # exact frame index
            text_31.setAutoDraw(True)
        if text_31.status == STARTED and t >= (1 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_31.setAutoDraw(False)
        
        # *text_32* updates
        if t >= 2 and text_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_32.tStart = t  # underestimates by a little under one frame
            text_32.frameNStart = frameN  # exact frame index
            text_32.setAutoDraw(True)
        if text_32.status == STARTED and t >= (2 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_32.setAutoDraw(False)
        
        # *text_33* updates
        if t >= 2.5 and text_33.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_33.tStart = t  # underestimates by a little under one frame
            text_33.frameNStart = frameN  # exact frame index
            text_33.setAutoDraw(True)
        if text_33.status == STARTED and t >= (2.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_33.setAutoDraw(False)
        
        # *dist1a* updates
        if t >= 3.0 and dist1a.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist1a.tStart = t  # underestimates by a little under one frame
            dist1a.frameNStart = frameN  # exact frame index
            dist1a.setAutoDraw(True)
        if dist1a.status == STARTED and t >= (3.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist1a.setAutoDraw(False)
        
        # *crit1a* updates
        if t >= 3.5 and crit1a.status == NOT_STARTED:
            # keep track of start time/frame for later
            crit1a.tStart = t  # underestimates by a little under one frame
            crit1a.frameNStart = frameN  # exact frame index
            crit1a.setAutoDraw(True)
        if crit1a.status == STARTED and t >= (3.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            crit1a.setAutoDraw(False)
        
        # *dist2a* updates
        if t >= 4 and dist2a.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist2a.tStart = t  # underestimates by a little under one frame
            dist2a.frameNStart = frameN  # exact frame index
            dist2a.setAutoDraw(True)
        if dist2a.status == STARTED and t >= (4 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist2a.setAutoDraw(False)
        
        # *crit2a* updates
        if t >= 4.5 and crit2a.status == NOT_STARTED:
            # keep track of start time/frame for later
            crit2a.tStart = t  # underestimates by a little under one frame
            crit2a.frameNStart = frameN  # exact frame index
            crit2a.setAutoDraw(True)
        if crit2a.status == STARTED and t >= (4.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            crit2a.setAutoDraw(False)
        
        # *dist3a* updates
        if t >= 5 and dist3a.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist3a.tStart = t  # underestimates by a little under one frame
            dist3a.frameNStart = frameN  # exact frame index
            dist3a.setAutoDraw(True)
        if dist3a.status == STARTED and t >= (5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist3a.setAutoDraw(False)
        
        # *endmaska* updates
        if t >= 5.5 and endmaska.status == NOT_STARTED:
            # keep track of start time/frame for later
            endmaska.tStart = t  # underestimates by a little under one frame
            endmaska.frameNStart = frameN  # exact frame index
            endmaska.setAutoDraw(True)
        if endmaska.status == STARTED and t >= (5.5 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            endmaska.setAutoDraw(False)
        
        # *text_34* updates
        if t >= 6.5 and text_34.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_34.tStart = t  # underestimates by a little under one frame
            text_34.frameNStart = frameN  # exact frame index
            text_34.setAutoDraw(True)
        
        # *key_resp_10* updates
        if t >= 6.5 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # underestimates by a little under one frame
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            key_resp_10.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_10.keys = theseKeys[-1]  # just the last key pressed
                key_resp_10.rt = key_resp_10.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "prac1"-------
    for thisComponent in prac1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
       key_resp_10.keys=None
    # store data for trials_4 (TrialHandler)
    trials_4.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        trials_4.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "prac1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


#------Prepare to start Routine "instrc_3"-------
t = 0
instrc_3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_11.status = NOT_STARTED
# keep track of which components have finished
instrc_3Components = []
instrc_3Components.append(text_35)
instrc_3Components.append(key_resp_11)
for thisComponent in instrc_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrc_3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrc_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_35* updates
    if t >= 0.0 and text_35.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_35.tStart = t  # underestimates by a little under one frame
        text_35.frameNStart = frameN  # exact frame index
        text_35.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t  # underestimates by a little under one frame
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        key_resp_11.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrc_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrc_3"-------
for thisComponent in instrc_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
   key_resp_11.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "instrc_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\Manuel\\Desktop\\Psychopy\\Numbers experimenttr.psyexp',
    trialList=data.importConditions('Prac.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "prac2"-------
    t = 0
    prac2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    text_19.setText(D1b)
    text_20.setText(C1b)
    text_21.setText(D2b
)
    text_22.setText(C2b)
    text_23.setText(D3b)
    key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_8.status = NOT_STARTED
    # keep track of which components have finished
    prac2Components = []
    prac2Components.append(text_16)
    prac2Components.append(text_17)
    prac2Components.append(text_18)
    prac2Components.append(text_19)
    prac2Components.append(text_20)
    prac2Components.append(text_21)
    prac2Components.append(text_22)
    prac2Components.append(text_23)
    prac2Components.append(text_24)
    prac2Components.append(text_25)
    prac2Components.append(key_resp_8)
    for thisComponent in prac2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "prac2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = prac2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_16* updates
        if t >= 1 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t  # underestimates by a little under one frame
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        if text_16.status == STARTED and t >= (1 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_16.setAutoDraw(False)
        
        # *text_17* updates
        if t >= 2 and text_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_17.tStart = t  # underestimates by a little under one frame
            text_17.frameNStart = frameN  # exact frame index
            text_17.setAutoDraw(True)
        if text_17.status == STARTED and t >= (2 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_17.setAutoDraw(False)
        
        # *text_18* updates
        if t >= 2.125 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t  # underestimates by a little under one frame
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        if text_18.status == STARTED and t >= (2.125 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_18.setAutoDraw(False)
        
        # *text_19* updates
        if t >= 2.25 and text_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_19.tStart = t  # underestimates by a little under one frame
            text_19.frameNStart = frameN  # exact frame index
            text_19.setAutoDraw(True)
        if text_19.status == STARTED and t >= (2.25 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_19.setAutoDraw(False)
        
        # *text_20* updates
        if t >= 2.375 and text_20.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_20.tStart = t  # underestimates by a little under one frame
            text_20.frameNStart = frameN  # exact frame index
            text_20.setAutoDraw(True)
        if text_20.status == STARTED and t >= (2.375 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_20.setAutoDraw(False)
        
        # *text_21* updates
        if t >= 2.50 and text_21.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_21.tStart = t  # underestimates by a little under one frame
            text_21.frameNStart = frameN  # exact frame index
            text_21.setAutoDraw(True)
        if text_21.status == STARTED and t >= (2.50 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_21.setAutoDraw(False)
        
        # *text_22* updates
        if t >= 2.625 and text_22.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_22.tStart = t  # underestimates by a little under one frame
            text_22.frameNStart = frameN  # exact frame index
            text_22.setAutoDraw(True)
        if text_22.status == STARTED and t >= (2.625 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_22.setAutoDraw(False)
        
        # *text_23* updates
        if t >= 2.750 and text_23.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_23.tStart = t  # underestimates by a little under one frame
            text_23.frameNStart = frameN  # exact frame index
            text_23.setAutoDraw(True)
        if text_23.status == STARTED and t >= (2.750 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_23.setAutoDraw(False)
        
        # *text_24* updates
        if t >= 2.875 and text_24.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_24.tStart = t  # underestimates by a little under one frame
            text_24.frameNStart = frameN  # exact frame index
            text_24.setAutoDraw(True)
        if text_24.status == STARTED and t >= (2.875 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_24.setAutoDraw(False)
        
        # *text_25* updates
        if t >= 3.875 and text_25.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_25.tStart = t  # underestimates by a little under one frame
            text_25.frameNStart = frameN  # exact frame index
            text_25.setAutoDraw(True)
        
        # *key_resp_8* updates
        if t >= 3.875 and key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t  # underestimates by a little under one frame
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            key_resp_8.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_8.keys = theseKeys[-1]  # just the last key pressed
                key_resp_8.rt = key_resp_8.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "prac2"-------
    for thisComponent in prac2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
       key_resp_8.keys=None
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        trials_3.addData('key_resp_8.rt', key_resp_8.rt)
    # the Routine "prac2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


#------Prepare to start Routine "instrc_4"-------
t = 0
instrc_4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_12.status = NOT_STARTED
# keep track of which components have finished
instrc_4Components = []
instrc_4Components.append(text_36)
instrc_4Components.append(key_resp_12)
for thisComponent in instrc_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrc_4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrc_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_36* updates
    if t >= 0.0 and text_36.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_36.tStart = t  # underestimates by a little under one frame
        text_36.frameNStart = frameN  # exact frame index
        text_36.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # underestimates by a little under one frame
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        key_resp_12.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_12.keys = theseKeys[-1]  # just the last key pressed
            key_resp_12.rt = key_resp_12.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrc_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrc_4"-------
for thisComponent in instrc_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
   key_resp_12.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()
# the Routine "instrc_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\Manuel\\Desktop\\Psychopy\\Numbers experimenttr.psyexp',
    trialList=data.importConditions(u'Prac.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "prac3_2"-------
    t = 0
    prac3_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    text_27.setText(u'))))))')
    text_28.setText(u'******')
    dist1.setText(D1c)
    crit1.setText(C1c)
    dist2.setText(D2c)
    crit2.setText(C2c)
    dist3.setText(D3c)
    key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_9.status = NOT_STARTED
    # keep track of which components have finished
    prac3_2Components = []
    prac3_2Components.append(text_26)
    prac3_2Components.append(text_27)
    prac3_2Components.append(text_28)
    prac3_2Components.append(dist1)
    prac3_2Components.append(crit1)
    prac3_2Components.append(dist2)
    prac3_2Components.append(crit2)
    prac3_2Components.append(dist3)
    prac3_2Components.append(text_29)
    prac3_2Components.append(text_30)
    prac3_2Components.append(key_resp_9)
    for thisComponent in prac3_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "prac3_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = prac3_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_26* updates
        if t >= 1 and text_26.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_26.tStart = t  # underestimates by a little under one frame
            text_26.frameNStart = frameN  # exact frame index
            text_26.setAutoDraw(True)
        if text_26.status == STARTED and t >= (1 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_26.setAutoDraw(False)
        
        # *text_27* updates
        if t >= 2 and text_27.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_27.tStart = t  # underestimates by a little under one frame
            text_27.frameNStart = frameN  # exact frame index
            text_27.setAutoDraw(True)
        if text_27.status == STARTED and t >= (2 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_27.setAutoDraw(False)
        
        # *text_28* updates
        if t >= 2.1 and text_28.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_28.tStart = t  # underestimates by a little under one frame
            text_28.frameNStart = frameN  # exact frame index
            text_28.setAutoDraw(True)
        if text_28.status == STARTED and t >= (2.1 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_28.setAutoDraw(False)
        
        # *dist1* updates
        if t >= 2.2 and dist1.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist1.tStart = t  # underestimates by a little under one frame
            dist1.frameNStart = frameN  # exact frame index
            dist1.setAutoDraw(True)
        if dist1.status == STARTED and t >= (2.2 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist1.setAutoDraw(False)
        
        # *crit1* updates
        if t >= 2.3 and crit1.status == NOT_STARTED:
            # keep track of start time/frame for later
            crit1.tStart = t  # underestimates by a little under one frame
            crit1.frameNStart = frameN  # exact frame index
            crit1.setAutoDraw(True)
        if crit1.status == STARTED and t >= (2.3 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            crit1.setAutoDraw(False)
        
        # *dist2* updates
        if t >= 2.4 and dist2.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist2.tStart = t  # underestimates by a little under one frame
            dist2.frameNStart = frameN  # exact frame index
            dist2.setAutoDraw(True)
        if dist2.status == STARTED and t >= (2.4 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist2.setAutoDraw(False)
        
        # *crit2* updates
        if t >= 2.5 and crit2.status == NOT_STARTED:
            # keep track of start time/frame for later
            crit2.tStart = t  # underestimates by a little under one frame
            crit2.frameNStart = frameN  # exact frame index
            crit2.setAutoDraw(True)
        if crit2.status == STARTED and t >= (2.5 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            crit2.setAutoDraw(False)
        
        # *dist3* updates
        if t >= 2.6 and dist3.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist3.tStart = t  # underestimates by a little under one frame
            dist3.frameNStart = frameN  # exact frame index
            dist3.setAutoDraw(True)
        if dist3.status == STARTED and t >= (2.6 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist3.setAutoDraw(False)
        
        # *text_29* updates
        if t >= 2.7 and text_29.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_29.tStart = t  # underestimates by a little under one frame
            text_29.frameNStart = frameN  # exact frame index
            text_29.setAutoDraw(True)
        if text_29.status == STARTED and t >= (2.7 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_29.setAutoDraw(False)
        
        # *text_30* updates
        if t >= 3.7 and text_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_30.tStart = t  # underestimates by a little under one frame
            text_30.frameNStart = frameN  # exact frame index
            text_30.setAutoDraw(True)
        
        # *key_resp_9* updates
        if t >= 3.7 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t  # underestimates by a little under one frame
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            key_resp_9.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys = theseKeys[-1]  # just the last key pressed
                key_resp_9.rt = key_resp_9.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac3_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "prac3_2"-------
    for thisComponent in prac3_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
       key_resp_9.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        trials.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "prac3_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "instr_real"-------
t = 0
instr_realClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
instr_realComponents = []
instr_realComponents.append(text_6)
instr_realComponents.append(key_resp_6)
for thisComponent in instr_realComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr_real"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr_realClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        key_resp_6.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_realComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr_real"-------
for thisComponent in instr_realComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
   key_resp_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "instr_real" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\Manuel\\Desktop\\Psychopy\\Numbers experimenttr.psyexp',
    trialList=data.importConditions('v1.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    d1.setText(D1)
    c1.setText(C1a)
    d2.setText(D2)
    c2.setText(C2a)
    d3.setText(D3)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(fixmask1)
    trialComponents.append(text_2)
    trialComponents.append(text_3)
    trialComponents.append(d1)
    trialComponents.append(c1)
    trialComponents.append(d2)
    trialComponents.append(c2)
    trialComponents.append(d3)
    trialComponents.append(text_9)
    trialComponents.append(text_10)
    trialComponents.append(key_resp_2)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixmask1* updates
        if t >= 1.0 and fixmask1.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixmask1.tStart = t  # underestimates by a little under one frame
            fixmask1.frameNStart = frameN  # exact frame index
            fixmask1.setAutoDraw(True)
        if fixmask1.status == STARTED and t >= (1.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixmask1.setAutoDraw(False)
        
        # *text_2* updates
        if t >= 2.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        if text_2.status == STARTED and t >= (2.0 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # *text_3* updates
        if t >= 2.1 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        if text_3.status == STARTED and t >= (2.1 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # *d1* updates
        if t >= 2.2 and d1.status == NOT_STARTED:
            # keep track of start time/frame for later
            d1.tStart = t  # underestimates by a little under one frame
            d1.frameNStart = frameN  # exact frame index
            d1.setAutoDraw(True)
        if d1.status == STARTED and t >= (2.2 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            d1.setAutoDraw(False)
        
        # *c1* updates
        if t >= 2.3 and c1.status == NOT_STARTED:
            # keep track of start time/frame for later
            c1.tStart = t  # underestimates by a little under one frame
            c1.frameNStart = frameN  # exact frame index
            c1.setAutoDraw(True)
        if c1.status == STARTED and t >= (2.3 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            c1.setAutoDraw(False)
        
        # *d2* updates
        if t >= 2.4 and d2.status == NOT_STARTED:
            # keep track of start time/frame for later
            d2.tStart = t  # underestimates by a little under one frame
            d2.frameNStart = frameN  # exact frame index
            d2.setAutoDraw(True)
        if d2.status == STARTED and t >= (2.4 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            d2.setAutoDraw(False)
        
        # *c2* updates
        if t >= 2.5 and c2.status == NOT_STARTED:
            # keep track of start time/frame for later
            c2.tStart = t  # underestimates by a little under one frame
            c2.frameNStart = frameN  # exact frame index
            c2.setAutoDraw(True)
        if c2.status == STARTED and t >= (2.5 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            c2.setAutoDraw(False)
        
        # *d3* updates
        if t >= 2.6 and d3.status == NOT_STARTED:
            # keep track of start time/frame for later
            d3.tStart = t  # underestimates by a little under one frame
            d3.frameNStart = frameN  # exact frame index
            d3.setAutoDraw(True)
        if d3.status == STARTED and t >= (2.6 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            d3.setAutoDraw(False)
        
        # *text_9* updates
        if t >= 2.7 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t  # underestimates by a little under one frame
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        if text_9.status == STARTED and t >= (2.7 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_9.setAutoDraw(False)
        
        # *text_10* updates
        if t >= 3.70 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 3.70 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(text)
endComponents.append(key_resp_3)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.close()
core.quit()
