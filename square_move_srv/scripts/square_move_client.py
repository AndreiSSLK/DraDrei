#!/usr/bin/env python
import rospy
from square_move_srv.srv import SquareMove, SquareMoveRequest

rospy.init_node('square_move_client')
rospy.wait_for_service('move_square')

try:
    move_square = rospy.ServiceProxy('move_square', SquareMove)
    req = SquareMoveRequest(side=1.0, repetitions=2)
    res = move_square(req)
    rospy.loginfo("success", res.success)
except rospy.ServiceException as e:
    rospy.logerr("call failed: %s", e)

