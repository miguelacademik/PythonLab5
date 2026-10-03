# Part 2: Recursion and Number Conversion

# Task 1: Convert Decimal to Binary (Recursion)
# Write a recursive function decimal_to_binary(n)
# that takes a positive integer n and returns its binary representation as a string.

def decimal_to_binary(n):
    if n == 0: return '0'
    if n == 1: return '1'
    next, digit = divmod(n, 2)
    return decimal_to_binary(next) + str(digit)

# Task 2: Convert Binary to Decimal (Recursion)
# Write a recursive function binary_to_decimal(b)
# that takes a binary string b and returns its decimal equivalent.

def binary_to_decimal(b:str):
    if b == '': return 0
    place = len(b) - 1
    return 2**place  * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))

# Test cases -------------------------------------------------------------------
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1"
print(decimal_to_binary(100))

print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1