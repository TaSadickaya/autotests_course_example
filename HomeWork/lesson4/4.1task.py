def which_triangle(a, b, c):
    type = ["Равносторонний", "Равнобедренный", "Обычный", "Не треугольник"]
    if a + b > c and b + c > a and a + c > b:
      if a == b == c:
        type_triangle = type[0]
      elif a == b:
        type_triangle = type[1]
      elif b == c:
        type_triangle = type[1]
      elif c == a:
        type_triangle = type[1]
      elif a != b != c:
        type_triangle = type[2]
    else:
        type_triangle = type[-1]
    return type_triangle

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник"
]


for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')