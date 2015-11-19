# -*- coding: utf-8 -*-

import random
a=random.randint(1,100)
print "숫자를 맞춰보세요 (1~100)"
b = int(raw_input())
while (b <> a):
    if b > a:
        print "숫자가 너무 큽니다."
    else:
        print "숫자가 너무 작습니다."
    b = int(raw_input())
else:
    print "정답입니다. ", "입력한 숫자는 " , b ,"입니다."
