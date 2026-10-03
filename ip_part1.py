# Part 1: Conditional Validation of IP Addresses.

# Task 1: Validating IP Address Parts
# Write a function is_valid_part(part) that takes a string as input and
# checks if the string represents a valid part of an IP address.

# Each part should:
# Be a number between 0 and 255 (inclusive).
# Not contain leading zeroes (e.g., "01" is invalid, but "1" is valid).

def is_valid_part(part):
    try:
        i_part = int(part)
        if part[0] == '0' and not i_part == 0: return False
        return 0 <= i_part < 256
    except ValueError as ve:
        return False

# Task 2: Validating the Full IP Address
# Using is_valid_part, write a function is_valid_ip(ip) that validates an entire IP address.
# The IP address will be passed as a string, and each part will be separated by dots (e.g., "192.168.1.1").
# Return True if the IP is valid, otherwise False.

def is_valid_ip(ip:str):
    parts = ip.split('.')
    if len(parts) != 4: return False
    for part in parts:
        if not is_valid_part(part): return False
    return True

# Calling the Functions -------------------------------------------------------------------

print(
    is_valid_part('AAA'),
    is_valid_part('257'),
    is_valid_part('-255'),
    is_valid_part('01'),
    is_valid_part('0'))

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False