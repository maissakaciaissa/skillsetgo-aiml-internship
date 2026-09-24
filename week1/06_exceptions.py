"""Exercise 6 - Exception handling: try/except/else/finally, custom exceptions, raise."""

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Both values must be numbers")
        return None
    else:                                  # only if no exception
        return result
    finally:                               # always runs
        print("division attempted")

print(safe_divide(10, 2), safe_divide(1, 0), safe_divide("a", 2))

def parse_age(text):
    try:
        age = int(text)
    except ValueError:
        raise ValueError(f"'{text}' is not a valid integer") from None
    if not 0 <= age <= 120:
        raise ValueError("Age out of range")
    return age

for t in ("25", "abc", "150"):
    try:
        print("Valid age:", parse_age(t))
    except ValueError as e:
        print("Invalid:", e)

# Custom exception
class InsufficientStockError(Exception):
    def __init__(self, item, requested, available):
        super().__init__(f"{item}: requested {requested}, only {available} available")

stock = {"laptop": 3}
def order(item, qty):
    if stock.get(item, 0) < qty:
        raise InsufficientStockError(item, qty, stock.get(item, 0))
    stock[item] -= qty

try:
    order("laptop", 5)
except InsufficientStockError as e:
    print("Order failed:", e)

# File errors
try:
    open("does_not_exist.txt")
except FileNotFoundError as e:
    print("File error:", e.strerror)
