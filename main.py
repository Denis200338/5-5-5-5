arr = [4, -2, 6, 1, 3, 1, 0]

first_pos = None
for num in arr:
    if num > 0:
        first_pos = num
        break

if first_pos is None:
    print("Нет положительных элементов в массиве")
else:
    count = 0
    for num in arr:
        if num == first_pos:
            count += 1
    print(f"Количество элементов, равных первому положительному элементу ({first_pos}): {count}")