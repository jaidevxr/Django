import datetime
import math
import random
# Todays date
today = datetime.date.today()
print("Today's date:", today)

#Format date
formatted_date = today.strftime("%B %d, %Y")
print("Formatted date:", formatted_date)

#Calculate future date
future_date = today + datetime.timedelta(days=30)
print("Date after 30 days:", future_date)

#Calculate past date
past_date = today - datetime.timedelta(days=30)
print("Date 30 days ago:", past_date)

#Find the square root of a number
print("Square root of 16:", math.sqrt(625))

#Calculate the factorial of 6
print("Factorial of 6:", math.factorial(6))

#Calculate the floor and ceiling of 4.5
print("Floor of 4.5:", math.floor(4.5))
print("Ceiling of 4.5:", math.ceil(4.5))

#compute 5 raised to the power of 3
print("5 raised to the power of 3:", math.pow(5, 3))

#find the absolute value of -18
print("Absolute value of -18:", math.fabs(-18))

#Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)

#Generate a random float between 0 and 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)

#Generate a random choice from a list
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices)
print("Random choice from the list:", random_choice)

#Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)

#Generate a random even number between 2 and 20
print("Random even number between 2 and 20:", random.randrange(2,21,2))

#Genrate a 5 random integers between 10 and 100
random_integers = random.sample(range(10, 101), 5)
print("5 random integers between 10 and 100:", random_integers)

#write a program to display current year and month and day separately
current_year = today.year
current_month = today.month
current_day = today.day
print("Current Year:", current_year)
print("Current Month:", current_month)
print("Current Day:", current_day)

#write a program to display current date and time in the format "Day, Month Date, Year Hour:Minute:Second AM/PM"
formatted_date = today.strftime("%A, %B %d, %Y %I:%M:%S %p")
print("Formatted date:", formatted_date)

