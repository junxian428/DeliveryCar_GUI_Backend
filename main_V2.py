#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32, Float32

# Define the ROS node
rospy.init_node('publisher_node')

# Define the publisher objects for each topic
int_pub1 = rospy.Publisher('int_topic_1', Int32, queue_size=10)
int_pub2 = rospy.Publisher('int_topic_2', Int32, queue_size=10)
float_pub1 = rospy.Publisher('float_topic_1', Float32, queue_size=10)
float_pub2 = rospy.Publisher('float_topic_2', Float32, queue_size=10)
float_pub3 = rospy.Publisher('float_topic_3', Float32, queue_size=10)

# Define the loop rate (in Hz)
rate = rospy.Rate(10) # 10 Hz

while not rospy.is_shutdown():
    # Publish a message to each topic
    int_pub1.publish(42)
    int_pub2.publish(99)
    float_pub1.publish(3.14)
    float_pub2.publish(2.718)
    float_pub3.publish(1.618)

    # Sleep for the remainder of the loop rate period
    rate.sleep()