from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time
import datetime

option = webdriver.ChromeOptions()
option.add_argument('lang=kr_KR')
driver = webdriver.Chrome('C:/Users/ChoYJ/Desktop/Data_Study/Asia/1st_team_project(multi_classification)/Asia_Projcet01_multy-classification/chromedriver.exe', options=option)
driver.get("https://novel.munpia.com/page/hd.platinum/group/pl.serial/view/serial")

time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="SECTION-MENU"]/ul/li[2]/a""").click()
time.sleep(0.5)

for i in 