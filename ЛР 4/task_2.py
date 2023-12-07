# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        file = csv.DictReader(f)
        lines = [line_ for line_ in file ]
        with open(OUTPUT_FILENAME, 'w') as ffile:
            return json.dump(lines, ffile, indent=4, ensure_ascii=False)


trr = open(OUTPUT_FILENAME, 'w')

    # сериализовать с отступами 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
