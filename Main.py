import base64
import os
import sys
import curses


def __Size_Check__(number):
    try:
        if(int(number) <= 2):
            print "Number must be greater than two (2)..."
            return False
    except ValueError:
        print "Not a valid type: must enter whole number"
        return False
    else:
        return True

print "Passworder Program"
pass_size = int(raw_input("Password Size: "))

if(__Size_Check__(pass_size) == False):

    __Size_Check__(pass_size)





