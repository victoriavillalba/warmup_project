#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from std_msgs.msg import Header
from geometry_msgs.msg import Point


class MoveSquare(object):
    def __init__(self):
        rospy.init_node("move_in_a_square")

        rospy.Subscriber("/scan",LaserScan,self.process_scan)

        self.twist_pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)

        lin = Vector3(0,0,0)
        ang = Vector3(0,0,0)
        self.twist = Twist(linear=lin,angular=ang)

    def process_scan(self,data):

        i = 0
        while i < 4:
            time = rospy.get_time()
#            my_header = Header(stamp=rospy.Time.now())
            while rospy.get_time() < (time + 5.0):
                if (i%2 == 0):
                    lin = Vector3(0.1,0,0)
                    ang = Vector3(z=0)
                else:
                    lin = Vector3(0,0.1,0)
                ang = Vector3(0,0,0)
                Twist(linear=lin,angular=ang)
            time = rospy.get_time()
#            my_header = Header(stamp=rospy.Time.now())
            while rospy.get_time() < (time + 1.0):
                lin = Vector3(0,0,0)
                ang = Vector3(0,0,(1.570796326794897/2))
                Twist(linear=lin,angular=ang)
            i = i + 1
        lin = Vector3(0,0,0)
        ang = Vector3(0,0,0)
        Twist(linear=lin,angular=ang)

        self.twist_pub.publish(self.twist)
        

    def run(self):
        rospy.spin()


if __name__ == '__main__':
    node = MoveSquare()
    node.run()

