import sys
import pandas as pd
from bs4 import BeautifulSoup
import requests

df = pd.read_excel("links.xlsx")

links= [] 
for index, row in df.iterrows(): 
    mylist = [row.url, row.title_tag, row.title_class, row.content_tag, row.content_class]
    links.append(mylist)


for link in links:
    url = link[0]
    title_tag = link[1]
    title_class_name = link[2]
    content_tag = link[3]
    content_class_name = link[4]

    try:
        html_content = requests.get(url).content
        soup = BeautifulSoup(html_content, "lxml")         
        article_title = soup.find(title_tag, class_=title_class_name)
        article_content = soup.find(content_tag, class_=content_class_name)
        print(article_title.text, article_content.text)
    except Exception:
        print(sys.exc_info())