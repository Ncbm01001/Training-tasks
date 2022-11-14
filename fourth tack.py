# Задание 4
#Требуется написать код, который высчитывает минимальное требуемое количество сотрудников, выполняющих
# однотипную работу, в предположении, что все сотрудники единовременно выполняют одну единицу работы за
# одинаковое время и без перерывов. Код должен состоять из пользовательской функции, выполняющей все расчеты,
# и запроса информации от пользователей.
#Общий принцип работы кода:
#1. От пользователя последовательно запрашивается информация:
# - *workers* - количество сотрудников, которые уже выполняют задачи;
# - *tasks* - количество задач, которые нужно выполнить;
# - *time* - время, за которое выполняется одна задача (все задачи выполняются за равное количество времени);
#  - *overall_time* - время, в которое нужно уложиться при выполнении задач. Эти же данные передаются в функцию *new_workers()*.
#2. Функции *new_workers()* передается вся полученная информация.
#3. Функция *new_workers()* производит расчеты и возвращает минимальное количество сотрудников для
# выполнения всех задач за заданное время *overall_time*.
#4. На экран выводится результат *new_workers()*.

import math

def new_workers():

    print("Введите количество сотрудников, которые уже выполняют задачи.")
    workers = input()
    while not workers.isnumeric():
        print("Некорректный ввод.Попробуйте еще раз.")
        workers = input()

    print("Введите количество задач, которые нужно выполнить.")
    tasks = input()
    while not tasks.isnumeric():
        print("Некорректный ввод.Попробуйте еще раз.")
        tasks = input()

    print("Введите время, за которое выполняется одна задача.")
    time = input()
    while not time.isnumeric():
        print("Некорректный ввод.Попробуйте еще раз.")
        time = input()

    print("Введите время, в которое нужно уложиться при выполнении задач.")
    overall_time = input()
    while not overall_time.isnumeric():
        print("Некорректный ввод.Попробуйте еще раз.")
        overall_time = input()

    new_worker =((int(tasks) / (int(overall_time) / int(time))) - int(workers))
    if new_worker == 0:
        print("Дополнительные сотрудники не требуются")
    elif new_worker < 0:
        new_worker = new_worker * -1
        new_worker = math.ceil(new_worker)
        print(f'Допустимо уволить сотрудников: {new_worker} ')
    else:
        new_worker = math. ceil(new_worker)
        print(f'Для выполнения поставленной задачи требуется следующее количество дополнительных сотрудников: {new_worker} ')

print(new_workers())
