import tkinter as tk


class SecondaryWindow:
    def __init__(self, count_award, reference_root_window):
        self.award = count_award
        self.root_window = reference_root_window
        self.secondary_window = tk.Toplevel()

        self.__config()
        self.__center_window()
        self.__widgets()

    def __widgets(self):
        label = tk.Label(
            self.secondary_window, text=f"Haz ganado ${self.award}", font=("", 20)
        )
        label.grid(row=0, column=0)

        if self.award == 0:
            tk.Label(
                self.secondary_window,
                text="Oh! no haz ganado nada, suerte para la proxima!!",
            ).grid(row=1, column=0, padx=4, pady=2)

        btn = tk.Button(self.secondary_window, text="Cerrar", command=self.__close_window)
        btn.grid(row=2, column=0)

    def __close_window(self):
        self.secondary_window.destroy()
        self.root_window.destroy()

    def __config(self):
        self.secondary_window.title("Verificando Premios")
        self.secondary_window.resizable(width=False, height=False)

    def __center_window(self):
        window_width = self.secondary_window.winfo_width()
        window_height = self.secondary_window.winfo_height()
        screen_width = self.secondary_window.winfo_screenwidth()
        screen_height = self.secondary_window.winfo_screenheight()

        x = (screen_width - window_width) // 3
        y = (screen_height - window_height) // 3

        self.secondary_window.geometry(f"+{x}+{y}")
