class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def get_balance(self):
        return self.__balance
    
account = BankAccount("Alice", 1000)
account.deposit(500)
print(f"Current balance: {account.get_balance()}")

#questions

#Create a class Student that has a private variable __marks and a method to display marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # Private attribute

    def display_marks(self):
        print(f"{self.name}'s marks: {self.__marks}")
student = Student("Mikasa", 85)
student.display_marks()


#Create a class Employee with a private variable __salary. Create a method to increase salary by a given amount.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def increase_salary(self, amount):
        self.__salary += amount
    def total_salary(self):
        return self.__salary
employee = Employee("Jerry", 50000)
employee.increase_salary(5000)
print(employee.total_salary())


#Create a class Account with private variable __balance. Create methods to deposit and display balance.

class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def display_balance(self):
        print(f"{self.owner}'s balance: {self.__balance}")
account = Account("Kiddo", 2000)
account.deposit(1000)


#Create a class Mobile with private variable __price. Create a method to change price.

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.__price = price  # Private attribute

    def change_price(self, new_price):
        self.__price = new_price
    def display_price(self):
        print(f"{self.brand} mobile price: {self.__price}")
mobile = Mobile("Samsung", 15000)
mobile.change_price(12000)
mobile.display_price()


#Create a class Person with private variable __age. Create a method to show age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def show_age(self):
        print(f"{self.name}'s age: {self.__age}")
person = Person("Eren", 30)
person.show_age()


#Create  a class Car with private variable __speed. Create a method to increase speed.

class Car:
    def __init__(self, model, speed):
        self.model = model
        self.__speed = speed  # Private attribute

    def increase_speed(self, increment):
        self.__speed += increment
    def display_speed(self):
        print(f"{self.model} car speed: {self.__speed} km/h")
car = Car("Toyota", 100)
car.increase_speed(20)
car.display_speed()
