# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:46:42 2024

@author: Administrator
"""

import requests

response = requests.get(r'https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna')
status_code = response.status_code
