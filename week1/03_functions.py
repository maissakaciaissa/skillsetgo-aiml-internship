"""Exercise 3 - Functions, recursion, lambda, *args/**kwargs."""

def greet(name, greeting="Hello"):
    """Return a greeting. `greeting` has a default value."""
    return f"{greeting}, {name}!"

def stats(*numbers):
    """Return (min, max, mean) of any number of arguments."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

def describe(**info):
    """Accept any keyword arguments and format them."""
    return ", ".join(f"{k}={v}" for k, v in info.items())

def factorial(n):
    """Recursive factorial."""
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    """First n Fibonacci numbers (iterative)."""
    seq, a, b = [], 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def word_count(sentence):
    counts = {}
    for w in sentence.lower().split():
        counts[w] = counts.get(w, 0) + 1
    return counts

print(greet("Maissa"), greet("Maissa", "Salut"))
print(stats(4, 8, 15, 16, 23, 42))
print(describe(model="CNN", epochs=10))
print(factorial(6), fibonacci(10))
print(is_palindrome("A man, a plan, a canal: Panama"), word_count("the cat and the hat"))

# lambda, map, filter, sorted with key
nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * x, nums)), list(filter(lambda x: x % 2 == 0, nums)))
students = [("Sara", 17), ("Ali", 12), ("Nour", 15)]
print(sorted(students, key=lambda s: s[1], reverse=True))

# Scope + closure
def make_multiplier(n):
    return lambda x: x * n
double = make_multiplier(2)
print(double(21))
