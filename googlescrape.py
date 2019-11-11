from bs4 import BeautifulSoup as bs
import requests as rq
from googlesearch import search
import pandas as pd

path = 'social2.csv'
social = pd.read_csv(path, encoding='latin-1')

def get_info(publisher):
    likes = None
    followers = None
    url = None
    try:
        query = str(publisher).split(" via")[0].split(" (")[0] + " facebook page"

        for i in search(query, tld="com", num=1, stop=1, pause=2):
            url = i

        soup = bs(rq.get(url).text, 'lxml')
        blocks = soup.find('div', class_= "_4-u2 _6590 _3xaf _4-u8")
        
        if blocks != None:
            blocks = blocks.find_all('div', class_= "_4bl9")
            likes = int(blocks[0].div.text.split(" people ")[0].replace(',', ''))
            followers = int(blocks[1].div.text.split(" people ")[0].replace(',', ''))
    except:
        print("error with publisher:", publisher)
    
    return {"publisher": str(publisher), "url": url, "likes": likes, "followers": followers}

source_info = []
sources = social['publisher'].values
for source in sources:
    source_info.append(get_info(source))
    print(source_info[-1])
    print(len(source_info)/len(sources))
result = pd.DataFrame(sources_info)
result.to_csv(path, index = None, header = True)
