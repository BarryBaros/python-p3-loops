#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

# Call the function
happy_new_year()


def square_integers(int_list):
    # code goes here!
    return[x ** 2 for x in int_list]

print(square_integers([1, 6, 3, 10, 9]))
    

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
fizzbuzz()
   
