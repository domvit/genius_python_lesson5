# calculator.py

def add(a, b):
    """Повертає суму двох чисел"""
    return a + b

def subtract(a, b):
    """Повертає різницю двох чисел"""
    return a - b

def multiply(a, b):
    """Повертає добуток двох чисел"""
    return a * b

def divide(a, b):
    """Повертає результат ділення a на b з перевіркою ділення на нуль"""
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b