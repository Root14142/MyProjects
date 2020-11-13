import requests
from bs4 import BeautifulSoup

load_url = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%86%E3%83%AC%E3%83%93%E3%82%A2%E3%83%8B%E3%83%A1%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_(2000%E5%B9%B4%E4%BB%A3_%E5%89%8D%E5%8D%8A)"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
a_dict = {}
a_list = [[""] * 5 for i in range(1)]

for table in soup.find_all(class_="wikitable"):
    i = 0
    j = 0
    for element in table.find_all("td"):    # すべてのliタグを検索して表示
        if j == 0:
            a_list[i][j] = element.text
            j += 1
            continue
        elif j == 1:
            a_list[i][j] = element.text
            j += 1
            continue
        elif j == 2:
            a_list[i][j] = element.text
            j += 1
            continue
        elif j == 3:
            a_list[i][j] = element.text
            j += 1
            continue
        elif j == 4:
            a_list[i][j] = element.text
            a_list.append([""] * 5)
            j = 0
        print(a_list[i])
        i += 1
