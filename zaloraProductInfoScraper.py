from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver
import time
import csv

driver = webdriver.Firefox()
driver.implicitly_wait(3)
page = 0
productBrandListShirts = []
productTitleListShirts = []
productDescListShirts = []
productColorListShirts = []

while True:
    
    page = page + 1
    url = 'https://www.zalora.com.hk/men/clothing/shirt/?gender=men&dir=desc&sort=popularity&category_id=31&page=' + str(page) +'&enable_visual_sort=1'
    try:
        driver.get(url)
    except:
        print('there is no next page man...')
        break

    print(str('URL = ' + driver.current_url))
    
    #break try:loaded no result page
    try:
        driver.find_element_by_xpath("//div[@class='catalog__noresultTip']")
        print('loaded no result page')
        break
    except:
        #get product links
        productLinks = ''
        try:
            links = driver.find_elements_by_xpath("//a[@class='b-catalogList__itmLink itm-link']")
        except:
            print('links error')

        for link in links:
            productLinks = productLinks + '\n' + str(link.get_attribute('href'))

        productsURL = productLinks.split('\n')[1:]
        print('Product\'s url = ' + str(productsURL))

        #get product information

        for i in productsURL:
            try:
                driver.get(i)
            except:
                print('cannot load product url @ ' + i)
                pass

            try:
                productBrand = driver.find_element_by_xpath("//div[@class='js-prd-brand product__brand']").text
                productBrandListShirts.append(productBrand)
            except:
                print('cannot load productBrand @ ' + i)
                productBrandListShirts.append('unknown')
                pass

            try:
                productTitle = driver.find_element_by_xpath("//div[@class='product__title fsm']").text
                productTitleListShirts.append(productTitle)
            except:
                print('cannot load productTitle @ ' + i)
                productTitleListShirts.append('unknown')
                pass

            try:
                productDesc = driver.find_element_by_xpath("//div[@id='productDesc']").text
                try:
                    productDesc = productDesc.replace('- ','').replace('\n',',')
                    productDescListShirts.append(productDesc)
                except:
                    print ('cannot do data manipulation @ ' + i)
                    pass
            except:
                print('cannot load productDesc @ ' + i)
                productDescListShirts.append('unknown')
                pass

            try:
                colors = driver.find_element_by_xpath("//td[@itemprop='color']").text
                productColorListShirts.append(colors)
            except:
                print('cannot load colors @ ' + i)
                productColorListShirts.append('unknown')
                pass

driver.close()

dfShirts = pd.DataFrame({"brandName":productBrandListShirts,"productTitle":productTitleListShirts,"productDesc":productDescListShirts,"productColor":productColorListShirts})

print(dfShirts)

dfShirts.to_csv('zaloraMenShirts.csv', index=False)