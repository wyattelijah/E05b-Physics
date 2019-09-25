# E05b-Physics
Exploring 2D physics and collisions

In *main1.py*, you will need to apply gravity to the balls on the screen. To do so, you will need to find an appropriate gravity constant and assign GRAVITY to that number (line 17). Because of the way the Y axis works in Python Arcade, GRAVITY will need to be a negative number for the balls to fall.

You will then need to accelerate the balls according to the GRAVITY constant. You can call b.accelerate(x,y) on line 67. In the case of applying gravity, x will be 0 and y will be GRAVITY.

*main2.py*, is a little more complicated. You will need to apply all the lessons you learned in main1.py, but now we want the balls to bounce off the walls. First apply the GRAVITY constant from main1.py and accelerate the balls. Then, lines 39, 45, 51, and 57 will ask you to bounce (reverse the velocity) of the ball when it hits a wall. Think about what we discussed in class. I am applying some friction so they don't bounce forever.

*main3.py* implements the worst, most-naive version of collision physics using the built-in sprite collision detection. Assuming all the animal heads have the same mass, adjust lines 53–60 to make the collisions more realistic.

