import sys
import os
import math

def bar():
    print(sys.argv, os.getcwd())

def baz() -> int:
    print("this is function baz")

def zab() -> int:
    return math.pi

if __name__ == "__main__":
    bar()
