#!/usr/bin/env python
import subprocess

child = subprocess.Popen (["atop -M 10 3 > /home/german/process.txt"], shell=True)

child.wait()

file_1 = open('/home/german/process.txt', 'r')
file_2 = open('/home/german/process_01.txt', 'w')
for line in file_1.xreadlines():
    PID = line [4:5]
    if PID.isdigit() and int(line [60:62]) > 0:
        print line
        file_2 = open('/home/german/process_01.txt', 'a')
        file_2.write(line + '\n')


