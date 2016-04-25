import os
import sys
import subprocess
from scrape import __scrape_from_web__

def __size_check__(number):
    try:
        if(int(number) <= 2):
            print "Too little words selected: must select more than two (2)"
            return False
        elif(int(number) >= 11):
            print "Too many words selected: must select less than eleven (11)"
    except ValueError:
        return False
    else:
        return True


def main():
    print "Passworder Program"
    pass_size = int(raw_input("Password Size: "))

    if(__size_check__(pass_size) == False):
        sys.exit()
    else:
        __scrape_from_web__(pass_size)
    sys.exit()

if __name__ == '__main__':
  main()







