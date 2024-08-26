#!/usr/bin/env python

import rospy

from ros_basic_topicmsg.msg import Infodata  
                                  
def callback(msg):
    print 'id_num:', msg.id_num
    print 'account:', msg.account
    print

rospy.init_node('info_subscriber')

sub = rospy.Subscriber('infodata', Infodata, callback)

rospy.spin()

