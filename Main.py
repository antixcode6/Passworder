import base64
import os
import sys
import random
import subprocess


def __size_check__(number): #Some would say this is useless - but I say to hell with bad test cases
    try:
        if(int(number) <= 2):
            print "Too little words selected: must select more than two (2)"
            return False
        elif(int(number) >= 8):
            print "Too many words selected: must select less than eight (8)"
    except ValueError:
        return False
    else:
        return True

def __get_pass__():
    words = list(open('text.txt'))
    random.SystemRandom().shuffle(words)
    target = open("pass.txt",'w')
    wodries = (' '.join(w.strip() for w in words[:4]))
    target.write(wodries)



def main():
    print "Passworder Program"
    pass_size = int(raw_input("Password Size: "))

    if(__size_check__(pass_size) == False):
        sys.exit()
    else:
        __get_pass__()
        '''
         open("text.txt", 'a')
        if sys.platform == "win32":
            os.startfile("text.txt")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "text.txt"])
        '''




    sys.exit()
if __name__ == '__main__':
  main()







