import pyautogui, win32api, win32con, time

goRight = [1010, 575]
boxRight = [1010, 550]
goLeft = [915, 520]
boxLeft = [915, 495]
goUp = [1000, 520]
boxUp = [1000, 495]
goDown = [920, 570]
boxDown = [920, 545]
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

def digUp():
    rclick(goUp[0], goUp[1])
    time.sleep(0.2)
    rclick(boxUp[0], boxUp[1])
    pyautogui.moveTo(831, 1050)
    time.sleep(1.5)
    lclick(goUp[0], goUp[1])
    checkFirework()

def digDown():
    rclick(goDown[0], goDown[1])
    time.sleep(0.2)
    rclick(boxDown[0], boxDown[1])
    pyautogui.moveTo(831, 1050)
    time.sleep(1.5)
    lclick(goDown[0], goDown[1])
    checkFirework()

def digLeft():
    rclick(goLeft[0], goLeft[1])
    time.sleep(0.2)
    rclick(boxLeft[0], boxLeft[1])
    pyautogui.moveTo(831, 1050)
    time.sleep(1.5)
    lclick(goLeft[0], goLeft[1])
    checkFirework()

def digRight():
    rclick(goRight[0], goRight[1])
    time.sleep(0.2)
    rclick(boxRight[0], boxRight[1])
    pyautogui.moveTo(831, 1050) 
    time.sleep(1.5)
    lclick(goRight[0], goRight[1])
    checkFirework()

def startDig():
    rclick(door[0], door[1])
    time.sleep(0.5)
    rclick(openDoor[0], openDoor[1])
    time.sleep(0.5)
    lclick(goUp[0], goUp[1])
    time.sleep(0.4)

def switchPaths():
    lclick(964, 602)
    time.sleep(0.4)

def goIn():
    rclick(700,350)
    time.sleep(0.5)
    lclick(700,320)
    time.sleep(4)
    startDig()

def checkFirework():
    switch = 0
    for i in range(70):
        r,g,b = pyautogui.pixel(1142, 524)
        if (g >= 220 and b >= 220):
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
    else:
        print("fuck u")

def start():
    goIn()
    dig("up", 2)
    dig("right", 2)
    switchPaths()
    dig("right", 6)
    dig("down", 6)
    dig("right", 1)
    dig("up", 3)
    time.sleep(1)
    start()

start()
