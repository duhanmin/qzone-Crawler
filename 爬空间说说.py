#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os

def shuoshuo():
    driver.switch_to.default_content()
    js = "var q=document .body .scrollTop =10000"
    driver.execute_script(js)
    time.sleep(1)
    driver.execute_script(js)
    time.sleep(1)
    driver.execute_script(js)
    time.sleep(1)
    driver.execute_script(js)
    driver.switch_to.frame('app_canvas_frame')
    ps = driver.page_source
    soup = BeautifulSoup(ps, "lxml")
    ol = soup.find("ol")
    pre = ol.find_all("pre")
    a = ol.find_all("a", class_="c_tx c_tx3 goDetail")
    with open(r"C:\Users\007\Desktop\b.txt", "a+", encoding='utf-8') as f:
        for i in range(len(pre)):
            f.write(pre[i].text.replace("\n", "。") + "\t")
            f.write(a[i].text + "\n")

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://user.qzone.qq.com/502971229?ADUIN=359391169&ADSESSION=1504832608&ADTAG=CLIENT.QQ.5539_FriendInfo_PersonalInfo.0&ADPUBNO=26730&ptlang=2052&source=namecardstar")
driver.implicitly_wait(10)
#自己手动登陆，没有代码
driver.find_element_by_css_selector('a[title="说说"]').click()
shuoshuo()
while True:
    try:
        driver.find_element_by_link_text('下一页').click()
        shuoshuo()
        time.sleep(1)
    except:
        print("complete")
        break