#!/usr/bin/env python

import rospy
from ros_basic_topicmsg.msg import Infodata
from random import random

rospy.init_node('info_publisher')
pub = rospy.Publisher('infodata', Infodata, queue_size=10)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    msg = Infodata()
    msg.id_num = random()
    msg.account = random()
    pub.publish(msg)
    rate.sleep()
