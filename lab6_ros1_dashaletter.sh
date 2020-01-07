    rosservice call /reset
    rosservice call /kill turtle1

    #2
     rosservice call /spawn 0.2 7.0 0.7 turtle2

     rostopic pub -1 /turtle2/cmd_vel geometry_msgs/Twist -- '[2.5, 0.0, 0.0]' '[0.0, 0.0, -3]'
     rostopic pub -1 /turtle2/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
     rostopic pub -1 /turtle2/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 2.3]'
     rostopic pub -1 /turtle2/cmd_vel geometry_msgs/Twist -- '[1.5, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
     rosservice call /kill turtle2

    #4
     rosservice call /spawn 3.0 4.3 0.0 turtle4

     rostopic pub -1 /turtle4/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.57]'
     rostopic pub -1 /turtle4/cmd_vel geometry_msgs/Twist -- '[2.7, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
     rostopic pub -1 /turtle4/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 2.4]'
     rostopic pub -1 /turtle4/cmd_vel geometry_msgs/Twist -- '[1.7, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
     rostopic pub -1 /turtle4/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 2.4]'
     rostopic pub -1 /turtle4/cmd_vel geometry_msgs/Twist -- '[1.5, 0.0, 0.0]' '[0.0, 0.0, 0.0]'

     rosservice call /kill turtle4

   #3
    rosservice call /spawn 3.3 7.0 0.79 turtle3

    rostopic pub -1 /turtle3/cmd_vel geometry_msgs/Twist -- '[2.5, 0.0, 0.0]' '[0.0, 0.0, -3.5]'
    rostopic pub -1 /turtle3/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 2.5]'
    rostopic pub -1 /turtle3/cmd_vel geometry_msgs/Twist -- '[2.8, 0.0, 0.0]' '[0.0, 0.0, -3.5]'

    rosservice call /kill turtle3

   #9
    rosservice call /spawn 5.3 7.0 0.79 turtle9

    rostopic pub -1 /turtle9/cmd_vel geometry_msgs/Twist -- '[7.0, 0.0, 0.0]' '[0.0, 0.0, -8.6]'
    rostopic pub -1 /turtle9/cmd_vel geometry_msgs/Twist -- '[1.5, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
    rostopic pub -1 /turtle9/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -3.14]'

    rosservice call /kill turtle9

   #5
    rosservice call /spawn 8.5 7.0 3.14 turtle5

    rostopic pub -1 /turtle5/cmd_vel geometry_msgs/Twist -- '[1.5, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
    rostopic pub -1 /turtle5/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.57]'
    rostopic pub -1 /turtle5/cmd_vel geometry_msgs/Twist -- '[0.7, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
    rostopic pub -1 /turtle5/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.9]'
    rostopic pub -1 /turtle5/cmd_vel geometry_msgs/Twist -- '[3.5, 0.0, 0.0]' '[0.0, 0.0, -3.5]'

    rosservice call /kill turtle5

   #6
   rosservice call /spawn 10.0 6.0 0.79 turtle6

   rostopic pub -1 /turtle6/cmd_vel geometry_msgs/Twist -- '[1.5, 0.0, 0.0]' '[0.0, 0.0, 3.14]'
   rostopic pub -1 /turtle6/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 0.7]'
   rostopic pub -1 /turtle6/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
   rostopic pub -1 /turtle6/cmd_vel geometry_msgs/Twist -- '[4.0, 0.0, 0.0]' '[0.0, 0.0, 8.6]'

   rosservice call /kill turtle6

