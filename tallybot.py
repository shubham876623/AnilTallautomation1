import requests
import pandas as pd
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed
from random import random
from time import process_time, sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import csv
from urllib.request import urlopen
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.alert import Alert
from datetime import date


import pyautogui as pg
import time
 
import win32gui
import win32con
def windowEnumHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def bringToFront(window_name):
    top_windows = []
    win32gui.EnumWindows(windowEnumHandler, top_windows)
    for i in top_windows:
        # print(i[1])
        if window_name.lower() in i[1].lower():
            # print("found", window_name)
            win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
            win32gui.SetForegroundWindow(i[0])
            break
winname = "Tally.ERP 9"
bringToFront(winname)

time.sleep(2)
for i in range (0,5):
    
    
    pg.press('enter')  # slecting account vaochar
    # time.sleep(4)
    pg.hotkey('ctrl', 'v') # co
    # pg.hotkey('ctrl', 'v')
    
    time.sleep(2)
    pg.press('f9')
    pg.write("dnfdjnfjshubham")
    # pg.press('enter')
    pg.press('f2')
    today = date.today()  # entering today date ..
    time.sleep(3)
    pg.write(today.strftime("%d/%m")) # entering today date .
    pg.press('enter')
    pg.press('enter')
    pg.write('04/02')  # entering 
    pg.press('enter')
    pg.write('petex')
    
    pg.press("enter", presses=6) 
    pg.write('600')
    pg.press("enter", presses=5)
    pg.write('700') 
    pg.press("enter", presses=3)
    pg.write('12345 TDS')
    # time.sleep(10)
    
    pg.press("enter", presses=4)
    pg.write("Purchase Accessories")
    pg.press("enter", presses=2)
    pg.write("400") # entering thr purchasing assocriesss codt
    pg.press("enter", presses=6)
    # pg.press("enter", presses=1)
    
    # # workink on CGST...............
    
    pg.write("CGST INPUT") # typing CGST
    pg.press("enter", presses=1)
    
    pg.write('50') #Slecting  Entering CGST Cost
    pg.press("enter", presses=2)
    pg.write('HO')
    pg.press("enter", presses=4)
    
    
    # #  working on SGST ...........
    pg.write("SGST INPUT") # typing SGST
    pg.press("enter", presses=1)
    
    pg.write('50') #Slecting  Entering SGST Cost
    pg.press("enter", presses=2)
    pg.write('HO')
    pg.press("enter", presses=3)
    
    # pg.press("esc", presses=2) 
    
    # TDS payable_goods @ 0.1%
    pg.press("enter", presses=1)
    pg.write("TDS payable_goods @ 0.1%")  
    pg.press("enter", presses=2)
    pg.write("KJL-123456")
    pg.press("enter",presses=1)
    pg.press("esc", presses=4) # to rea
    pg.press("enter",presses=1)
    pg.hotkey('ctrl', 'v')
    
    pg.press("esc", presses=2)
    time.sleep(3)
































