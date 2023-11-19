import curses
import time

def Game(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.refresh()

    time.sleep(1)
    stdscr.addstr(10, 25, "             ▄▄                   ")
    stdscr.addstr(11, 25, "▀███▀▀▀██▄   ██                   ")
    stdscr.addstr(12, 25, "  ██    ▀██▄                 ▄▄▄  ")
    stdscr.addstr(13, 25, "  ██     ▀█████  ▄█▀██▄     ▀███  ")
    stdscr.addstr(14, 25, "  ██      ██ ██ ██   ██       ██  ")
    stdscr.addstr(15, 25, "  ██     ▄██ ██  ▄█████       ██  ")
    stdscr.addstr(16, 25, "  ██    ▄██▀ ██ ██   ██       ██  ")
    stdscr.addstr(17, 25, "▄████████▀ ▄████▄████▀██▄   ▄████▄")
    stdscr.refresh()
    
    time.sleep(2.5)
    stdscr.clear()
    stdscr.border()
    stdscr.refresh()