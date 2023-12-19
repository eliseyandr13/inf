from random import randint
all = [randint(100, 500) for i in range(10)]
print(all)

def sumDigits(no): 
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10)) 


for i in all:
    print(sumDigits(i))