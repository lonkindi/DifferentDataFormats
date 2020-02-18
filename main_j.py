import json
import functions


def read_news(file, encode='cp1251'):
    with open(file, encoding=encode) as json_file:
        return json.load(json_file)


def get_items(news):
    items = news['rss']['channel']['items']
    descriptions = list()
    for item in items:
        descriptions.append(item['description'])
    return descriptions


def main():
    news = read_news('newsafr.json', 'utf-8')
    news_items = get_items(news)
    words_list = functions.get_words_list(news_items)
    functions.sort_print(words_list)


main()
