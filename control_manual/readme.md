# Control con gamePad
Este es un ejemplo de navegación utilizando un control [Logitech F710](https://www.logitechg.com/en-us/products/gamepads/f710-wireless-gamepad.html)

## ¿Cómo lanzar control manual?
* En una pestaña lanzar el roscore
```bat
roscore
```
* En otra pestaña lanzar el robot con el mundo gazebo
```bat
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```
* En otra pestaña lanzar el nodo para el gamepad [Joy](/http://wiki.ros.org/joy), teniendo en cuenta que "X" es un número que se puede detectar utilizando la isntrucción: ls /dev/input/
```bat
sudo chmod a+rw /dev/input/jsX
rosparam set joy_node/dev "/dev/input/jsX"
rosrun joy joy_node
```
* Opcional en otra pestaña lanzar el nodo del robot para rviz
```bat
roslaunch turtlebot3_fake turtlebot3_fake.launch
```
* Finalmente lanzar el nodo del game pad
```bat
rosrun control_manual gamePad_manual.py
```

## ¿Cómo lanzar mapeo manual?
* En una pestaña lanzar el roscore
```bat
roscore
```
* En otra pestaña lanzar el robot con el mundo gazebo
```bat
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```
* En otra pestaña lanzar el nodo para el gamepad [Joy](/http://wiki.ros.org/joy), teniendo en cuenta que "X" es un número que se puede detectar utilizando la isntrucción: ls /dev/input/
```bat
sudo chmod a+rw /dev/input/jsX
rosparam set joy_node/dev "/dev/input/jsX"
rosrun joy joy_node
```
* En una nueva pestaña lanzar el SLAM del turtlebot3
```bat
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```
* Finalmente lanzar el nodo del game pad
```bat
rosrun control_manual gamePad_manual.py
```
