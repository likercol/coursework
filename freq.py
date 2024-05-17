import re
import json


def generate_freq_dict(alphabet: str) -> dict:
    # Открываем "Войну и Мир"
    with open(r'texts\LeoTolstoyWarАndPeace.txt', 'r', encoding='utf-8') as freq_t:
        text = freq_t.read()
        freq_t.close()
    text = text.lower().replace(' ', '')  # Преобразование текста
    text = ''.join(re.findall('[а-я]', text))

    list_for_counted_letters = []
    dict_with_counted_letters = {}

    for i in range(len(alphabet)):
        list_for_counted_letters.insert(i, 1)
        dict_with_counted_letters[alphabet[i]] = list_for_counted_letters[i]

    for i in range(len(text)):
        dict_with_counted_letters[text[i]] += 1

    # upload_to_json(dict_with_counted_letters)

    return dict_with_counted_letters


def create_freq_list(alphbet: str) -> list:
    dict_with_counted_letters = generate_freq_dict(alphbet)
    freq_list = [
        letter for letter, value in sorted(dict_with_counted_letters.items(), key=lambda item: item[1], reverse=True)
    ]
    return freq_list


def upload_to_json(data):  # Функция для загрузки данных в файл
    with open("frequency.json", "w") as fr:
        json.dump(data, fr)
    with open("frequency.json", "r") as fr:
        d = json.load(fr)