# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:38:04 2024

@author: Administrator
"""
import requests
from selectolax.parser import HTMLParser
import re,datetime
import random
from urllib.parse import urlparse

#random.seed(datetime.datetime.now())

def getInternalLinks(html, includeUrl):
    includeUrl = f'{urlparse(includeUrl).scheme}://{urlparse(includeUrl).netloc}'
    internalLinks=[]
    tree = HTMLParser(html)
    for link in tree.css('a'):
        href = link.attrs.get('href')
        if href is not None:
            if href.startswith('/'):
                full_link = includeUrl + href
            else:
                full_link = href
            if full_link not in internalLinks:
                internalLinks.append(full_link)
    return internalLinks

def getExternalLinks(html, excludeUrl):
    excludeUrl = urlparse(excludeUrl).netloc
    externalLinks = []
    tree = HTMLParser(html)
    for link in tree.css('a'):
        href = link.attrs.get('href')
        if href is not None:
            if (href.startswith('http') or href.startswith('www')) and excludeUrl:
                if href not in externalLinks:
                    externalLinks.append(href)
    return externalLinks

def getRandomExternalLinks(startingPage):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4567.89 Safari/537.36'}
        response = requests.get(startingPage, headers=headers, timeout =3)
        html = response.content
    except requests.exceptions.RequestException as e:
        print(f"Error opening {startingPage}:{e} ")
        return None
    
    soup = HTMLParser(html)
    externalLinks = getExternalLinks (html, startingPage)
    if not externalLinks:
        internalLinks = getInternalLinks(html,startingPage)
        if not internalLinks:
            print('No link found on the page')
            return None
        else:
            return getRandomExternalLinks(internalLinks[random.randint(0, len(internalLinks))])
    else:
        return random.choice(externalLinks)
            
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLinks(startingSite)
    if externalLink:
        print(f'Random external link is : {externalLink}')
        followExternalOnly(externalLink)
        
        
if __name__ =='__main__':
    followExternalOnly('https://en.wikipedia.org/')    