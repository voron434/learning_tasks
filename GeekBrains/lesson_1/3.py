# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

input_variable = input('Input age ')
print("Доступ разрешен" if int(input_variable) >= 18 else "Извините, пользование данным ресурсом только с 18 лет")
