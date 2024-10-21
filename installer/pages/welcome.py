import curses
from pages.eula import page as pg

def page(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    while True:
        height, width = stdscr.getmaxyx()

        stdscr.clear()
        stdscr.bkgd(' ', curses.color_pair(1))

        title = "Установка flexOS"
        x_title = (width // 2) - (len(title) // 2)
        stdscr.addstr(1, x_title, title, curses.color_pair(1))

        stdscr.hline(2, 2, curses.ACS_HLINE, width - 4)

        control_text = """
    Вас приветствует мастер установки flexOS
    Данный мастер поможет вам установить flexOS на ваш компьютео


    * Чтобы приступить к установке, нажмите Enter.

    * Чтобы выйти из мастера, не устанавливая flexOS, нажмите F3
        """
        stdscr.addstr(4, 2, control_text, curses.color_pair(1))

        stdscr.hline(height - 3, 2, curses.ACS_HLINE, width - 4)

        keys_text = "F3: Выход  |  Enter: Продолжить"
        x_keys = (width // 2) - (len(keys_text) // 2)
        stdscr.addstr(height - 2, x_keys, keys_text, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getch()

        if key in (curses.KEY_ENTER, 10):
            curses.wrapper(pg)
        elif key == curses.KEY_F3:
            exit()