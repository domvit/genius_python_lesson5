"""
**Завдання 2: Створення та імпорт власних модулів**

Створіть власний Python-модуль з ім'ям `utilities.py`. У цьому модулі створіть наступні функції:

1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.

Після створення цього модуля, створіть інший Python-файл (наприклад, `main.py`), який імпортує модуль `utilities.py` і використовує його функції для обробки списку чисел.

В `main.py` створіть список чисел та використовуйте функції з модуля `utilities` для знаходження середнього значення та найбільшого числа у списку. Виведіть результати на екран.
"""

# main.py

# Імпортуємо модуль utilities
from module import utilities

# Створюємо список чисел
numbers = [4, 12, 7, 23, 9, 15, -966, 0]

# Використовуємо функції з модуля utilities
average = utilities.calculate_average(numbers)
maximum = utilities.find_max(numbers)

# Виводимо результати
print(f"Список чисел: {numbers}")
print(f"Середнє арифметичне: {average}")
print(f"Найбільше число: {maximum}")

# Тестуємо порожній список
empty_list = []
print(f"\nТест із порожнім списком:")
print(f"Середнє арифметичне: {utilities.calculate_average(empty_list)}")
print(f"Найбільше число: {utilities.find_max(empty_list)}")