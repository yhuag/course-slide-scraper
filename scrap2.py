from lxml import html
import requests
import os
#from urllib.parse import urlencode

page = requests.get('https://course.cse.ust.hk/comp4632/Lecture-Slides-COMP4632.html')
tree = html.fromstring(page.text)

links = tree.xpath('//tr/td/a/@href')

def encode(text):
    return text.replace(" ", "%20")


#print(links)

# https://course.cse.ust.hk/comp4632/Week%201%20Slides.pdf
for link in links:
    #print(link)
    encoded_link = encode(link)
    print(encoded_link)
    os.system("wget https://course.cse.ust.hk/comp4632/"+encoded_link)
