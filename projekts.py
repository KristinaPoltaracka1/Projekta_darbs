from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time 
import pandas 
service = Service() 
option = webdriver.ChromeOptions() 
driver = webdriver.Chrome(service=service, options=option) 

url = "https://www.rimi.lv/e-veikals" 
driver.get(url) 
time.sleep(2) 
accept_cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll") 
accept_cookies.click() 
s=[] 

fails = pandas.read_excel("Produkti.xlsx", sheet_name="Sheet1")  
info_list = fails.values.tolist() 
match=False 

for produkt in range(len(info_list)):  
    d=info_list[produkt][1]  
    s.clear()    
 
    if d == "x":  
        product_name=info_list[produkt][0]  
        product_amount=info_list[produkt][2]  
        match=True  
        s.append(product_name)  
        print(s) 
 
             
        for pro in range(len(s)):  
            time.sleep(1)  
 
                 
            find = driver.find_element(By.ID, "search-input")  
            find.clear()  
            time.sleep(1)  
     
            find.send_keys(str(product_name))  
            time.sleep(2) 
