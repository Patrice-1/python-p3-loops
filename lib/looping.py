#!/usr/bin/env python3

def happy_new_year():

    num = 10
    # Print numbers from 10 to 1, decrementing by 1 each time
    while num > 0:
        print(num)
        num -= 1
    #print "Happy New Year" once loop is finished
    print('Happy New Year!')

    #Test
happy_new_year()  # Outputs: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1




def square_integers(int_list):
    # Create a new list where each element is the square of the corresponding element in the input list
    return [i ** 2 for i in int_list]

# Test cases to validate the function
# Example list of positive integers
int_list1 = [1, 2, 3, 4, 5]
# Example list of negative integers
int_list2 = [-1, -2, -3, -4, -5]

# Print the result of squaring each integer in the first test list
print(f"Result for [1, 2, 3, 4, 5]:", square_integers(int_list1))
# Print the result of squaring each integer in the second test list
print(f"Result for [-1, -2, -3, -4, -5]:", square_integers(int_list2))





def fizzbuzz():

    # Print numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz"
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
            
#Test
fizzbuzz()

