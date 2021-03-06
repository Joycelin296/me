# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """
    the_numbers = []
    x = start
    while x < stop:
        print(x)
        the_numbers.append(x)
        x = x + step
    return the_numbers


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """

    numbers = []
    while start < stop:
        numbers.append(start)
        start = start + step
    return numbers

def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    deh_numbers = []
    while start < stop:
        deh_numbers.append(start)
        start = start + 2
    return deh_numbers
    


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    
    import random

    number_guessed = random.randint(low, high)
    number = random.randint(low, high)
    guesses = 1

    while guesses == 1:
        if number_guessed > number:
            print('The number is higher')
            number = number + 1
        if number < number_guessed:
            print('The number is lower')
            number = number - 1
        if number_guessed == number:
            print('You got it!')
            return number

    import random
    number = random.randint(low, high)
    guess = random.randint(low,high)
    guesses = False
    while not guesses:
        guess = int(input('Guess a number: '))
        if guess < number:
            print('The number is higher.')
            number = number - 1
        if guess > number:
            print('The number is lower.')
            number = number + 1
        if guesses == number:
            print('You got the number!')
            guesses = True
    return guess
    """
    import random

    random_number = random.randint(low, high)
    guess = 1
    while guess == 1:
        number = input('Guess a number: ')
        if number < high and number > low:
            return number
            guess = 0



    


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
   
    while True:
        number = input('Enter a number: ')
        try:
            number = int(number)
            break
        except ValueError:
            continue
    return number 
    """
    thing = input("Enter a number: ")
    while not thing.isdigit():
        thing = input(message)
        return thing

    return thing


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    
    import random
    number = random.randint(low, high)
    guesses = False
    print('I am thinking of a number.')
    while not guesses:
        try:
            guess = int(input('Take a guess: '))
            if guess < number:
                print('The number is higher.')
            if guess > number:
                print('The number is lower.')
            if guess == number:
                print('You are right!')
                guesses = True
        except ValueError:
            print('Please enter an integer: ')
    return 'You got it!'
    """
    import random

    random_numbers = random.randint(low, high)
    guess = 1
    while guess == 1:
        try:
            number = input('Guess a number: ')
            if number < high and number > low:
                guess = 0
        except ValueError:
            print('Please enter an integer: ')
    return number
        
            


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
