### 1. Переменные, типы данных, ввод/вывод
# 1
# name=input("Enter your name: ")
# print(f"Hello {name}")

# 2
# age=int(input("Enter your age: "))
# print(f'After 10 years, you will be {age+10} years old')

# 3
# a=int(input('Enter a number: '))
# b=int(input('Enter another number: '))
# print(f'The sum of those two numbers is {a+b}')

# 4
# num1=int(input("enter first number: "))
# num2=int(input("enter second number: "))
# print(f'The sum of those two numbers: {num1+num2}')
# print(f'The product of those two numbers: {num1*num2}')
# print(f'The difference of those two numbers: {num1-num2}')
# print(f'The quotient of those two numbers: {num1/num2}')

# 5
# side1=int(input("enter the width: "))
# side2=int(input("enter the length: "))
# print(f'The area of the rectangular: {side1*side2}')

# 6
# import math
# radius=int(input("enter the radius of the circle: "))
# print(f'The are of a circle: {round(math.pi*radius**2)}')

# 7
# celsius = float(input("Enter the temperature in Celsius: "))
# fahrenheit = celsius * 9 / 5 + 32
# print("Fahrenheit:", fahrenheit)

# 8
# second = int(input('Enter the time in seconds: '))
# hours = second // 3600
# minutes = (second % 3600) // 60
# seconds = second % 60
# print(f'{hours}h {minutes}m {seconds}s')

# 9
# first = int(input("enter the first number: "))
# second = int(input("enter the second number: "))
# temp = first
# first = second
# second = temp
# print(f'First number is {first}, second number is {second}')

# 10
# value=input('Enter soemthing: ')
# toString=str(value)
# toInteger=int(toString)
# toFloat=float(toString)
# print(type(value))

### 2. Условия if / elif / else
# 11
# number=int(input("enter the number: "))
# if number<0:
#     print("the number is negative")
# elif number==0:
#     print("the number is zero")
# else:
#     print("the number is positive")

# 12
# number1=int(input("enter the number: "))
# if number1%2==0:
#     print(f'The number is even')
# else:
#     print(f'The number is odd')

# 13
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# if a>b:
#     print(f'{a} is the greatest number')
# else:
#     print(f'{b} is the greatest number')

# 14
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# c=int(input('Enter third number: '))
# if a>b and a>c:
#     print(f'{a} is the biggest number')
# elif b>a and b>c:
#     print(f'{b} is the biggest number')
# else:
#     print(f'{c} is the biggest number')

# 15
# number=int(input("enter the number: "))
# if number%3==0 and number%5==0:
#     print("number is divisible by 3 and 5")
# else:
#     print("number is not divisible by 3 and 5")

# 16
# year=int(input("enter the year: "))
# if year%4==0 and year%100!=0 or year%400==0:
#     print('The year is leap year')
# else:
#     print('The year is not leap year')

# 17
# age1=int(input("Enter your age: "))
# if age1<=7:
#     print('Little child')
# elif age1>7 and age1<=18:
#     print('Teenager')
# elif age1>18 and age1<=65:
#     print('Adult')
# else:
#     print('Elderly')

# 18
# login=input('Enter your username: ')
# password=input('Enter your password: ')
# if login=='admin' and password=='12345':
#     print('Login Successful')
# else:
#     print('Login Failed')

# 19
# month=int(input("Enter the number of the month: "))
# if month<=2 and month<=12:
#     print('Winter')
# elif month>=3 and month<=5:
#     print('Spring')
# elif month>=6 and month<=8:
#     print('Summer')
# elif month>=9 and month<=11:
#     print('Autumn')
# else:
#     print('Invalid number')

# 20
# side1=int(input("enter side 1: "))
# side2=int(input("enter side 2: "))
# side3=int(input("enter side 3: "))
# if side1+side2>side3:
#     print('Triangle')
# elif side1+side3>side2:
#     print('Triangle')
# elif side2+side3>side1:
#     print('Triangle')
# else:
#     print('Unsuccessful')

### 3. Цикл for
# 21
# for i in range(1,101):
#     print(i)

# 22
# for i in range(1,101):
#     if i%2 ==0:
#         print(i)

# 23
# for i in range(100,0, -1):
#     print(i)

# 24
# n=int(input('Enter any number: '))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# 25
# num=int(input("enter any number: "))
# multiply=1
# for i in range(1,num+1):
#     multiply*=i
# print(multiply)

# 26
# number=int(input("enter any number: "))
# for i in range(1,11):
#     print(f"{i} x {number} = {i*number}")

# 27
# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i*j}')

# 28
# for i in range(1,1001):
#     if i%3==0:
#         print(i)

# 29
# number2=int(input("Enter any number: "))
# sum1=0
# for i in range(1,number2+1):
#     if i%2!=0:
#         sum1+=i
# print(sum1)

# 30
# for i in range(1,21):
#     print(i**2)

### 4. Цикл while
# 31
# i=1
# while i<=100:
#     print(i)
#     i=i+1

# 32
# password=''
# while password!='12345':
#     password=input("enter your password: ")

# 33
# zero=''
# while zero!='0':
#     zero=input('Enter a number: ')
#     print('You find the logic')

# 34
# zero1=''
# count=0
# while zero1!='0':
#     zero1=input('enter number: ')
#     if int(zero1)!=0:
#         count+=int(zero1)
#     else:
#         continue
# print(count)

# 35
# number=input('Enter any number: ')
# print(f'The number consists of {len(number)} digits')

# 36
# number=input('Enter any number: ')
# counter=0
# for digit in number:
#     counter=counter+int(digit)
# print(f'The sum of digits of number: {counter}')

# 37
# number1 = input("Enter a number: ")
# print(f'Reversed version: {number1[::-1]}')

# 38
# number2=input('Enter any number: ')
# if number2==number2[::-1]:
#     print('The number is palindrome')
# else:
#     print('The number is not palindrome')

# 39
# import random
# secret_number = random.randint(1, 100)
# while secret_number != 88:
#     secret_number=int(input("Enter a number between 1 and 100 to guees the number: "))
#     print('Congratulations! You guessed the number!')

# 40
# number = 0
# while number <= 0:
#     number = int(input('Enter a positive number: '))
# print('Thank you! You entered a positive number.')

### 5. Строки
# 41
# word=input('Enter any word: ')
# print(len(word))

# 42
# word1=input('Enter any word: ')
# print(word1.count('a'))

# 43
# word2=input('Enter any word: ')
# splitted=word2[::-1]
# print(splitted)

# 44
# word3=input('Enter any word: ')
# splitted=word3[::-1]
# if splitted==word3:
#     print('The word is palindrome')
# else:
#     print('The word is not palindrome')

# 45
# vowels = ['a', 'e', 'i', 'o', 'u']
# word4=input("Enter a word: ")
# for vowel in vowels:
#     print(f'{vowel}: {word4.count(vowel)}')

# 46
# text = input('Enter any text: ')
# count = 0
# for letter in text:
#     if letter.isalpha() and letter.lower() not in 'aeiou':
#         count += 1
#
# print(f'The number of consonants: {count}')

# 47
# sentence=input('Enter any sentence: ')
# splitted=sentence.split(' ')
# print(f'The sentence has {len(splitted)} words')

# 48
# sentence1=input('Enter short text: ')
# splitted1=sentence1.split(' ')
# print(max(splitted1,key=len))

# 49
# sentence=input('Enter any sentence: ')
# print(sentence.replace(' ','-'))

# 50
# sentence3=input('Enter any sentence: ')
# word=input('Enter the word that you think that sentence started with: ')
# splitted = sentence3.split(' ')
# if splitted[0].lower()==word:
#     print('Right')
# else:
#     print('Wrong')

### 6. Списки
# 51
# numbers=[1,2,3,4,5]
# print(f'The sum of all numbers: {sum(numbers)}')

# 52
# nums=[1,2,3,4,5,6,7,8,9,10]
# nums.sort(reverse=True)
# print(nums[0])

# 53
# nums2=[2,4,1,6,5,8,3]
# nums2.sort()
# print(nums2[0])

# 54
# numbers2=[1,2,3,4,5,6,7,8,9,10]
# evens=[]
# for number in numbers2:
#     if number%2==0:
#         evens.append(number)
#     else:
#         continue
# print(f'The number of even numbers: {len(evens)}')

# 55
# numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
# odds=[]
# for number in numbers:
#     if number % 2 != 0:
#         odds.append(number)
#     else:
#         continue
# print(odds)

# 56
# numbers = [1, 2, -3, -4, 5, 3, -6, -7]
# positive_numbers = []
# for number in numbers:
#     if number >= 0:
#         positive_numbers.append(number)
# print(positive_numbers)

# 57
# numss=[1,2,3,4,5]
# print(numss[::-1])

# 58
# numberss=[1,2,3,4,5,6,7]
# numberss.sort(reverse=True)
# print(numberss[1])

# 59
# numsss = [1, 1, 2, 3, 4, 5, 3, 6, 7]
# unique_nums = []
# for num in numsss:
#     if num not in unique_nums:
#         unique_nums.append(num)
# print(unique_nums)

# 60
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common = []
#
# for num in list1:
#     if num in list2 and num not in common:
#         common.append(num)
#
# print(common)

### 7. tuple, set, dict
# 61
# numbers=(2,11,6,3,8,25,33,76,14)
# print(max(numbers))

# 62
# repeated=[1,1,2,3,4,5,5,6,7,8,1,2]
# print(set(repeated))

# 63
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A & B)

# 64
# A = set(map(int, input('Enter the first set: ').split()))
# B = set(map(int, input('Enter the second set: ').split()))
#
# print(A - B)

# 65
# name=input("Enter your name: ")
# age=input("Enter your age: ")
# city=input("Enter your city: ")
# info={
#     "name":name,
#     "age":age,
#     "city":city
# }
# print(info)

# 66
# car={
#     'brand':'BMW',
#     'model':'M',
# }
# car['year']='2006'
# print(car)

# 67
# information={
#     'name':'Ali',
#     'age':18,
#     'city':'Nukus'
# }
# information.pop('city')
# print(information)

# 68
# word=input('Enter any word: ')
# justDict={}
# for letter in word:
#     counted=word.count(letter)
#     justDict[letter]=counted
# print(justDict)

# 69
# sentence=input('Enter any sentence: ')
# splitted=sentence.split(' ')
# wordCounter={}
# for word in splitted:
#     counted=splitted.count(word)
#     wordCounter[word]=counted
# print(wordCounter)

# 70
# just={
#     "a":1,
#     "b":2,
#     "c":3,
#     "d":4,
#     "e":5,
#     "f":6,
#     "g":7
# }
# nums=[]
# for key,value in just.items():
#     nums.append(value)
# maxNum=max(nums)
# for key,value in just.items():
#     if value==maxNum:
#         print(key)
#     else:
#         continue

### 8. Функции
# 71
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# def Addition(a,b):
#     sum=a+b
#     return sum
# print(Addition(a,b))

# 72
# number=int(input("Enter any number: "))
# def isEven(number):
#     if number % 2 == 0:
#         return 'This number is even'
#     else:
#         return 'This number is odd'
# print(isEven(number))

# 73
# num1=int(input("enter first number: "))
# num2=int(input("enter second number: "))
# num3=int(input("enter third number: "))
# def maxOne(num1,num2,num3):
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num1 and num2>num3:
#         return num2
#     else:
#         return num3
# print(maxOne(num1,num2,num3))

# 74
# number=int(input('Enter the number: '))
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(number))

# 75
# oddDigits=[2,3,5,7]
# number1=int(input("Enter any number: "))
# def isPrime(n):
#     for i in oddDigits:
#         if n%i==0:
#             return 'This number is not prime'
#         else:
#             return 'This number is prime'
#
# print(isPrime(number1))

# 76
# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input('Enter any word: ')
# def count_vowels(word):
#     for i in vowels:
#         if i in word:
#             print(f'{i}: {word.count(i)}')
# count_vowels(word)

# 77
# word2=input('Enter any word: ')
# def Reversed(word):
#     return word[::-1]
# print(Reversed(word2))

# 78
# numberList=[1,2,3,4,5,6,7]
# def Average(n):
#     avrg=sum(numberList)/len(numberList)
#     print(avrg)
# Average(numberList)

# 79
# def Sum(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum
# print(Sum(1,2,3,4,5,6,7,8,9))

# 80
# def info(**kwargs):
#     print(kwargs)
# info(name='John', age=22, city='Washington, DC', siblings='2 siblings')

# # 81
# squares = [x ** 2 for x in range(1, 21)]
# print(squares)
#
# # 82
# evens = [x for x in range(1, 101) if x % 2 == 0]
# print(evens)
#
# # 83
# words = ["apple", "banana", "cat", "elephant"]
# lengths = [len(word) for word in words]
# print(lengths)
#
# # 84
# words = ["banana", "cat", "elephant", "apple"]
# words.sort(key=lambda word: len(word))
# print(words)
#
# # 85
# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x * 2, numbers))
# print(result)
#
# # 86
# numbers = [-5, 3, -2, 8, 0, 7]
# positive = list(filter(lambda x: x > 0, numbers))
# print(positive)
#
# # 87
# words = ["apple", "elephant", "cat", "banana"]
# result = list(filter(lambda word: len(word) > 5, words))
# print(result)
#
# # 88
# numbers = ["1", "2", "3", "4", "5"]
# result = list(map(int, numbers))
# print(result)
#
# # 89
# users = [
#     {"name": "Ali", "age": 20},
#     {"name": "Vali", "age": 16},
#     {"name": "Sara", "age": 25}
# ]
# users.sort(key=lambda user: user["age"])
# print(users)
#
# # 90
# users = [
#     {"name": "Ali", "age": 20},
#     {"name": "Vali", "age": 16},
#     {"name": "Sara", "age": 25}
# ]
# names = [user["name"] for user in users if user["age"] > 18]
# print(names)
#
# # 91
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
# user1 = User("Ali", 20)
# user1.show_info()
#
# # 92
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def show_info(self):
#         print(f"{self.brand} {self.model}, {self.year}")
#
# car1 = Car("Toyota", "Camry", 2024)
# car1.show_info()
#
# # 93
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient balance or invalid amount.")
#
#     def show_balance(self):
#         print(f"Balance: {self.balance}")
#
# account = BankAccount(100)
# account.deposit(50)
# account.withdraw(30)
# account.show_balance()
#
# # 94
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def show_info(self):
#         print(
#             f"Product: {self.name}, "
#             f"Price: {self.price}, Quantity: {self.quantity}"
#         )
#
# product = Product("Laptop", 800, 5)
# product.show_info()
#
# # 95
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def show_info(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")
#
#
# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language = programming_language
#
#     def show_info(self):
#         super().show_info()
#         print(f"Programming language: {self.programming_language}")
#
#
# developer = Developer("Ali", 5000, "Python")
# developer.show_info()
#
# # 96
# users = ["Ali", "Vali", "Sara"]
#
# with open("users.txt", "w", encoding="utf-8") as file:
#     for user in users:
#         file.write(user + "\n")
#
# # 97
# with open("users.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#
# print("Number of users:", len(lines))
#
# # 98
# try:
#     a = float(input("Enter the first number: "))
#     b = float(input("Enter the second number: "))
#     print("Result:", a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Please enter valid numbers.")
#
# # 99
# products = []
#
# while True:
#     print("\n1. Add product")
#     print("2. Delete product")
#     print("3. Show products")
#     print("4. Exit")
#
#     choice = input("Choose an option: ")
#
#     if choice == "1":
#         product = input("Enter product name: ")
#         products.append(product)
#         print("Product added.")
#
#     elif choice == "2":
#         product = input("Enter product name to delete: ")
#         if product in products:
#             products.remove(product)
#             print("Product deleted.")
#         else:
#             print("Product not found.")
#
#     elif choice == "3":
#         if products:
#             for product in products:
#                 print(product)
#         else:
#             print("No products.")
#
#     elif choice == "4":
#         break
#
#     else:
#         print("Invalid option.")
#
# # 100
# import json
# import os
#
# FILE_NAME = "tasks.json"
#
#
# def load_tasks():
#     if os.path.exists(FILE_NAME):
#         try:
#             with open(FILE_NAME, "r", encoding="utf-8") as file:
#                 return json.load(file)
#         except json.JSONDecodeError:
#             return []
#     return []
#
#
# def save_tasks(tasks):
#     with open(FILE_NAME, "w", encoding="utf-8") as file:
#         json.dump(tasks, file, indent=4)
#
#
# tasks = load_tasks()
#
# while True:
#     print("\n1. Add task")
#     print("2. Show tasks")
#     print("3. Delete task")
#     print("4. Complete task")
#     print("5. Exit")
#
#     choice = input("Choose an option: ")
#
#     if choice == "1":
#         title = input("Enter task: ")
#         tasks.append({"title": title, "completed": False})
#         save_tasks(tasks)
#         print("Task added.")
#
#     elif choice == "2":
#         if not tasks:
#             print("No tasks.")
#         else:
#             for index, task in enumerate(tasks, start=1):
#                 status = "Completed" if task["completed"] else "Not completed"
#                 print(f"{index}. {task['title']} — {status}")
#
#     elif choice == "3":
#         try:
#             index = int(input("Enter task number to delete: ")) - 1
#             if 0 <= index < len(tasks):
#                 tasks.pop(index)
#                 save_tasks(tasks)
#                 print("Task deleted.")
#             else:
#                 print("Invalid task number.")
#         except ValueError:
#             print("Enter a valid number.")
#
#     elif choice == "4":
#         try:
#             index = int(input("Enter task number to complete: ")) - 1
#             if 0 <= index < len(tasks):
#                 tasks[index]["completed"] = True
#                 save_tasks(tasks)
#                 print("Task completed.")
#             else:
#                 print("Invalid task number.")
#         except ValueError:
#             print("Enter a valid number.")
#
#     elif choice == "5":
#         break
#
#     else:
#         print("Invalid option.")

