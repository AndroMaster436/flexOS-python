import curses
from pages.location import page as pg

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
    Лицензионное соглашение

    Настоящее соглашение (далее – "Соглашение") является юридическим документом 
    между вами и создателями flexOS.

    1. Лицензия
    Вы получаете ограниченную, неисключительную лицензию на использование
    flexOS на ваших устройствах.

    2. Интеллектуальная собственность
    Все права на flexOS остаются за разработчиками.

    3. Отказ от ответственности
    flexOS предоставляется "как есть".
    Разработчик не несет ответственностиза убытки.

    4. Изменения
    Разработчик может вносить изменения в Соглашение.
    Использование flexOS после изменений означает ваше согласие.

    Если вы не согласны с условиями, не устанавливайте flexOS.
        """
        stdscr.addstr(4, 2, control_text, curses.color_pair(1))

        stdscr.hline(height - 3, 2, curses.ACS_HLINE, width - 4)

        keys_text = "F3: Выход  |  Enter: Принять"
        x_keys = (width // 2) - (len(keys_text) // 2)
        stdscr.addstr(height - 2, x_keys, keys_text, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getch()

        if key in (curses.KEY_ENTER, 10):
            curses.wrapper(pg)
        elif key == curses.KEY_F3:
            exit()