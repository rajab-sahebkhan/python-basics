a = input("Enter the operator (+, -, /, *): ")
b = float(input("Enter first number: "))
c= float(input("Enter second number: "))

if a == "+":
    d = b+c
    print(round(d, 3))
elif a== "-":
    d = b-c
    print(round(d, 3))
elif a== "/":
    d = b/c
    print(round(d, 3))
elif a== "*":
    d = b*c
    print(round(d, 3))
else:
    print("{d} is not a valid operator")

