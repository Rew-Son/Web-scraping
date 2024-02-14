# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:03:21 2024

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import random

pages = set ()

def getLinks(pageUrl):
    global pages 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4567.89 Safari/537.36'}
    # add delay to not overload the server
    time.sleep(random.uniform(0,2))
    #make HTTP request with headers
       
    response = requests.get(r'https://pl.wikipedia.org{}'.format(pageUrl), headers=headers)
    html = response.content
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-content-text').find_all('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-'* 200)
                pages.add(newPage)
                getLinks(newPage)
                getLinks('')
if __name__ == "__main__":
    getLinks('')
        