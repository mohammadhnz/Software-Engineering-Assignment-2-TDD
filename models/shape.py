class Shape:
    def __init__(self, height, width):
        if not (isinstance(height, int) or isinstance(height, float)):
            raise TypeError("Height must be numeric")
        if not (isinstance(width, int) or isinstance(width, float)):
            raise TypeError("Width must be numeric")
        if height < 0 or width < 0:
            raise ValueError("Width and Height must be positive")

        self.height = height
        self.width = width

    def compute_area(self):
        return self.height * self.width
