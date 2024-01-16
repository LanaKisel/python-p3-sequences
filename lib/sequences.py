#!/usr/bin/env python3

def print_fibonacci(length):
    result_array = []
    second_previous_num = 0
    previous_num = 1
    
    if (length == 0):
        print(result_array)
        return
   
    result_array.append(second_previous_num)          
    if (length == 1):
        print(result_array)
        return
    
    result_array.append(previous_num)          
    if (length == 2):
        print(result_array)
        return

    for n in range(2, length):
        new_num = second_previous_num + previous_num
        result_array.append(new_num)
        # shift the new number that was "created" into previous number
        # then shift the previous number into second previous number
        second_previous_num = previous_num
        previous_num = new_num
    
    print(result_array)


#     for n in length:
#         if (n == 0):
#             print(result_array)
#         elif (length ==1):
#             print(result_array(n))
#         elif (length == 2):
#             print (result_array)        


#         result_array.append(fibonacci_at(n))
#     print(result_array)         
#     pass

# def fibonacci_at(index):
#     if (index == 0):
#         return 0
#     elif (index == 1):
#         return 1
#     elif (index == 2):
#         return 0 + 1   
#     elif (index > 2):
#         return fibonacci_at(index-2) + fibonacci_at(index-1)   
   
#     pass