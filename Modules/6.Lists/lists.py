## Declare a List
x = ["a", "b", "c", "d"]
##	  0    1    2    3

## Get the number of items stored in the list
print (len(x))
## Get the 3rd index from the list "x"
print (x[3])






## Declare a List
names = ["John", "Andrew", "Zoe"]

## Print the 2nd index (3rd item in list)
print (names[2])

## Add a new name into the list
## You could do : names = ["John", "Andrew", "Zoe", "Jessica"]
## but it is better practice especially when doing things on the fly to append new items
names.append("Jessica")

## Show the contents of the new list to show that "Jessica" has been added
print (names)






## Declare an empty List
newNames = []

## Show that the list is empty
print (newNames)

## Add some names to the empty list
newNames.append("John")
newNames.append("Andrew")
newNames.append("Zoe")
newNames.append("Jessica")

## Show that the list is no longer empty
print (newNames)

## Add a further name to the list
newNames.append("Jack")

## Show that the new name has been added as well as the 4 previous ones
print (newNames)






## Declare a multi dimensional list
couples = [["John", "Zoe"], ["Andrew", "Jessica"]]
##			[0][0]  [0][1]    [1][0]     [1][1]

## Print the first value in the first internal list
print (couples[0][0])

## Print the first value int the second internal list
print (couples[1][0])