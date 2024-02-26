import requests
import pandas as pd
import numpy as np
from scrapy import Selector
from pprint import pprint

response = requests.get('https://socialdatascience.network/index.html#schedule')
sel = Selector(response)

titles = sel.css('h6.card-title::text').extract()

speakers = []
dates = []
n = 0

for i in sel.css('.card-body p::text').getall():
    i = i.lstrip()
    if i.startswith('Speaker:'):
        speaker_name = i.replace('Speaker: ', "")
        speakers.append(speaker_name)
        n = 1
    elif i.startswith('Date:'):
        date = i.replace('Date: ', '').lstrip("Wednesday, ")
        dates.append(date)
        n = 0
    else:
        if n == 0:
            speakers.append(' ')
            n = 1
        else:
            dates.append(' ')
            n = 0
'''
print(speakers)
print(dates)
print(titles)
'''

print(len(speakers))
print(len(dates))
print(len(titles))

df = pd.DataFrame({'title': titles,
                   'date': dates,
                   'speaker': speakers})
df