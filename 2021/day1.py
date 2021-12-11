def part1(depths):
    previous = depths[0]
    count = 0
    for depth in depths:
        if depth > previous : 
            count += 1  
        previous = depth
    return count

def part2():
    print("TODO")

def main():
    print(part1([int(x) for x in open('./inputs/day1.input')]))

if __name__ == '__main__':
    main()