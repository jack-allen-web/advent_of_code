"""Day one"""

INPUT_PATH = "./inputs/day_one.txt"

def part_one():
    """Part one"""
    with open(INPUT_PATH, mode="r", encoding="UTF-8") as input_file:
        lines = [line.strip() for line in input_file.readlines()]

        print(lines)


if __name__ == '__main__':
    part_one()
