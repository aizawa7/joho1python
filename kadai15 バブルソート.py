list = [24,17,16,18]
a = 0
for i in range(3,0,-1):
    for j in range(i):
        if list[j] > list[j + 1]:
            a = list[j]
            list[j] = list[j + 1]
            list[j + 1] = a
print(list)