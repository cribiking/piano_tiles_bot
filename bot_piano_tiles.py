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
        
        
    #size_screen = pyautogui.size()
    #offset =size_screen[1] - 200 #To prevent error from limit screen
    
    offset = 530
    
    while keyboard.is_pressed('q') == False:
        
        
        if pyautogui.pixel(713, offset)[0] < 60:
            click(713, offset)

        if pyautogui.pixel(871, offset)[0] < 60:
            click(871, offset)

        if pyautogui.pixel(1032, offset)[0] < 60:
            click(1032, offset)

        if pyautogui.pixel(1199, offset)[0] < 60:
            click(1199, offset)
            
    
def click(x, y):
    x+=7
    pyautogui.moveTo(x, y)
    pyautogui.click()
    print(x , y)
    
if __name__=="__main__":
    main()