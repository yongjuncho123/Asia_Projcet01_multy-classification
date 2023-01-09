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
category = category = ['판타지', '퓨전', '현대판타지', '무협', '스포츠', '대체역사', '로맨스', "SF", 'BL', '전쟁·밀리터리']


driver.get(url)

df_novels = pd.DataFrame()
for i in range(1,51):
    titles = []
    intros = []
    genres = []
    if i in range(1,6):
        driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[{}]/a'.format(i)).click() # 포멧 형태 {}.format(i)
        time.sleep(2)
        for k in range(1, 51):
            driver.find_element_by_xpath('//*[@id="SECTION-LIST"]/ul/li[{}]/a[2]'.format(k)).click()

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
                intro = driver.find_element_by_xpath(x_intro).text
                intro = re.compile('[^가-힣]').sub('', intro) # re.compile: 한글만 추출 / sub: 문자열 치환
                intros.append(intro) # 위에 만든 리스트에 넣기
            except NoSuchElementException as e:
                time.sleep(0.5)
                print(NoSuchElementException)
            except StaleElementReferenceException as e:
                print(e)
            except:
                pass

            try:
                genre = driver.find_element_by_xpath(x_genre).text
                genre = re.compile('[^가-힣]').sub('', genre) # re.compile: 한글만 추출 / sub: 문자열 치환
                genres.append(genre) # 위에 만든 리스트에 넣기
            except NoSuchElementException as e:
                time.sleep(0.5)
                print(NoSuchElementException)
            except StaleElementReferenceException as e:
                print(e)
            except:
                pass
            



        ### 1부터 5일때는 위에것 실행 그 이후 6으로 고정되는건 아래걸로

    else:
        driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[6]/a'.format(i)).click() # 6으로 고정되니까 그대로
        time.sleep(2)
        for k in range(1, 51):
            driver.find_element_by_xpath('//*[@id="SECTION-LIST"]/ul/li[{}]/a[2]'.format(k)).click()

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
                intro = driver.find_element_by_xpath(x_intro).text
                intro = re.compile('[^가-힣]').sub('', intro) # re.compile: 한글만 추출 / sub: 문자열 치환
                intros.append(intro) # 위에 만든 리스트에 넣기
            except NoSuchElementException as e:
                time.sleep(0.5)
                print(NoSuchElementException)
            except StaleElementReferenceException as e:
                print(e)
            except:
                pass

            try:
                genre = driver.find_element_by_xpath(x_genre).text
                genre = re.compile('[^가-힣]').sub('', genre) # re.compile: 한글만 추출 / sub: 문자열 치환
                genres.append(genre) # 위에 만든 리스트에 넣기
            except NoSuchElementException as e:
                time.sleep(0.5)
                print(NoSuchElementException)
            except StaleElementReferenceException as e:
                print(e)
            except:
                pass
    time.sleep(1)        
    print(titles)
    print(intros)
    print(genres)
    # 페이지 2번(총 100개 소설)을 크롤링 한 후 이것을 저장
    if i % 2 == 0:
        df_section = pd.DataFrame.from_dict({'titles':titles, 'intros': intros, 'genres': genres}, orient = 'index').T # valueerror: all arrays must be of the same length 해결
        print(df_section)
        # df_section = pd.DataFrame({'titles':titles, 'intros': intros, 'genres': genres})
        df_novels = pd.concat([df_novels, df_section], ignore_index= True)
        df_novels.to_csv('./Moonpia_clawing_data/Moonpia_clawing_data_{}.csv'.format(i), index = False)
    time.sleep(1)
    # df_section = pd.DataFrame({'titles':titles, 'intros': intros, 'genres': genres})
    # df_novels = pd.concat([df_novels, df_section], ignore_index= True)
    # df_novels.to_csv('./Moonpia_clawing_data/Moonpia_clawing_data_5.csv', index = False)

driver.close()