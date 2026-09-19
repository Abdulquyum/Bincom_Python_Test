#!/usr/bin/env python3

# Write a program to sum the first 50 fibonacci sequence.
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        #print(a, end=' ')
        a, b = b, a + b
    return a

# Calculate the sum of the first 50 Fibonacci numbers
total = sum(fibonacci(i) for i in range(50))
print(f"Sum of the first 50 Fibonacci numbers: {total}")
