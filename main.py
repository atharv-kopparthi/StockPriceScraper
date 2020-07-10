# Apple Stock Price Tracker 
#By AtharvK
#Made on April 24(Friday) 2020
#https://finance.yahoo.com/quote/AAPL/(link)
Tracker = ["Apple Stock Price Tracker"]

print(Tracker)

import bs4
import requests
from bs4 import BeautifulSoup
import lxml

    
def parsePrice():    #Stock Price Of Apple 
    r=requests.get("https://finance.yahoo.com/quote/AAPL/") #Enter any stock link from yahoo
    soup=bs4.BeautifulSoup(r.text,"lxml")
    price=soup.find_all("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text
    return price

while True:
    print("Current Price: "+str(parsePrice()))

   