import time
from os import system as sys
import pyautogui
import mouse, keyboard
cmd = ''
while cmd != 'exit':
    cmd = input('|open_app| , |hack| , |del_life| , |start| , |off_comp| , |clock| , |autoclicker| or |bomber| and |exit|:\n')
    sys('color 02')
    if cmd == 'open_app':
        app = input('Way to app:')
        app.replace('/', '\\')
        sys(app)
    elif cmd == 'hack':
        """sys('start')"""
        sys('C:\\Windows\\System32')
        sys('tree')
    elif cmd == 'del_life':
        sys('del C:\\Program Files')
    elif cmd == 'off_comp':
        sys('shutdown /s /t 1')
    elif cmd == 'start':
        while True:
            sys('start')
    elif cmd == 'bomber':
        print('Open place with <write_line> and Bomber start spam!')

        time.sleep(5)
        f = open('beemovie.txt', 'r')
        agree = input('mes or find:')
        for line in f:
            pyautogui.typewrite(line)
            if agree == 'mes':
                pyautogui.press('enter')
    elif cmd == 'autoclicker':
        isClicking = False


        def click(LorR):
            while LorR != 'ex':
                if isClicking:
                    mouse.click(button=LorR)
                    time.sleep(0.1)


        def isclicing():
            global isClicking
            isClicking = not isClicking


        while True:
            LorR = input('left or right:')
            print('Alt+L or ALT+R')
            if LorR == 'left':
                keyboard.add_hotkey('Alt+L', isclicing)
                click(LorR)
            else:
                keyboard.add_hotkey('Alt+R', isclicing)
                click(LorR)
    elif cmd == 'clock':
        clock1 = 0
        clock2 = 0
        min1 = 0
        min2 = 0
        print(f'{clock1}{clock2}:{min1}{min2}')
        while clock1 != 2 and clock2 != 4:
            if min1 != 3:
                if min2 != 10:
                    min2 = min2 + 1
                else:
                    min2 = 0
                    min1 = min1 + 1
            if min1 == 3:
                min1 = 0
                min2 = 0
                clock2 = clock2 + 1
            if clock2 == 10:
                clock2 = 0
                clock1 = clock1 + 1
            print(f'{clock1}{clock2}:{min1}{min2}')
            time.sleep(60)



