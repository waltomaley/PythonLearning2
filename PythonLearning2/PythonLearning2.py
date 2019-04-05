
# this prints out the Zen of Python poem by Tim Peters
#import this 

import statistics as s
import math as m
import pizza 
from car import *
import json

from name_function import get_formatted_name

print(" Enter 'q' at any time to quit.") 
while True: 
    first = input("\ nPlease give me a first name: ")
    if first == 'q':
        break 
    last = input(" Please give me a last name: ")
    if last == 'q':
        break 
    formatted_name = get_formatted_name(first, last)
    print("\ tNeatly formatted name: " + formatted_name + '.')




# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    return ' ' * int(20 * m.cos(m.radians(x)) + 20) + 'o'

message ='hello in \tpython\n'
message2 ='hello in python'
num = 2 +5
print ("hello visual studio")
print (message.title() + message2 + " " + str(num) )

for i in range(10):
    print(m.cos(m.radians(i)))

for i in range (0,360,12):
     x1 = make_dot_string (i)
     print (x1)

bicycles = [' trek', 'cannondale', 'redline', 'specialized']

print (bicycles[0])
print (bicycles[0:2])
for bicycle in bicycles:
	print ("this is " + bicycle.title())


squares = [value** 2 for value in range( 1,11)] 
print( squares)

bicycles[0] = 'walt'
print(len(bicycles))
print('length of list is  ' +str(len(bicycles)))
print (bicycles[-1]) 
for x in bicycles:
	print(x)
squares = [] 
for value in range( 1,111): 
	square = value** 2 
	squares.append( square) 
print( squares)
print ( "max is " + str(max(squares)))
print ( "min is " + str(min(squares)))
print ( "mean is " + str(s.mean(squares)))

players = [' charles', 'martina', 'michael', 'florence', 'eli'] 
print(" Here are the first three players on my team:") 
for player in players[: 3]: 
	print( player.title())

# () instead of square bracket make it an immutable tuple

dimensions = (200, 50)
print( dimensions[ 0])
print( dimensions[ 1])

cars = [' audi', 'bmw', 'subaru', 'toyota'] 
for car in cars: 
	if car == 'bmw': 
		print( car.upper())
	else : 
		print(car.title())
age = 22 
if age < 4: 
	price = 0 
elif age < 18: 
	price = 5 
elif age < 65: 
	price = 10 
else: price = 5 
print(" Your admission cost is $" + str( price) + ".")

available_toppings = [' mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] 
requested_toppings = [' mushrooms', 'french fries', 'extra cheese'] 
for requested_topping in requested_toppings: 
	if requested_topping in available_toppings: 
		print(" Adding " + requested_topping + ".") 
	else: print(" Sorry, we don't have " + requested_topping + ".") 
print("\nFinished making your pizza!")


favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python' }

print ("Sarah's fav lang is " + favorite_languages['sarah'])

for key, value in favorite_languages. items(): 
	print("\nKey: " + key) 
	print(" Value: " + value)
	
	
friends = [' phil', 'sarah'] 
for name in favorite_languages.keys(): 
	print( name.title()) 
	if name in friends: print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[ name]. title() + "!")
	

favorite_languages2 = { 'jen': [' python', 'ruby'], 'sarah': [' c'], 'edward': [' ruby', 'go'], 'phil': [' python', 'haskell'], } 
for name, languages in favorite_languages2.items(): 
	print("\n" + name.title() + "'s favorite languages are:") 
	
	for language in languages: 
		print("\t" + language.title())

users = { 'aeinstein': { 'first': 'albert', 'last': 'einstein', 'location': 'princeton', }, 'mcurie': { 'first': 'marie', 'last': 'curie', 'location': 'paris', }, } 
for username, user_info in users.items(): 
	print("\nUsername: " + username) 
	full_name = user_info['first'] + " " + user_info['last'] 
	location = user_info['location'] 
	print("\tFull name: " + full_name.title()) 
	print("\tLocation: " + location.title())

# Input 


height = input(" How tall are you, in inches? ") 
height = int( height) 
if height >= 36: 
	print("\ nYou're tall enough to ride!") 
else:
	print("\ nYou are NOT tall enough to ride!") 
"""

number = input(" Enter a number, and I'll tell you if it's even or odd: ") 
number = int( number) 
if number % 2 == 0: 
	print("\nThe number " + str( number) + " is even.") 
else: 
	print("\nThe number " + str( number) + " is odd.")
	
prompt = "\ nTell me something, and I will repeat it back to you:" 
prompt += "\ nEnter 'quit' to end the program. "
active = True
while active: 
    message = input( prompt)
    if message == 'quit': 
        active = False
    else: 
        print( message)

"""
# Start with users that need to be verified, 
# and an empty list to hold confirmed users. 
unconfirmed_users = [' alice', 'brian', 'candace'] 
confirmed_users = [] # Verify each user until there are no more unconfirmed users. 
# Move each verified user into the list of confirmed users. 
while unconfirmed_users:
	current_user = unconfirmed_users.pop() 
	print(" Verifying user: " + current_user.title()) 
	confirmed_users.append( current_user) 

# Display all confirmed users. 
print("\nThe following users have been confirmed ")

for confirmed_user in confirmed_users: 
	print( confirmed_user.title())

def describe_pet( animal_type, pet_name): 
	# Display information about a pet. 
	print("\nI have a " + animal_type + ".") 
	print(" My " + animal_type + "'s name is " + pet_name.title() + ".") 
	
describe_pet(' hamster', 'harry') 
describe_pet(' dog', 'willie')

def greet_users( names): 
	# Print a simple greeting to each user in the list.
	for name in names: 
		msg = "Hello, " + name.title() + "!" 
		print( msg) 
		
usernames = [' hannah', 'ty', 'margot'] 
greet_users( usernames)


def make_pizza(* toppings): 
	#Summarize the pizza we are about to make. 
	print("\nMaking a pizza with the following toppings:") 
	for topping in toppings: 
		print("- " + topping) 
		
make_pizza(' pepperoni') 
make_pizza(' mushrooms', 'green peppers', 'extra cheese')



pizza.make_pizza( 16, 'pepperoni') 
pizza.make_pizza( 12, 'mushrooms', 'green peppers', 'extra super duper cheese')

banned_users = [' andrew', 'carolina', 'david'] 
user = 'marie' 
if user not in banned_users: 
    print( user.title() + ", you can post a response if you wish.")

requested_toppings = [' mushrooms', 'extra cheese'] 
if 'mushrooms' in requested_toppings: 
    print(" Adding mushrooms.") 
elif 'pepperoni' in requested_toppings: 
    print(" Adding pepperoni.") 
elif 'extra cheese' in requested_toppings: 
    print(" Adding extra cheese.") 
print("\nFinished making your pizza!")

available_toppings = [' mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] 
requested_toppings = [' mushrooms', 'french fries', 'extra cheese'] 
for requested_topping in requested_toppings:
    if requested_topping in available_toppings: 
        print(" Adding " + requested_topping + ".") 
    else: 
        print(" Sorry, we don't have " + requested_topping + ".") 
    print("\ nFinished making your pizza!")
 
favorite_languages = { 
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python', 
    } 
print(" Sarah's favorite language is " + favorite_languages['sarah'].title() +   ".")

for key, value in favorite_languages.items():
     print("\ nKey: " + key)
     print(" Value: " + value)

friends = ['phil', 'sarah'] 
for name in favorite_languages.keys():
    print( name.title())
    if name in friends: 
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[ name]. title() + "!")

favorite_languages2 = { 
    'jen': [' python', 'ruby'], 
    'sarah': [' c'], 
    'edward': [' ruby', 'go'], 
    'phil': [' python', 'haskell'],
   } 
for name, languages in favorite_languages2.items(): 
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages: 
        print("\t" + language.title())
 
def build_person( first_name, last_name): 
    """ Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person(' jimi', 'hendrix')
print( musician)
for key, value in musician.items(): 
	print("\nKey: " + key) 
	print(" Value: " + value)
print("First Name is " + musician['first'])
print("Last Name is " + musician['last'])

def greet_users(names):
     """ Print a simple greeting to each user in the list.""" 
     for name in names:
        msg = "Hello, " + name.title() + "!" 
        print( msg) 

usernames = [' hannah', 'ty', 'margot'] 
greet_users(usernames)

my_new_car = Car(' audi', 'a4', 2016) 
print( my_new_car.get_descriptive_name())

""" here create ElectricCar class which is child of Car.  Part of ElectricCar is attribute """
"""    battery which a Battery object and describe_battery is method in the Battery object """
my_tesla = ElectricCar('tesla', 'model s', 2016)
print( my_tesla.get_descriptive_name()) 
my_tesla.battery.describe_battery()

""" note it likes forward slash for windows path.  go figure """

filepath = 'C:/Users/walt.omaley/source/repos/PythonLearning2/PythonLearning2/textstuff.txt'

# if open for write with w then overwrites file while a appends it
 
with open(filepath, 'a') as file_object:
    file_object.write(" I love programming. \n")

with open(filepath) as file_object:
    contents = file_object.read()
    print(contents)

print(" Give me two numbers, and I'll divide them.")
print(" Enter 'q' to quit.")
while True: 
    first_number = input("\ nFirst number: ")
    if first_number == 'q': 
        break 
    second_number = input(" Second number: ")
    if second_number == 'q': 
        break 
    try: 
        answer = int( first_number) / int( second_number)
    except ZeroDivisionError:
        print(" You can't divide by 0!")
    else: 
        print(answer)
 # here is how to deal with file exceptions
filename = 'alice.txt' 
try: 
    with open(filename) as f_obj: 
        contents = f_obj.read() 
except FileNotFoundError: 
    msg = "Sorry, the file " + filename + " does not exist." 
    print(msg)

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
 
with open(filename) as f_obj: 
    numbers = json.load(f_obj)
    print(numbers)
# Load the username, if it has been stored previously. 
# Otherwise, prompt for the username and store it. 
filename = 'username.json' 
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input(" What is your name? ")
    with open( filename, 'w') as f_obj:
        json.dump(username, f_obj) 
        print(" We'll remember you when you come back, " + username + "!")
else: 
    print(" Welcome back, " + username + "!")

  
"""

multiline comment
good for debug or doc

"""




