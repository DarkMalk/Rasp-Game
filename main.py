from utils import Window, Data, Images
from secondary_window import SecondaryWindow

from functools import partial
from os import getcwd
import tkinter as tk


class Rasp(Window, Data, Images):
    def __init__(self):
        Window.__init__(self, "Game Rasp")
        Data.__init__(self)
        Images.__init__(self, f"{getcwd()}/assets")
        # Inicialización
        self.rasped_cells = [set(), set(), set()]

        # Configuración y acciones
        self.__widgets()

    def __widgets(self):
        for row, _ in enumerate(self.data):
            label_award = tk.Label(self.window, text=f"Premio: ${self.awards[row]}")
            label_award.grid(row=row, column=3)

            for col, _ in enumerate(self.data[row]):
                canva = tk.Canvas(
                    self.window, width=self.size_cell[0], height=self.size_cell[1]
                )
                canva.grid(column=col, row=row)
                canva.create_rectangle(
                    0, 0, self.size_cell[0], self.size_cell[1], fill="white", outline="black", tags="text"
                )
                value = self.data[row][col]

                x_center = self.size_cell[0] // 2
                y_center = self.size_cell[1] // 2
                canva.create_text(
                    x_center, y_center, text=value, font=("TkDefaultFont", 24), fill="black", tags="text"
                )

                canva.create_image(0, 0, anchor=tk.NW, image=self.image_rasp_tk, tags="layer_rasp")

                self.__events(canva, (row, col))

    def __check_win(self):
        count_award = 0
        for x, _ in enumerate(self.rasped_cells):
            if len(self.rasped_cells[x]) != 3:
                return

            if len(set(self.data[x])) == 1:
                count_award += self.awards[x]

        SecondaryWindow(count_award, self.window)

    def __rasp(self, _, element, pos):
        if (pos[0], pos[1]) not in self.rasped_cells:
            self.rasped_cells[pos[0]].add(pos[1])

        element.itemconfig("layer_rasp", state="hidden")
        self.__check_win()

    def __events(self, element, pos):
        element.bind("<Button-1>", partial(self.__rasp, element=element, pos=pos))


if __name__ == "__main__":
    Rasp().run()
