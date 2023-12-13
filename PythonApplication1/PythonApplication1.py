import random

o = ["Камень", "Ножницы", "Бумага"]

userwins = 0
computerwins = 0
ties = 0

r = []
for _ in range(10):

    random.shuffle(o)
    while True:
        try:
            userchoice = input("Выберите Камень, Ножницы или Бумага: ").capitalize()
          
            if userchoice not in o:
                raise ValueError("Некорректный выбор. Пожалуйста, выберите Камень, Ножницы или Бумага.")

            break 

        except ValueError as e:
            print(e)

    computerchoice = random.choice(o)

    print(f'Компьютер выбрал: {computerchoice}')
    print(f'Вы выбрали: {userchoice}')

    if userchoice == computerchoice:
        print('Ничья!')
        ties += 1
    elif (userchoice == 'Камень' and computerchoice == 'Ножницы') or \
         (userchoice == 'Ножницы' and computerchoice == 'Бумага') or \
         (userchoice == 'Бумага' and computerchoice == 'Камень'):
        print('Вы победили!')
        userwins += 1
    else:
        print('Компьютер победил!')
        computerwins += 1

    r.append((userchoice, computerchoice))

print(f'\nИтоги после 10 раундов:')
print(f'Выигрыши пользователя: {userwins}')
print(f'Выигрыши компьютера: {computerwins}')
print(f'Ничьи: {ties}')

print(f'Результаты каждого раунда: {r}')

