import caesarCipher
import freq

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def main():
    with open(r'texts\ForUser.txt', 'r', encoding='utf-8') as t:
        text = t.read()
        t.close()
    print(caesarCipher.caesar_encrypt(text, 3, alphabet))

    # with open(r'texts\ToHack.txt', 'w', encoding='utf-8') as upload_t:
    #     upload_t.write(a)
    #     upload_t.close()

    n = caesarCipher.create_freq_list_for_ciphertext(alphabet)

    caesarCipher.decrypt_caesar_cipher_using_freq_an(n, )


if __name__ == '__main__':
    main()
