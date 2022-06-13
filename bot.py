import pyautogui, time
from bot_utils import lclick, rclick, switchPaths, goIn

goRight = [1010, 575]
boxRight = [1010, 550]
goLeft = [905, 515]
boxLeft = [915, 490]
goUp = [1000, 520]
boxUp = [1000, 495]
goDown = [920, 570]
boxDown = [920, 545]
lastDig = "up"

def digUp():
    global lastDig
    rclick(goUp[0], goUp[1])
    time.sleep(0.2)
    rclick(boxUp[0], boxUp[1])
    pyautogui.moveTo(831, 1050)
    checkEnd()
    lclick(goUp[0], goUp[1])
    pyautogui.moveTo(831, 1050)
    time.sleep(0.3)
    lastDig = "up"

def digDown():
    global lastDig
    rclick(goDown[0], goDown[1])
    time.sleep(0.2)
    rclick(boxDown[0], boxDown[1])
    pyautogui.moveTo(831, 1050)
    checkEnd()
    lclick(goDown[0], goDown[1])
    pyautogui.moveTo(831, 1050)
    time.sleep(0.3)
    lastDig = "down"

def digLeft():
    global lastDig
    rclick(goLeft[0], goLeft[1])
    time.sleep(0.2)
    rclick(boxLeft[0], boxLeft[1])
    pyautogui.moveTo(831, 1050)
    checkEnd()
    lclick(goLeft[0], goLeft[1])
    pyautogui.moveTo(831, 1050)
    time.sleep(0.3)
    lastDig = "left"

def digRight():
    global lastDig
    rclick(goRight[0], goRight[1])
    time.sleep(0.2)
    rclick(boxRight[0], boxRight[1])
    pyautogui.moveTo(831, 1050) 
    checkEnd()
    lclick(goRight[0], goRight[1])
    pyautogui.moveTo(831, 1050)
    time.sleep(0.3)
    lastDig = "right"

def checkEnd():
    switch = 0
    for i in range(115):
        if (lastDig == "up"):
            r,g,b = pyautogui.pixel(1141 , 335)
        elif (lastDig == "down"):
            r,g,b = pyautogui.pixel(1255, 275)
        elif (lastDig == "left"):
            r,g,b = pyautogui.pixel(1255, 335)
        elif (lastDig == "right"):
            r,g,b = pyautogui.pixel(1142, 274)
        if ((g >= 220 and b >= 220)):
            switch = 1
            break
    if (switch == 1):
        time.sleep(3)
        start()
        
def dig(direction, iterations):
    if (direction == "up"):
        for i in range(iterations):
            digUp()
    elif (direction == "left"):
        for i in range(iterations):
            digLeft()
    elif (direction == "right"):
        for i in range(iterations):
            digRight()
    elif (direction == "down"):
        for i in range(iterations):
            digDown()

def start():
    goIn()
    dig("up", 2)
    dig("right", 2)
    switchPaths()
    dig("right", 6)
    dig("down", 6)
    dig("left", 1)
    dig("up", 5)
    dig("left", 1)
    time.sleep(3)
    start()

time.sleep(2)
start()

