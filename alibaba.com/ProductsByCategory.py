__author__ = 'Adnan Siddiqi'
import requests
from bs4 import BeautifulSoup

#Product Page
url = 'http://www.alibaba.com/Products'
r = requests.get(url)
soup = BeautifulSoup(r.text)

categories = soup.select('dl > dt')
print('Category Name'+"\tCount\n")
print('=========================')
for category in categories:
    name = category.find('a')
    name = name.text
    count = category.find('em')
    if count:
        count = count.text
        count = count.strip('(')
        count = count.strip(')')
        #This could be saved in a TSV file
        print(name+"\t"+count+"\n")