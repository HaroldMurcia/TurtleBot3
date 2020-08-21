#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:51:08 2020

@author: www.haroldmurcia.com
"""

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy


def callback(data):
    # Charectization GamePad Logitech F710
    # READ BUTTONS
    A=data.buttons[0]
    B=data.buttons[1]
    X=data.buttons[2]
    Y=data.buttons[3]
    LB=data.buttons[4]
    RB=data.buttons[5]
    BACK=data.buttons[6]
    START=data.buttons[7]
    LOGITECH=data.buttons[8]
    ANALOG_L=data.buttons[9]
    ANALOG_R=data.buttons[10]
    # READ Axes
    LEFT_ANALOG_HOR=data.axes[0] # <<(+)
    LEFT_ANALOG_VER=data.axes[1] # ^^(+)
    LT=data.axes[2] #[1 -1]
    RIGHT_ANALOG_HOR=data.axes[3] # <<(+)
    RIGHT_ANALOG_VER=data.axes[4] # ^^(+)
    RT=data.axes[5] #[1 -1]
    LEFT_RIGHT = data.axes[6] # left=1, right=-1
    FRONT_BACK = data.axes[7] # front=1, back=-1
    rospy.loginfo(LEFT_ANALOG_HOR)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('joy', Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
