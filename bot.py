from turtle import up
from pyautogui import *
import pyautogui, time, keyboard, random, win32api, win32con
import numpy as np

goRight = [1035, 580]
boxRight = [1035, 550]
goLeft = [890, 510]
boxLeft = [890, 480]
goUp = [1040, 510]
boxUp = [1040, 480]
goDown = [900, 580]
boxDown = [900, 550]
door = [1000, 500]
openDoor = [1000, 470]


def lclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def rclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def startDig():
    rclick(door[0], door[1])
    time.sleep(0.5)
    lclick(openDoor[0], openDoor[1])

def digUp():
    rclick(goUp[0], goUp[1])
    time.sleep(0.5)
    lclick(boxUp[0], boxUp[1])
    time.sleep(2)

def digDown():
    rclick(goDown[0], goDown[1])
    time.sleep(0.5)
    lclick(boxDown[0], boxDown[1])
    time.sleep(2)

def digLeft():
    rclick(goLeft[0], goLeft[1])
    time.sleep(0.5)
    lclick(boxLeft[0], boxLeft[1])
    time.sleep(2)

def digRight():
    rclick(goRight[0], goRight[1])
    time.sleep(0.5)
    lclick(boxRight[0], boxRight[1])
    time.sleep(2)

def doPath():
    startDig()
    lclick(goUp[0], goUp[1])
    time.sleep(1)
    digUp()
    digUp()
    digRight()
    digRight()
    lclick(goRight[0], goRight[1])
    time.sleep(0.5)
    lclick(goDown[0], goDown[1])
    time.sleep(0.5)
    digRight()
    digRight()
    digRight()
    digUp()
    digRight()
    digRight()
    digDown()
    digRight()



# while keyboard.is_pressed('q') == False:
#     pyautogui.displayMousePosition()
    
doPath()