import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import random

skinClass= "sc-hwwEjo jpCwsE"
rifles=['aug','famas','galil-ar','m4a1-s','m4a4','sg-553','awp','g3sg1','scar-20','ssg-08']
skinDB= "https://wiki.cs.money/weapons/"

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
urllib._urlopener = AppURLopener()

def download_image(url,gunName,num):
    name = gunName+num
    fullname = str(name)+".jpg"
    urllib._urlopener.retrieve(url,fullname)

for rifle in rifles:
    i=0
    urls=[]
    result = requests.get(skinDB+rifle+'')

    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")
        img = soup.find_all('img',{'class':skinClass})

    for x in img:
        x=str(x)
        x=x[x.find("src=")+5:-3]
        urls.append(x)

    for x in urls:
        download_image(x,rifle,str(i))
        i += 1
#filename = x.split('/')[-1]
#r = requests.get(x, allow_redirects=True)
#open(filename, 'wb').write(r.content)
