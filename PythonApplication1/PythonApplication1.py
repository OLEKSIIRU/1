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

#4 index
indexid=["Tallinn",
    "Narva, Narva-Jõesuu",
    "Kohtla-Järve",
    "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",
   "Tartu linn",
  "Tartumaa, Põlvamaa, Võrumaa, Valgamaa",
    "Viljandimaa, Järvamaa, Harjumaa, Raplamaa",
    "Pärnumaa",
    "Läänemaa, Hiiumaa, Saaremaa"]

while True:
    try:
        index=int(input("Введите свой почтовый индекс"))
        if len(str(index))=5:
            break
        except:
            print("Vigaa!")
print("Indexi analüüs")
is_number(index)
index_list=list(index)
s1=index_list[0] # 1->0 Tallinn indexiga 0
print("Index {0} on {1} piirkonnas".format(index,indexid[s1-1]))
if indexid[s1-1]<4:
    print("Оставайтесь дома!")
except
    print("Носите маски!")

#5
from ast import While
from random import*
from stringprep import c22_specials
kokku=randint(2,20)
num_list=[]
for i in range(kokku):
    num_list.append(randint(-100,100))
print(num_list)
print()
while True:
    try:
        kogus=int(input("Mitu positsiooni vahetaga?"))
        if kogus<=kokku/2:
            break
        except:
            print("Proovi uuesti")

for i in range (0,kogus,1):
    X_tmp = num:list[i]
    print(str(i)," ",str(num_list[i])," ",str(num_list[(len(num_list)-i)-1]),"\n")
    print(X_tmp, "\n")

    num_list[i]=num_list[(len(num_list)-i)-1]
    num_list[(len(num_list)-i)-1]=X_tmp
print("\n",num_list)

#6

from random import*
kokku=randint(2,20)
num_list=[]
for i in range(kokku):
    num_liste.append(round(random()*1000,2))
print(num_list)
while
max(num_list)>1:
m=max(num_list)
n=num_list.index(m)
print("\t",m,"positsioonil:",n+1)
num_list.pop(n)
m=m/len(num_list)
num_list.insert(n,m)
print("{num_list}")
print("The end")

#7
from random import*
kokku=randint(2,20)
num_list=[]
for i in range(kokku):
    num_list.append(randint(-1000,1000))
print(num_list)
print()
print("Len of numeric_list -"+str(len(num_list)))
for i in range(0,kokku,1):
    num_list[i] = abs(num_list[i])
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
