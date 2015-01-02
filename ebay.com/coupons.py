__author__ = 'Adnan Siddiqi'
import requests
from bs4 import BeautifulSoup
url = 'http://www.ebay.com/sch/Coupons-/172010/i.html?rt=nc&_dmd=2'
#headers = {'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text)
li = soup.select('#GalleryViewInner > li')
for item in li:
    title = item.select('.gvtitle > h3 > a')
    title = title[0].text
    #amount = item.select('.amt > .bold')
    amount = item.find('span',{'class':'bold'})
    if amount is not None:
        print(title+"\t"+amount.text.strip()+"\n")
#soup = BeautifulSoup(r.text)
