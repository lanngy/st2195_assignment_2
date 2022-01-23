from bs4 import BeautifulSoup
import requests


import pandas
import numpy

csv_wiki = requests.get("https://en.wikipedia.org/wiki/Comma-separated_values")
soup = BeautifulSoup(csv_wiki.text,'html.parser')

text1= soup.find('table', class_='wikitable').findNext('pre').text

f = open('name.csv', 'w')
f.write(text1)
f.close()