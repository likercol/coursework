import re
from typing import Dict


def caesar_encrypt(plaintext: str, key: int, alphabet: str):
    plaintext = change_text(plaintext)
    # Создали удобный словарь с параметрами {буква : номер буквы}
    alphabet_dict: dict[str, int] = {}
    for i in range(len(alphabet)):
        alphabet_dict[alphabet[i]] = i

    # Создали список для открытого (исходного) текста в виде чисел
    plaintext_int = [alphabet_dict[plaintext[i]] for i in range(len(plaintext))]

    ciphertext = []

    for i in range(len(plaintext_int)):
        if (plaintext_int[i] + key) > (len(alphabet) - 1):
            symbol_value_for_ciphertext = plaintext_int[i] + key - len(alphabet)
        else:
            symbol_value_for_ciphertext = plaintext_int[i] + key

        ciphertext += alphabet[symbol_value_for_ciphertext]

    return ''.join(ciphertext)


def caesar_decrypt(ciphertext: str, key: int, alphabet: str):
    return caesar_encrypt(ciphertext, -key, alphabet)


def upload_caesar_ciphertext_to_file(ciphertext: str):
    with open(r'..\texts\ToHack.txt', 'w', encoding='utf-8') as upload_t:
        upload_t.write(ciphertext)
        upload_t.close()


def change_text(text) -> str:
    text = text.lower().replace(' ', '')  # Преобразование текста
    text = ''.join(re.findall('[а-я]', text))
    return text
