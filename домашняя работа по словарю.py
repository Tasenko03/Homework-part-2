"""Дан словарь d = {'snow': 'снег', 'sun': 'солнце', 'rain': 'дождь', 'cloud': 'облако'}.
Используя данные из этого словаря, выведите на экран предложения в формате:
The translation of "<слово на английском>" into Russian is "<слово на русском>".
Должно получиться:
The translation of "snow" into Russian is "снег".
The translation of "sun" into Russian is "солнце".
The translation of "rain" into Russian is "дождь".
The translation of "cloud" into Russian is "облако"."""

d = {"snow": "снег", "sun": "солнце", "rain": "дождь", "cloud": "облако"}
for k, v in d.items():
    print(f"The translation of '{k}' into Russian is '{v}'.")

k = (
    input("\nChoose the word: snow, sun, rain, cloud. Your choice: ").lower().strip()
)  # 2 вариант, ввод от пользователя
while True:
    try:
        print(f"The translation of '{k}' into Russian is '{d[k]}'.")
        break
    except KeyError:
        print("Enter the word in list: ")
        k = input().strip().lower()
