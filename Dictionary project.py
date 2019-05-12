import json
import re

data = json.load(open('076 data.json','r'))

def work():
    x = input('Enter the word you want to search: ')
    if x.lower() in data.keys():
        print(data[x])
    else:
        print('You may have misspelt the word')
    work()    

work()

