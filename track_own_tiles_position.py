import pyautogui
import time
import keyboard

print("Press 'w' to know the mouse position 'q' to quit")

x, y , i = 0, 0, 0

while keyboard.is_pressed("q") == False:
    if keyboard.is_pressed("w") == True:
        x , y =pyautogui.position()
        print(f"Click {i} : {x} , {y}")
        i +=1
        time.sleep(0.3)