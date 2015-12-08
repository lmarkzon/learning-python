## Comments still use a pound sign!

"""
You can make multiline comments with 3 quotation marks!
"""



## Variable Assignment and Printing
my_variable = 10
python = "Welcome to Python!"
print python
# CONSOLE: "Welcome to Python!"



## Integers/Floats/Booleans
my_int = 7
# integer format code: %d
my_float = 1.23
# float format code: %f
my_bool = True
my_bool = False




## Same basic math skills...
addition = 1 + 1
difference = 5 - 3
multiply = 5 * 5
five = 5 * "five " # will give you "five, five, five, five, five"
divide = 10 / 2 # 5
modulo = 5 % 4 # gives you 1



## Comparison operators...
3 < 4
5 > 3
5 >= 5
5 <= 5
10 == 10
12 != 13



## To be And/Or Not to be...
1 < 2 and 2 < 3
# Both must be true to return true

1 < 2 or 2 > 3
# One must be true to return true

true_bool = not 3 ** 2 < 2 ** 3
false_bool = not not False
# 'not False' returns true
# not is evaluated first, and is evaluated next, or is evaluated last.



# Whitespace: IndentationError: expected an indented block
    # Python uses 4 space indentation
def spam():
    eggs = 12
    return eggs
print spam()



## Calculating the total cost of a meal...
meal = 44.50
tax = 0.0675
tip = 0.15

meal += meal * tax
total = meal + meal * tip

print("%.2f" % total)
# CONSOLE: 54.63



## escape backslashs!
'This isn\'t flying, this is falling with style!'



## Access by index
fifth_letter = "MONTY"[4]
print fifth_letter
# CONSOLE: 'Y'



## STRING METHODS:
    # methods that use dot notation can ONLY be used on strings
    # methods that don't (len and str) can be used on other types of objects
parrot = "Norwegian Blue"
print parrot.lower() # lowercase (dot notation)
print parrot.upper() # uppcase (dot notation)

print len(parrot) # length of parrot

pi = 3.14
print str(pi) # turns object into string



## String Conversion
    # String Concatenation
print "Spam " + "and " + "eggs"
    # Explicit string conversion
print "The value of pi is around " + str(3.14)
    # CONSOLE: "The value of pi is around 3.14"



## String Formatting with %
name = "Lauren"
print "Hello %s" % (name)
# CONSOLE: "Hello Lauren"


name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)
# CONSOLE: "Ah, so your name is Lauren, your quest is to learn Python,
# and your favorite color is Blue."
    # raw_input collects user data



## Datetime Library and datetime.now() function
from datetime import datetime # importing a module
now = datetime.now()

print now
# CONSOLE: 2015-12-06 18:30:50.743462

# Printing the datetime with better format...
from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
# CONSOLE: 12/6/2015 18:42:22



## If Else Statements...
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        # 'elif' is short for 'else if'
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()



## PygLatin
pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:] + first + pyg
        # :1 collects indexes 1 through the end
        print new_word
else:
    print 'Invalid Word.'



## Calculating total cost of a meal 2...
def tax(bill):
    bill *= 1.08 # Adds 8% tax to a restaurant bill.
    print "With tax: %f" % bill
    return bill

def tip(bill):
    bill *= 1.15 # Adds 15% tip to a restaurant bill.
    print "With tip: %f" % bill
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
# CONSOLE: With tax: 108.000000  With tip: 124.200000



## Functions have 3 components:
def hello_world(): # HEADER with def keyword, function name, and any parameters.
"""Comment explaining what the function does!""" # OPTIONAL
    print "Hello World!"    # Indented Body(block) of function


def spam():
    """optional!"""
    print "Eggs!"

spam() # Have to call the function name and pass in any required arguments/params if applicable


def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

square(10)


def power(base, exponent):
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)



## Functions can call other functions...
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2 # calls the function above it


def cube(number):
    """Cube's a number"""
    return number ** 3

def by_three(number):
    if number % 3 == 0:
        answer = cube(number) # Calls the function above it
        return answer
    else:
        return False



## Imports of Modules
import math # imports math module for access to math methods...
print math.sqrt(25) # (sqrt) --> square root
# CONSOLE: 5.0


# Just import sgrt so you don't have to keep typing math...
# if that's the only function you need:
from math import sqrt
print sqrt(25)


# if you need other functions in math...
from math import *
print sqrt(25)


## Math Module DISCLAIMER
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!(everything available in the math module)
# CONSOLE: ['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
        # 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp',
        # 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf',
        # 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin',
        # 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

"""Even if your own definitions don't directly conflict with names from imported
modules, if you import * from several modules at once, you won't be able to figure
out which variable or function came from where. For these reasons, it's best to stick
with either import module and type module.name or just import specific variables and
functions from various modules as needed.
"""



## Built in python functions (that don't requre modules...):
maximum = max(1,2,3)
print maximum # max() returns the largest number

minimum = min(1,2,3)
print minimum # min() returns the smallest number

absolute = abs(-42)
print absolute # abs() returns absolute value of a number

# returns type of object
print type(25)
print type(2.5)
print type('hey')
# CONSOLE: <type 'int'> <type 'float'> <type 'str'>


# example of built in functions with an if/else...
def distance_from_zero(arg):
    if type(arg) == int or type(arg) == float:
        return abs(arg)
    else:
        return "Nope"



# Planning a trip costs function...
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    else:
        return 475

def rental_car_cost(days):
    rental = 40 * days
    if days < 7 and days >= 3:
        return rental - 20
    elif days >= 7:
        return rental - 50
    else:
        return rental

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)
