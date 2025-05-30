#!/usr/bin/env python
import rospy
from square_move_srv.srv import SquareMove, SquareMoveResponse
from geometry_msgs.msg import Twist
import time

def handle_square_move(req):
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    move_cmd = Twist()

    for i in range(req.repetitions):
        for _ in range(4):
            move_cmd.linear.x = 0.2
            move_cmd.angular.z = 0.0
            pub.publish(move_cmd)
            rospy.sleep(req.side / 0.2)  

            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.5
            pub.publish(move_cmd)
            rospy.sleep(3.2) 

    move_cmd.linear.x = 0.0
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)
    return SquareMoveResponse(success=True)

if __name__ == "__main__":
    rospy.init_node('square_move_server')
    s = rospy.Service('move_square', SquareMove, handle_square_move)
    rospy.loginfo("ready.")
    rospy.spin()

