class Button:
    def __init__(self, x: int, y: int, title: str):
        self.x = x
        self.y = y
        self.title = title
        self.appearance = True 
    def hide(self):
        self.appearance = False
    def show(self):
        self.appearance = True
    def print_status(self):
        print(f'Дані про віджет\n{self.title} {self.x} {self.y} {self.appearance}')
    