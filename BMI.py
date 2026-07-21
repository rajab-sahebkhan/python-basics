weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the height in centimeters: "))

bmi = weight / ((height/100) ** 2)

print(f"The bmi is: {round(bmi, 1)}   kg/m^2")
