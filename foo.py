"""Test module."""
import math
import sys
from pathlib import Path


def bar():
    """Print some information."""
    print(sys.argv, Path.cwd())  # noqa: T201


def baz() -> int:
    """Print message and return 0."""
    print("this is function baz")  # noqa: T201
    return 0


def zab() -> float:
    """Return math.pi."""
    return math.pi


def rab() -> float:
    return None

if __name__ == "__main__":
    bar()
