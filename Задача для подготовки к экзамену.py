"""Создайте и вызовите функцию decypher(), которая принимает в качестве аргумента строку с числами, расшифровывает её
и возвращает расшифрованную строку-предложение.
Каждое число в исходной строке переводится в букву с помощью таблицы:

1 = A
2 = B
...
26 = Z

В исходной строке числа разделены между собой пробелами, а слова - символом +.

Пример:
>>> decypher("1 14 4+14 15 20 8 9 14 7+5 12 19 5+13 1 20 20 5 18 19")
AND NOTHING ELSE MATTERS"""


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decypher(numbers: str) -> None:
    numbers = numbers.replace("+", "  ")
    numbers_list = numbers.split(" ")
    str_return = ""
    for i in numbers_list:
        if i == "":
            str_return += " "
        else:
            try:
                d = int(i)
            except ValueError:
                print("Error")
            else:
                str_return += alphabet[d - 1]
    print(str_return)


decypher("1 14 4+14 15 20 8 9 14 7+5 12 19 5+13 1 20 20 5 18 19")
