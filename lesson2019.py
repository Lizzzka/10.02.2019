words = {
    'красивый': 'прекраснвый',
    'плохой': 'ужасный',
    'умный': 'мудрый',
    'необычный': 'нет синонима',
}
value = input('Введите синоним слова необычный\n')
words['необычный'] = value
print(words)
del words['необычный']

print (words)
