#!/usr/bin/env python3

def print_fibonacci(length):
    result_array = []
    for n in range(length):
        result_array.append(fibonacci_at(n))
    print(result_array)         
    pass

def fibonacci_at(index):
    if (index == 0):
        return 0
    elif (index == 1):
        return 1
    elif (index == 2):
        return 0 + 1   
    elif (index > 2):
        return fibonacci_at(index-2) + fibonacci_at(index-1)   
   
    pass