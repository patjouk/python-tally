#!/usr/bin/env python
from pathlib import Path
import io
import sys


ONE = chr(0x1D369)
TWO = chr(0x1D36A)
THREE = chr(0x1D36B)
FOUR = chr(0x1D36C)
FIVE = chr(0x534C)
NEXT = {ONE:TWO, TWO:THREE, THREE:FOUR, FOUR:FIVE, FIVE:FIVE + ONE}

def increment(file_name):
    path = Path(file_name)
    if not path.exists():
        with path.open("x") as f:
            f.write(ONE)
    else:
        with path.open() as f:
            content = f.read().strip()
        last = content[-1]
        new_content = content[:-1] + NEXT[last]
        with path.open("w") as f:
            f.write(new_content)
            f.write("\n")

if __name__ == "__main__":
    increment(sys.argv[1])
