class Direction:
    # Never Eat Sour Watermelons
    N = 'N'
    E = 'E'
    S = 'S'
    W = 'W'

    def turn(direction, command):
        directions = "NESW"
        for d in directions:
            if d == direction:
                # clean this up eventually
                if command == 'l':
                    offset = directions.find(d) - 1
                    new_direction = directions[offset % len(directions)]
                    print("\nRover turned LEFT from", d, '\n', new_direction, "<-", d)
                elif command == 'r':
                    offset = directions.find(d) + 1
                    new_direction = directions[offset % len(directions)]
                    print("\nRover turned RIGHT from", d, '\n', d, "->", new_direction)
                else:
                    print("Something is wrong.")
                return new_direction

    def __init__(self):
        print("implement")
