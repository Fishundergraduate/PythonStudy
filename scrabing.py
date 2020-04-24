import requests
from bs4 import BeautifulSoup

print("hello,world!")

r = requests.get('https://weather.yahoo.co.jp/weather/jp/13/4410/13212.html')
#r : html all source
"""
with open('weatherdata.txt','w') as txtfile:
    print(r.headers,file=txtfile)
    print("------------------------")
    print(r.encoding,file=txtfile)
    print(r.content,file=txtfile)
"""
soup = BeautifulSoup(r.content,"html.parser")
#soup : text analyze profile
with open('weathertable.html','w') as tablefile:
    print(soup.find("div",id="yjw_pinpoint_today"),file=tablefile)
    print(soup.find("div",id = "yjw_pinpoint_tomorrow"),file=tablefile)