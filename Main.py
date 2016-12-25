import os
import sys
import subprocess
from scrape import __scrape_from_web__

def repeatOnError(*exceptions):
  def checking(function):
    def checked(*args, **kwargs):
      while True:
        try:
          result = function(*args, **kwargs)
        except exceptions as problem:
          print "There was a problem with the input:"
          print problem.__class__.__name__
          print problem
          print "Please enter a valid base-10 number\nWe support password generation for 3 to 25 words!"
        else:
          return result
    return checked
  return checking


def main():
   @repeatOnError(ValueError)
    def getNumber():
      return int(raw_input("Please enter your password length: "))

    passCounter = getNumber()
    print "You have chosen a ", passCounter, " word password."
    
if __name__ == '__main__':
  main()







