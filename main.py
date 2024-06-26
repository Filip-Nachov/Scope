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
import movement as mv

class func:
    def __init__(self):
        self.path = os.getcwd()
        
    def colors(self):
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK) # folder color
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK) # basic file color
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) # executable file color
        self.CYAN = curses.color_pair(1)
        self.WHITE = curses.color_pair(2)
        self.GREEN = curses.color_pair(3)



    def show(self, stdscr):
        # start functions
        stdscr.clear()
        files = os.listdir(self.path)

        # dimensions for the window
        height = len(files) + 2
        width = 40
        start_y = 1
        start_x = 1 
        
        # creating the window and border 
        self.show_win = curses.newwin(height, width, start_y, start_x)
        self.show_win.border(0)
    
        self.show_win.bkgd(' ', curses.COLOR_BLACK)
        # showing process
        for idx, filename in enumerate(files):
            self.show_win.addstr(idx + 1, 2, filename)
       
        # catching movement
        mv.getmv(self)
    
        # end commands
        self.show_win.refresh()
        self.show_win.getkey()
        

    def refresh(self, stdscr):
        stdscr.clear()
        stdscr.refresh()

    def main(self, stdscr):
        self.colors()
        self.refresh(stdscr)
        stdscr.clear()
        self.show(stdscr)
        stdscr.refresh()

    def running(self):
        wrapper(self.main)

if __name__ == "__main__":
    system = func()
    system.running()       
    
