import curses
from curses import wrapper 

def main(stdscr):
    stdscr.clear()
    stdscr.addstr('press any key to continue..', curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
