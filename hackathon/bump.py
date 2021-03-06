"""
BUMPの歌詞を保存 : 分かち書きして整形するスクリプトを書く
"""
from bs4 import BeautifulSoup
import requests
import pickle
"""
URLを集める
"""
response = requests.get("http://j-lyric.net/artist/a000673/")
soup = BeautifulSoup(response.content, "lxml")
a_tags = [tag.a for tag in soup.find(id="mnb").find_all("p") if tag.a is not None]

title_url_dict = {}
for a_tag in a_tags:
  title_url_dict[a_tag["title"].replace("BUMP OF CHICKEN", "").replace("歌詞", "").strip()] = a_tag["href"]

with open("title_url.pkl", "wb") as f:
  pickle.dump(title_url_dict, f)


"""
response = requests.get("http://j-lyric.net/artist/a000673/l002b50.html")
soup = BeautifulSoup(response.content, "lxml")
"""
#import ipdb; ipdb.set_trace()