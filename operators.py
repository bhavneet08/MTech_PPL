# Take input from user
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# 1. Arithmetic Operators
print("\n--- Arithmetic Operators ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Power:", a ** b)

# 2. Comparison Operators
print("\n--- Comparison Operators ---")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Less Than:", a < b)
print("Greater Than:", a > b)
print("Less Than or Equal:", a <= b)
print("Greater Than or Equal:", a >= b)

# 3. Logical Operators
print("\n--- Logical Operators ---")
print("AND:", a > 0 and b > 0)
print("OR:", a > 0 or b > 0)
print("NOT:", not(a > 0))

# 4. Assignment Operators
print("\n--- Assignment Operators ---")
x = a
print("Initial x:", x)

x += b
print("x += b:", x)

x -= b
print("x -= b:", x)

x *= b
print("x *= b:", x)

x /= b
print("x /= b:", x)

# 5. Bitwise Operators
print("\n--- Bitwise Operators ---")
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# 6. Membership Operators
print("\n--- Membership Operators ---")
numbers = [a, b]
print("a in numbers:", a in numbers)
print("b not in numbers:", b not in numbers)

# 7. Identity Operators
print("\n--- Identity Operators ---")
x = a
y = b
print("x is y:", x is y)
print("x is not y:", x is not y)