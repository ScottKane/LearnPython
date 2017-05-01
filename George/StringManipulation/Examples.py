#Run the script to see the output!



my_string = "i'm learning python!"

#Print the first character of my_string
print (my_string[0])

#print from the first to the 5th character of my_string
print (my_string[0:5])

#print the last 3 characters of my_string
print (my_string[:3])

#print the first and last letter of my_string
print (my_string[0] + my_string[len(my_string) - 1 ])

#get the length of my_string
print (len(my_string))

#print from the 6th character to the last character of my_string
print (my_string[5:len(my_string)])

#Query whether my_string starts with an i
print (my_string.startswith("i"))

#in my_string, replace all i's with q's
print (my_string.replace('i', 'q'))

# in my_string, replace the word "learning" with the word "owning"
print (my_string.replace('learning', 'owning'))

#delete all n's from my_string
print (my_string.replace('n', ''))

#make all characters in my_string upper case
print (my_string.upper())

#Count the number of times 'm' appears in my_string
print (my_string.count("m"))

#Convert my_string into a list of each character
print (list(my_string))

#Split my_string into a list by whitespace
print (my_string.split(' '))
