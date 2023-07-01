b = int(input("Введите количество монет: "))
tails = 0
emblem = 0
for i in range(b):
    a = int(input())
    if a == 0:
        tails +=1
    else:
        emblem +=1  
if tails > emblem:
    print(emblem)
else:
    print(tails)
