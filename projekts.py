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
