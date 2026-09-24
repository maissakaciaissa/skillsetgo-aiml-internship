"""Exercise 4 - Object-Oriented Programming: classes, inheritance, encapsulation, polymorphism."""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance          # "protected" by convention

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def __str__(self):
        return f"{self.owner}: {self._balance:.2f} DA"


class SavingsAccount(BankAccount):        # inheritance
    def __init__(self, owner, balance=0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self._balance * self.rate)


class Shape:                              # polymorphism
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2


class Student:
    school = "USTHB"                      # class attribute

    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades or []

    def add_grade(self, g): self.grades.append(g)
    def average(self): return sum(self.grades) / len(self.grades) if self.grades else 0

    def __repr__(self): return f"Student({self.name!r}, avg={self.average():.1f})"
    def __eq__(self, other): return self.name == other.name


acc = SavingsAccount("Maissa", 1000)
acc.deposit(500); acc.withdraw(200); acc.add_interest()
print(acc)
try:
    acc.withdraw(10_000)
except ValueError as e:
    print("Error:", e)

for shape in (Rectangle(3, 4), Circle(2)):
    print(type(shape).__name__, round(shape.area(), 2))

s = Student("Ali", [12, 15]); s.add_grade(18)
print(s, Student.school, s == Student("Ali"))
