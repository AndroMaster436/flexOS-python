import tkinter as tk
from PIL import Image, ImageTk

def init_desktop():
    root = tk.Tk()
    root.title("flexOS Desktop")
    root.attributes("-fullscreen", True)
    background = ImageTk.PhotoImage(Image.open("Assets/background.png"))
    label = tk.Label(root, image=background)
    label.place(relwidth=1, relheight=1)
    taskbar = tk.Frame(root, bg="lightgray", height=40)
    taskbar.pack(side="bottom", fill="x")
    start_button = tk.Button(taskbar, text="Пуск")
    start_button.pack(side="left", padx=10)
    root.mainloop()