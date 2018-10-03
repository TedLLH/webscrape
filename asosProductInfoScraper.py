import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import csv

options=Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options)
driver.implicitly_wait(2)

#asos_men_product_link_list.csv product information

options=Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options)
driver.implicitly_wait(2)
gender_list = []
cat1_nameList = []
cat2_nameList = []
cat3_nameList = []
cat4_nameList = []
cat5_nameList = []
cat6_nameList = []
cat7_nameList = []
cat8_nameList = []
cat9_nameList = []
cat10_nameList = []
productBrandList = []
productTitleList = []
productDescList = []
productColorList = []
product_url_list = []

#loop thru the df_product_link_list
for product_link in df_product_link_list:

        #get product information
        try:
            driver.get(product_link)
        except:
            print('cannot load product url @ ' + product_link)
            pass
        
        try:
            driver.find_element_by_xpath("//div[@class='hero__buttons']")
            print('error page back to front page @ ' + driver.current_url)
        except:
            try:
                driver.find_element_by_xpath("//p[@id='titleMessage']")
                print('no result page @ ' + driver.current_url)
            except:
                #find categories & last element
                try:
                    categories = driver.find_elements_by_xpath("//div[@id='breadcrumb']/ul/li/a")
                except:
                    print('cannot find categories')
                    break
                try:
                    category_list = []
                    for category in categories[1:]:
                        category_list.append(category.text.strip())
                except:
                    print('category_list error')
                    category_list.append('unknown')
                    pass

                #gender_list
                try:
                    gender_list.append(category_list[0])
                except:
                    gender_list.append('unknown')
                    pass

                #cat1 name
                try:
                    cat1_nameList.append(category_list[1])
                except:
                    cat1_nameList.append('unknown')
                    pass

                #cat2 name
                try:
                    cat2_nameList.append(category_list[2])
                except:
                    cat2_nameList.append('unknown')
                    pass

                #cat3 name
                try:
                    cat3_nameList.append(category_list[3])
                except:
                    cat3_nameList.append('unknown')
                    pass

                #cat4 name
                try:
                    cat4_nameList.append(category_list[4])
                except:
                    cat4_nameList.append('unknown')
                    pass

                #cat5 name
                try:
                    cat5_nameList.append(category_list[5])
                except:
                    cat5_nameList.append('unknown')
                    pass

                #cat6 name
                try:
                    cat6_nameList.append(category_list[6])
                except:
                    cat6_nameList.append('unknown')
                    pass

                #cat7 name
                try:
                    cat7_nameList.append(category_list[7])
                except:
                    cat7_nameList.append('unknown')
                    pass

                #cat8 name
                try:
                    cat8_nameList.append(category_list[8])
                except:
                    cat8_nameList.append('unknown')
                    pass

                #cat9 name
                try:
                    cat9_nameList.append(category_list[9])
                except:
                    cat9_nameList.append('unknown')
                    pass

                #cat10 name
                try:
                    cat10_nameList.append(category_list[10])
                except:
                    cat10_nameList.append('unknown')
                    pass
                
                #product Brand
                try:
                    productBrand = driver.find_element_by_xpath("//div[@class='product-description']/span/a/strong")
                    productBrandList.append(productBrand.text.strip())
                except:
                    print('cannot load productBrand @ ' + product_link)
                    productBrandList.append('unknown')
                    pass

                #product title
                try:
                    productTitle = driver.find_element_by_xpath("//li[@id='bcProduct']")
                    productTitleList.append(productTitle.text.strip())
                except:
                    print('cannot load productTitle @ ' + product_link)
                    productTitleList.append('unknown')
                    pass

                #product desc
                try:
                    productDescs = driver.find_elements_by_xpath("//div[@class='product-description']/span/ul/li")
                    
                    try:
                        productDescStr = ''
                        for productDesc in productDescs:
                            productDescStr = productDescStr + '|||||' + productDesc.text.strip()

                        productDescList.append(str(productDescStr.split('|||||')[1:]).replace('[','').replace(']','').replace('\'',''))
                    except:
                        print('cannot do data manipulation for productDesc @ ' + product_link)
                        productDescList.append('unknown')
                        pass
                except:
                    print('cannot load productDesc @ ' + product_link)
                    productDescList.append('unknown')
                    pass

                #colors
                try:
                    colors = driver.find_element_by_xpath("//span[@class='product-colour']").text.strip()
                    productColorList.append(colors)
                except:
                    print('cannot load colors @ ' + product_link)
                    productColorList.append('unknown')
                    pass
                
                #product_link_list
                product_url_list.append(str(driver.current_url))

print("gender list : " + str(len(gender_list)))
print("cat 1 : " + str(len(cat1_nameList)))
print("cat 2 : " + str(len(cat2_nameList)))
print("cat 3 : " + str(len(cat3_nameList)))
print("cat 4 : " + str(len(cat4_nameList)))
print("cat 5 : " + str(len(cat5_nameList)))
print("cat 6 : " + str(len(cat6_nameList)))
print("cat 7 : " + str(len(cat7_nameList)))
print("cat 8 : " + str(len(cat8_nameList)))
print("cat 9 : " + str(len(cat9_nameList)))
print("cat 10 : " + str(len(cat10_nameList)))
print("product brand : " + str(len(productBrandList)))
print("product title : " + str(len(productTitleList)))
print("product desc : " + str(len(productDescList)))
print("product color : " + str(len(productColorList)))
print('product url : ' + str(len(product_url_list)))
driver.close()

df_product_info = pd.DataFrame({"gender":gender_list, "cat_1": cat1_nameList, "cat_2":cat2_nameList, "cat_3":cat3_nameList,
                                 "cat_4": cat4_nameList, "cat_5": cat5_nameList, "cat_6": cat6_nameList, "cat_7": cat7_nameList,
                                 "cat_8": cat8_nameList, "cat_9": cat9_nameList, "cat_10": cat10_nameList, "brand": productBrandList,
                                  "title": productTitleList, "desc": productDescList, "color": productColorList, "url": product_url_list})

df_product_info.to_csv('asos_men_product_info.csv', index=False)

df_product_info_csv = pd.read_csv('asos_men_product_info.csv')
print(df_product_info_csv)