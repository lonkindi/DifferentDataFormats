import xml.etree.ElementTree as ET
import functions


def read_news(file, encode='cp1251'):
    parser = ET.XMLParser(encoding=encode)
    x_tree = ET.parse(file, parser)
    return x_tree


def get_items(news):
    root = news.getroot()
    x_items = root.findall("channel/item/description")
    descriptions = list()
    for item in x_items:
        descriptions.append(item.text)
    return descriptions


def main():
    tree_news = read_news('newsafr.xml', 'utf-8')
    news_items = get_items(tree_news)
    words_list = functions.get_words_list(news_items)
    functions.sort_print(words_list)


main()
