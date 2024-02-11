"""Test module."""
import math
import os
from pathlib import Path
import sys


def bar():
    print(sys.argv, Path.cwd())


def baz() -> int:
    print("this is function baz")
    return 0


def zab() -> float:
    return math.pi


if __name__ == "__main__":
    bar()
