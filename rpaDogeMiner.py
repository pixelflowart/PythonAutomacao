import pyautogui
import random
from time import sleep

pyautogui.moveTo(383,376, duration=2)
for i in range(222):
    valor = random.uniform(0.05,0.12)
    sleep(valor)
    pyautogui.click()