"""
Question 021 - Level 03
A robot moves in a plane starting from the original point (0,0). The robot can move toward Up, DOWN, LEFT and RIGHT
with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a
sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example: If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
--- Nguyen Van Duc ---
"""

import math

pos = [0, 0]
while True:
    s = input("Enter direction and steps: ")
    if not s:
        break
    movement = s.split(" ")
    if movement[0].upper() == "UP":
        pos[1] += int(movement[1])
    elif movement[0].upper() == "DOWN":
        pos[1] -= int(movement[1])
    elif movement[0].upper() == "LEFT":
        pos[0] -= int(movement[1])
    elif movement[0].upper() == "RIGHT":
        pos[0] += int(movement[1])
    else:
        pass

print(int(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2))))
