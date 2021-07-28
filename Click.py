import pyautogui as pag
import time
import random as rd
import keyboard

ClickEvent = 0

pag.PAUSE = 0.1
pag.FAILSAFE = True

while ClickEvent < 600:
    if keyboard.is_pressed("."):
        ClickEvent = ClickEvent * 999999999999999999999999999
        print("종료!")
    else:
        ClickEvent = ClickEvent + 1
        print("클릭을 %d번 합니다" % ClickEvent)
        
        time.sleep(10
        
        pag.click(button='left', clicks=1)
