import json
from pprint import pprint


def read_news(file, encode):
    with open(file, encoding=encode) as json_file:
        return json.load(json_file)


def get_items(news):
    items = news['rss']['channel']['items']
    descriptions = list()
    for item in items:
        descriptions.append(item['description'])
    return descriptions


def get_words_list(news_list):
    words = dict()
    for item in news_list:
        word_list = list(item.split(' '))
        for word_raw in word_list:
            word = word_raw.lower()
            if len(word) > 6:
                frequency = 0
                if words.get(word) == None:
                    frequency = 1
                else:
                    frequency = words.get(word)
                    frequency += 1
                words[word] = frequency
    words_list = list(words.items())
    return words_list


def main():
    news = read_news('newsafr.json', 'utf-8')
    news_items = get_items(news)
    words_list = get_words_list(news_items)
    words_list.sort(key=lambda val: val[1], reverse=True)
    for counter in range(0, 9):
        print(words_list[counter])


main()
