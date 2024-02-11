import sys
import os

def bar():
    print(sys.argv, os.getcwd())

if __name__ == "__main__":
    bar()
