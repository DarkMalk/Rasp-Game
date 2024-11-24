from tkinter import Tk

class Window:
    def __init__(self, name):
        self.window = Tk()
        self.__name = name
        self.window.geometry("")

        self.__center_window()
        self.config_window()

    def config_window(self):
        self.window.title(self.__name)
        self.window.wm_resizable(width=False, height=False)

    def __center_window(self):
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width - window_width) // 3
        y = (screen_height - window_height) // 3

        self.window.geometry(f"+{x}+{y}")

    def run(self):
        self.window.mainloop()
