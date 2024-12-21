my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    j = my_list[i]
    i += 1
    if j == 0:
        continue
    elif j < 0:
        break
    print(j)

