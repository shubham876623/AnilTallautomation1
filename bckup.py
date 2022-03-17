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

# pg.press("down")
# pg.press("enter")
time.sleep(2)
# pg.press("esc", presses=1)  #  going to the option of selecting the account vaochaer

# pg.press('enter')

# time.sleep(4)
# # pg.moveTo(200, 100)
# # pg.click(400,200)
# pg.press('enter')
# pg.press("down", presses=1)  # selecting the karniwal dummy industries ..
# pg.press('enter')
# # # time.sleep(3)
# pg.press("down", presses=2)  #  going to the option of selecting the account vaochaer

pg.press('enter')  # slecting account vaochar
time.sleep(2)
pg.hotkey('ctrl', 'v')

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
pg.press('enter')

pg.press("enter", presses=6) 
pg.write('600')
pg.press("enter", presses=4)
pg.write('700') 
pg.press("enter", presses=3)
pg.write('123 TDS')

pg.press("enter", presses=4)
pg.write("Purchase Accessories")
pg.press("enter", presses=2)
pg.write("400") # entering thr purchasing assocriesss codt
pg.press("enter", presses=5)
pg.press("enter", presses=1)

# workink on CGST...............

pg.write("CGST INPUT") # typing CGST
pg.press("enter", presses=3)

pg.write('50') #Slecting  Entering CGST Cost
pg.write('HO')
pg.press("enter", presses=3)


#  working on SGST ...........
# pg.write("SGST INPUT") # typing SGST
# pg.press("enter", presses=3)

# pg.write('50') #Slecting  Entering SGST Cost
# pg.write('HO')
# pg.press("enter", presses=3)
# pg.write("SGST INPUT") # typing GST
# pg.write('50')
# pg.press("esc", presses=2) 

time.sleep(100)

# for _ in range(1):
#             actions.send_keys(Keys.LEFT).perform()
            
#             actions.send_keys(Keys.ENTER).perform()
#             time.sleep(1)   
# driver.switchTo().alert().sendKeys(KeyENTERs)
# # //First store parent window to switch back
# String parentWindow = driver.getWindowHandle();

# # //Perform the click operation that opens new window
# driver.findElement(By.id('//*[@id="buttonLogOn"]')).click();

# # //Switch to new window opened
# for(String winHandle : driver.getWindowHandles()){
#     if(winHandle.equals(parentWindow)) {
#         driver.switchTo().window(winHandle);
#     }
# }

# # //Now find checkbox and click 
# driver.findElements(By.id("checkbox0")).click();

# # //Now close opened popup window 
# driver.close();

# # //Switch back to parent window 
# driver.switchTo().window(parentWindow);

# //Continue with parent window 
# driver.find_ele
time.sleep(100)






    





















































# import pyautogui as pg
# import time
# import pandas as pd

# FailSafeException=True


# #OPENING THE TALLY APPLICATION


# pg.click(x=2,y=1080,button="left")

# time.sleep(1)

# pg.write("vs code")


# time.sleep(1)

# pg.press("enter")

# time.sleep(10)

# pg.press("f1")

# time.sleep(2)


# pg.write("sabo")

# time.sleep(2)


# pg.press("down")

# time.sleep(2)

# pg.press("enter")

# time.sleep(1)


# pg.press("v")

# time.sleep(2)

# pg.press("f7")

# time.sleep(2)


# #for loopING THROUGH THE EXCEL FILES

# akm=pd.read_excel(r"C:\Users\Desktop\Audit FY 21-22\Audit FY 21-22\Audit FY 21-22\Python\All Entries Row Added_1.xlsx")

# jvno=akm["Transaction"].values


# dates=akm["Date_1"].values

# glname=akm["G_L Acct_BP Name"].values
# amt=akm["amount"].values
# drcr=akm["Debit/Credit"].values


# zipped=zip(jvno,dates,glname,amt,drcr)

# for (a,b,c,d,e) in zipped:
    
#     if e=="Debit":
#         time.sleep(0.1)
        
#         astr=str(a)
        

#         pg.write(astr)

#         time.sleep(0.1)

#         pg.press("enter")
#         pg.write(b)

#         time.sleep(0.1)
#         pg.press("enter")

#         pg.write(c)
#         time.sleep(1)

#         pg.press("enter")
        
#         dstr=str(d)
        
        

#         pg.write(dstr)
#         time.sleep(1)


#         pg.press("enter")
        
#         pg.write("t")
        
#         pg.press("enter")
        
    
#     else:
#         pg.write(c)
#         time.sleep(1)
        
#         pg.press("enter")
        
#         dstr=str(d)
#         pg.write(dstr)
#         time.sleep(1)
        
        
#         pg.press("enter")
        
#         pg.press("enter")
        
#         pg.press("enter")





# import pandas as pd

# time.sleep(5)

# # print((df))

# driver=webdriver.Chrome(ChromeDriverManager().install())


# driver.get('https://cloud80.tallywale.com/')
# driver.find_element_by_xpath('//*[@id="Editbox1"]').send_keys('cloud80.p3')
# driver.find_element_by_xpath('//*[@id="Editbox2"]').send_keys('_y@E6rWw')

# driver.find_element_by_id('buttonLogOn').click()
# time.sleep(2)
# actions = ActionChains(driver) time.sleep(3)
driver.get('https://stockexcel.com/BookKeeperView.aspx')
soup=BeautifulSoup(driver.page_source,'html.parser')
table=soup.find('table',{'id':'ContentPlaceHolder1_gvBillNotYetBK'}).find_all('tr')
# print(1,len(table),)
for i  in range (1,len(table)-1,2):
    all_anchor_tag=table[i].find('td').find('a')
    # print("https://stockexcel.com/"+all_anchor_tag.get('href'))
    driver.get("https://stockexcel.com/"+all_anchor_tag.get('href'))
    time.sleep(3)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    invoice_no=soup.find('span',{'id':'ContentPlaceHolder1_lblBillNo'})
    Date=soup.find('span',{'id':'ContentPlaceHolder1_lblBillDate'})
    invoice_ammount=soup.find('span',{'id':'ContentPlaceHolder1_lblBillAmount'})
    paid_ammaunt=soup.find('span',{'id':'ContentPlaceHolder1_lblBillPassedAmt_sel'})
    # print(invoice_no.text,Date.text,invoice_ammount.text,paid_ammaunt.text)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    table=soup.find('table',{'id':'ContentPlaceHolder1_gvLedgerBillPros'}).find_all('tr')
    cost_text=table[1].find_all('td')[0]
    cost_text=table[1].find_all('td')[1]
    cost_text=table[1].find_all('td')[2]
    print(cost_text)