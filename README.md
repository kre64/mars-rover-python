# mars-rover-python
## Challenge

You are on a team programming the remotely controlled Mars Rover robot.
Given an initial starting point (x,y), an initial direction the robot is facing, and a list of commands, you want to be able to calculate what the end point (x’, y’) will be.
The robot can move forward and backward, as well as turn left and right. Turning does not change the position of the rover, but the action must update the cardinal direction of the rover.

Using the test file as guidance, please develop a program that will calculate the final location of the rover after it has executed a list of commands.

### Available commands
"L" -> turn left

"R" -> turn right

"F" -> go forward

"B" -> go backward

Note: These are not simple Up, Down, Left, Right commands! In order to go up, the rover must face up (either by turning left or right, depending on its direction) and then execute a "F" command. Keep this in mind while designing tests. 

### Cardinal Directions
East

North

West

South

## To Execute tests

Run `python tests.py`


## Advanced Post Passing Tests Tasks

1. Imagine the grid is infinite -- if the rover receives an "F" command when it is facing right on the rightmost edge of the grid, the rover should appear on the leftmost edge of the grid in the same Y positon in the grid, still facing right. This "wrapping" should hold for all corners of the board. 

2. Implement a visualization that shows the user where they are at each stage of the string of commands. You have a lot of freedom here! You may start with printing positions to the command line, and ideally you will wire up a Flask app that gives users a frontend from the web!

## banana branch established
