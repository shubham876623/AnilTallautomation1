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
# driver=webdriver.chrome(webdriver_manager)
driver=webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://stockexcel.com/Login.aspx')
driver.find_element_by_id('ContentPlaceHolder1_txtEmailID').send_keys('shubhamsaini8766@gmail.com')
driver.find_element_by_id('ContentPlaceHolder1_txtPassword').send_keys('gFNX0EUo')

driver.find_element_by_id('ContentPlaceHolder1_btnLogin').click()
time.sleep(10)
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
    
    
    
    print("invoice_no",invoice_no.text,"Date",Date.text,"inovoice_ammount",invoice_ammount.text,"paid_ammount",paid_ammaunt.text)
    # soup=BeautifulSoup(driver.page_source,'html.parser')
    
    # # getting data first row table .. 
    # table1=soup.find('table',{'id':'ContentPlaceHolder1_gvLedgerBillPros'}).find_all('tr')
    # cost1_text=table1[1].find_all('td')[0]
    # cost1_Cost_Center=table1[1].find_all('td')[1]
    # cost1_amount=table1[1].find_all('td')[2]
    
    # cgst_Cost_Center=table1[2].find_all('td')[1]
    # if "FALTA" in cgst_Cost_Center.text :
    #     print("case of falta")
    # elif "Real Estate" in cost1_Cost_Center.text:
    #     print(" case of real estate ")
    # else:
    # # cGST Input ...
    #     cgst_text=table1[2].find_all('td')[0]
    #     cgst_Cost_Center=table1[2].find_all('td')[1]
    #     cgst_amount=table1[2].find_all('td')[2]
    #     # sgst...........
        
    #     sgst_text=table1[3].find_all('td')[0]
    #     sgst_Cost_Center=table1[3].find_all('td')[1]
    #     sgst_amount=table1[3].find_all('td')[2]
        
        
    #     print(cost1_text.text,"cosst fist")
    #     print(cost1_Cost_Center.text,"cost first")
    #     print(cost1_amount.text,"cost first")
    
    #     print(cgst_text.text,"cgst")
    #     print(cgst_Cost_Center.text,"cgst")
    #     print(cgst_amount.text,"cgst")
        
    #     print(sgst_text.text,"sgst")
    #     print(sgst_Cost_Center.text,"sgst")
    #     print(sgst_amount.text,"sgst")

    # time.sleep(5)
time.sleep(100)

