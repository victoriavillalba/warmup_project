#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


class FollowPerson(object):
    def __init__(self):
        rospy.init_node("follow_wall")

        rospy.Subscriber("/scan",LaserScan,self.process_scan)

        self.twist_pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)

        lin = Vector3()
        ang = Vector3()
        self.twist = Twist(linear=lin,angular=ang)

    def process_scan(self,data):
        # checking where the closest object is
        closest = data.ranges[0]
        index = 0
        for i in range(len(data.ranges)):
            if closest > data.ranges[i]:
                closest = data.ranges[i]
                index = i
        # turn if the closest object isn't in front of the robot
        if data.ranges[0] < 3.5:
            if data.ranges[0] > 1:
                self.twist.angular.z = 0
                self.twist.linear.x = 0.5
            else:
                self.twist.linear.x = 0
                self.twist.angular.z = 0
        else:
            self.twist.linear.x = 0
            if index < 10:
                self.twist.linear.x = 0.05
                self.twist.angular.z = (1.570796326794897/8)
            elif index < 179:
                self.twist.angular.z = (1.570796326794897/2)
            elif index < 350:
                self.twist.angular.z = -(1.570796326794897/2)
            else:
                self.twist.linear.x = 0.05
                self.twist.angular.z = -(1.570796326794897/8)
        self.twist_pub.publish(self.twist)



    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = FollowPerson()
    node.run()
