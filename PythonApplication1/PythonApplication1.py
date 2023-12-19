
o = ["Камень", "Ножницы", "Бумага"]

uw = 0  # user wins
cw = 0  # computer wins
t = 0   # ties

r = []  # results
for _ in range(10):
    random.shuffle(o)
    while True:
        try:
            uc = input("Выберите Камень, Ножницы или Бумага: ").capitalize()
          
            if uc not in o:
                raise ValueError("Некорректный выбор. Пожалуйста, выберите Камень, Ножницы или Бумага.")

            break 
        except ValueError as e:
            print(e)

    cc = random.choice(o)

    print(f'Компьютер выбрал: {cc}')
    print(f'Вы выбрали: {uc}')

    if uc == cc:
        print('Ничья!')
        t += 1
    elif (uc == 'Камень' and cc == 'Ножницы') or \
         (uc == 'Ножницы' and cc == 'Бумага') or \
         (uc == 'Бумага' and cc == 'Камень'):
        print('Вы победили!')
        uw += 1
    else:
        print('Компьютер победил!')
        cw += 1

    r.append((uc, cc))

print('\nИтоги после 10 раундов:')
print(f'Выигрыши пользователя: {uw}')
print(f'Выигрыши компьютера: {cw}')
print(f'Ничьи: {t}')

print(f'Результаты каждого раунда: {r}')
