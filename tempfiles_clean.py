import keyboard
import pyautogui as ui
import time

keyboard.press_and_release('win+m')
time.sleep(0.5)
keyboard.press_and_release('win+r')
time.sleep(0.5)
ui.write("temp", interval=0.1)
keyboard.press_and_release('enter')
time.sleep(1)
keyboard.press_and_release('ctrl+a')
time.sleep(0.5)
keyboard.press_and_release('shift+delete')
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(10)
keyboard.press_and_release('esc')
keyboard.press_and_release('win+tab')
time.sleep(0.5)
keyboard.press_and_release('ctrl+w')
time.sleep(1)
keyboard.press_and_release('win+r')
time.sleep(1)
ui.write("%temp%", interval=0.1)
keyboard.press_and_release('enter')
time.sleep(1)
keyboard.press_and_release('ctrl+a')
time.sleep(0.5)
keyboard.press_and_release('shift+delete')
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(10)
keyboard.press_and_release('esc')
time.sleep(0.5)
keyboard.press_and_release('win+tab')
time.sleep(0.5)
keyboard.press_and_release('ctrl+w')
time.sleep(0.5)
keyboard.press_and_release('ctrl+w')
time.sleep(0.5)
keyboard.press_and_release('esc')
time.sleep(0.5)
keyboard.press_and_release('alt+tab')
print("good news , your temp files successfully deleted\n.  \t\t\t\tTHANK YOU!\t\t\t--Reddy007")