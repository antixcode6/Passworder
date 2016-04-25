import os
import sys
import subprocess
import threading
from scrape import __scrape_from_web__

def __size_check__(number):
    try:
        if(int(number) <= 2):
            print "Too little words selected: must select more than two (2)"
            return False
        elif(int(number) >= 21):
            print "Too many words selected: must select less than twenty-one (21)"
    except ValueError:
        return False
    else:
        return True


def main():
    print "This program generates word based passwords." + '\n' +  "You get to decide how many words it contains." + '\n' + "Your password can be between 3 and 21 words"

    pass_size = int(raw_input("\nPassword Size:"))

    if(__size_check__(pass_size) == False):
        sys.exit()
    else:
        print "\nProcessing request\nSit tight"

        __scrape_from_web__(pass_size)
    sys.exit()

if __name__ == '__main__':
  main()
