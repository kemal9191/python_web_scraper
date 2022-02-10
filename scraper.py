from base64 import encode
import encodings
from json import encoder
import sys
import pandas as pd
from bs4 import BeautifulSoup
import requests

'''
This is a small program that takes a file named "links" and 
iterate through URLs inside it.links has 5 columns, namely url, 
title_tag, title_class, content_tag, and content_class. Program 
takes this information, goes to the url, finds the article 
specified, then writes it to an excel file called results.xlsx. 
This was designed to fetch articles from a blog site.
'''

df = pd.read_excel("links.xlsx")

items= [] 
for index, row in df.iterrows(): 
    item = [row.url, row.title_tag, row.title_class, row.content_tag, row.content_class]
    items.append(item)

titles = []
contents = []

for item in items:
    url = item[0]
    title_tag = item[1]
    title_class_name = item[2]
    content_tag = item[3]
    content_class_name = item[4]

    try:
        html_content = requests.get(url).content
        soup = BeautifulSoup(html_content, "lxml")         
        article_title = soup.find(title_tag, class_=title_class_name).text.replace("\n", "")
        article_content = soup.find(content_tag, class_=content_class_name).text.replace("\n", "")
        titles.append(article_title)
        contents.append(article_content)
    except Exception:
        print(sys.exc_info())

df_results = pd.DataFrame({
    'Title':titles,
    'Content':  contents
})

with pd.ExcelWriter("results.xlsx") as writer:
    df_results.to_excel(writer, encoding="utf-8")
