#!/usr/bin/env python3

import random

# Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
# Generate a random 4-digit number of 0s and 1s

random_number = ''.join(random.choice('01') for _ in range(4))

# Convert the generated number to base 10
base10_number = int(random_number, 2)

print(f"Random 4-digit binary number: {random_number}")
print(f"Base 10 equivalent: {base10_number}")
