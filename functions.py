def get_words_list(news_list):
    words = dict()
    for item in news_list:
        word_list = list(item.split(' '))
        for word_raw in word_list:
            word = word_raw.lower()
            if len(word) > 6:
                if not words.get(word):
                    frequency = 1
                else:
                    frequency = words.get(word)
                    frequency += 1
                words[word] = frequency
    words_list = list(words.items())
    return words_list


def sort_print(words_list):
    print('ТОП-10 слов длиннее шести букв по частоте их использования:')
    words_list.sort(key=lambda val: val[1], reverse=True)
    for counter in range(0, 10):
        print(f'Место № {counter + 1} - "{words_list[counter][0]}" найдено {words_list[counter][1]} шт.')
