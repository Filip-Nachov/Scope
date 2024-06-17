'''
MIT License

Copyright (c) 2024 Filip-Nachov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import curses
from curses import wrapper
import os

class func:
    def init(self):
        path = os.getcwd()
        
    def colors(self):
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK) # folder color
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK) # basic file color
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) # executable file color
        CYAN = curses.color_pair(1)
        WHITE = curses.color_pair(2)
        GREEN = curses.color_pair(3)


    def refresh(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Press any key to continue...")
        stdscr.refresh()
        stdscr.getkey()

    def main(self, stdscr):
        self.colors()
        self.refresh(stdscr)

    def running(self):
        wrapper(self.main)

if __name__ == "__main__":
    system = func()
    system.running()
