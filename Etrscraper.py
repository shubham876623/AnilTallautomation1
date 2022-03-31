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
from emailotp import get_otp
from selenium.webdriver.common.alert import Alert
from datetime import date
import pyautogui as pg
import time
import re
import win32con
import win32gui
discount_list=["Hindoostan Mills Limited"]                                                                                                                                 
comany_list=["HINDOOSTAN MILLS LIMITED","DHL EXPRESS IGST","SPAN PUBLICITY","AJANTA TEXTILES","BKS TEXTILES PVT LTD","PETEX","PRYM FASHION ASIA PACIFIC LIMLTD","SHILPA ENTERPRISES","DIPAK TRADING COMPANY","JAIN NARROW FABRICS","THREADS INDIA LTD","ANSUN MULTITECH INDIA LTD","AMFINO TEX INDIA PVT LTD","CASH","YKK INDIA PVT LTD","VARTIKA PACKAGING P LTD","ANTARCTICA LIMITED","DEEYA INTERNATIONAL","KALPATARU PVT LTD","PECKEL","SATTIK PACKAGING PVT LTD","SREE KARPAGAMBAL MILLS LTD"]
# driver=webdriver.chrome(webdriver_manager)SREE KARPAGAMBAL MILLS LTD
driver=webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://stockexcel.com/Login.aspx')
driver.find_element_by_id('ContentPlaceHolder1_txtEmailID').send_keys('shubhamsaini8766@gmail.com')
driver.find_element_by_id('ContentPlaceHolder1_txtPassword').send_keys('gFNX0EUo')

driver.find_element_by_id('ContentPlaceHolder1_btnLogin').click()
time.sleep(5)
email_input=driver.find_element_by_id('ContentPlaceHolder1_txtUOTP')
while True:
    if email_input is not None:
        email_input.send_keys(get_otp())
        break
driver.find_element_by_id('ContentPlaceHolder1_btnValidate').click()
driver.maximize_window()
# hiting the link of BookKeeperView.aspx..........
time.sleep(3)
driver.get('https://stockexcel.com/BookKeeperView.aspx')
soup=BeautifulSoup(driver.page_source,'html.parser')
table=soup.find('table',{'id':'ContentPlaceHolder1_gvBillNotYetBK'}).find_all('tr')
time.sleep(3)

for i  in range (1,2):
    all_anchor_tag=table[i].find('td').find('a')
    # print("https://stockexcel.com/"+all_anchor_tag.get('href'))
    # driver.get("https://stockexcel.cyom/"+all_anchor_tag.get('href'))
    driver.get('https://stockexcel.com/BillProcess.aspx?bpd=50370&bk=y')
    time.sleep(3)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    company_name=soup.find('span',{'id':'ContentPlaceHolder1_lblSupplierName'})
    invoice_no=soup.find('span',{'id':'ContentPlaceHolder1_lblBillNo'})
    Date=soup.find('span',{'id':'ContentPlaceHolder1_lblBillDate'})
    invoice_ammount=soup.find('span',{'id':'ContentPlaceHolder1_lblBillAmount'})
    narration=soup.find('span',{'id':'ContentPlaceHolder1_lblSRNO'})
    paid_ammaunt=soup.find('span',{'id':'ContentPlaceHolder1_lblBillPassedAmt_sel'})
    
    if company_name.text.upper() in comany_list:
     ###############  opening the windows of tally ##################
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
        
        time.sleep(3)
        
         
        pg.press('enter')  # slecting account vaochar
        time.sleep(1)
        pg.hotkey('ctrl', 'v') # co
        # pg.hotkey('ctrl', 'v')
        
        
        time.sleep(2)
        pg.press('f9')
        time.sleep(1)
        # if comanin comany_list:
        
        pg.write(invoice_no.text.strip())
        time.sleep(1)# entering the invoice number ..
        pg.press('f2')
        time.sleep(1)
        today = date.today()  # entering today date ..
        time.sleep(2)
        pg.write(today.strftime("%d/%m")) # entering today date .
        pg.press('enter')
        pg.press('enter')
        pg.write(Date.text)  # entering 
        pg.press('enter')
        
        pg.write(company_name.text.strip())#entering comapny name ...... or supplier  name 
        pg.press("enter", presses=6)
        time.sleep(1)
        
        if company_name.text not in discount_list:
            pg.write(paid_ammaunt.text.split('.')[1].strip())
            
            pg.press("enter", presses=4)
            time.sleep(1)
        # print(invoice_ammount.text)
            pg.write(invoice_ammount.text.strip())
            time.sleep(1)
            print(invoice_ammount.text ,paid_ammaunt.text.split('.')[1]+"."+paid_ammaunt.text.split('.')[2])
            if invoice_ammount.text==paid_ammaunt.text.split('.')[1]+"."+paid_ammaunt.text.split('.')[2]:
                pg.press("enter", presses=2)
            else:
                print(invoice_ammount.text)
                time.sleep(1)
                pg.press("enter", presses=3)
                time.sleep(1)
                pg.write(invoice_no.text.strip()+"T")
                time.sleep(1)
                
                pg.press("enter", presses=5)
                
            
        # 31633
            table1=soup.find('table',{'id':'ContentPlaceHolder1_gvLedgerBillPros'}).find_all('tr')
           
            
            
            # time.sleep(100)
            list_a=[]
            for i in range(1,len(table1)-1):
                
                pg.write(table1[i].find_all('td')[0].text)
                time.sleep(1)
                
                pg.press("enter", presses=1)
                time.sleep(1)
                
                if "-" in table1[i].find_all('td')[2].text.strip():
                    list_a.append(table1[i].find_all('td')[2].text.strip()[1:])
                else: 
                    list_a.append(table1[i].find_all('td')[2].text.strip())
                    
                
                pg.write(list_a[-1])
                # time.sleep(1)
                # pg.write("600")
                time.sleep(1)
                pg.press("enter", presses=2)
                time.sleep(1)
                pg.write(table1[i].find_all('td')[1].text.strip())
                time.sleep(1)
                print(table1[i].find_all('td')[0].text)
                # print(i,len(table1))
                if i+1==len(table1)-1:
                    # if "Discount (CD)" in table1[i].find_all('td')[0].text :
                        # print(i+1,len(table1)-1 ,"andrr")
                        pg.press("enter", presses=3)
                else:
                    pg.press("enter", presses=4)
                    
           
            
            pg.write("KJL-"+narration.text.strip()) 
            # time.sleep(1)
            pg.press("enter",presses=2)
           
            # print("invoice_no",invoice_no.text,"Date",Date.text,"invoice_ammount",invoice_ammount.text,"paid_ammount",paid_ammaunt.text)
    
        else:
            # pass'
            list_a=[]
            table1=soup.find('table',{'id':'ContentPlaceHolder1_gvLedgerBillPros'}).find_all('tr')
            
            pg.write(invoice_ammount.text.strip())
            pg.press("enter", presses=6)
            for i in range(1,len(table1)-1):
                if "Discount (CD)"  in table1[i].find_all('td')[0].text:
                    pg.press("backspace", presses=1)
                    pg.write("Cr")
                    pg.press("enter")
                    
                pg.write(table1[i].find_all('td')[0].text)
                time.sleep(1)
                
                pg.press("enter", presses=1)
                time.sleep(1)
                
                if "-" in table1[i].find_all('td')[2].text.strip():
                    list_a.append(table1[i].find_all('td')[2].text.strip()[1:])
                else: 
                    list_a.append(table1[i].find_all('td')[2].text.strip())
                    
                
                pg.write(list_a[-1])
                # time.sleep(1)
                # pg.write("600")
                time.sleep(1)
                pg.press("enter", presses=2)
                time.sleep(1)
                pg.write(table1[i].find_all('td')[1].text.strip())
                time.sleep(1)
                # print(table1[i].find_all('td')[0].text)
                # print(i,len(table1))
                if i+1==len(table1)-1:
                    # if "Discount (CD)" in table1[i].find_all('td')[0].text :
                        print(i+1,len(table1)-1 ,"andrr")
                        pg.press("enter", presses=3)
                else:
                    pg.press("enter", presses=4)
                    
           
                
            pg.write("KJL-"+narration.text.strip()) 
            # time.sleep(1)
            pg.press("enter",presses=2)
            
            
    
    else:
        print("no comapnty name ",company_name.text.upper())
       
    
        # time.sleep(5)
    time.sleep(100)

