def encryption_in_russian(chars, shift):
    capital_rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    small_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    new_string = ''
    for c in chars:
        if c not in capital_rus and c not in small_rus:
            new_string += c
            continue

        elif c == c.upper():
            res = capital_rus.index(c) + shift
            if res >= 31:
                buf = len(capital_rus) - capital_rus.index(c)
                res = shift - buf
                new_string += capital_rus[res]
            else:
                new_string += capital_rus[res]
        elif c == c.lower():
            res = small_rus.index(c) + shift
            if res >= 31:
                buf = len(small_rus) - small_rus.index(c)
                res = shift - buf
                new_string += small_rus[res]
            else:
                new_string += small_rus[res]

    return new_string


def encryption_in_english(chars, shift):
    capital_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_eng = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    for c in chars:
        if c not in capital_eng and c not in small_eng:
            new_string += c
            continue

        elif c == c.upper():
            res = capital_eng.index(c) + shift
            if res >= 25:
                buf = len(capital_eng) - capital_eng.index(c)
                res = shift - buf
                new_string += capital_eng[res]
            else:
                new_string += capital_eng[res]
        elif c == c.lower():
            res = small_eng.index(c) + shift
            if res >= 25:
                buf = len(small_eng) - small_eng.index(c)
                res = shift - buf
                new_string += small_eng[res]
            else:
                new_string += small_eng[res]

    return new_string


def decryption_in_russian(chars, shift):
    capital_rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    small_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    new_string = ''
    for c in chars:
        if c not in capital_rus and c not in small_rus:
            new_string += c
            continue

        elif c == c.upper():
            res = capital_rus.index(c) - shift
            if res >= 31:
                buf = len(capital_rus) - capital_rus.index(c)
                res = shift + buf
                new_string += capital_rus[res]
            else:
                new_string += capital_rus[res]
        elif c == c.lower():
            res = small_rus.index(c) - shift
            if res >= 31:
                buf = len(small_rus) - small_rus.index(c)
                res = shift + buf
                new_string += small_rus[res]
            else:
                new_string += small_rus[res]

    return new_string


def decryption_in_eng(chars, shift):
    capital_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_eng = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    for c in chars:
        if (c not in capital_eng and c not in small_eng):
            new_string += c
            continue

        elif c == c.upper():
            res = capital_eng.index(c) - shift
            if res >= 31:
                buf = len(capital_eng) - capital_eng.index(c)
                res = shift + buf
                new_string += capital_eng[res]
            else:
                new_string += capital_eng[res]
        elif c == c.lower():
            res = small_eng.index(c) - shift
            if res >= 31:
                buf = len(small_eng) - small_eng.index(c)
                res = shift + buf
                new_string += small_eng[res]
            else:
                new_string += small_eng[res]

    return new_string




print('Введите строку: ')
chars = input()
print('Направление: шифрование или дешифрование? ш/д ')
if input() == 'ш':
    direction = True
else:
    direction = False
print('Язык алфавита: русский или английский? р/а')
if input() == 'а':
    language = True
else:
    language = False
print('Шаг сдвига (со сдвигом вправо): ')
shift = int(input())

if direction and language:
    res = encryption_in_english(chars, shift)
elif direction and not language:
    res = encryption_in_russian(chars, shift)
elif not direction and not language:
    res = decryption_in_russian(chars, shift)
elif not direction and language:
    res = decryption_in_eng(chars, shift)

print(res)
