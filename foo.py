"""Test module."""
import sys
import os
import math


def bar():
    print(sys.argv, os.getcwd())


def baz() -> int:
    print("this is function baz")
    return 0


def zab() -> float:
    return math.pi


if __name__ == "__main__":
    bar()
