import re
import math

GAME_GROUP_REGEX = r"Game (\d+): "
MAX_CUBES_NUMBER = {"red": 12, "green": 13, "blue": 14}


def get_cube_subsets(line: str):
    line = re.sub(GAME_GROUP_REGEX, "", line)
    cube_subsets = line.split("; ")

    return cube_subsets


def check_fewest_cubes(line: str):
    max_types = {"red": 0, "green": 0, "blue": 0}
    cube_subsets = get_cube_subsets(line)

    for subset in cube_subsets:
        for possible_group in MAX_CUBES_NUMBER.keys():
            cube_color_value = re.search(rf"(\d+) ({possible_group})", subset)
            if cube_color_value:
                value = int(cube_color_value.group(1))
                color = cube_color_value.group(2)
                if value > max_types[color]:
                    max_types[color] = value

    return math.prod(max_types.values())


def check_possible_game(line: str):
    game_group = re.search(GAME_GROUP_REGEX, line)
    game_idx = int(game_group.group(1))
    cube_subsets = get_cube_subsets(line)

    for subset in cube_subsets:
        for possible_group in MAX_CUBES_NUMBER.keys():
            cube_color_value = re.search(rf"(\d+) ({possible_group})", subset)
            if cube_color_value:
                value = int(cube_color_value.group(1))
                color = cube_color_value.group(2)
                if (
                    int(value) > MAX_CUBES_NUMBER[color]
                ):
                    return 0

    return game_idx


def check_possible_games(lines: [str]):
    valid_games_idx = set()

    for line in lines:
        game_idx = check_possible_game(line)
        valid_games_idx.add(game_idx)

    return sum(valid_games_idx)


def check_fewest_cubes_possible(lines: [str]):
    max_types_for_games = []

    for line in lines:
        max_types_for_games.append(check_fewest_cubes(line))

    return sum(max_types_for_games)


if __name__ == "__main__":
    with open("./input_1.txt") as input_file:
        part_one_result = check_possible_games(input_file.read().splitlines())

    with open("./input_1.txt") as input_file:
        part_two_result = check_fewest_cubes_possible(input_file.read().splitlines())

    print("part_one_result", part_one_result)
    print("part_two_result", part_two_result)
