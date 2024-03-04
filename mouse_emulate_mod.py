#!/usr/bin/python
"""
Credits: https://github.com/Ricc4rdo0107 | Riccardo Zappitelli
Original Creation: https://github.com/Shubhamvis98/badbt
"""
import random as rd
import curses, sys
try:
    from mouse_emulate import MouseClient
except ModuleNotFoundError:
    print("Download the module files first")
    print("git clone https://github.com/Shubhamvis98/badbt")
    exit()


client = MouseClient()

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

if len(sys.argv) == 2:
    if sys.argv[1].isdigit():
        sensibility = int(sys.argv[1])
    else:
        print("Usage: python3 mouse_client_mod.py <sensibility>")
else:
    sensibility = 10

right = 0
left = 272

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == ord("r"):
            screen.addstr(0, 0, 'right click   ')
            client.state[0] = right
            client.state[1] = 1
            client.state[2] = 1
            client.state[3] = 0
        elif char == ord("l"):
            screen.addstr(0, 0, 'left click   ')
            client.state[0] = left
            client.state[1] = 1
            client.state[2] = 1
            client.state[3] = 0
        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'right arrow  ')
            client.state[0] = 0
            client.state[1] = sensibility
            client.state[2] = 0
            client.state[3] = 0
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left arrow   ')
            client.state[0] = 0
            client.state[1] = 255-sensibility
            client.state[2] = 0
            client.state[3] = 0
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up arrow    ')
            client.state[0] = 0
            client.state[1] = 0
            client.state[2] = 255-sensibility
            client.state[3] = 0
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down arrow   ')
            client.state[0] = 0
            client.state[1] = 0
            client.state[2] = sensibility
            client.state[3] = 0
        client.send_current()
finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
