import random
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getLinks(articleUrl):
    html = urlopen(f"http://en.wikipedia.org{articleUrl}")
    bs = BeautifulSoup(html, 'html.parser')

    return bs.find('div', {'id':'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
