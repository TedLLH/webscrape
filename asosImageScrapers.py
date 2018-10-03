import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import csv
import urllib

options=Options()
options.set_headless(headless=False)
driver = webdriver.Firefox(firefox_options=options)
imgLinkList=[]
page = 0

for i in range(21):
    page = page + 1
    categoryLink = 'http://www.asos.com/search/?page=' + str(page) + '&q=adidas'

    driver.get(categoryLink)
    print(str(page))
    try:
        driver.find_element_by_xpath("//div[@class='hero__buttons']")
        print('error page back to front page @ ' + driver.current_url)
        break
    except:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//img[@data-auto-id='productTileImage']"))
        )
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='_2etlMSJ']"))
        )
        
        element = driver.find_element_by_xpath("//div[@class='_2etlMSJ']");
        driver.execute_script("arguments[0].scrollIntoView();", element)
        
        time.sleep(1)
        
        try:
            imgLinks = driver.find_elements_by_xpath("//img[@data-auto-id='productTileImage']")
        except:
            print('cannot retrieve product links @ ' + driver.current_url)

        for imgLink in imgLinks:
            imgLinkList.append(imgLink.get_attribute('src'))

print(imgLinkList)
driver.close()

len(imgLinkList)

imgLinkList = pd.DataFrame({'imgLinkList':imgLinkList})
imgLinkList.to_csv('adidasASOSClothes.csv', index=False)

imgLinkList = pd.read_csv('adidasASOSClothes.csv')['imgLinkList']

page = 0
for link in imgLinkList:
    page = page + 1
    filename = str(page) + '.jpg'
    urllib.request.urlretrieve(link, filename)