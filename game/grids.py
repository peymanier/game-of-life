import json
from collections import defaultdict
from dataclasses import dataclass
import tomllib
from pathlib import Path

ALIVE_CHAR = "♥"
DEAD_CHAR = "‧"


def get_neighbors(x: int, y: int):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in dirs:
        yield x + dx, y + dy


@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def from_toml(cls, name: str, data: list[list[int]]):
        return cls(name, alive_cells={(int(x), int(y)) for x, y in data})


PATTERNS_FILENAME = Path(__file__).parent / 'patterns.toml'


def get_pattern_names():
    with PATTERNS_FILENAME.open('rb') as f:
        data = tomllib.load(f)

    return data.keys()


def get_pattern(name: str):
    with PATTERNS_FILENAME.open('rb') as f:
        data = tomllib.load(f)

    game_config = data[name]
    return Pattern.from_toml(name, game_config['alive_cells'])


class Grid:
    def __init__(self, pattern: Pattern, num_rows: int, num_cols: int):
        self.pattern = pattern
        self.num_rows = num_rows
        self.num_cols = num_cols

    def evolve(self):
        alive_neighbors_counter = defaultdict(int)

        for x, y in self.pattern.alive_cells:
            for a, b in get_neighbors(x, y):
                alive_neighbors_counter[(a, b)] += 1

        stay_alive = set()
        for cell, count in alive_neighbors_counter.items():
            if cell in self.pattern.alive_cells and count == 2 or count == 3:
                stay_alive.add(cell)

        become_alive = set()
        for cell, count in alive_neighbors_counter.items():
            if cell not in self.pattern.alive_cells and count == 3:
                become_alive.add(cell)

        self.pattern.alive_cells = stay_alive | become_alive

    def as_string(self):
        display = [self.pattern.name.center(2 * self.num_cols)]
        for row in range(self.num_rows):
            display_row = []
            for col in range(self.num_cols):
                if (row, col) in self.pattern.alive_cells:
                    display_row.append(ALIVE_CHAR)
                else:
                    display_row.append(DEAD_CHAR)

            display.append(" ".join(display_row))

        return "\n ".join(display)

    def __str__(self):
        return (
            f'name: {self.pattern.name}\n'
            f'alive cells: {sorted(self.pattern.alive_cells)}'
        )
