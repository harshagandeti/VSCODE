import random
import pyautogui as pg
import time
animal=('golduuu','bangaram','akkaa','My Little Heart','so much akka')
time.sleep(10)
for i in range(10):
    a=random.choice(animal)
    pg.write('i love you '+a)
    pg.press('enter')
