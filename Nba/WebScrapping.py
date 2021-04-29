#libs
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json

#pegando html da url do site
url = "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&Season=2020-21&SeasonType=Regular%20Season"

option = Options()
option.headless = True
driver = webdriver.Chrome()

driver.get(url)


time.sleep(3)
print('ok')
driver.find_element_by_xpath(" //div[@class='banner-actions-container']").click()
time.sleep(3)
print('ok')
# driver.find_element_by_xpath( "//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

elementhtml = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = elementhtml.get_attribute('outerHTML')

# #extraindo informações
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# jogando os dados para o df
df_site = pd.read_html( str(table) )[0].head(10)
df = df_site[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['POS', 'PLAYER', 'TEAM', 'TOTAL']

top10ranking = {}
top10ranking['points'] = df.to_dict('records')

driver.quit()

#transformando em json

js = json.dumps(top10ranking)
fp = open('NBA/ranking.json', 'w')
fp.write(js)
fp.close()