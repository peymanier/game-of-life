import argparse

from game.grids import get_pattern_names, get_pattern
from game.views import CursesView

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Conway's game of life",
        description="Conway's Game of Life in your terminal"
    )
    parser.add_argument(
        "-p",
        "--pattern",
        choices=get_pattern_names(),
        default="Blinker",
        help="take a pattern for the Game of Life (default: %(default)s)",
    )
    parser.add_argument(
        "-g",
        "--gen",
        metavar="NUM_GENERATIONS",
        type=int,
        default=10,
        help="number of generations (default: %(default)s)",
    )
    parser.add_argument(
        "-f",
        "--fps",
        metavar="FRAMES_PER_SECOND",
        type=int,
        default=7,
        help="frames per second (default: %(default)s)",
    )
    args = parser.parse_args()

    view = CursesView(get_pattern(args.pattern), args.gen, args.fps)
    view.show()
