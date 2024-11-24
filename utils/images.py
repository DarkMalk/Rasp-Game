from PIL import Image, ImageTk

class Images:
    def __init__(self, path_images):
        self.size_cell = (200, 200)
        self.path_images = path_images
        self.image_rasp = None

        self.__load_images()

    def __load_images(self):
        self.image_rasp = Image.open(f"{self.path_images}/layer_rasp.png").resize(
            (self.size_cell[0], self.size_cell[1])
        )

        self.image_rasp_tk = ImageTk.PhotoImage(self.image_rasp)
