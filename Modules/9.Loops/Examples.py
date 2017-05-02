#1) Basic While Loop
x = 0
while x <= 10:
    print (x)
    x += 1



#2) Basic For Loop
shopping_list = ["eggs", "bacon", "tomatoes", "waffles"]
for item in shopping_list:
    print (item)



#3) Basic For Loop - range
for number in range(10):
    print (number)



#4) Nested For Loop
shopping_list = ["grapes", "apples", "eggs", "ovaltine"]
inventory = ["grapes", "nuts", "apples", "fish", "chicken"]
for item in shopping_list:
    for stock in inventory:
        if item == stock:
            print ("we have {0} in stock!".format(item))



#5) Nested While Loop
x = 0
while x <= 5:
    y = 0
    print ("x is on " + str(x))
    while y <= 3:
        print ("y is on " + str(y))
        y = y + 1
    x = x + 1


#6) Conditionals in loops
for i in range(0, 10):
    if i == 2:
        print ("i is 2")
    elif i == 4:
        print ("i is 4")


# Conditionally breaking a while loops
x = 0
while x <= 10:
    if x == 5:
        print ("exiting at 5")
        break
    print (x)
    x = x + 1
