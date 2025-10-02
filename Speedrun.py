# Python As Fast As Possible

# Data Types ##
# Int
4. -3
# Float
50.5 , 51.0, 1.0
#String
'Hello World', "Yogurt"
# Boolean
True ,1, False ,0

# Output and Printing ##
print('Hello World!') # Can use single or double quotations (' or ")
print(4.5)
print (3.3,"Hello")

# Variables ##
hello_tim = 'tim'
print(hello_tim)

# User Input ##

#input('Name: ')
#job = input('Job: ')

# Arithmetic Operator ##
x = 9
y = 3
result = x + y
print(result)
result_2 = x/y #Using the division operator will always return a float
int(result_2) #This will convert the result back to int
print (result_2)
result_2_int = x // y #This will also give us an int value
print (result_2_int)
result_3 = x % y # This operation takes the mod
print(result_3)

# String Methods ##
hello = 'hello' 
print(hello.upper())#uppercases the string
print(hello.lower()) #lowercases the string
print(hello.capitalize()) #Capitalizes first letter
print(hello.count('l')) #Returns the count of substrings in main string
print(type(hello)) #returns the data type of the variable
print(hello * 9) # Prints the string 9 times

# Conditional Operators ##

# ==
# !=
# <=
# >=
# >
# <
print(ord('a'))

# Chained Conditionals ##
# Combining multiple conditionals together
z = 0
r1 = x == y
r2 = y > x
r3 = z - 2 < x + 2
# and or not
r4 = r1 or r2 # If r1 OR r2 are true, r4 is true.
print(r4)
r4 = r1 or not r2 
print (r4)
print(True and False or True)
# If/ Else / Elif ##
z= 2
if z == 0:
    print("z is real")
elif z == 2:
    print("wowz")
else:
    print("z is fake")

# List/ Tuples ##
x = [4,True,'hi'] # List - An ordered collection that can store multiple elements of any type
print(len(x)) # Prints length of list
x.append('hello') # adds an element to the end of the list
print(x)
x.extend([1,2,3]) #adds a list to the end of the list
print(x)
print(x.pop()) # removes the last element from the list and returns it
print(x)
print(x[1]) #Accesses the second element of the list
x[0] = 'hello' # Changes the first element in the list
print(x)

x = (0,0,2,2) # A tuple is a list that is immutable ( cannot be changed)
# For Loops ##
for i in range(10): #Range is a function that creates a collection of numbers based on the input 
    print(i)
# While Loops ##

# Slice Operator ##

# Sets ##

# Dicts ##

# Comprehensions ##

# Functions ##
