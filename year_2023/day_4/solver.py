def part_one():
    pass


def part_two():
    pass


def main():
    import os

    dirpath = os.path.dirname(__file__)

    with open(f"{dirpath}/input_1.txt") as input_file:
        part_one_result, part_one_time = part_one(input_file.read().splitlines())

    with open(f"{dirpath}/input_1.txt") as input_file:
        part_two_result, part_two_time = part_two(input_file.read().splitlines())

    print("part_one_result", part_one_result)
    print("part_two_result", part_two_result)

    return {
        "p1": {"result": part_one_result, "time": part_one_time},
        "p2": {"result": part_two_result, "time": part_two_time},
    }


if __name__ == "__main__":
    main()
