#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
без команды python не запускается, нужно сохранить в другой кодировке (еще не разбирался)
'''

import subprocess

'''
запуск программы atop с интервалом 10 сек 3 раз, запись результатов в файл
'''
child = subprocess.Popen (["atop -C 10 3 > /home/german/atop.txt"], shell=True)

child.wait() # ждем окончания процесса

file_1 = open('/home/german/atop.txt', 'r') # открываем файл с результатами 'atop' для чтения
file_2 = open('/home/german/atop_sort.txt', 'w') # обнуляем файл с предыдущими результатами сортировки
for line in file_1.xreadlines(): # читаем файл построчно
    PID = line [4:5]
    if PID.isdigit() and int(line [60:62]) > 1: # определяем строку с процессом, если PU загружено больше чем на 1 % выводим строку на экран и пишем в файл
        print line # печатаем строку с "отклонениями"
        file_2 = open('/home/german/atop_sort.txt', 'a') # открываем файл для дозаписи
        file_2.write(line + '\n') # записываем строку с "отклонениями"


