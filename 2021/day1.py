def part1(depths):
    previous = depths[0]
    count = 0
    for depth in depths:
        if depth > previous : 
            count += 1  
        previous = depth
    return count

def part2(depths):
    previous = sum(depths[:3])
    count = 0
    for depth in range(1, len(depths) - 2):
        current = sum(depths[depth:depth + 3])
        if current > previous:
            count += 1
        previous = current
    return count

def main():
    input = [int(x) for x in open('./inputs/day1.input')]
    print(part1(input))
    print(part2(input))

if __name__ == '__main__':
    main()