class Menu:
    def __init__(self, a, b, c, cycles):
        self.aquaris = Aquaris()
        self.a = a
        self.b = b
        self.c = c
        self.cycles = cycles
        self.non_first = false
    def start_square(self):
        self.aquaris.square(self.a, self.b, self.c, self.cycles, self.non_first)
    def start_beds(self):
        pass
    def continue_square(self):
        pass
    def continue_beds(self):
        pass