## Variables in Python

## This is declaring a variable
x = 2
## we have stored in memory that the variable x has the value of 2

## You can also give a variable a text value
y = "Hello World"
## we have stored in memory that the variable x has the value of Hello World

"""
In these examples x is an int variable - this means it is an integer value or whole number
y is a string - is used to represent litteral data
It is comprised of a set of characters that can also contain spaces and numbers.
For example, the word "hamburger" and the phrase "I ate 3 hamburgers" are both strings.
Even "12345" could be considered a string in this sense as it is not being used mathematically and is just being stored in quotes.
Strings must be wrapped in quotation marks e.g "hello" instead of hello
Integers and floats (none whole numbers - floating point) don't need to be wrapped
"""
print (x)
print (y)
"""
Here we are telling Python to write the value of x to the screen. and display y on the next line
"""

## Now lets look at printing integers and strings to the screen at the same time
capacity = 40		## Integer value
driver = 1			## Integer value
passengers = 25		## Integer value
available = capacity - passengers - driver		## Here we are calculating the number of seats left available
												## the variable "available" will be equal to the sum of the
												## total capacity of the bus (40) minus the number of passengers that get on the bus (25)
												## minus the driver (1). (40 - 25 - 1 = 14)

print ("An empty bus arrives at a stop, it has", driver, "driver on the bus and all the seats are empty.")
print ("The bus can hold", capacity, "people including the driver.")
print (passengers, "passengers get on the bus.")
print ("There are now", available, "seats left on the bus on the bus.")