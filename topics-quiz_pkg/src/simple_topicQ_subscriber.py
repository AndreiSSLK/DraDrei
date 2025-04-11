#! /usr/bin/env python

import rospy
from std_msgs.msg import float32

def callback(mag):
	print (msg.data)

rospy.init_node('topicQ_subscriber')
sub = rospy.Subscriber('/scan', LaserScan, callback)


rospy.spin()
