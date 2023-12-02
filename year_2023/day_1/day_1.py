def compute_result(digits: [str]):
    result = 0
    result += int(f"{digits[0]}{digits[-1]}")

    return result


def part_one(lines: [str]):
    result = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if digits:
            result += compute_result(digits)

    return result


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


if __name__ == "__main__":
    with open("./input_1.txt") as input_file:
        part_one_result = part_one(input_file.read().splitlines())

    with open("./input_1.txt") as input_file:
        part_two_result = part_two(input_file.read().splitlines())

    print("part_one_result", part_one_result)
    print("part_two_result", part_two_result)
