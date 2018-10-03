import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import csv
import urllib
import os

brand = 'armanibeauty'

options=Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options)
page=0
imgLinkList=[]
driver.implicitly_wait(2)

tagLink = 'https://www.instagram.com/explore/tags/' + str(brand)

driver.get(tagLink)

for i in range(250):
    page = page + 1
    
    print(str(page))
    
    try:
        imgLinks = driver.find_elements_by_xpath("//img[@class='FFVAD']")
        for imgLink in imgLinks:
            imgLinkList.append(imgLink.get_attribute('src'))
        
    except:
        print('failed @' + driver.currenturl)
        break  

    element = driver.find_element_by_xpath("//footer[@class='_8Rna9  _3Laht ']");
    driver.execute_script("arguments[0].scrollIntoView();", element)
    
    time.sleep(1)

print(imgLinkList)
driver.close()

imgLinkList = pd.DataFrame(imgLinkList)
imgLinkList = a.drop_duplicates()
imgLinkList.duplicated().value_counts()
imgLinkList.to_csv(brand + ".csv", index=False)

theBrandCSV = pd.read_csv(brand + ".csv")

page = 256

if not os.path.exists(brand):
    os.makedirs(brand)

for i in theBrandCSV['0'][257:]:
    page = page + 1
    urllib.request.urlretrieve(i, str(brand) + "/" + str(page) + brand + ".jpg")
    print(i)