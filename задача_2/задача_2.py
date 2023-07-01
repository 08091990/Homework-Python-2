x = int(input("введите сумму двух чисел "))
y = int(input("введите произведение двух чисел "))
for i in range(x):
    for j in range(y):
        if x == i+j and y == i * j:
            print(i, j) 