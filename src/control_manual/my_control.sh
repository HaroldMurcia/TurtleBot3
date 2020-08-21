#!/bin/bash
# -*- ENCODING: UTF-8 -*-

echo "Configaron mi control"

sudo chmod a+rw /dev/input/js3
echo "2"
rosparam set joy_node/dev "/dev/input/js3"
rosrun joy joy_node
