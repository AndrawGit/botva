import csv
import re
import datetime
import plotly
import plotly.graph_objs
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

filepath1 = r"C:\Users\Andrey\Documents\query.csv"
filepath2 = r"C:\Users\Andrey\Documents\query1.csv"
now_date = datetime.date.today() # Текущая дата (без времени)

arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
#годы существования
arr6 = []
#годы войны
arr7 = []
#количество войн по годам
arr8 = []
#E
arr9 = []
with open(filepath1, "r", newline="") as file:
    #читаем файл целиком
    reader = csv.reader(file)

    for row in reader:
        #получаем 2 столбец stert_time
        cur_arr1 = row[1].split(',')
        #берём строку
        str1 = cur_arr1[0]
        #получаем первые 4 символа (дату)
        dat1 = str1[0:4]
        cur_arr2 = row[2].split(',')
        str2 = cur_arr2[0]
        dat2 = str2[0:4]
        #записываем в массив
        arr1.extend([dat1])
#        print(arr1)
        arr2.extend([dat2])
    #удаляем первый элемент
    del arr1[0]
    del arr2[0]
    #преобразуем элементы из str в int
    for i in range(len(arr1)):
        arr1[i] = int(arr1[i])
    for i in range(len(arr2)):
        arr2[i] = int(arr2[i])

    for i in range(len(arr1)):
        #если дата начала и конца битвы совпадают, добавляем дату начала в новый массив
        if arr1[i] == arr2[i] :
            arr3.append(arr1[i])
        #иначе добавляем каждую дату в интервале начала и конца битвы
        else:
            arr4.append(arr1[i])
            while arr1[i] != arr2[i]:
                arr1[i] = arr1[i] + 1
                arr4.append(arr1[i])


    arr7 = arr4 + arr3
    arr7.sort()
    print (arr7)
    c = Counter(arr7)
    print (c)
    #получаем дату основания
    with open(filepath2, "r", newline="") as file:
        # читаем файл целиком
        reader = csv.reader(file)
        for row in reader:
            cur_arr3 = row[0].split(',')
            str3 = cur_arr3[0]
            dat3 = str3[0:4]
            arr5.extend([dat3])
    del arr5[0]
    arr5[0] = int(arr5[0])
    arr6.append(arr5[0])
    #получаем текущую дату
    a = now_date.year
    #получаем массив дат, начиная с даты основания до текущей
    for i in range(len(arr5)):
        while arr5[i] != a:
            arr5[i] = arr5[i] + 1
            arr6.append(arr5[i])
    print(arr6)
    #Период существования страны
    Tc = len(arr6)
    print(Tc)

    #Получаем массив с ежегодным количеством битв
    for j in range(len(arr6)):
        a = 0;
        for i in range(len(arr7)):
            if arr6[j] == arr7[i]:
                a = a + 1
        arr8.append(a)
    print(arr8)

#    plotly.offline.plot({
#        "data": [
#            plotly.graph_objs.Bar(x=arr6, y=arr8)
#        ]
#    })

    plt.plot(arr6, arr8)
    plt.show()

# Эпсилон = 5
    E = 5
    n = 0
    #Находим количество мирных периодов (Tpi) и добавляем их в массив
    for i in range(len(arr8)):
        if arr8[i] == 0:
            n = n + 1
#            print(n)
        elif arr8[i] != 0 and n != 0:
            arr9.append(n)
            n = 0
    arr9.append(n)
    print(arr9)

    #Находим количество мирных периодов, которые больше или равны E (TpE)
    TpE = 0
    for i in range(len(arr9)):
        if arr9[i] >= E:
            TpE = TpE + arr9[i]
    print(TpE)

    #Находим период войны
    TwE = Tc - TpE
    print(TwE)
