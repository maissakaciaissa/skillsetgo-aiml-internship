"""Exercise 1 - Variables, data types, strings and collections."""

# --- Variables & basic types ---
name = "Maissa"          # str
age = 22                # int
gpa = 15.5               # float
is_student = True        # bool
print(f"{name=}, {age=}, {gpa=}, {is_student=}")
for v in (name, age, gpa, is_student):
    print(type(v).__name__, end=" ")
print()

# --- Type casting ---
print(int("42") + 8, float("3.14") * 2, str(100) + "%", bool(0), bool("text"))

# --- Strings ---
s = "  Machine Learning with Python  "
print(s.strip().upper(), "|", s.strip().split(), "|", s.count("i"), "|", s.strip()[::-1])

# --- Collections ---
nums = [5, 3, 8, 1, 9, 3]                    # list: ordered, mutable
nums.append(7); nums.sort()
point = (10, 20)                             # tuple: ordered, immutable
unique = set(nums)                           # set: unique values only
student = {"name": "Maissa", "field": "AI", "year": 2}   # dict: key -> value
student["year"] += 1
print(nums, point, unique, student)

# --- Comprehensions ---
squares = [x ** 2 for x in range(1, 6)]
evens = [x for x in nums if x % 2 == 0]
sq_map = {x: x ** 2 for x in range(1, 4)}
print(squares, evens, sq_map)

# --- Mini task: swap, min/max, average ---
a, b = 3, 7
a, b = b, a
print("swap:", a, b, "| min/max:", min(nums), max(nums), "| avg:", round(sum(nums) / len(nums), 2))
