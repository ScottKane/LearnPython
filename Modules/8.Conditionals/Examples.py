# Basic if/else:
on = True

if on == True:
    print ("The machine is on!")
else:
    print ("The machine is off!")



#Adding elif
temperature = 5

if temperature > 5:
    print ("Too hot!")
elif temperature < 5:
    print ("Too cold!")
else:
    print ("Just right!")



#Conditional variable assignment
miles_ran = 100

if miles_ran >= 10:
    tired = True
else:
    tired = False


if tired == True:
    print ("I am tired!")
else:
    print ("I'm not tired!")



#If number is even
number = 20

if number % 2 == 0:
    print ("Number is even!")
else:
    print ("Number is odd!")




#Nested conditional:
colour = "Red"
suit = "Clubs"

if colour == "Red":
    if suit == "Clubs" or suit == "Spades":
        print ("Winner")
    else:
        print ("Loser")
else:
    print ("Loser")



#Another Nested Conditional (if a number is less than 50 check if it is even. If it is, check if it is evenly divisble by 3):
number = 6

if number < 50:
    print ("The number is less than 50...")
    if number % 2 == 0:
        if number % 3 == 0:
            print ("Number is less than 50, divisble by both 2 and 3")
        else:
            print ("Number is less than 50 and is divisible by 2, but not by 3")
    else:
        print ("Number is not divisble by 2, so we don't care")
else:
    print ("The number is greater than 50, so we don't care!")
