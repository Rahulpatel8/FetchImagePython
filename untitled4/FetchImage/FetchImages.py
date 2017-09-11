import requests
from bs4 import BeautifulSoup
import webbrowser
import cgi,cgitb


def downloadPage():
    url = "http://www.techmaniya.in/1000-best-hd-wallpapers-for-mobile-wallpapers-hd-1080p/"
    source_code = requests.get(url)
    plainText = source_code.text
    soup = BeautifulSoup(plainText)
    list = []
    for link in soup.findAll('a',{'target':'_blank'}):
        # print link
        if link.img:
            list.append(link.img['src'][0:-17])
            # print(link.img['src'][0:-17])
        href = link.get('href')
    return list