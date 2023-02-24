from typing import Union

from fastapi import FastAPI
import os
import rospy
from std_msgs.msg import String, Int32, Float32, Bool, UInt8


rospy.init_node('publisher_node')

app = FastAPI()

# Define the publisher objects for each topic
int_pub1 = rospy.Publisher('int_topic_1', Int32, queue_size=10)
int_pub2 = rospy.Publisher('int_topic_2', Int32, queue_size=10)
float_pub1 = rospy.Publisher('float_topic_1', Float32, queue_size=10)
float_pub2 = rospy.Publisher('float_topic_2', Float32, queue_size=10)
float_pub3 = rospy.Publisher('float_topic_3', Float32, queue_size=10)
bool_pub = rospy.Publisher('bool_topic', Bool, queue_size=10)
uint8_pub = rospy.Publisher('uint8_topic', UInt8, queue_size=10)

rate = rospy.Rate(10) # 10 Hz


#@app.get("/")
#def read_root():
#    return {"Hello": "World"}
@app.get("/publisher1")
def publisher_1():
    int_pub1.publish(42)

#@app.get("/motor_run")
#def motor_run():
#   try:
#       os.system("rostopic pub toggle_led std_msgs/Empty --once")
@app.get("/publisher2")
def publisher_2():
    int_pub2.publish(99)
#except:
# print("An exception occurred")
        
#return {"Hello": "World"}
@app.get("/publisher3")
def publisher_3():
    float_pub1.publish(3.14)

@app.get("/publisher4")
def publisher_4():
    float_pub2.publish(2.718)

@app.get("/publisher5")
def publisher_5():
    float_pub3.publish(1.618)

@app.get("/publisher6")
def publisher_6():
    bool_pub.publish(False)


@app.get("/publisher7/{speed}")
async def read_item(speed: int, q: Union[int, None] = None):
    uint8_pub.publish(speed)
    if q:
        return {"speed": speed, "q": q}
    return {"speed": speed}

#@app.get("/motor_stop")
#def motor_stop():
#    os.system("rostopic pub stop_motor std_msgs/Empty --once")
#    return {"Hello": "World"}


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}
