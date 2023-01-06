from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re
import time
import datetime

option = webdriver.ChromeOptions()
option.add_argument('lang=kr_KR')
driver = webdriver.Chrome('C:/Users/ChoYJ/Desktop/Data_Study/Asia/1st_team_project(multi_classification)/Asia_Projcet01_multy-classification/chromedriver.exe', options=option)
url = "https://novel.munpia.com/page/hd.platinum/group/pl.serial/finish/true/view/allend"

time.sleep(0.5)

driver.get(url)


for i in range(1,6):
    titles = []
    intros = []
    genres = []

    driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[{}]/a'.format(i)).click() # 포멧 형태 {}.format(i)
    time.sleep(2)
    for j in range(1, 51):
        driver.find_element_by_xpath('//*[@id="SECTION-LIST"]/ul/li[{}]/a[2]'.format(j)).click()

        x_title = '//*[@id="board"]/div[1]/div[3]/h2/a' # 타이틀 제목이 담긴 x_path
        x_intro = '//*[@id="STORY-BOX"]/p[1]' # 인트로 내용이 담긴 x_path
        x_genre = '//*[@id="board"]/div[1]/div[3]/p[1]/strong' # 장르 내용이 담긴 x_path
        # 소설 제목
        try:
            title = driver.find_element_by_xpath(x_title).text
            title = re.compile('[^가-힣]').sub('', title) # re.compile: 한글만 추출 / sub: 문자열 치환
            titles.append(title) # 위에 만든 리스트에 넣기
        except NoSuchElementException as e:
            time.sleep(0.5)
            print(NoSuchElementException)
        except StaleElementReferenceException as e:
            print(e)
        except:
            pass

        try:
            intro = driver.find_element_by_xpath(x_title).text
            intro = re.compile('[^가-힣]').sub('', title) # re.compile: 한글만 추출 / sub: 문자열 치환
            intros.append(intro) # 위에 만든 리스트에 넣기
        except NoSuchElementException as e:
            time.sleep(0.5)
            print(NoSuchElementException)
        except StaleElementReferenceException as e:
            print(e)
        except:
            pass

        try:
            genre = driver.find_element_by_xpath(x_title).text
            genre = re.compile('[^가-힣]').sub('', title) # re.compile: 한글만 추출 / sub: 문자열 치환
            genres.append(genre) # 위에 만든 리스트에 넣기
        except NoSuchElementException as e:
            time.sleep(0.5)
            print(NoSuchElementException)
        except StaleElementReferenceException as e:
            print(e)
        except:
            pass
        

        time.sleep(0.5) # element is not attached to the page document 타임슬립 넣으면 해결

driver.close