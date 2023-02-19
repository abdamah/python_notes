from dataclasses import dataclass
from math import pi
from abc import ABC, abstractmethod

# Tips:
student_count = 100_000
rate_count = 4.9
course_name = 'Python Programming'

# proj#1: even_odd -> check whether a number is even or odd

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# proj#2: echo command -> print what ever typed in the terminal back to user until typed quit.
# 1. read command from user
# 2. convert command to lower case
# 3. check if command is quit
# 4. echo back what ever user typed.

# finite loop
command = ''
while command.lower() != 'quit':
    command = input(" >: ")
    print('echo ', command)

# or infinate loop
while True:
    command = input(" >: ")
    if command.lower() == 'quit':
        break
    print('echo ', command)


# proj#3: Guess game , use guesses secret number within 3 chances.
secret = 7
for i in range(1, 4):
    print(f'You have {i} guesses left')

    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print('You guessed it right!')
        break

    print('Try again!')
else:
    print('you lose')


# prog#5: factorial-> to find the factorial of a number

def factorial(the_number):
    result = 1

    for n in range(1, the_number + 1):
        result *= n
    return result


print('factorial: ', factorial(5))


# proj#6: fibonacci -> to find the nth fibonacci number using recursion

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)
# 0, 1 , 1, 2, 3, 5, 8, 13, 21,
# 0  1   2  3  4  5  6  7   8


print('fibonacci: ', fibonacci(8))


# proj#8: fizzbuzz -> to find the fizzbuzz from 1 to 100
# 1. multiples of 3 and 5 -> FizzBuzz
# 2. multiples of 3 -> Fizz
# 3. multiples of 5 -> Buzz
# 4. multiples of none: number.

def fizzbuzz(num):

    for n in range(1, num + 1):
        if n % 15 == 0:
            print('fizzbuzz', end=' ')
        elif n % 3 == 0:
            print('fizz', end=' ')
        elif n % 5 == 0:
            print('buzz', end=' ')
        else:
            print(n, end=' ')

    print()


numb = int(input('Enter fizzbuzz number: '))
fizzbuzz(numb)


# proj#9: tip calculator
price = float(input("Enter the price: "))

percentage_tip = int(input("Enter the percentage tip: "))

tip = price * (percentage_tip / 100)

total_price = price + tip

print(f"Total price: {round(total_price, 2)}")


# proj#10: class


@dataclass
class Shape(ABC):

    shape_type: str = 'Any shape'

    @abstractmethod
    def area(self) -> float:
        """
        Function to calculate the area of the shape.
        """

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self,  shape_type: str, length: float, width: float):
        super().__init__(shape_type)
        self.shape_type = shape_type
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.width * self.length

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self,  radius: float):
        super().__init__()
        self.shape_type = 'Circle'
        self.radius = radius

    def area(self) -> float:
        return round(pi * self.radius ** 2, 2)

    def perimeter(self) -> float:
        return round(2 * pi * self.radius, 2)


for shape in (Rectangle('Rectangle', 4, 5), Circle(4)):
    print(f'{shape.shape_type} area is {shape.area()}')
    print(f'{shape.shape_type} area is {shape.perimeter()}')
