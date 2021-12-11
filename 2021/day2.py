from io import StringIO
from os import X_OK


import re

def part1(directions):
    x,y = 0,0
    for direction in directions:
        d = int(re.search(r'\d+', direction).group())
        if("forward" in direction):
            x += d
        elif("down" in direction):
            y += d
        elif("up" in direction):
            y -= d
    return x*y

def main():
    print(part1([str(x) for x in open('day2.input')]))

if __name__ == '__main__':
    main()