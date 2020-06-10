"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""

#
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

   # I think this will print "what" imported from some_words calling the print function
for word in some_words:
    print(word) # It printed the words in some_words individually in separate lines

    # I think this will print "?" imported from some_words that isn't a word calling the print function 
for x in some_words:
    print(x) # It also prints the words in some_words individually in separate lines

# I think this will print "what does this line do ?"
print(some_words) # It printed some_words exactly by the layout it was in

#I think this will print "what does this line do ? contains more than 3 words"
if len(some_words) > 3:
    print('some_words contains more than 3 words') # It printed some_words contains more than 3 words

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # I think this will disregard items that are undefined, they become 'none'
    print(platform.uname()) # Instead of not naming things, it named all the platforms used

# I think this addresses the information as important
usefulFunction() # this wasn't a code?
