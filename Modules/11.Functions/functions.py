## Define your function name
def myFunction():
	## TAB in
	## Make your function do something
	print ("This is a Function!")
#TAB back out to end the function
## Call the function to make it run the print
myFunction()


	


## Define your function and what arguments it takes
def myFunctionWithArgs(name, company):
	## Use the variables/arguments to build a string
	print("My name is", name + ", I work for", company)
## Call the function to make it run the print
myFunctionWithArgs("Scott", "DXC")





## Define your function and what arguments it takes
def sumTwoNumbers(a, b):
	## Return the sum of value a + value b (3 + 7) and store it as sum
	funcSum = a + b
	## When called return the value of sum
	return funcSum
## Call the function with arguments (numbers) and store it in a variable
varSum = sumTwoNumbers(3, 7)
## Print the returned value (10)
print (varSum)





## Define your function and what arguments it takes
def functionWithConditions(company):
	## In this case we are validating that the user works for the correct company
	## so to avoid case sensitivity we are setting the whole string to lower case
	company = company.lower()
	## If the company is dxc
	if company == "dxc":
		print ("Congratulations")
	## If the comapny is not dxc
	else:
		print ("Should you be taking this class?")
## Call the function - change the company below and try for yourself
functionWithConditions("dXc")