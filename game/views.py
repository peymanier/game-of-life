import curses
import time

from game.grids import Grid, Pattern


class CursesView:
    def __init__(self, pattern: Pattern, gen=10, fps=7):
        self.pattern = pattern
        self.gen = gen
        self.fps = fps

    def show(self):
        curses.wrapper(self._draw)

    def _draw(self, screen):
        grid = Grid(self.pattern, 20, 20)
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0, 0, grid.as_string())
        except curses.error:
            raise ValueError(f'terminal too small for pattern: {self.pattern.name}')

        for _ in range(self.gen):
            grid.evolve()
            screen.addstr(0, 0, grid.as_string())
            screen.refresh()
            time.sleep(1 / self.fps)
