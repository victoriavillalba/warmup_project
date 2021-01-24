#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

#global atWall
#atWall = 0

class FollowWall(object):
    def __init__(self):
        rospy.init_node("follow_wall")

        rospy.Subscriber("/scan",LaserScan,self.process_scan)

        self.twist_pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)

        lin = Vector3()
        ang = Vector3()
        self.twist = Twist(linear=lin,angular=ang)

    def process_scan(self,data):
        # imitating stop_at_wall exercise to approach wall before following it
        turning = 0
        if data.ranges[0] > 0.5:
            self.twist.angular.z = 0
            self.twist.linear.x = 0.5
        else:
            self.twist.linear.x = 0
            self.twist.angular.z = (1.570796326794897/2)
            turning = 1
        self.twist_pub.publish(self.twist)



    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = FollowWall()
    node.run()
