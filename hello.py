print('Hello World!')

def say_hello():
    print('Hello from a function!')

def sum(a, b):
    return a + b

# function that thakes a list of numbers and returns the sum of the squares of all the numbers
def sum_of_squares(numbers):
    sum = 0
    for number in numbers:
        sum += number ** 2
    return sum

print(sum_of_squares([1, 2, 3, 4, 5]))

def my_sum(a,b):
    return sum(a,b)

print(my_sum(1,2))

def find_root(a,b,c):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    elif d == 0:
        return -b/(2*a)
    else:
        return (-b + d**0.5)/(2*a), (-b - d**0.5)/(2*a)
    
# ask the user for nunmber 
# print a lilst of all the divisors of that number 
# exclude 1 and the number iteself from the list 

def divisors():
    number = int(input('Enter a number: '))
    divisors = []
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    return divisors

print(divisors())