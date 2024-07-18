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

cr = 0

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



    def show(self, stdscr, cr):
        stdscr.clear()
        
        # Get list of files in the current directory
        self.files = os.listdir(self.path)
        
        # Dimensions for the window
        height = len(self.files) + 2  # Adjusted height to fit files + border
        width = 40
        start_y = 1
        start_x = 1 
        
        # Ensure the window fits within screen boundaries
        max_y, max_x = stdscr.getmaxyx()
        if start_y + height > max_y or start_x + width > max_x:
            stdscr.addstr(0, 0, "Window too large for screen")
            stdscr.refresh()
            return
        
        # Create the window and draw border
        self.show_win = curses.newwin(height, width, start_y, start_x)
        self.show_win.border(0)
        
        while True:
            # Display files in the window
            for idx, file_name in enumerate(self.files):
                if idx == cr:
                    self.show_win.addstr(idx + 1, 1, file_name, curses.A_REVERSE)
                else:
                    self.show_win.addstr(idx + 1, 1, file_name)
        
            mv.getmv(self.show_win, cr, self.files)    
            
            print(cr)

            # Refresh the window to display changes
            self.show_win.refresh() 

    def refresh(self, stdscr):
        stdscr.clear()
        stdscr.refresh()

    def main(self, stdscr):
        # hide cursor
        curses.curs_set(0)

        self.colors()
        self.refresh(stdscr)
        stdscr.clear()
        self.show(stdscr, cr)
        stdscr.refresh()

    def running(self):
        wrapper(self.main)

if __name__ == "__main__":
    system = func()
    system.running()       
    
