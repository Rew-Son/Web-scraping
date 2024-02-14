# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:34:27 2024

@author: Administrator
"""

from selectolax.parser import HTMLParser

html_string='''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced HTML Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }

        h1, h2, h3 {
            color: #333;
        }

        p {
            color: #666;
        }

        img {
            max-width: 100%;
            height: auto;
        }

        a {
            color: #007bff;
            text-decoration: none;
        }

        form {
            margin-top: 20px;
        }

        input, textarea {
            margin-bottom: 10px;
        }

        button {
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>

<body>

    <header>
        <h1>Welcome to My Website</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section>
        <h2>Featured Article</h2>
        <article>
            <h3>Article Title</h3>
            <p>This is a brief description of the featured article.</p>
            <a href="#">Read more</a>
        </article>
    </section>

    <section>
        <h2>Image Gallery</h2>
        <div class="image-gallery">
            <img src="image1.jpg" alt="Image 1">
            <img src="image2.jpg" alt="Image 2">
            <img src="image3.jpg" alt="Image 3">
        </div>
    </section>

    <section>
        <h2>Contact Form</h2>
        <form action="/submit" method="post">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Your Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <button type="submit">Submit</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2024 My Website. All rights reserved.</p>
    </footer>

</body>

</html>
'''
doc = HTMLParser(html_string)

title = doc.css_first('title').text

input_tags= doc.css('input[type="text"]')
for input_tag in input_tags:
    print(input_tag.attributes)
    
div_elements = doc.css('div.content')
for div in div_elements:
    print(div.attributes)
    
    
header = doc.css_first('h1')
print(header.text())

parsed_html = doc.html

h2_elemnt =doc.css_first('h2')
h2_tag_nme = h2_elemnt.tag


input_elemnt = doc.css_first('input')
input_elemnt_attrs = input_elemnt.attributes
