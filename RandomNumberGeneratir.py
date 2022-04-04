#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:03:21 2022

@author: johnkim
"""

"Project 1: Random Number Generator (Ints)"

import random as rand

step = 0 
add = 0


num_of_input = int(input('1. How many numbers? '))

if (num_of_input == 0):
    "Input is Zero"
    raise Exception('Enter Number Not Zero')

lowest_input = int(input('2. Lowest number wanted? '))

highest_input = int(input('3. Highest number wanted? '))

if (highest_input <= lowest_input):
    "Highest Number is Lower than Lowest Number"
    raise Exception('Highest Number Too Low')

type_int = input('4. Evens or Odd? (yes or no) ')

if ((type_int.lower().strip() != 'yes') and (type_int.lower().strip() != 'no')):
    "Answer to Question 4 is Invalid"
    raise Exception('Invalid Input for 4!')

repeat = input('5. Repeats? (yes or no) ')

if ((repeat.lower().strip() != 'yes') and (repeat.lower().strip() != 'no')):
    "Answer to Question 5 is Invalid"
    raise Exception('Invalid Input for 5!')


"Error: If Results Aren't Possible"

if ((repeat.lower().strip() == 'no') and (type_int.lower().strip() == 'no') and (num_of_input > highest_input)):
    "Number of Desired Numbers Exceeds Possible Numbers Despite No Repeats"
    raise Exception('Asking for Too Many Numbers')


"Generate Random Numbers"

array = list(range(lowest_input, highest_input+1))
new_arr = []

if (type_int.lower().strip() == 'yes'):
    "Returns Evens and Odds"
    step = 2
    
    even_or_odd = input('Even or Odd? ')
    
    if ((even_or_odd.lower().strip() != 'even') and (even_or_odd.lower().strip() != 'odd')):
        "Answer to Even or Odd is Invalid"
        raise Exception('Invalid Input for Even or Odd!')                
                
    if (even_or_odd.lower().strip() == 'even'):
        "Even Numbers Wanted"
        if ((lowest_input % 2) != 0):
            "Starting Number is Odd"
            add += 1
        for x in range(num_of_input):
            "Make Array of Even"
            if ((array[x] % 2) == 0):
                new_arr.append(array[x])
                
    else:
        "Odd Number Wanted"
        if ((lowest_input % 2) == 0):
            "Starting Number is Even"
            add += 1
        for x in range(num_of_input):
            "Make Array of Odd"
            if ((array[x] % 2) != 0):
                new_arr.append(array[x])

                        
    if (repeat.lower().strip() != 'no'):
        "Print Random Even and/or Odd Numbers with No Repeat"
        for i in range(num_of_input):
            new_arr.append(rand.randrange((lowest_input + add), (highest_input+1), step))
        print(new_arr)
    else:
        "Print Random Array of Evens or Odds with Repeat"
        print(rand.sample(new_arr, num_of_input))
else:
    "Return Random Numbers"
    if (repeat.lower().strip() == 'no'):
        "No Repeat"
        print(rand.sample(array, num_of_input))
    else:
        "Repeat"
        for i in range(num_of_input):
            new_arr.append(rand.randrange(highest_input+1))
        print(new_arr)
    
    






