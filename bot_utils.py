import win32api, win32con, time, pyautogui

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
    rclick(1000, 500)
    time.sleep(0.5)
    rclick(1000, 470)
    time.sleep(0.5)
    lclick(1000, 520)
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

def clickBox(dir):
    rclick(dir[0], dir[1])
    time.sleep(0.2)
    rclick(dir[0], dir[1] - 25)
    pyautogui.moveTo(831, 1050)

def goNext(dir):
    lclick(dir[0], dir[1])
    pyautogui.moveTo(831, 1050)
    time.sleep(0.3)
