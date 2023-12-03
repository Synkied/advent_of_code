from utils import timeit


def compute_result(digits: [str]):
    result = 0
    result += int(f"{digits[0]}{digits[-1]}")

    return result


@timeit
def part_one(lines: [str]):
    result = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if digits:
            result += compute_result(digits)

    return result


@timeit
def part_two(lines: [str]):
    valid_string_numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    result = 0

    for line in lines:
        result_digits = []
        for char_idx, char in enumerate(line):
            if char.isdigit():
                result_digits.append(char)
            for idx, val in enumerate(valid_string_numbers):
                if line[char_idx:].startswith(val):
                    result_digits.append(str(idx + 1))

        result += compute_result(result_digits)

    return result


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
