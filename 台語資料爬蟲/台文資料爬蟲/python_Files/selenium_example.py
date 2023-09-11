from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException as wde
from bs4 import BeautifulSoup
import time
from tqdm.auto import tqdm
import pandas as pd

zh_class = "bstw"
tb_kenji_class = "nbstw"
tb_romaji_class = "bstwre"
zh_nor_class = "nor" # 和合本2010上帝版經文
# url_pattern = "https://cb.fhl.net/read1.php?VERSION18=ttvhl2021&VERSION19=ttvcl2021&VERSION15=tcv2019&TABFLAG=1&chineses=##chineses&chap=##chap&submit1=%E9%96%B1%E8%AE%80"
url_pattern = "https://cb.fhl.net/read1.php?VERSION13=rcuv&TABFLAG=1&chineses=##chineses&chap=##chap&submit1=%E9%96%B1%E8%AE%80"

sec_contents_zh = []
sec_contents_tb_kenji = []
sec_contents_tb_romaji = []
sec_nums_zh = []
sec_contents_zh_nor = []

# use selenium to get the content of each chapter
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito") 
chrome_options.add_argument("user-agent={}".format(get_random_user_agent()))       # 使用偽造的 user-agent

# 使用 selenium開啟瀏覽器
driver = webdriver.Chrome("./chromedriver.exe", options=chrome_options)

# 使用requests庫向各超連結的網頁發送GET請求
for chinese in tqdm(chineses_ls):
    for chap in tqdm(range(1, chap_nums[chineses_ls.index(chinese)]+1)):
        url = url_pattern.replace("##chineses", chinese).replace("##chap", str(chap))
        # response = requests.get(url, headers={"User-Agent": get_random_user_agent()})
        # 暫停5秒，避免被網站擋掉
        # time.sleep(random.randint(5, 15))
        soup = getSoup(url)
        # 取得所有class為zh_class的<td>標籤內的文字
        # zh_contents = soup.find_all('td', class_=zh_class)
        # 取得所有class為tb_kenji_class的<td>標籤內的文字
        # tb_kenji_contents = soup.find_all('td', class_=tb_kenji_class)
        # 取得所有class為tb_romaji_class的<td>標籤內的文字
        # tb_romaji_contents = soup.find_all('td', class_=tb_romaji_class)
        # 如果沒有取得任何文字，則跳出迴圈
        sec_num_contents = soup.find_all('b')

        zh_contents = soup.find_all('td', class_=zh_nor_class)

        if len(zh_contents) == 0:
            print("chap:", chap, "soup:", soup, "url:", url)
            break
        # 將取得的文字加入sec_contents_zh
        # sec_contents_zh = sec_contents_zh + [content.text.strip() for content in zh_contents]
        # 將取得的文字加入sec_contents_tb_kenji
        # sec_contents_tb_kenji = sec_contents_tb_kenji + [content.text.strip() for content in tb_kenji_contents]
        # 將取得的文字加入sec_contents_tb_romaji
        # sec_contents_tb_romaji = sec_contents_tb_romaji + [content.text.strip() for content in tb_romaji_contents]
        # 將取得的文字加入sec_contents_zh_nor
        sec_contents_zh_nor = sec_contents_zh_nor + [content.text.strip() for content in zh_contents]

        # 將取得的文字加入sec_nums_zh
        sec_nums_zh = sec_nums_zh + [chinese + ':' + content.text.strip() for content in sec_num_contents]