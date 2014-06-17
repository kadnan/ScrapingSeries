__author__ = 'Adnan Siddiqi'
import requests
from bs4 import BeautifulSoup

#DailyDeal Page
url = 'http://globaldeals.ebay.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text)
divFeature = soup.find('div',{'class':'pnlFeature'})
divFeature = soup.select('.pnlFeature > div')
print("Description\tDiscount\tprice\n")
print("---------------------------------------------------------------")
for item in divFeature:
    salesTag = item.find('span')
    salesTag = salesTag.text.strip()
    salesTag = salesTag.replace('% OFF','').strip()
    desc = item.find('a',{'class':'description'})
    desc = desc.text.strip()
    price = item.find('span',{'class':'price'})
    price = price.text.replace('US$','').strip()
    print(desc+"\t"+salesTag+"\t"+price+"\b")