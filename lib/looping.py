#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

        
happy_new_year()
def square_integers(int_list):
    # code goes here!
    int_list= [int**2 for int in int_list]
    return int_list
    
square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)

fizzbuzz()
 
        
