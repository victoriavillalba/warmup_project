#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from std_msgs.msg import Header
from geometry_msgs.msg import Point


class MoveSquare(object):
    def __init__(self):
        rospy.init_node("move in a square")

        rospy.Subscriber("/scan",LaserScan,self.process_scan)

        self.twist_pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)

        lin = Vector3()
        ang = Vector3()
        self.twist = Twist(linear=lin,angular=ang)

    def proces_scan(self,data):
        if data.ranges[0] >= distance:
            self.twist.linear.x = 0.1
        else:
            self.twist.linear.x = 0

        self.twist_pub.publish(self.twist)
        

    def run(self):
        rospy.spin()


if __name__ == '__main__':
    node = MoveSquare()
    node.run()

