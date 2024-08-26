#!/usr/bin/env python

import rospy

from ros_basic_service.srv import WordCount,WordCountResponse


def count_words(request):
    return WordCountResponse(len(request.words.split()))


rospy.init_node('srv_server')

#TODO
service = rospy.Service('word_count', WordCount, count_words)

rospy.spin()

