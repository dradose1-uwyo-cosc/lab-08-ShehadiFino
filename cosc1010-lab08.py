# Shehadi Fino
# UWYO COSC 1010
# 11-4-24
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to: Ryan
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

import math

def convert_number(value):
    try:
        if '.' in value:
            float_value = float(value)
            if value.count('.') == 1:
                return float(value)
            else:
                return False
        else:
            return int(value)
    except ValueError:
        return False
print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, lower_x, upper_x):
    if not isinstance(lower_x, int) or not isinstance(upper_x, int) or lower_x > upper_x:
        return False

    y_values = []
    for x in range(lower_x, upper_x + 1):
        y = m * x + b
        y_values.append(y)
    return y_values

while True:
    m_user_input = input("Enter the slope (m) or 'exit' to quit: ")
    if m_user_input.lower() == 'exit':
        break
    b_user_input = input("Enter the intercept (b): ")
    lower_x_input = input("Enter value of lower x bound: ")
    upper_x_input = input("Enter value of upper x bound: ")

    m = convert_number(m_user_input)
    b = convert_number(b_user_input)
    lower_x = convert_number(lower_x_input)
    upper_x = convert_number(upper_x_input)

    if m is False or b is False or lower_x is False or upper_x is False:
        print("Invalid input, enter numbers only")
        continue

    y_values = slope_intercept(m, b, lower_x, upper_x)
    print("y values:", y_values)
print("*" * 75)



# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def sqrt(value):
    if value < 0:
        return None
    return math.sqrt(value)

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4 * a * c
    sqrt_discriminant = sqrt(discriminant)

    if sqrt_discriminant is None:
        return None
    
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    return x1, x2

while True:
    a_user_input = input("Enter a value for a or 'exit' to quit: ")
    if a_user_input.lower() == 'exit':
        break
    b_user_input = input("Enter a value for b: ")
    c_user_input = input("Enter a vlaue for c: ")

    a = convert_number(a_user_input)
    b = convert_number(b_user_input)
    c = convert_number(c_user_input)

    if a is False or b is False or c is False:
        print("Invalid input, enter numbers only")
        continue

    result = quadratic_formula(a, b, c)
    if result is None:
        print("No real solutions")
    else:
        print("Solutions:", result)