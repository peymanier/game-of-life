from collections import defaultdict


def get_neighbors(x: int, y: int):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in dirs:
        yield x + dx, y + dy


class Grid:
    def __init__(self, pattern):
        self.pattern = pattern

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
        pass

    def __str__(self):
        return (
            f'name: {self.pattern.name}\n'
            f'alive cells: {sorted(self.pattern.alive_cells)}'
        )
