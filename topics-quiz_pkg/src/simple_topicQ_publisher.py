#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
	rospy.init_node('topic_quiz')
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	front = scan.ranges[]
	left = scan.ranges[]
	right = scan.ranges[]

	cmd = Twist()

	if front < 1.0:
	   cmd.angular.z = 0.5
	elif right < 1.0:
	   cmd.angular.z = 0.5
	elif left < 1.0:
	   cmd.angular.z = -0.5
	else:
	   cmd.linear.x = 0.3

	pub.publish(cmd)

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
