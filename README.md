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
is, in this case, 0.5 meters. 
The class FollowWall has an init function that initializes everything, the
subscriber, publisher, and Twist stuff. The process_scan function is called by the
subscriber to determine if it's distance from the wall calls for an angular velocity
or linear velocity. The run function calls rospy.spin(), and the last function
initiates the whole thing to make sure it is run.
The only problem I see is that the noise makes the robot go straight at first, then
move at an angle.

![gif](wall_follower.gif)
