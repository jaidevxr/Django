class car:
    def __init__(self, brand,color):
        self.brand=brand
        self.color=color
    def start(self):
        print(f"{self.color} {self.brand} car is starting")
car1=car("tesla","Red")
car2=car("BMW","Black")
car1.start()
car2.start()
        
        
#Instance variable vs class variable
class Employee:
    company="Google" #class variable
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e1=Employee("Ravi",50000)
e2=Employee("Rahul",60000)
print(e1.company)
print(e2.company)
print(e2.salary)

#Inheritance

class Animal:
    def speak(self):
        print("Animal make sound")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d=Dog()
d.speak()
d.bark()
