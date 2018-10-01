from position import Position
from direction import Direction


class Rover:
    def __init__(self, Position, Direction):
        self.position = Position
        self.direction = Direction

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def update_direction(self, command):
        self.direction = Direction.turn(self.direction, command)
        return True

    def update_position(self, command):
        # finish this
        return True

    def execute(self, commands):
        # can I make this any better?
        for command in commands:
            if command == 'l' or 'r':
                self.update_direction(command)
            elif command == 'f' or 'b':
                self.update_direction(command)
            else:
                print("Invalid command.")
