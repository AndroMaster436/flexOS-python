from Core import Display
import curses, time

def init(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    while True:
        stdscr.clear()
        stdscr.bkgd(' ', curses.color_pair(1))

        title = "Запуск flexOS..."
        frames = ["[                    ]", "[=                   ]", "[==                  ]", "[===                 ]", "[====                ]", "[=====               ]", "[======              ]", "[=======             ]", "[========            ]", "[=========           ]", "[==========          ]", "[===========         ]", "[============        ]", "[=============       ]", "[==============      ]", "[===============     ]", "[================    ]", "[=================   ]", "[==================  ]", "[=================== ]", "[====================]"]

        height, width = stdscr.getmaxyx()
        x_title = (width // 2) - (len(title) // 2)
        stdscr.addstr(height // 2 - 2, x_title, title, curses.color_pair(1))

        for frame in frames:
            x_frame = (width // 2) - (len(frame) // 2)
            stdscr.addstr(height // 2, x_frame, frame, curses.color_pair(1))
            stdscr.refresh()
            time.sleep(0.2)
        break

curses.wrapper(init)
Display.init_desktop()