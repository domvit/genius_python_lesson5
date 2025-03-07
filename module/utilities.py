# utilities.py

def calculate_average(numbers):
    """Обчислює середнє арифметичне списку чисел"""
    if not numbers:  # Перевірка на порожній список
        return "Помилка: список порожній!"
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """Знаходить найбільше число у списку"""
    if not numbers:  # Перевірка на порожній список
        return "Помилка: список порожній!"
    return max(numbers)