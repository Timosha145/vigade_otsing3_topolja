from random import *
s=nol=pos=neg=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => ")) 
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
        generaator(n,s,mini,maxi)
        print()
        print("Результаты:")
        print("Полученный список от",mini,"до",maxi,s)
        s.sort()
        print("Отсортированный список",s)
        jagamine(s,pos,neg,nol)
        print("Список положительных элементов",pos)
        print("Список отрицательных элементов",neg)
        print("Список нулевых элементов",nol)
        kesk=keskmine(pos)
        lisamine(s,kesk)
        print("Среднее положительных:",kesk)
        kesk=keskmine(neg)
        isamine(s,kesk)
        print("Среднее отрицательных:",kesk)
        print("Добавляем средние в изначалный массив:")
        s.sort()
        print(s)

def vahetus(a:int,b:int):
    """kui a>b, siis vahetame neid
    :param int a: Arv, mis on suurem kui b
    :param int b: Arv, mis on väiksem kui a
    :rtype:int, int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n,loend,a,b):
    """paneb numbrid loendisse
    :param int n: kui palju väärtusi on
    :param list loend: loend kuhu me paneme väärtused
    :param int a: min arv
    :param int b: max arv
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend,p,n,nol):
    """teeme kolm loenid ühest loendist
    :param list loend: loend kus on kõik väärtused
    :param int p: positiivsed väärtused
    :param int n: mitte positiivsed väärtused
    :param int nol: väärtused mis võrdne nulliga 
    """
    for el in loend:
        if el>0:
            p(append(pos))
        elif el<0:
            n(append(neg))
        else:
            nol(append(nol))

def keskmine(loend):
    """saame aru mis on keskmine arv loendis
    :param list loend: loend kus on kõik väärtused
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    """paneme kõik väärtused loendisse
    :param list loend: loend kus on kõik numbrid
    :param str el: ükskõik väärtus loendis
    """
    loend(append(el))
    loend(sort)

arvud_loendis()
