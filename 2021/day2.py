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

def part2(directions):
    x,y,aim = 0,0,0
    for direction in directions:
        d = int(re.search(r'\d+', direction).group())
        if("forward" in direction):
            x += d
            y += aim * d
        elif("down" in direction):
            aim += d
        elif("up" in direction):  
            aim -= d
    return x * y

def main():
    input = [str(x) for x in open('./inputs/day2.input')]
    print(part1(input))
    print(part2(input))

if __name__ == '__main__':
    main()