#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    print msg.data

#TODO
rospy.init_node('rostopic_sub')
sub = rospy.Subscriber('counter', Int32, callback)

rospy.spin()
