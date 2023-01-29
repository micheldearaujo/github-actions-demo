from hello import add, multiply

number1 = float(input("Type number 1: "))
number2 = float(input("Type number 2: "))

print(f"Adding {number1} + {number2}...")
print(f"The result is: {add(number1, number2)}")

print(f"Multiplying {number1} * {number2}...")
print(f"The result is: {multiply(number1, number2)}")