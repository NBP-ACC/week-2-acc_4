import os
import sys
import pygame
from math import atan2,degrees


#Initialise pygame
pygame.init()
#small screen size
SCREENSIZE = (800,600)
#Get current resolution of screen
infoObject = pygame.display.Info()
#set screen size based on size of monitor
SCREEN = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
# SCREEN = pygame.display.set_mode(SCREENSIZE)
# SCREEN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)


#Get width and height of the screen at fullscreen mode
WIDTH, HEIGHT = SCREEN.get_size()

# distance of subject from SCREEN
distance = 30
# get visual degrees for x and y dimensions (can be different \
# for different resolutions of the monitor)
ydegree_per_px = degrees(atan2(.5*HEIGHT, distance)) / (.5*infoObject.current_h)
xdegree_per_px = degrees(atan2(.5*WIDTH, distance)) / (.5*infoObject.current_w)

#set radius of the stimulus circle
RADIUS = int(round(5/ydegree_per_px))

#set center point of the screen
(Cx,Cy) = (int(round(WIDTH/2)), int(round(HEIGHT/2)))

#set length of the fixation cross
crosslen = 1.6/ydegree_per_px
VLINE = [(Cx,Cy - crosslen), (Cx, Cy + crosslen), 4]
HLINE = [(Cx - crosslen,Cy), (Cx + crosslen, Cy), 4]

#Default colors for the stimulus and text
WHITE = (255,255,255)
BLACK = (0,0,0)
NOGO_COLOR = (255, 0 , 0)
GO_COLOR = (0, 255, 0)

#Set color of background
BG_COLOR = (123,123,123)

#Set fontsize of the text
FONTSIZE = 60
# Set number of trials in the experiment
# How should you name the variable?
# Use the same name as in main
NUMTRIAL = 100

# Set number of nogo trials in the experiment
# How should you name the variable?
# The NoGo trials are used as a percentage in the main file
# Therefore it has to be 1/6 to get 20 NoGo Trials in 120 Trials
PCT_NOGO = 0.2

# Set the time interval in seconds of the delay
# from end of trial n and beginning of trial n+1
TRIALINTERVAL = 1

#Set the time interval in milliseconds of the delay
#from end of trial n and beginning of trial n+1
TRIALINTERVAL = 500

#Frames per second of the experiment
FPS = 60

# Create a directory called 'Data' in your working-directory
# where the experiment data for each subject is saved
# before creating it check if the directory 'Data' already exists
# define where to save the data
dirName = "C:/Users/Sophia/Documents/GitHub/week-2-acc_4/Data"
# check whether the folder Data allready exists
# if no than create it
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
# if yes print a message to let me know
else:
    print("Directory " , dirName ,  " already exists")
