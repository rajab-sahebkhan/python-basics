weight = float(input("Enter the weight: "))
unit = input("Enter the unit kg or lbs (K/P): ")

if unit == "K":
    weight= weight * 2.20462
    print(f"The weight in pounds is {round(weight,1)} lbs")
elif unit == "P":
    print(f"The weight in Kilograms is {round(weight, 1)} kg")
else:
    print("The unit is not valid.")



