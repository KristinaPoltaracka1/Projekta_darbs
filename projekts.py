import selenium 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time 
from openpyxl import Workbook, load_workbook 
import pandas 

service = Service() 
option = webdriver.ChromeOptions() 
driver = webdriver.Chrome(service=service, options=option) 
url = "https://www.rimi.lv/e-veikals" 
driver.get(url) 
time.sleep(3) 
s=[] 
accept_cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll") 
accept_cookies.click() 
 
#time.sleep(3) 
 
#ad_close_button = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/button") 
#ad_close_button.click() 
 
fails = pandas.read_excel("Produkti.xlsx", sheet_name="Sheet1")  
info_list = fails.values.tolist() 
match=False 
for produkt in range(len(info_list)): 
    d=info_list[produkt][1] 
    if d=="x": 
        product_name=info_list[produkt][0] 
        match=True 
        s.append(produkt) 
        for pro in range(len(s)): 
            time.sleep(3) 
 
            find = driver.find_element(By.ID, "search-input") 
            find.clear() 
 
            time.sleep(3) 
 
            find.send_keys(str(product_name)) 
 
            time.sleep(3) 
 
            search_button= driver.find_element(By.XPATH, "/html/body/header/div[2]/div[3]/div[1]/form/label/div/button") 
            search_button.click() 
#find.send_keys(Keys.ENTER) 
 
            time.sleep(3) 
 
            possible_product = driver.find_element (By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/div[1]/div/div[2]/ul/li[1]/div/a') 
            possible_product.click() 
 
            time.sleep(3) 
 
            find = driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/h1')   
            x=find.text 
            print(x)   
 
            time.sleep(3) 
 
#if x.lower()==product_name.lower():  
#if product_name.lower() in str(x.lower()): 
            if product_name.lower() in str(x.lower()): 
                add_to_cart = driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/div[2]/form[1]/button') 
                add_to_cart.click()  
 
                time.sleep(5) 
 
find = driver.find_element(By.XPATH, '/html/body/header/div[2]/a/div[1]/span')   
y=find.text 
print(y.strip())  
 
time.sleep(3) 
 
c=y.rstrip()   
d=c[0:len(c)]   
e=d.replace(",",".")   
f=e.replace("€","")   
g=float(f)  
# -----------------------------------------------------------------------------------------------------------------------