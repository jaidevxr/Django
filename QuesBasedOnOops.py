#create a class student with attribute name and roll_no. Create an object of the class and print the values
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
s1=Student("Ravi",101)
print(s1.name)
print(s1.roll_no)

#create a class rectangle with attributes length and breadth. Create a method to calculate and print the area of the rectangle. 
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
r1=Rectangle(5,3)
print(r1.area())

#Create a class Person with a method display() that prints "Hello, Person!". Create an object and call the method.
class Person:
    def display(self):
        print("Hello, Person!")
p1=Person()
p1.display()

#Create a class Car with attributes brand and price. Initialize the attributes using a constructor and create a method to display the car details. Create an object and call the method.
class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"Car Brand: {self.brand}, Price: {self.price}")
car1=Car("Tesla",50000)
car1.display()

#create a class employee with attributes name and salary. Create a method to calculate the annual salary and print it. Create an object and call the method.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return self.salary*12
e1=Employee("Ravi",50000)
print(e1.annual_salary())

#Create a base class Animal with a method sound(). Create a derived class Dog that prints "Dog barks"
class Animal:
    def sound(self):
        print("Animal makes sound")
        
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d1=Dog()
d1.sound()
d1.bark()

 #Create a class Person with attributes name and age. Inherit it in class Student and add roll_no.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
s1=Student("Kiddo",20,22)
print(s1.name)
print(s1.age)
print(s1.roll_no)

#Create a base class Vehicle with attribute type. Create a child class Bike with attribute brand.

class Vehicle:
    def __init__(self,type):
        self.type=type
class Bike(Vehicle):
    def __init__(self,type,brand):
        super().__init__(type)
        self.brand=brand
b1=Bike("Two-wheeler","Honda")
print(b1.type)
print(b1.brand)

#Create a base class Shape with a method draw(). Override it in a derived class Circle.
class Shape:
    def draw(self):
        print("Drawing a shape")
        
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

c1=Circle()
c1.draw()

#Create a base class Employee with attribute salary. Inherit it in class Manager and add bonus.
class Employee:
    def __init__(self,salary):
        self.salary=salary
class Manager(Employee):
    def __init__(self,salary,bonus):
        super().__init__(salary)
        self.bonus=bonus
m1=Manager(50000,10000)
print(m1.salary)
print(m1.bonus)

#Create two classes Cat and Dog with a method sound() and demonstrate polymorphism.
class Cat:
    def sound(self):
        print("Cat meows")
class Dog:
    def sound(self):
        print("Dog barks")
c1=Cat()
d1=Dog()
c1.sound()
d1.sound()

