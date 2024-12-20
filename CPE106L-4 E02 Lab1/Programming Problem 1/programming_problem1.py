#Programming Problem 1:

'''
Statisticians would like to have a set of functions to compute the median and mode of a list of numbers.
The median is the number that would appear at the midpoint of a list if it were sorted.
The mode is the number that appears most frequently in the list.
Define these functions in a module named stats.py.
Also include a function named mean, which computes the average of a set of numbers.
Each function expects a list of numbers as an argument and returns a single number.
'''

'''
This file requires the stats.py to run. Make sure this program has access to the file.
'''

import stats

n = input("Enter numbers separated by commas: ")
if not n:
    print("The list of numbers is empty.")
else:
    numbers = [float(num) for num in n.split(",")]
    print("Mean:", stats.mean(numbers))
    print("Median:", stats.median(numbers))
    print("Mode:", stats.mode(numbers))
