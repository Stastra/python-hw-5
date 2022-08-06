""" Створіть функцію def popularity(text) яка приймає текст text і повертає унікальний массив 
строк відсортований за популярністью.

Уявіть що вам надсилають текст роману чи вірша і хочуть побачити найбільш популярні слова які 
зустрічаються у цьому тексті.

Для початку ви повинні розбити текст на слова. Слова розділені звичайними пробілами.
В тексті не будуть використовуватись точки або коми.
Регістр слів не повинен мати значення. Тобто 'Apple' і 'aPPle' - одне слово.
При формуванні результуючого массива слово повинно бути конвертовано в нижній регістр 
(lovercase).
Сортування повинно бути виконано від найпопулярніших слів до найменш популярних.
Якщо слова мають однакову популярність, сортування повинно бути виконано за абеткою.
Приклади:

popularity('apple kiwi pineapple kiwi apple kiwi') -> ['kiwi', 'apple', 'pineapple']
popularity('aPPle pine Apple kiwi Apple kiwi') -> ['apple', 'kiwi', 'pine']
popularity('aPPle pine Apple kiwi Apple kiwi') -> ['apple', 'kiwi', 'pine']
popularity('aab aaa aac aab aac aaa x') -> ['aaa', 'aab', 'aac', 'x'] """


#from collections import Counter

def popularity(text):

    new_tx_lower = text.lower()
    new_text = new_tx_lower.split()

    #cnt = Counter(''.join(sorted(s.split())) for s in new_text)

    dct = {}
    for word in new_text:
        key = word
        dct[key] = dct.get(key,0) +1
    
    def get_second_key(item):
        return item[1]
    
    def get_first_key(item):
        return item[0]


    dct.items()

    # 4. sort by words
    sorted_by_word = sorted(dct.items(), key=lambda item: item[0])

    # 5. sort by occurances
    sorted_by_popularity = sorted(sorted_by_word, key=get_second_key, reverse=True)
    
    # return
    sorted_words = list(map(get_first_key, sorted_by_popularity))
    return sorted_words

    

print(popularity('apple kiwi pineapple kiwi apple kiwi')) # ['kiwi', 'apple', 'pineapple']
print(popularity('aPPle pine Apple kiwi Apple kiwi')) # ['apple', 'kiwi', 'pine']
print(popularity('aPPle pine Apple kiwi Apple kiwi')) # ['apple', 'kiwi', 'pine']
print(popularity('aab aaa aac aab aac aaa x')) # ['aaa', 'aab', 'aac', 'x']


