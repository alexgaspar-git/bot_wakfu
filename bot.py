import pyautogui, time
from bot_utils import switchPaths, goIn, clickBox, goNext

goRight = [1010, 575]
goLeft = [905, 515]
goUp = [1000, 520]
goDown = [920, 570]
lastDig = "up"

def digDir(direction):
    global lastDig
    if (direction == "left"):
        dir = goLeft
    elif (direction == "right"):
        dir = goRight
    elif (direction == "down"):
        dir = goDown
    elif (direction == "up"):
        dir = goUp
    clickBox(dir)
    checkEnd()
    goNext(dir)
    lastDig = direction

def checkEnd():
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
            time.sleep(3)
            start()
        
def dig(direction, iterations):
    if (direction == "up"):
        for i in range(iterations):
            digDir(direction)
    elif (direction == "left"):
        for i in range(iterations):
            digDir(direction)
    elif (direction == "right"):
        for i in range(iterations):
            digDir(direction)
    elif (direction == "down"):
        for i in range(iterations):
            digDir(direction)

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

def main():
    time.sleep(2)
    for i in range(150):
        start()

main()