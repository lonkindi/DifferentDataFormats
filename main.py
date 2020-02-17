import json
from pprint import pprint

with open('newsafr.json', encoding='utf-8') as json_file:
    news = json.load(json_file)
    pprint(news)