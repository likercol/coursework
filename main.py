import caesarCipher
import freq

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def read_text_from_file_in_texts(filename: str) -> str:
    with open(fr'texts\{filename}', 'r', encoding='utf-8') as t:
        text = t.read()
    return text


def upload_text_to_file(text: str, file: str):
    with open(file, 'w', encoding='utf-8') as upload_t:
        upload_t.write(text)
        upload_t.close()


def main():
    print("Выберите шифр: {}\n1) Шифр Цезаря\n2) Шифр Виженера")
    selected_cipher = int(input(": "))

    if selected_cipher == 1:
        print(
            'Вы выбрали манипуляции с шифром Цезаря.\nВыберите действие:\n1) Зашифровать\n2) Дешифровать\n3) Взломать')
        caesar_cipher_action = int(input(": "))

        match caesar_cipher_action:
            case 1:
                # Шифрование и запись шифротекста в файл
                filename_for_encrypt = input('Введите имя файла из каталога texts, чтобы зашифровать ваш текст: ')
                caesar_key = int(input('Выберите ключ шифрования: '))
                caesar_ciphertext = caesarCipher.caesar_encrypt(read_text_from_file_in_texts(
                    filename_for_encrypt),
                    caesar_key,
                    alphabet
                )
                print(caesar_ciphertext)
                upload_text_to_file(caesar_ciphertext, r'texts\Encrypted.txt')
                print('Этот зашифрованный текст записан в файл Encrypted.txt в каталоге texts')
            case 2:
                # Дефрование и запись дешифрованного текста в файл
                filename_for_decrypt = input('Введите имя файла из каталога texts, чтобы дешифровать ваш текст: ')
                caesar_key = int(input('Выберите ключ дешифрования: '))
                caesar_decrypted = caesarCipher.caesar_decrypt(read_text_from_file_in_texts(
                    filename_for_decrypt),
                    caesar_key,
                    alphabet
                )
                print(caesar_decrypted)
                upload_text_to_file(caesar_decrypted, r'texts\Decrypted.txt')
                print('Этот зашифрованный текст записан в файл Encrypted.txt в каталоге texts')
            case 3:
                real_freq_list = freq.create_freq_list(alphabet)
                filename_for_hack = input('Введите имя файла из каталога texts, чтобы взломать ваш текст: ')
                ciphertext_freq_list = caesarCipher.create_freq_list_for_ciphertext(
                    read_text_from_file_in_texts(filename_for_hack),
                    alphabet
                )
                caesar_hacked = caesarCipher.decrypt_caesar_cipher_using_freq_an(
                    read_text_from_file_in_texts(filename_for_hack),
                    ciphertext_freq_list,
                    real_freq_list
                )
                print(caesar_hacked)
                upload_text_to_file(caesar_hacked, r'texts\AfterFreqAnalysis.txt')

                print('\nЭтот предположительно взломанный текст записан в файл AfterFreqAnalysis.txt в каталоге texts')
                print('\nСписок реальной частотности букв и список частотности букв вашего шифротекста:')
                print(real_freq_list)
                print(ciphertext_freq_list)
            case _:
                print('Неверный выбор!')
    elif selected_cipher == 2:
        pass
    else:
        print('Неверный выбор!')


if __name__ == '__main__':
    main()
