import re
import math


GAME_GROUP_REGEX = r"Game (\d+): "
MAX_CUBES_NUMBER = {"red": 12, "green": 13, "blue": 14}


def check_fewest_cubes(line: str):
    max_types = {"red": 0, "green": 0, "blue": 0}

    for possible_group in MAX_CUBES_NUMBER.keys():
        cube_color_value = [int(cube[0]) for cube in re.findall(rf"(\d+) ({possible_group})", line)]
        if (max(cube_color_value) > max_types[possible_group]):
            max_types[possible_group] = max(cube_color_value)

    return math.prod(max_types.values())


def check_possible_game(line: str):
    game_group = re.search(GAME_GROUP_REGEX, line)
    game_idx = int(game_group.group(1))

    for possible_group in MAX_CUBES_NUMBER.keys():
        cube_color_value = [int(cube[0]) for cube in re.findall(rf"(\d+) ({possible_group})", line)]
        if (max(cube_color_value) > MAX_CUBES_NUMBER[possible_group]):
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


def main():
    import os
    dirpath = os.path.dirname(__file__)

    with open(f"{dirpath}/input_1.txt") as input_file:
        part_one_result = check_possible_games(input_file.read().splitlines())

    with open(f"{dirpath}/input_1.txt") as input_file:
        part_two_result = check_fewest_cubes_possible(input_file.read().splitlines())

    print("part_one_result", part_one_result)
    print("part_two_result", part_two_result)

    return {"p1": part_one_result, "p2": part_two_result}

if __name__ == "__main__":
    main()
