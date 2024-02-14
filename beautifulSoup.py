# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:06:11 2024

@author: Administrator
"""
from bs4 import BeautifulSoup

html_doc='''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Article Title</title>

</head>

<body>

   <header>
   <nav>
   <ul>
       <li><a href='a'>Home</a></li>
       <li><a href='a'>About</a></li>
       <li><a href='a'>Me</a></li>
   </ul>
   </nav>
   <h1 class= 'title'> Welcome </h1>
   </header>
   <main>
       <section>
       <article>
           <p class='article'>Lorem ipsum</p>
       </article>
       </section>
       <aside>
           <h2>Recent Post</h2>
           
       </aside>
   </main>
    <footer>
        <p>All reserved</p>
    </footer>
</body>

</html>
'''

#BeautifulSoup object
soup = BeautifulSoup(html_doc,'html.parser')

# Find the first paragraph with class 'article'
first_pargraph = soup.find('p',class_='article')

# find all links with href attribute
all_links = soup.find_all('a',href=True)

# find all paragraphs inside  div container 
div_paragraphs = soup.select('div.container p')

#Find the first link and get its href attribute
a_tag = soup.find('a')
link = a_tag.get('href')

#Find the text inside the first h1 element with class 'title'
header = soup.find('h1', class_='title').text

# Find the parent elemnts od the first link
a_tag = soup.find('a')
path = [e.name for e in a_tag.find_parents()[::-1]]
path.append(a_tag.name)