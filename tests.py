import unittest

from rover import Rover
from position import Position
from direction import  Direction

class RoverTest(unittest.TestCase):

    def test_move_one_forward(self):
        direction = Direction.N
        position = Position(0,0)
        rover = Rover(position, direction)
        commands = ('f')
        rover.execute(commands)
        self.assertEquals(Position(-1, 0), rover.position())
        self.assertEquals(Direction.N, rover.direction())

    def test_move_one_forward_one_backward(self):
        direction = Direction.N
        position = Position(0,0)
        rover = Rover(position, direction)
        commands = ('f', 'b')
        rover.execute(commands)
        self.assertEquals(Position(0, 0), rover.position())
        self.assertEquals(Direction.N, rover.direction())

    def test_move_one_forward_two_backward_north(self):
        direction = Direction.N
        position = Position(0,0)
        rover = Rover(position, direction)
        commands = ('f', 'b', 'b')
        rover.execute(commands)
        self.assertEquals(Position(0, -1), rover.position())
        self.assertEquals(Direction.N, rover.direction())

    def test_move_one_forward_two_backward_turn_left(self):
        direction = Direction.N
        position = Position(0,0)
        rover = Rover(position, direction)
        commands = ('f', 'b', 'b', 'l')
        rover.execute(commands)
        self.assertEquals(Position(0, -1), rover.position())
        self.assertEquals(Direction.W, rover.direction())

    def test_turn_left_and_go_forward(self):
        direction = Direction.N
        position = Position(0,0)
        rover = Rover(position, direction)
        commands = ('l', 'f', 'f', 'f')
        rover.execute(commands)
        self.assertEquals(Position(-3, 0), rover.position())
        self.assertEquals(Direction.W, rover.direction())

    def test_turn_right_and_go_forward(self):
        direction = Direction.N
        position = Position(0,0)
        rover = Rover(position, direction)
        commands = ('r', 'f', 'f', 'f')
        rover.execute(commands)
        self.assertEquals(Position(0, 3), rover.position())
        self.assertEquals(Direction.E, rover.direction())

    def test_do_a_lot_of_silly_stuff(self):
        direction = Direction.S
        position = Position(0,0)
        rover = Rover(position, direction)
        commands = ('r', 'f', 'f', 'f', 'b', 'r')
        rover.execute(commands)
        self.assertEquals(Position(0, 2), rover.position())
        self.assertEquals(Direction.N, rover.direction())

if __name__ == '__main__':
    unittest.main()
