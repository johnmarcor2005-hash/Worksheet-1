# --------------------------------------------
# ICT105 Worksheet 1 - Session 2
# --------------------------------------------

# Variable Declaration and Types
a = 15
b = 12

print("Value of a:", a)
print("Value of b:", b)

print("Type of a:", type(a))
print("Type of b:", type(b))

# Basic Arithmetic Operations
print("\nArithmetic Operations")

addition = a + b
print("a + b =", addition)

subtraction = a - b
print("a - b =", subtraction)

multiplication = a * b
print("a * b =", multiplication)

division = a / b
print("a / b =", division)

# Using Variables and Type Casting
print("\nType Casting")

c = int(a / b)
print("Value of c:", c)
print("Type of c:", type(c))

c = float(c)
print("New value of c:", c)
print("New type of c:", type(c))

# Working with Strings
print("\nStrings")

message = "The result of a divided by b is "

result = message + str(c)
print(result)

# Comparison Operators
print("\nComparison Operators")

print("Is a greater than b?", a > b)

print("Is a equal to b?", a == b)
