#Goal is to make a basic calculator (No GUi)
x=float(input("Insert your number: "))
op = (input("Insert your operation: "))
y= float(input("Insert your number:"))

#Operations: +, -, *, /
if(op == "+"):
    result = x + y
elif(op == "-"):
    result = x - y
elif(op == "*"):
    result = x*y
elif(op == "/"):
    result = x/y
else:
    result = "Error, Please enter a valid operation symbol"


print(f'{x} {op} {y} = {result}')