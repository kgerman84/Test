#!/usr/bin/env python
import sys
a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
caunt = 0

for i in range (a1,a2+1):
    if ((i%10 + i%100//10 + i%1000//100)
        == (i%10000//1000 + i%100000//10000 + i%1000000//100000)):
        caunt = caunt + 1

f = open('test.txt', 'w')
f.write(str(caunt))
f.close()
print caunt 

