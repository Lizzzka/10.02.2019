vote = {

}

count = int(input('Сколько групп\n'))
for number in range(count):
    key = input('Введите номер группы\n')
    value = input('Количество студентов\n')
    vote[key] = value

print(vote)
for chislo in range(count):
    group = input ('Группа под номером\n')
    kolyada = input ('Сколько проголосовало за Коляду?\n')
    vote[group] = kolyada

for chislo in range(count):
    print ('За Коляду проголосовало:' + str(kolyada))

for lo in range(count):
    group = input ('Группа под номером\n')
    modest = input ('Сколько проголосовало за Модест\n')
    vote[group] = modest
for lo in range(count):
    print ('За Модеста проголосовало:' + str(modest))


