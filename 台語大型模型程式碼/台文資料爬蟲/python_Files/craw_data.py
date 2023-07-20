from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException as wde
import requests
from bs4 import BeautifulSoup
import time
from tqdm.auto import tqdm
import pandas as pd
from tqdm.contrib import tzip
# use selenium to get the content of each chapter
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito") 
chromedriver = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chromedriver, options=chrome_options)
driver.get("https://db.nmtl.gov.tw/site3/home") # 更改網址以前往不同網頁
elems = driver.find_elements_by_css_selector(".down_a [href]")
to_be_craw_links = [elem.get_attribute('href') for elem in elems]
chapter_name     = [elem.text for elem in elems]
driver.close()
total_data = []
columns = ['台羅','漢羅','篇名']
for url, chap_name in tzip(to_be_craw_links, chapter_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")  #把網頁程式碼(HTML)丟入 bs4 模組分析
    table = soup.find('table', {'class': 'article_d peh lmj1'})
    trs = table.find_all('tr')[:]
    rows = list()
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
    for row in rows:
        row.append(chap_name)
    total_data = total_data + rows
    time.sleep(5)
df = pd.DataFrame(data=rows, columns=columns)
print(df.shape[0])
df.head(5)
df.to_csv('白話字數位典藏館.csv', index = False)
