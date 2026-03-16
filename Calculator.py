def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b    
PI = 3.14159
EULER = 2.71828
def square(a):
    return a * a
def cube(a):
    return a * a * a

#Temperature conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

#Area calculation functions
def area_of_circle(radius):
    return PI * (radius ** 2)
def area_of_rectangle(length, width):
    return length * width
def area_of_triangle(base, height):
    return 0.5 * base * height

def unique_values(lst):
    return list(set(lst))

