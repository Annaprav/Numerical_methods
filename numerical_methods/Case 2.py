#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Задание 2. Матрицы, матричные преобразования, поиск детерминанта. 


# In[3]:


# в данной части кода заданы все основные функции, её необходимо запустить для выполнения дальнейших заданий.

try: # в данной части кода мы пробуем импортировать библиотеки, и если их нет - устанавливаем и заново подключаем.
    import random
except ModuleNotFoundError:
    install('random')
    import random
    
try:
    import csv
except ModuleNotFoundError:
    install('csv')
    import csv
    
try:
    import numpy as np
except ModuleNotFoundError:
    install('numpy')
    import numpy as np
    
try:
    import time
except ModuleNotFoundError:
    install('time')
    import time
    
try:    
    import webbrowser
except ModuleNotFoundError:
    install('webbrowser')
    import webbrowser


def Print_M(matrix): #вывод матрицы построчно
    for i in range(len(matrix)):
        print(matrix[i])
        
def Command_List(): # список команд для типа ввода матрицы
    print('\nВведите, каким способом вы хотите задать матрицу: ')
    a = input('1. Вручную \n2. CSV-файл \n3. Рандомная генерация\n0. Выход \nВведите команду: ')
    return a
        
def Input_M_T(strings, columns): # ввод с клавиатуры матрицы произвольной длины
    matrix_out = []
    print('Вводите значения строки через пробел: ')
    for i in range(strings):
        s = input() 
        row = [x for x in s.split()] 
        matrix_out.append(row)
    for i in range(len(matrix_out)): 
        for j in range(len(matrix_out)):
            matrix_out[i][j] = matrix_out[i][j]
    return matrix_out

def Input_M(strings, columns): # ввод с клавиатуры матрицы произвольной длины
    matrix_out = []
    print('Вводите значения строки через пробел: ')
    while (True):
        is_complex = input('Если хотите вводить c комплексными числами, введите 1,  только действительные - 2: ')
        if is_complex == '1':
            print('Вводите значения строки через пробел: ')
            print('Вводите значения комплексного числа через запятую,пример: 1,2 = 1 + i*2')
            for i in range(strings):
                s = input() 
                row = [x for x in s.split()]
                row2 = []
                for j in range(len(row)):
                    
                    row3 = []
                    row3.append([float(x) for x in row[j].split(',')])
                    if len(row3[0]) == 1:
                        row3[0].append(0) 
                    row2.append(complex(row3[0][0],row3[0][1]))   
                matrix_out.append(row2)
            for i in range(len(matrix_out)):
                for j in range(len(matrix_out)):
                    matrix_out[i][j] = complex(matrix_out[i][j])
            return matrix_out
            return 
            break
        elif is_complex == '2':
            print('Вводите значения строки через пробел: ')
            for i in range(strings):
                s = input() 
                row = [float(x) for x in s.split()] 
                matrix_out.append(row)
            for i in range(len(matrix_out)):
                for j in range(len(matrix_out)):
                    matrix_out[i][j] = float(matrix_out[i][j])
            return matrix_out
            break
        else:
            print('Неправильная команда')
    
        
def Gen_M(strings, columns): #рандомная генерация матрицы по указанному кол-ву столбцов и строк
    matrix = []
    for i in range(strings):
        row = []
        for j in range(columns):
            gen_num = random.randint(1, 20)
            row.append(gen_num)
        matrix.append(row)
    return matrix

def Addiction(matrix_1, matrix_2): #сложение
    matrix_out = []
    for i in range(len(matrix_1)):
        if (len(matrix_1)==len(matrix_2)):
            if (len(matrix_1[i])==len(matrix_2[i])):
                row = []
                for j in range(len(matrix_1[i])):
                    summ = matrix_1[i][j]+matrix_2[i][j]
                    row.append(summ)
                matrix_out.append(row)
            else:
                print('Разное кол-во столбцов')
        else:
            print('Разное кол-во строк')
    return matrix_out

def Substarction(matrix_1, matrix_2): #вычитание
    matrix_out = []
    for i in range(len(matrix_1)):
        if (len(matrix_1)==len(matrix_2)):
            if (len(matrix_1[i])==len(matrix_2[i])):
                row = []
                for j in range(len(matrix_1[i])):
                    summ = matrix_1[i][j]-matrix_2[i][j]
                    row.append(summ)
                matrix_out.append(row)
            else:
                print('Разное кол-во столбцов')
        else:
            print('Разное кол-во строк')
    return matrix_out

def Multiply_by_number(matrix_1, number): #умножение матрицы на число
    matrix_out = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[i])):
            new_number = matrix_1[i][j]*number
            row.append(new_number)
        matrix_out.append(row)
    return matrix_out

def Multiply(matrix_1, matrix_2): #умножение двух матриц, проверка на то, можно ли их умножить
    summ = 0
    row = []
    matrix_out = []
    if (len(matrix_1)==len(matrix_2[0])):
        for z in range(0, len(matrix_1)):
            for j in range(0, len(matrix_2[0])):
                for i in range (0, len(matrix_1[0])):
                    summ = summ + matrix_1[z][i]*matrix_2[i][j]
                row.append(summ)
                summ = 0
            matrix_out.append(row)
            row = []
        return matrix_out
    else:
        print('Данные матрицы нельзя перемножить. ')

def Transpose(matrix_1): #транспонирование
    matrix_t=[]
    for j in list(range(len(matrix_1[0]))):
        row=[]
        for i in list(range(len(matrix_1))):
            row.append(matrix_1[i][j])
        matrix_t.append(row)
    return(matrix_t)

def det2(matrix): #определитель 2*2
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
 
def minor(matrix, i, j): #миноры матрицы
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp
 
def determinant(matrix): #определитель в целом поиск
    if (len(matrix))==(len(matrix[0])):
        size = len(matrix)
        if size == 2:
            return det2(matrix)
        return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
                   for j in range(size))
    else:
        print('Это не квадратная матрица. Найти определитель невозможно. ')

def CSV_files_A(): # считываем матрицу A из CSV файла
    try:
        with open('Matrix_A.csv', encoding='utf-8-sig') as data_file:
            string_csv = []
            A = []
            for line in data_file:
                string_csv=line.strip().split(';')
                string_csv = [float(x) for x in string_csv]
                A.append(string_csv)
        return A
    except FileNotFoundError:
        print('Перед выполнением операции с CSV файлами создайте в директории CSV-файл с названием Matrix_A.csv и перезапустите программу')

def CSV_files_A_T(): # считываем матрицу A из CSV файла
    try:
        with open('Matrix_A.csv', encoding='utf-8-sig') as data_file:
            string_csv = []
            A = []
            for line in data_file:
                string_csv=line.strip().split(';')
                string_csv = [x for x in string_csv]
                A.append(string_csv)
        return A
    except FileNotFoundError:
        print('Перед выполнением операции с CSV файлами создайте в директории CSV-файл с названием Matrix_A.csv и перезапустите программу')
        
def CSV_files_B(): # считываем матрицу B из CSV файла
    try:
        with open('Matrix_B.csv', encoding='utf-8-sig') as data_file:
            string_csv = []
            B = []
            for line in data_file:
                string_csv=line.strip().split(';')
                string_csv = [float(x) for x in string_csv]
                B.append(string_csv)
        return B
    except FileNotFoundError:
        print('Перед выполнением операции с CSV файлами создайте в директории CSV-файл с названием Matrix_B.csv и перезапустите программу')


# функции для проверки и сравнение по времени

def Transpose_NP(matrix): # транспонирование с использованием numpy
    c0 = time.perf_counter()
    matrix_out = matrix.transpose()
    c1 = time.perf_counter()
    c2 = c1 - c0
    return c2

def Eval(c): # считывание A+B*C и прочее
    cc = eval(c)
    return cc

def Determinant_NP(matrix): # поиск детерминанта с использованием numpy
    c0 = time.perf_counter()
    np.linalg.det(matrix)        
    c1 = time.perf_counter()
    c2 = c1-c0
    return c2


def What_is_faster(a, b):
    if a<b:
        return print('Встроенная функция numpy быстрее. ')
    else:
        return print('Функция, написанная нами, быстрее. ')


# Задание 1. Транспонирование матрицы.

# In[123]:


while (True):
    command_input = Command_List()
    
    if command_input == '1':
        strings = int(input('Введите количество строк: '))
        columns = int(input('Введите количество символов: '))
        A = Input_M_T(strings, columns)
        print('Ваша матрица: ')
        Print_M(A)
        print('Транспонирование: ')
        c0 = time.perf_counter()
        Print_M(Transpose(A))
        c1 = time.perf_counter()
        print('Время, которое заняло транспонирование:',c1-c0)
        print('Время, которое заняло транспонирование с помощью numpy:', Transpose_NP(np.matrix(A)))
        What_is_faster(Transpose_NP(np.matrix(A)), c1-c0)
    
    elif command_input == '2':
        A = CSV_files_A_T()
        if A:
            print('Ваша матрица: ')
            Print_M(A)
            print('Транспонирование: ')
            c0 = time.perf_counter()
            Print_M(Transpose(A))
            c1 = time.perf_counter()
            print('Время, которое заняло транспонирование:',c1-c0)
            print('Время, которое заняло транспонирование с помощью numpy:', Transpose_NP(np.matrix(A)))
            What_is_faster(Transpose_NP(np.matrix(A)), c1-c0)
    
    elif command_input == '3':
        strings = int(input('Введите количество строк: '))
        columns = int(input('Введите количество символов: '))
        A = Gen_M(strings, columns)
        print('Ваша матрица: ')
        Print_M(A)
        print('Транспонирование: ')
        c0 = time.perf_counter()
        Print_M(Transpose(A))
        c1 = time.perf_counter()
        print('Время, которое заняло транспонирование:',c1-c0)
        print('Время, которое заняло транспонирование с помощью numpy:', Transpose_NP(np.matrix(A)))
        What_is_faster(Transpose_NP(np.matrix(A)), c1-c0)
    
    elif command_input == '0':
        print('Cпасибо, что были с нами. ')
        break
        
    else:
        print('Ошибка, вы ввели неправильную команду. ')


# 2 задание. Действия с матрицами.

# In[6]:


def Matrix_choice_B():
    print('Выберите способ ввода матрицы')
    command = input('1. Вручную\n2. CSV-файл\n3. Рандомная генерация.\nКоманда: ')
    if command == '1':
        strings = int(input('Кол-во строк: '))
        columns = int(input('Кол-во столбцов: '))
        B = Input_M(strings, columns)
        Print_M(B)
        return B
    elif command == '2':
        B = CSV_files_B()
        Print_M(B)
        return B
    elif command == '3':
        strings = int(input('Кол-во строк: '))
        columns = int(input('Кол-во столбцов: '))
        B = Gen_M(strings, columns)
        Print_M(B)
        return B
    else:
        print('Неправильная команда.')
        
matrix_moves = []

print('Выберите способ ввода матрицы A: ')
command_main = input('1. Вручную\n2. CSV-файл\n3. Рандомная генерация.\nКоманда:')

if command_main == '1': # ввод основной матрицы с клавиатуры
    print('Введите матрицу A: ')
    strings = int(input('Кол-во строк: '))    
    columns = int(input('Кол-во столбцов: '))
    A = Input_M(strings, columns)
    print('Ваша матрица: ')
    Print_M(A)
elif command_main == '2': # считывание основной матрицы с CSV-файла
    print('Ваша матрица: ')
    A = CSV_files_A()
    Print_M(A)
elif command_main == '3': # генерация основной матрицы рандомно.
    print('Введите матрицу A: ')
    strings = int(input('Кол-во строк: '))    
    columns = int(input('Кол-во столбцов: '))
    A = Gen_M(strings, columns)
    print('Ваша матрица: ')
    Print_M(A)
else:
    print('Неправильная команда')

command_input = 'abc'
if command_main == '1' or command_main == '2' or command_main == '3':
    while command_input != '0':

        print('Выберите действие: ')
        print('1. Умножить на число, 2. Умножить на другую матрицу, 3. Сложить с другой матрицей, 4. Вычесть другую матрицу, 0. Выход.')
        command_input = input('Команда: ')

        if command_input == '1':
            number = int(input('Введите число, на которое будет умножена матрица: '))
            A = Multiply_by_number(A, number)
            print('Матрица *', number,':')
            Print_M(A)
            matrix_moves.append('Умножение на число')

        elif command_input == '2':
            B = Matrix_choice_B()
            print('Нужно ли умножить 2 матрицу на какое-то число? Введите "Да", нажмите "enter", если хотите пропустить этот шаг.')
            command_input_2 = input('Команда: ')

            if command_input_2 == 'Да' or command_input_2 == 'да':
                number = int(input('Введите число, на которое будет умножена матрица: '))
                B = Multiply_by_number(B, number)
                print('Матрица *', number,':')
                Print_M(B)
                matrix_moves.append('Умножение второй матрицы на число')

            print('Результат промежуточных вычислений: ')
            Print_M(A)    
            print('*')
            Print_M(B)
            print('=')
            A = Multiply(A, B)
            Print_M(A)
            matrix_moves.append('Умножение на другую матрицу')

        elif command_input == '3':
            B = Matrix_choice_B()
            print('Нужно ли умножить 2 матрицу на какое-то число? Введите "Да", нажмите "enter", если хотите пропустить этот шаг. ')
            command_input_2 = input('Команда: ')

            if command_input_2 == 'Да' or command_input_2 == 'да':
                number = int(input('Введите число, на которое будет умножена матрица: '))
                B = Multiply_by_number(B, number)
                print('Матрица *', number,':')
                Print_M(B)
                matrix_moves.append('Умножение второй матрицы на число')

            print('Результат промежуточных вычислений: ')
            Print_M(A)    
            print('+')
            Print_M(B)
            print('=')
            A = Addiction(A, B)
            Print_M(A)
            matrix_moves.append('Сложение с другой матрицей')

        elif command_input == '4':
            B = Matrix_choice_B()
            print('Нужно ли умножить 2 матрицу на какое-то число? Введите "Да", нажмите "enter", если хотите пропустить этот шаг.')
            command_input_2 = input('Команда: ')

            if command_input_2 == 'Да' or command_input_2 == 'да':
                number = int(input('Введите число, на которое будет умножена матрица: '))
                B = Multiply_by_number(B, number)
                print('Матрица *', number,':')
                Print_M(B)
                matrix_moves.append('Умножение второй матрицы на число')

            print('Результат промежуточных вычислений: ')
            Print_M(A)    
            print('-')
            Print_M(B)
            print('=')
            A = Substarction(A, B)
            Print_M(A)
            matrix_moves.append('Вычитание другой матрицы')

        elif command_input == '5':
            webbrowser.open('https://i.gifer.com/H5KZ.mp4', new=2)
        
        elif command_input == '0':
            break
        else:
            print('Неправильная команда. ')


    print()    
    print('Матрица после итоговых вычислений: ')
    Print_M(A)
    print('\n Действия, которые вы выполняли с исходной матрицей: ')
    for i in range(len(matrix_moves)):
        print(i+1,'-', matrix_moves[i])
        
else:
    print('Перезапускайте. ')


# In[ ]:


# сравнение с numpy


# In[125]:


A = None
B = None
C = None
D = None
E = None

while (True):
    comm = int(input('0. Для выхода из программы. \nВведите кол-во матриц: '))
    if comm == 0:
        print('Спасибо за работу. ')
        break
        
    print(comm)
    if comm>=1:
        A = np.array(Gen_M(5, 5))
    if comm>=2:
        B = np.array(Gen_M(5, 5))
    if comm>=3:
        C = np.array(Gen_M(5, 5))
    if comm>=4:
        D = np.array(Gen_M(5, 5))
    if comm>=5:
        E = np.array(Gen_M(5, 5))

    if comm>5:
        print('Слишком много матриц')
        break

    if A is not(None):
        print('Матрица A: ')
        Print_M(A)
        print()
        if B is not(None):
            print('Матрица B: ')
            Print_M(B)
            print()
            if C is not(None):
                print('Матрица C: ')
                Print_M(C)
                print()
                if D is not(None):
                    print('Матрица D: ')
                    Print_M(D)
                    print()
                    if E is not(None):
                        print('Матрица E: ')
                        Print_M(E)
                        print()
    
    com = 'abc'
    while com!='0':
        com = input('0.Для выхода в меню генерации матриц. \nВведите выражение.')
        if com!='0':
            c0 = time.perf_counter()
            print('Ответ: ')
            Print_M(Eval(com))
            c1 = time.perf_counter()
            print('Время выполнения программы:', c1-c0)
    


# 3 задание. Нахождение определителя, сравнение с numpy.

# In[9]:


while (True):
    command_input = Command_List()
    print('0. Выход. ')
    
    if command_input == '1':
        strings = int(input('Введите размерность матрицы: '))
        A = Input_M(strings, strings)
        print('Ваша матрица: ')
        Print_M(A)
        c0 = time.perf_counter()
        det = determinant(A)
        c1 = time.perf_counter()
        print('Определитель равен:', det)
        if det is not(None):
            print('Время нахождения определителя:', c1-c0)
            print('Время нахождения определителя с помощью numpy', Determinant_NP(np.matrix(A)))
            What_is_faster(Determinant_NP(np.matrix(A)), c1-c0)
    
    elif command_input == '2':
        A = CSV_files_A()
        if A:
            print('Ваша матрица: ')
            Print_M(A)
            c0 = time.perf_counter()
            det = determinant(A)
            c1 = time.perf_counter()
            print('Определитель равен:', det)
            if det is not(None):
                print('Время нахождения определителя:', c1-c0)
                print('Время нахождения определителя с помощью numpy', Determinant_NP(np.matrix(A)))
                What_is_faster(Determinant_NP(np.matrix(A)), c1-c0)
    
    elif command_input == '3':
        strings = int(input('Введите размерность матрицы '))
        A = Gen_M(strings, strings)
        print('Ваша матрица: ')
        Print_M(A)
        c0 = time.perf_counter()
        det = determinant(A)
        c1 = time.perf_counter()
        print('Определитель равен:', det)
        if det is not(None):
            print('Время нахождения определителя:', c1-c0)
            print('Время нахождения определителя с помощью numpy', Determinant_NP(np.matrix(A)))
            What_is_faster(Determinant_NP(np.matrix(A)), c1-c0)
            
    elif command_input == '0':
        print('Спасибо за работу.')
        break
        
    else:
        print('Неправильная команда. ')
    


# In[ ]:




