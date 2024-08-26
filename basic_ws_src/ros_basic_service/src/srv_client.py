#!/usr/bin/env python

import rospy

from ros_basic_service.srv import WordCount

import sys


rospy.init_node('srv_client')

#TODO
rospy.wait_for_service('word_count')

word_counter = rospy.ServiceProxy('word_count', WordCount)

words = ' '.join(sys.argv[1:])

word_count = word_counter(words)

print words, '->', word_count.count

