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
        time = rospy.get_time()
        print("moving")
        self.twist.linear.x = 0.1
#        self.twist = Twist(linear=Vector3(1,0,0),angular=Vector3(0,0,0))
        while rospy.get_time() < (time + 5.0):
            continue
        time = rospy.get_time()
        print("turning")
        self.twist.linear.x = 0
        self.twist.angular.z = (1.570796326794897/2)
#        self.twist = Twist(linear=Vector3(0,0,0),angular=Vector3(0,0,(1.570796326794897/2)))
        while rospy.get_time() < (time + 1.0):
            continue
        time = rospy.get_time()
        print("moving")
        self.twist.linear.y = 0.1
        self.twist.angular.z= 0
#        self.twist = Twist(linear=Vector3(0,1,0),angular=Vector3(0,0,0))
        while rospy.get_time() < (time + 5.0):
            continue
        time = rospy.get_time()
        print("turning")
        self.twist.linear.y = 0
        self.twist.angular.z = (1.570796326794897/2)
#        self.twist = Twist(linear=Vector3(0,0,0),angular=Vector3(0,0,(1.570796326794897/2)))
        while rospy.get_time() < (time + 1.0):
            continue
        time = rospy.get_time()
        print("moving")
        self.twist.linear.x = -0.1
        self.twist.angular.z = 0
#        self.twist = Twist(linear=Vector3(0,1,0),angular=Vector3(0,0,0))
        while rospy.get_time() < (time + 5.0):
            continue
        time = rospy.get_time()
        print("turning")
        self.twist.linear.x = 0
        self.twist.angular.z = (1.570796326794897/2)
#        self.twist = Twist(linear=Vector3(0,0,0),angular=Vector3(0,0,(1.570796326794897/2)))
        while rospy.get_time() < (time + 1.0):
            continue
        time = rospy.get_time()
        print("moving")
        self.twist.linear.y = -0.1
        self.twist.angular.z = 0
#        self.twist = Twist(linear=Vector3(0,1,0),angular=Vector3(0,0,0))
        while rospy.get_time() < (time + 5.0):
            continue
        self.twist = Twist(linear=Vector3(0,0,0),angular=Vector3(0,0,0))
        print("stopped")
#                if (i%2 == 0):
 #                   lin = Vector3(1,0,0)
  #                  ang = Vector3(0,0,0)
   #             else:
    #                lin = Vector3(1,0,0)
     #           ang = Vector3(0,0,0)
      #          self.twist = Twist(linear=lin,angular=ang)
       #     time = rospy.get_time()
        #    print("turning")
         #   while rospy.get_time() < (time + 1.0):
          #      lin = Vector3(0,0,0)
           #     ang = Vector3(0,0,(1.570796326794897/2))
            #    self.twist = Twist(linear=lin,angular=ang)
#            i = i + 1
 #       lin = Vector3(0,0,0)
  #      ang = Vector3(0,0,0)
   #     self.twist = Twist(linear=lin,angular=ang)

        self.twist_pub.publish(self.twist)
        

    def run(self):
        rospy.spin()


if __name__ == '__main__':
    node = MoveSquare()
    node.run()

