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
        # how to optimize?
        print('(', self.position.x, ',', self.position.y, ')', sep='')
        if command == 'f':
            if self.direction == 'N':
                self.position.y += 1
            elif self.direction == 'E':
                self.position.x += 1
            elif self.direction == 'S':
                self.position.y -= 1
            elif self.direction == 'W':
                self.position.x -= 1
        elif command == 'b':
            if self.direction == 'N':
                self.position.y -= 1
            elif self.direction == 'E':
                self.position.x -= 1
            elif self.direction == 'S':
                self.position.y += 1
            elif self.direction == 'W':
                self.position.x += 1
        print("->", '(', self.position.x, ',', self.position.y, ')', sep='')

    def execute(self, commands):
        # can I make this any better?
        for command in commands:
            if command == 'l' or command == 'r':
                self.update_direction(command)
            elif command == 'f' or 'b':
                self.update_position(command)
            else:
                print("Invalid command.")
