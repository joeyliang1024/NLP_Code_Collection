import requests
from bs4 import BeautifulSoup

# 取得所有要爬的網頁連結

# 要爬取的網頁URL
url = "https://funbiochampion.com/"

# 使用requests庫向網頁發送GET請求
response = requests.get(url, headers={"User-Agent": "XY"})

# 使用BeautifulSoup解析網頁內容
soup = BeautifulSoup(response.content, "html.parser")

# 找到指定的ul元素
ul_element = soup.find("ul", {"class": "nav-menu"})

# 找到所有的li元素
li_elements = ul_element.find_all("li")

# 提取所有li元素的連結
links = []
for li_element in li_elements:
    link = li_element.find("a").get("href")
    links.append(link)


# 移除首個和最後一個、以及分類頁面的連結
links = [s for s in links[1:-1] if "category" not in s]
len(links)

# 爬內容
def get_title_and_content(url):
    # 使用requests庫向網頁發送GET請求
    response = requests.get(url, headers={"User-Agent": "XY"})

    # 使用BeautifulSoup解析網頁內容
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到指定的h1元素(標題)
    hi_element = soup.find("h1", {"class": "entry-title"})
    title = hi_element.text.split(" ")[0]

    # 找到所有的p元素(內容) 條件式: p元素沒有id和class屬性
    p_element = soup.select("p:not([id]):not([class])")
    contents = [p.text if is_major_kanji(p.text) else '\n' for p in p_element[:-1]] # 最後一個p元素是廣告

    return title, post_process(contents)

def post_process(contents):

    # 去掉前面的換行符
    while contents[0] == '\n':
        contents = contents[1:]

    # 結尾的換行符不要
    while contents[-1] == '\n':
        contents = contents[:-1]
    
    # 並且在兩段文字中只能有一個換行符
    for idx in range(len(contents)-1):
        if contents[idx] == '\n' and contents[idx+1] == '\n':
            contents[idx] = ''
    
    return ''.join(contents)

# 爬內容、寫入檔案
file_path = "corpus\\讀台語學科學.txt"
with open(file_path, 'w', encoding='utf-8') as f:
    for idx in tqdm(range(len(links))):
        title, content = get_title_and_content(links[idx])
        f.write(content)
        f.write('\n')

count_words_in_txt(file_path)