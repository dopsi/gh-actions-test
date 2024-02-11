import sys
import os

def bar():
    print(sys.argv, os.getcwd())

def baz() -> int:
    print("baz")

if __name__ == "__main__":
    bar()
