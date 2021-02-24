

import re
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
import os
import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver




driver = webdriver.Chrome(executable_path=r'C:/Users/maxim/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(30)

download_path = "images/ifunnyclimat"
if not os.path.exists(download_path ):
            os.makedirs(download_path)





try:
    SCROLL_PAUSE_TIME = 0.5
    driver.get("https://ifunny.co/tags/climate")

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

   


    pagetoscrap=driver.page_source
    images = driver.find_elements_by_tag_name("img")

    srcimages=[]
    for i in range(len(images)):
        srcimages.append(images[i].get_attribute("data-src"))

    altimages=[]
    for i in range(len(images)):
        altimages.append(images[i].get_attribute("alt"))


    
    
   

    for i in range(len(srcimages)):
        req = urllib.request.Request(srcimages[i])
        raw_img = urllib.request.urlopen(req).read()
        f = open(download_path + str(i)+".jpeg", "wb")
        f.write(raw_img)
        f.close
  

  
   
   


finally:
    driver.quit()


   

