## Main Program file to load Modules into - Usually something along the lines of main.py

## Import another module (the one we created name module.py)
from lib import moduleFile

def main():
	## Pull the variable from the module using the function ("return available" from moduleFile.py)
	available = moduleFile.getAvailableCapacity(40, 1, 25)
	print (available)

if __name__ == "__main__":
    main()