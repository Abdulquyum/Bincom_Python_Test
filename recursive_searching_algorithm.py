#!/usr/bin/env python3

# BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.

def recursive_search(arr, target, index=0):
    # Base case: if index is out of bounds, return -1 (not found)
    if index >= len(arr):
        return -1
    
    # If the current element matches the target, return the index
    if arr[index] == target:
        return index
    
    # Recursive case: search in the rest of the array
    return recursive_search(arr, target, index + 1)
