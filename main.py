from random import choice
emp1 = ["Дорога", "Рабство", "Революция", "Уничтожение", "Улица", "Убийства", "Притеснение", "Африканец", "Афёра", "Поля", "Хлопок", "Лён", "Нитрат", "Нитрит", "Разгром", "Ассимиляция", "Монархия", "Штурм", "Преграда", "Дом", "Обвинение", "Автотроника"]
p1 = 10
a = choice(emp1).lower()
hf = a
hf = list(a.lower())
print("Добро пожаловать в игры на виселицу! В первый раз?")
z = ""
win = False
zg = z
z = list(len(hf)*"*")
while p1 > 0:
    print("Твои шансы", p1)
    print("Слово", z)
    print("Слово целиком или одна буква?")
    print("[1] слово целиком")
    print("[2] одна буква")
    na = input("Вы выбрали: ")
    if na == "1":
        titanholo = input("Слово(буквы писать черел пробел").lower()
        if titanholo == p1:
            print("Ты выиграл!")
            ins = True
            break
        else:
            print("Неправильно")
            hp -= 1
    if na == "2":
        ne = input("Буква: ").lower()
        if ne on a:
            for x in range(len(a)):
                if ne == a[x]:
                    z[x] = ne
        else:
            print("Такой буквы здесть нету")
            p1 -= 1
    if z == a:
        win = true
        break
  if win == True:
    print("Молодец, ты угадал слово")
