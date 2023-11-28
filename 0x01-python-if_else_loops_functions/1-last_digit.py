#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
line1 = " and is greater than 5"
line2 = " and is 0"
line3 = " and is less than 6 and not 0"
if num < 0:
    last = num % -10
else:
    last = num % 10
if last > 5:
    print("Last digit of {} is {}".format(num, last) + line1)
elif last == 0:
    print("Last digit of {} is {}".format(num, last) + line2)
else:
    print("Last digit of {} is {}".format(num, last) + line3)
