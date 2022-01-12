import pynput
import keyboard
from time import sleep
from sys import exit

mouse = pynput.mouse.Controller()
kb = pynput.keyboard.Controller()
print("You have 10 seconds before the script starts.")
print("Press SPACE or ESC to stop the script.")
sleep(5)
print("5")
sleep(1)
print("4")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
for i in range(0, 1500):
    if keyboard.is_pressed("esc"): exit()
    if keyboard.is_pressed("space"): exit()
    sleep(0.2)
    mouse.click(pynput.mouse.Button.left, 1)
    if keyboard.is_pressed("esc"): exit()
    if keyboard.is_pressed("space"): exit()
    sleep(0.2)
    kb.press(pynput.keyboard.Key.esc)
    kb.release(pynput.keyboard.Key.esc)
    print("Round ",i,", ",1500-i," remaining.")

