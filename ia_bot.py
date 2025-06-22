import numpy as np #Manipulació d'arryas
from PIL import ImageGrab #Mirar si es diu Pillow, obrir modificar i guardar imatges
import cv2 # IMPORTANT: crec que sera com la ia
import pyautogui
from time import sleep


def main():
    
    screen_coordenates = [640 , 35 ,1285 , 1400]#x , y , alt, llarg

    sleep(2)
    
    tile1 = [711,0 , 716,1079]
    tile2 = [877,0 , 882,1079]
    tile3 = [1036,0, 1041,1079]
    tile4 = [1195,0, 1200,1079]

    while True:
        
        screen1 = np.array(ImageGrab.grab(bbox=tile1))
        screen2 = np.array(ImageGrab.grab(bbox=tile2))
        screen3 = np.array(ImageGrab.grab(bbox=tile3))
        screen4 = np.array(ImageGrab.grab(bbox=tile4))
        
        screen1 = cv2.cvtColor(screen1, cv2.COLOR_BGR2GRAY)    
        screen2 = cv2.cvtColor(screen2, cv2.COLOR_BGR2GRAY)    
        screen3 = cv2.cvtColor(screen3, cv2.COLOR_BGR2GRAY)    
        screen4 = cv2.cvtColor(screen4, cv2.COLOR_BGR2GRAY)    

        cv2.imshow("Captura", screen1)
        cv2.imshow("Captura", screen2)
        cv2.imshow("Captura", screen3)
        cv2.imshow("Captura", screen4)
            
            
        # Espera 1ms y sale si presionas 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

    cv2.destroyAllWindows()


def click(x, y):
    pyautogui.position(x , y)
    pyautogui.click()
    

if __name__=="__main__":
    main()