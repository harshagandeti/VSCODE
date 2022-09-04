import random
import pyautogui as pg
import time
animal=('monkey','donkey','dog','idiot','waste fellow')
time.sleep(10)
for i in range(100):
    a=random.choice(animal)
    pg.write('you are a '+a)
    pg.press('enter')
    

    