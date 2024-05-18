import re


def create_freq_list_for_ciphertext(text: str, alphabet: str) -> list:
    text = text.lower().replace(' ', '')  # Преобразование текста
    text = ''.join(re.findall('[а-я]', text))

    list_for_counted_letters = []
    dict_with_counted_letters = {}

    for i in range(len(alphabet)):
        list_for_counted_letters.insert(i, 1)
        dict_with_counted_letters[alphabet[i]] = list_for_counted_letters[i]

    for i in range(len(text)):
        dict_with_counted_letters[text[i]] += 1

    freq_list = [
        letter for letter, value in sorted(dict_with_counted_letters.items(), key=lambda item: item[1], reverse=True)
    ]
    return freq_list


def decrypt_caesar_cipher_using_freq_an(ciphertext: str, freq_list: list, real_freq_list: list):
    # Создаем словарь для расшифровки
    decryption_dict = {enc_char: real_char for enc_char, real_char in zip(freq_list, real_freq_list)}
    # Расшифровываем текст
    decrypted_text = ''.join(decryption_dict.get(char, char) for char in ciphertext)
    return decrypted_text
