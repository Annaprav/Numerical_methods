#!/usr/bin/env python
# coding: utf-8

# Правила ввода функции:
# 1. Функции НЕ должны быть заданы неявно. Все фукнции пишутся с переменной x. Переменные a,b,c,d,s,e и прочие буквы лат. алфавита не допускаются.
#     прим: Введите функцию: x+1; x/2
# 2. Знаки для обозначения выражений:
#     2.1. + - сложение
#     2.2. - - вычитание
#     2.3. / - деление
#     2.4. * - умножение
#     2.5. // - целочисленное деление
#     2.6. % - остаток от деления чисел.
#         прим: Введите функцию: x//2; x*x**4
# 3. После написания функции не нужно ставить никаких знаков в виде точки или точки с запятой.
#     прим: Введите функцию: x/2. - это неправильно, правильно: x/2
# 4. Другие действия с переменными:
#     4.1. Факториал - factorial(x)
#     4.2. Экспонента - exp
#     4.3. Логарифим по базе log(x, [base]), если base не записано, то вычисляется нат. логарифм.
#     4.4. Логарифм от 10 - log10()
#     4.5. Логарифм от 2 - log2()
#     4.6. Квадратный корень - sqrt()
#     4.7. arcsin, arctg, arccos, arcctg - acos(), asin(), atg(), actg()
#     4.8. Константа пи - pi
#     4.9. 
#     

# In[ ]:


# основной код и графики
from math import factorial, exp, log, log10, log2, sqrt, pow, acos, asin, atan, pi, atan2, cos, sin, tan, cosh, sinh, tanh, acosh, atanh
import matplotlib.pyplot as plt
from mpmath import *
mas1 = []; mas2 = []; mas3 = []
mas4 = []; mas5 = []; mas6 = []


def f(x):
    return eval(func)

def fdx(x, h): # рассчет дифференциала от значения x с шагом h
    func = (f(x+h)-f(x-h))/(2*h)
    return func

def F(a, x): # рассчет интеграла от значения шо на шо не пОнЯтНо, АнЯ оБъЯсНиТ
    func = (f(a) + f(x)) * (x-a)/2
    return func

def integ(a, b, step): # рассчет интеграла и вывод результата
    inter = a + step  
    plt.plot()
    plt.title("Графики функций f(x), f'(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid() # сеточка
    for i in range (1,int((b-a)/step)): #(1)
        print('x =' ,mpf(inter),'f(x) =', mpf(f(inter)),"F(x) =", mpf(F(a,inter)))
        plt.scatter(mpf(inter),mpf(F(inter, step)),color = 'g')
        plt.scatter(mpf(inter),mpf(f(inter)), color='b')
        inter = inter + step 
    return ('Интегрирование завершено.')
    

def diff(a, b, step): # рассчет дифференциала и вывод результата, когда a,b>0
    inter = a # шаг итерации функции или как это называется я хз 
    plt.plot()
    plt.title("Графики функций f(x), f'(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid() # сеточка
    for i in range (1, int((b-a)/step)+2): #(1)
        print('x =', mpf(inter),'f(x) =', mpf(f(inter)),"f'(x) =", mpf(fdx(inter, step))) 
        plt.scatter(mpf(inter),mpf(fdx(inter, step)),color = 'g')
        plt.scatter(mpf(inter),mpf(f(inter)), color='b')
        inter = inter + step 
    plt.show()   
    return ('Дифференцирование завершено.')


while (1==1): # для бесконечного повторения цикла
    func = input('Введите функцию: ')
    a = float(input('Введите нижний предел: '))
    b = float(input('Введите верхний предел: '))     
    if (a>b): # если предел a > b - это невозможно, выводим ошибку отправляем в начало.
        print ('Ошибка ввода. Вы ввели неправильный предел. ')       
    else:
        com = 'abc'
        while com != '0': # чтобы команды спрашивались бесконечно, пока нормально не будут введены
            com = input('Введите "1" для дифференцирования, введите "2" для интегрирования.\n "0" для выхода из программы ')
            if com == '1':
                step = float(input('Введите шаг дифференцирования: '))
                if (int(b-a)<step): # если шаг больше, чем область дифф-ия, то тогда выводим ошибку и отправляем в начало
                    print ('Ошибка ввода, шаг дифференцирования не может быть больше области дифференцирования.')
                else:               #если шаг меньше, и все хорошо, тогда выводим результат и забываем о существовании программы.
                    print(diff(a, b, step))
                    break
                break
            if com == '2':
                step = float(input('Введите шаг интегрировния : '))
                if (int(b-a)<step): # если шаг больше, чем область дифф-ия, то тогда выводим ошибку и отправляем в начало
                    print ('Ошибка ввода, шаг дифференцирования не может быть больше области интегрирования .')
                else:               #если шаг меньше, и все хорошо, тогда выводим результат и забываем о существовании программы.
                    print(integ(a, b, step))
                    break
                break
            else:
                print('Введена неправильная команда.')
    


# In[ ]:


# Строим графики для дифференциала

plt.plot(mas1, mas2, mas1, mas3)
plt.title("Графики функций f(x), f'(x)") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid() # сеточка
plt.scatter( label = "f'(x)") # легенда для графика производной
plt.plot( label = "f(x)") # легенда для графика функции
plt.legend() # запись легенды
plt.show() # вывод графика

plt.plot(mas1, mas3,'g')
plt.title("График функции f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
        
plt.scatter(mas1, mas2)
plt.title("График функции f'(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


# In[4]:


# Строим графики для интеграла

plt.plot(mas4, mas5, mas4, mas6)
plt.title("Графики функций f(x), f'(x)") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid() # сеточка
plt.scatter(mas4, mas5, label = "f'(x)") # легенда для графика производной
plt.plot(mas4, mas6, label = "f(x)") # легенда для графика функции
plt.legend() # запись легенды
plt.show() # вывод графика

plt.plot(mas4, mas6,'g')
plt.title("График функции f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
        
plt.scatter(mas4, mas5)
plt.title("График функции f'(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


# In[ ]:


plt.scatter( label = "f'(x)") # легенда для графика производной
plt.plot( label = "f(x)") # легенда для графика функции
plt.legend() # запись легенды
plt.show() 


# In[ ]:




