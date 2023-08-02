list = [24,17,16,18]
for i in range(4):
    for j in range(i + 1,4):
        if list[i] > list[j]:
            a = list[i]
            list[i] = list[j]
            list[j] = a
print(list)