#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

sides_ = {	# создаем словарь с исследуемыми сторонами
	'right': 0,
	'front': 0,
	'left': 0,
}

def laser(msg): # функция для определения минимального свободного пространства спереди, слева и справа
	global sides_ # разделив исследуемое пространство в 180 градусов на 100 частей(сенсоров), определяем минимальный искомый сектор
	sides_ = { # для каждой стороны сравниваем полученное минимальное значение с 4 и выбираем из них минимальное
		'right': min(min(msg.ranges[0:30]),4), 
		'front': min(min(msg.ranges[31:70]),4),
		'left': min(min(msg.ranges[71:99]),4),
	}

rospy.init_node('reading_laser') 
sub = rospy.Subscriber('/base_scan', LaserScan, laser)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

while not rospy.is_shutdown(): # пока нода жива
	msg = Twist()
	if sides_['front'] > 1.2: # если спереди больше 1.2
		err = -0.4 + sides_['left'] # держаться на расстоянии от левой стены
		msg.angular.z = err * 0.5
		msg.linear.x = 1
	elif sides_['right'] > sides_['left']: # если расстояние справа больше, чем слева, то поворот вправо
		msg.linear.x = 0
		msg.angular.z = -0.7
	elif sides_['right'] < sides_['left']: # если расстояние справа меньше, чем слева, то поворот влево
		msg.linear.x = 0
		msg.angular.z = 0.7
	else:				# если расстояние до стены спереди меньше, чем 1.2, а расстояние справа=слева, то небольшой поворот направо
		msg.linear.x = 0.2
		msg.angular.z = -0.4
	
	pub.publish(msg)
	
