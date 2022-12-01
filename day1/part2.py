from utils import getInput


def main(aoc: str):
    groups = aoc.split("\n\n")
    calories = (
        sum(int(c) for c in g.split("\n"))
        for g in groups
    )

    print(sum(sorted(calories, reverse=True)[:3]))


if __name__ == "__main__":
    main(getInput("./input.txt"))
