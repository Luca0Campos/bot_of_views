import pyautogui
import time


pyautogui.PAUSE = 6  # tempo de cada ação

pyautogui.click(x=1254, y=11)

for navegador in range (20):

    pyautogui.click(x= 173, y= 228, clicks= 2)
    pyautogui.click(x= 726, y= 52)

    pyautogui.write('https://youtube.com/')
    pyautogui.press('enter')
    time.sleep(8)


    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://youtube.com/')
    pyautogui.press('enter')
    time.sleep(8)

    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://youtube.com/')
    pyautogui.press('enter')
    time.sleep(8)

    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://youtube.com')
    pyautogui.press('enter')
    time.sleep(8)

    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://youtube.com')
    pyautogui.press('enter')
    time.sleep(8)

    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://youtube.com')
    pyautogui.press('enter')
    time.sleep(20)

    pyautogui.click(x=1333, y=21)

