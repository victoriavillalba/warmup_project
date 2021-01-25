# warmup_project
## Driving in a Square
The problem is to make the robot drive for eaual lengths, and stop to turn 90 degrees 
between each length. In order to do this, I set up a class called MosSquare. 
In this class, I initialized a self.twist and a publisher for "/cmd_vel" using Twist.
Anothr functon in the class is process_square, which carries at the movements the robot
should follow and publishes them. Then, there's a run function thhat keeps a flow
of messages while the program runs.
The class is called by main and the program continues running until I press Cntrl+C.
My approach was to first write out the code from office hours for Problem 2 
and determine what I need to remove, keep, or change. I took out the subscriber since
it doesn't even need to take in data, completely changed the process_scan() code 
to imitate the movements of a square. In that function, I learned that the movements 
must be published every time it has been changed. I also changed the run function to
have a while loop to send messages while the program isn't shutdown. My main problem 
had been from keeping the subscriber line for so long when it wasn't necessary. 
It was preventing my robot from following all the instructions. After removing it,
my next problem was trying to get the robot to move at all.
Turns out! Since nothing was calling my process_square function (because of lack of subscriber),
it just wasn't doing anything. So I put it all in the run function and it's fine now!

![gif](drive_square.gif) 

## Wall Follower
The goal of this part of the project was to get a robot to approach a wall and follow
it around the whole room indefinitely. At first, I applied the stop_at_wall code to
set up a similar foundation and then add the extra steps. Then, I made the whole
thing spaz for hours after a bunch of experimenting because the callback function
can't handle waiting for 2 seconds. I learned that the callback function is
constantly being called, without regard of the previous call being completed or not.
So, what I ended up doing is letting the code decide if it's done turning by changing
the linear and angular velocity when the path in front of it is cleared by at least
the amount of distance the robot wants to keep between itself and the wall, which
is, in this case, 0.5 meters. Another requirement, which the picture on the warmup
project page inspired me to include, is that the distance of the wall to the right
of the robot has to be smaller than the distance of the robot ot the wall at an angle
between its right and front sides.
The class FollowWall has an init function that initializes everything, the
subscriber, publisher, and Twist stuff. The process_scan function is called by the
subscriber to determine if it's distance from the wall calls for an angular velocity
or linear velocity. The run function calls rospy.spin(), and the last function
initiates the whole thing to make sure it is run.
The only problem I see is that the noise makes the robot go straight at first, then
move at an angle.

![gif](wall_follower.gif)

## Person Follower
The goal of the part of the project is to get the robot to follow the object closest
to itself. My approach was, at first, to find the angle with the shortest possible
distance, bu that would make it spin forever until it finally hit that one specific
angle. Then I realized that most values would be inf. So i tried to do an if
statement to see if it was inf or not, but I didn't know it's data type and 
interpreting it as a string wasn't working. Then I realized that any non-inf value
would have to be less than 3.5 meters, so I made that my condition for the if 
statement. I also made it more specific so that it would look less robotic when
the robot was serching for the object. So if the object was within 10 degrees
of the closest distance, it would slow down the rotaation so it can't rotate past
the object, and start moving linearly, too. It would also start rotating right or
left depending on which side the object was on relative to the robot.
I made a FollowPerson class with an init function that establishes the subscriber,
publisher, and twist. There's also the process_scan function that carries out the
code that looks for and follows the person, and then the run function that does
rospy.spin(). And lastly, the main function that gets the whole class to run.

![gif](person_follower.gif)

Challenges:
The biggest challenges were figuring out the difference between code when subscriber
is used and when it isn't, figuring out how to manipulate the data.ranges info, 
and figuring out what can and can't be used in a callback function that might screw
things over. The subscriber issue was carified to me after a lot of studying and 
comparing code, along with consultation to figure out what really happens behind
the scenes. Figuring out how to manipulate the data.ranges information took a lot
of trial and error and avoiding directly referencing the INF values. Figuring out
which statements can be used in callback functions also took a lot of trial and
error, manipulating, and rewording my code. In the end, I just tried to make the
code as simple as possible and make the most concise changes in increments.

Future work:
I would improve my robot behaviors by making them act more smoothly, or more like
they know what they'redoing. Almost as if  they're "smart" or something. Like 
with the person follower, I made it change angular speed and linear speed based
on where it was compared to the object. If I could do that but add more, I would
make its movements more fluid. I would also try to fix my code to make it more
concise and easier to follow.

Takeaways:
1. Avoid using while/for loops. That clogged up the messages and made everything
	spaz. You should never assume that one message is waiting for another,
	but that it's a constant stream of messages.
2. Don't overthink it, it's probably better to start with something familiar and
	then work your way up to the goal in small steps. I just came up with
	one idea, wrote it up, then wondered why nothing was working after so
	many lines of code and so much time wasted. It usually even ends up
	being simpler than you expected it to be.
