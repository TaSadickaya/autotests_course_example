def josephus_task(num_people, kill_num):
    survivor = 0
    for i in range(1, num_people +1):
        survivor = (survivor + kill_num) % i
    survivor += 1
    return survivor

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (7, 3), (11, 19), (1, 300), (14, 2), (100, 1), (1234, 56), (987, 11)
]

test_data = [
    4, 10, 1, 13, 100, 1130, 379
]


for i, d in enumerate(data):
    assert josephus_task(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')