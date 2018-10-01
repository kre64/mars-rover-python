class Rover:
    def __init__(self, p, d):
        self.position = p
        self.direction = d

    def get_position(self):
        return self.position

    def execute(self, commands):
        print("implement me!")
