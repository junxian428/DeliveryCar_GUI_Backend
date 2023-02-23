from typing import Union

from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/motor_run")
def motor_run():
    try:
        os.system("rostopic pub toggle_led std_msgs/Empty --once")

    except:
        print("An exception occurred")
        
    return {"Hello": "World"}



@app.get("/motor_stop")
def motor_stop():
    os.system("rostopic pub stop_motor std_msgs/Empty --once")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
