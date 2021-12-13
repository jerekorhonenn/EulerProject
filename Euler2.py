limit=4000000
a = 1
b = 1
summa = 0
while b<=limit:
    temp = a
    a = b
    b = temp + b
    if b%2==0:
        summa += b
print(summa)






