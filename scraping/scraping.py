from urllib import request
from bs4 import BeautifulSoup
opurl = input('---->> ')
html = request.urlopen(opurl).read()

soup = BeautifulSoup(html,features="html.parser")
tags = soup("span")
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)