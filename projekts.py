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
 
             
        for pro in range(len(s)):  
            time.sleep(1)  
 
                 
            find = driver.find_element(By.ID, "search-input")  
            find.clear()  
            time.sleep(1)  
     
            find.send_keys(str(product_name))  
            time.sleep(2) 

            try:   
  
                search_button= driver.find_element(By.XPATH, "/html/body/header/div[2]/div[3]/div[1]/form/label/div/button")   
                search_button.click()     
                time.sleep(1)   
          
                possible_product = driver.find_element (By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/div[1]/div/div[2]/ul/li[1]/div/a')   
                possible_product.click()    
                time.sleep(1)   
          
                find = driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/h1')     
                x=find.text      
                time.sleep(1)   
  
                if product_name.lower() in str(x.lower()):   
                    add_to_cart = driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/div[2]/form[1]/button')   
                    add_to_cart.click()    
                    n=1  
                    float_product_amount=float(product_amount)  
                    for m in range(int(product_amount)):  
                        if float_product_amount>1 and n < float_product_amount:  
                            add_more=driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div/form/button[2]')   
                            add_more.click()   
                            n=n+1  
                            time.sleep(2)  
                        else:  
                            break  
                    time.sleep(10)

            except Exception:
                close_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/button')
                close_button.click()
                time.sleep(1)
                search_button= driver.find_element(By.XPATH, "/html/body/header/div[2]/div[3]/div[1]/form/label/div/button") 
                search_button.click()   
                time.sleep(1) 
        
                possible_product = driver.find_element (By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/div[1]/div/div[2]/ul/li[1]/div/a') 
                possible_product.click()  
                time.sleep(1) 
        
                find = driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/h1')   
                x=find.text    
                time.sleep(1) 

                if product_name.lower() in str(x.lower()): 
                    add_to_cart = driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/div[2]/form[1]/button') 
                    add_to_cart.click()  
                    n=1
                    float_product_amount=float(product_amount)
                    for m in range(int(product_amount)):
                        if float_product_amount>1 and n < float_product_amount:
                            add_more=driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div/form/button[2]') 
                            add_more.click() 
                            n=n+1
                            time.sleep(2)
                        else:
                            break
                    time.sleep(10)

find = driver.find_element(By.XPATH, '/html/body/header/div[2]/a/div[1]/span')   
y=find.text 
time.sleep(3) 
 
c=y.rstrip()   
d=c[0:len(c)]   
e=d.replace(",",".")   
f=e.replace("€","")   
cena_rimi=float(f)  



# -----------------------------------------------------------------------------------------------------------------------



cena_maxima_l=[]
url2 = "https://www.barbora.lv/" 
driver.get(url2) 
time.sleep(2) 
accept_cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll") 
accept_cookies.click() 

fails = pandas.read_excel("Produkti.xlsx", sheet_name="Sheet1")  
info_list = fails.values.tolist() 
match=False 

for produkt in range(len(info_list)):
    c=info_list[produkt][1]
    s.clear()

    if c == "x":
        product_name=info_list[produkt][0]
        match=True
        s.append(product_name)

        for prod in range(len(s)):    
            time.sleep(1)
            
            find = driver.find_element(By.XPATH, '//*[@id="fti-search"]') 
            find.clear()             
            time.sleep(1) 
             
            find.send_keys(str(product_name))             
            time.sleep(1) 
 
            find.send_keys(Keys.ENTER)             
            time.sleep(1) 
            
            possible_product2 = driver.find_element (By.ID, 'fti-product-title-category-page-0') 
            possible_product2.click()             
            time.sleep(1) 
            
            find = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/h1')   
            x1=find.text              
            time.sleep(1) 

            if product_name.lower() in str(x1.lower()):            
                find = driver.find_element(By.XPATH, '//*[@id="fti-product-info-price"]/div/div[2]/div/span')   
                y2=find.text 
                y_norm=y2[1:]+y2[0]  

                time.sleep(1) 
                c2=y2.rstrip()   
                d2=c2[0:len(c2)]   
                e2=d2.replace(",", ".")   
                f2=e2.replace("€", "")   
                g2=float(f2)
                skaits = info_list[produkt][2]
                g3 = float(g2*skaits)
                cena_maxima_l.append(g3)

cena_maxima1 = round((sum(cena_maxima_l)), 2)
cena_maxima2 = str(cena_maxima1)
cena_maxima3 = cena_maxima2.replace(".", ",")


print("Rimi: ", y.strip())
print("Maxima: ", cena_maxima3, "€")


cena_maxima = float(sum(cena_maxima_l))

if cena_maxima < cena_rimi: 
    difer = round(cena_rimi - cena_maxima, 2)
    starp = str(difer) 
    starpiba = starp.replace(".", ",")
    print(starpiba + " €") 
    print("Maxima ir izdevīgāk") 

elif cena_rimi < g2: 
    difer2 = round(cena_maxima - cena_rimi, 2) 
    starp2 = str(difer2) 
    starpiba2 = starp2.replace(".", ",")
    print(starpiba2 + " €") 
    print("Rimi ir izdevīgāk") 

else: 
    print("Vienāda cena")
