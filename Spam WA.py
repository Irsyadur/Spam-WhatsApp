# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:11:59 2023

@author: IRSYADUR
"""

import pyautogui as pt
import time

name = 'Hallo kak, Kakaknya udah berapa kali tembus jackpot?'
msg = 'Tutor in JACKPOT-nya dong kak ...'
trap = 'Hehehe SURPRISE '
trap2 = 'Selamat kakak telah mendapat JACKPOT '
emote = '🎉🎉🎉'
emote1 = '✌✌✌'

time.sleep(3)
i = 0
while i < 62:
    if i < 1:
        pt.typewrite(name)
        print(name)
        pt.press('enter')
    elif i >= 1 and i <= 60:
        pt.typewrite(msg)
        print(msg)
        pt.press('enter')
    elif i > 60:
        pt.typewrite(trap)
        pt.hotkey("ctrl", "v")
        print(trap)
        pt.press('enter')
    i += 1
else:
    pt.typewrite(trap2)
    pt.hotkey("ctrl", "v")
    print(trap2)
    pt.press('enter')


