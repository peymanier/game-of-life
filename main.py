from game.grids import get_pattern
from game.views import CursesView

if __name__ == "__main__":
    view = CursesView(get_pattern('blinker'))
    view.show()
