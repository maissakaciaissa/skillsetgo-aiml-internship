"""Exercise 2 - Conditionals and loops."""

def grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 50: return "D"
    return "F"

print([grade(s) for s in (95, 83, 71, 55, 20)])

# FizzBuzz
for i in range(1, 16):
    print("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i, end=" ")
print()

# Prime numbers up to n
def primes_up_to(n):
    result = []
    for num in range(2, n + 1):
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                break
        else:                       # runs only if the loop was not broken
            result.append(num)
    return result
print(primes_up_to(30))

# While loop: sum of digits, and Collatz steps
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps
print(digit_sum(12345), collatz_steps(27))

# Nested loops: multiplication table and triangle pattern
for i in range(1, 4):
    print(*[i * j for j in range(1, 6)])
for i in range(1, 5):
    print(" " * (4 - i) + "*" * (2 * i - 1))

# continue / break
for x in range(10):
    if x % 2: continue
    if x > 6: break
    print(x, end=" ")
print()
