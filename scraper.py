import sys
import pandas as pd
from bs4 import BeautifulSoup
import requests

df = pd.read_excel("links.xlsx")

items= [] 
for index, row in df.iterrows(): 
    mylist = [row.url, row.title_tag, row.title_class, row.content_tag, row.content_class]
    items.append(mylist)

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
        article_title = soup.find(title_tag, class_=title_class_name).text
        article_content = soup.find(content_tag, class_=content_class_name).text
        titles.append(article_title)
        contents.append(article_content)
    except Exception:
        print(sys.exc_info())

df_results = pd.DataFrame({
    'Title': [title for title in titles],
    'Content': [content for content in contents]
})

writer = pd.ExcelWriter("results.xlsx")
df_results.to_excel(writer)
writer.save()
print(titles)
print([title for title in titles])