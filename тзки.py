import random

def encrypt(text, alphabet, substitution):
    """Функция шифрования"""
    used_symbols = {}
    encrypted_text = ""

    for char in text:
        if char not in used_symbols:  # Если символ встретился впервые
            used_symbols[char] = substitution[alphabet.index(char)]
        else:  # Если символ уже встречался
            r = random.randint(0, len(alphabet) - 1)
            a_idx = alphabet.index(char)
            # Меняем символы местами
            substitution[r], substitution[a_idx] = substitution[a_idx], substitution[r]
            used_symbols[char] = substitution[r]

        encrypted_text += used_symbols[char]

    return encrypted_text, substitution

def decrypt(encrypted_text, alphabet, substitution):
    """Функция дешифрования"""
    decrypted_text = ""

    for char in encrypted_text:
        decrypted_text += alphabet[substitution.index(char)]

    return decrypted_text

if __name__ == "__main__":
    # Исходный алфавит и подстановка
    alphabet = [' '] + [chr(i) for i in range(1040, 1072)] + ['b']
    substitution = alphabet[:]
    random.shuffle(substitution)

    # Текст для шифрования
    input_text = " ИНСТИТУТ "
    print(f"Исходный текст: {input_text}")

    # Шифрование
    encrypted_text, final_substitution = encrypt(input_text, alphabet, substitution)
    print(f"Зашифрованный текст: {encrypted_text}")

    # Дешифрование
    decrypted_text = decrypt(encrypted_text, alphabet, final_substitution)
    print(f"Расшифрованный текст: {decrypted_text}")
