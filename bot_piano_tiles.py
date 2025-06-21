import pyautogui
import time
import keyboard

def main():
    print("Sleep..")
    time.sleep(3)  #Wait 3seconds
    x , y , start_coordenates = 0,0,0
    
    #Click start tile
    try:
        start_coordenates = pyautogui.locateCenterOnScreen("my_tiles/start.png", confidence=0.8)
        x = start_coordenates[0]
        y = start_coordenates[1]
        click(x , y)
    except pyautogui.ImageNotFoundException:
        print("Imatge Not Found")
        
        
    size_screen = pyautogui.size()
    offset =size_screen[1] - 200 #To prevent error from limit screen
    
    while keyboard.is_pressed('q') == False:
        
        if is_dark(pyautogui.pixel(713, offset)):
            click(713, offset)

        if is_dark(pyautogui.pixel(871, offset)):
            click(871, offset)

        if is_dark(pyautogui.pixel(1032, offset)):
            click(1032, offset)

        if is_dark(pyautogui.pixel(1199, offset)):
            click(1199, offset)
            
    
def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    print(x , y)

# Blue tiles has diferent colors
def is_dark(pixel, threshold=60):
    r, g, b = pixel
    return r < threshold and g < threshold and b < threshold

    
if __name__=="__main__":
    main()