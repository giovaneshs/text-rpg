import curses
from Game import Game
from curses import wrapper
import sys
#14, 57 meio da tela

def main(stdscr):
    
    stdscr.clear()
    stdscr.border()
    

    title_win = curses.newwin(10, 70, 2, 26)
    startMenu_win = curses.newwin(7, 11, 17, 53)
    stdscr.refresh()

    title_win.addstr(1,1, "      ██     ▀███▄   ▀███▀ ▄▄█▀▀██▄ ▀████▄     ▄███▀████▀███▀▀▀███ ")
    title_win.addstr(2,1, "     ▄██▄      ███▄    █ ▄██▀    ▀██▄ ████    ████   ██   ██    ▀█ ")
    title_win.addstr(3,1, "    ▄█▀██▄     █ ███   █ ██▀      ▀██ █ ██   ▄█ ██   ██   ██   █  ")
    title_win.addstr(4,1, "   ▄█  ▀██     █  ▀██▄ █ ██        ██ █  ██  █▀ ██   ██   ██████  ")
    title_win.addstr(5,1, "   ████████    █   ▀██▄█ ██▄      ▄██ █  ██▄█▀  ██   ██   ██   █  ▄")
    title_win.addstr(6,1, "  █▀      ██   █     ███ ▀██▄    ▄██▀ █  ▀██▀   ██   ██   ██     ▄█")
    title_win.addstr(7,1, "▄███▄   ▄████▄███▄    ██   ▀▀████▀▀ ▄███▄ ▀▀  ▄████▄████▄██████████")
    title_win.refresh()

    startMenu_win.clear()
    startMenu_win.border()
    startMenu_win.addstr(2, 1, "  JOGAR  ", curses.A_STANDOUT)
    startMenu_win.addstr(4, 1, "  SAIR   ", curses.A_BOLD)
    startMenu_win.refresh()
    
    option = 1
    while True:
        key = stdscr.getkey()
        
        match key.upper():
            case "KEY_DOWN":
                option = 2
                startMenu_win.clear()
                startMenu_win.border()
                startMenu_win.addstr(2, 1, "  JOGAR  ", curses.A_BOLD)
                startMenu_win.addstr(4, 1, "  SAIR   ", curses.A_STANDOUT)
                startMenu_win.refresh()

            case "KEY_UP":
                option = 1
                startMenu_win.clear()
                startMenu_win.border()
                startMenu_win.addstr(2, 1, "  JOGAR  ", curses.A_STANDOUT)
                startMenu_win.addstr(4, 1, "  SAIR   ", curses.A_BOLD)
                startMenu_win.refresh()

            case "E":
                if option == 2:
                    sys.exit()
                    
                elif option == 1:
                    Game(stdscr)
                    stdscr.addstr("só tem até aqui kkkkkkk, aperta qualquer coisa pra sair")
                    stdscr.getch()
                    break    

wrapper(main)