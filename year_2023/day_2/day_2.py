import re


def check_possible_games(lines: [str]):
    validity = {"red": 12, "green": 13, "blue": 14}
    valid_games_idx = set()

    for line in lines:
        game_group_regex = r"Game (\d+): "
        game_group = re.search(game_group_regex, line)
        game_idx = int(game_group.group(1))
        valid_games_idx.add(game_idx)

        line = re.sub(game_group_regex, "", line)

        subsets = line.split("; ")
        groups = {"red": 0, "green": 0, "blue": 0}
        for subset in subsets:
            for possible_group in groups.keys():
                sub_type = re.search(rf"(\d+) ({possible_group})", subset)
                if sub_type:
                    if (
                        int(sub_type.group(1)) > validity[sub_type.group(2)]
                        and game_idx in valid_games_idx
                    ):
                        valid_games_idx.remove(game_idx)

    return sum(valid_games_idx)


if __name__ == "__main__":
    with open("./input_1.txt") as input_file:
        part_one_result = check_possible_games(input_file.read().splitlines())

    print("part_one_result", part_one_result)
