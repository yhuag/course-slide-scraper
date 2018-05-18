from lxml import html
import requests
from requests.auth import HTTPBasicAuth
import os
#from urllib.parse import urlencode

HOME_URL = "https://course.cse.ust.hk/comp4332/Password_Only/exerciseLink.html"
BASE_URL = "https://course.cse.ust.hk/comp4332/Password_Only/"
USERNAME = "comp4332"
PASSWORD = "bigdata"

# page = requests.get('https://course.cse.ust.hk/comp4632/Lecture-Slides-COMP4632.html')

page = requests.get(HOME_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))
tree = html.fromstring(page.text)

# links = tree.xpath('//tr/td/a/@href')
links = tree.xpath('//a/@href')


def encode(text):
    return text.replace(" ", "%20")


print(links)

# https://course.cse.ust.hk/comp4632/Week%201%20Slides.pdf
for link in links:
    print(link)
    encoded_link = encode(link)
    print(encoded_link)
    print("wget --user "+USERNAME+" --password "+PASSWORD+" " + BASE_URL + encoded_link)
    os.system("wget --user "+USERNAME+" --password "+PASSWORD+" " + BASE_URL + encoded_link)
