import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import csv

options=Options()
options.set_headless(headless=False)
driver = webdriver.Firefox(firefox_options=options)
product_link_list=[]
# page = 0

category_link_list = ['http://www.asos.com/men/shoes-boots-trainers/cat/?cid=4209&nlid=mw|shoes|shop%20by%20product&page=',
                  'http://www.asos.com/men/accessories/cat/?cid=4210&nlid=mw|accessories|shop%20by%20product&page=',
                  'http://www.asos.com/men/activewear/cat/?cid=26090&nlid=mw|activewear|shop%20by%20product&page=',
                  'http://www.asos.com/men/face-body/cat/?cid=19517&nlid=mw|face%20+%20body|shop%20by%20product&page=',
                  'http://www.asos.com/men/gifts/cat/?cid=16091&nlid=mw|gifts|shop%20by%20product&page=']

for category_link in category_link_list:
    page = 0
    while True:
        page = page + 1
        driver.get(category_link + str(page))
        print(str(page))
        try:
            driver.find_element_by_xpath("//div[@class='hero__buttons']")
            print('error page back to front page @ ' + driver.current_url)
            break
        except:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='_3x-5VWa']"))
            )
            try:
                product_links = driver.find_elements_by_xpath("//a[@class='_3x-5VWa']")
            except:
                print('cannot retrieve product links @ ' + driver.current_url)

            for product_link in product_links:
                product_link_list.append(product_link.get_attribute('href'))

print(product_link_list)
driver.close()

df_product_link_list = pd.DataFrame({'product_link_list':product_link_list})
df_product_link_list.to_csv('asos_men_product_link_list.csv', index=False)

df_product_link_list = pd.read_csv('asos_men_product_link_list.csv')['product_link_list']
print(str(len(df_product_link_list)))