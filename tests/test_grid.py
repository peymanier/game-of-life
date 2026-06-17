from game import grids
from game.grids import ALIVE_CHAR


def test_grid_as_string():
    pattern = grids.Pattern("blinker", {(2, 1), (2, 2), (2, 3)})
    grid = grids.Grid(pattern, 5, 5)

    assert grid.as_string() == f' blinker  \n ‧ ‧ ‧ ‧ ‧\n ‧ ‧ ‧ ‧ ‧\n ‧ {ALIVE_CHAR} {ALIVE_CHAR} {ALIVE_CHAR} ‧\n ‧ ‧ ‧ ‧ ‧\n ‧ ‧ ‧ ‧ ‧'

    grid.evolve()
    assert grid.as_string() == f' blinker  \n ‧ ‧ ‧ ‧ ‧\n ‧ ‧ {ALIVE_CHAR} ‧ ‧\n ‧ ‧ {ALIVE_CHAR} ‧ ‧\n ‧ ‧ {ALIVE_CHAR} ‧ ‧\n ‧ ‧ ‧ ‧ ‧'

    grid.evolve()
    assert grid.as_string() == f' blinker  \n ‧ ‧ ‧ ‧ ‧\n ‧ ‧ ‧ ‧ ‧\n ‧ {ALIVE_CHAR} {ALIVE_CHAR} {ALIVE_CHAR} ‧\n ‧ ‧ ‧ ‧ ‧\n ‧ ‧ ‧ ‧ ‧'
