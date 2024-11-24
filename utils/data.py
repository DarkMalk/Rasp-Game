from random import randrange

class Data:
    def __init__(self):
        self.data = [[], [], []]
        self.awards = [100, 200, 300]

        # Inicializar datos en "data"
        self.__load_data()

    def __load_data(self):
        for index, _ in enumerate(self.data):
            for _ in range(3):
                self.data[index].append(self.generate_random_number())

    def generate_random_number(self):
        return randrange(1, 7)
