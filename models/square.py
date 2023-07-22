from models.shape import Shape


class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)
