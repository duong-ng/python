import convert
from convert import m_to_cm
from convert import cm_to_m
from convert import max
import pyautogui

print(pyautogui.position())
pyautogui.moveTo(600,1050,duration=0)
pyautogui.click(600, 1050, interval=0.01)
pyautogui.typewrite("Dragon city")
pyautogui.moveTo(600, 300,duration=1)
pyautogui.click(600, 300,duration=1)
