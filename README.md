# DeliveryCar_GUI_Backend

 RC Car
 
 roscore
 
 rosrun rosserial_python serial_node.py /dev/ttyACM0

export PATH=$PATH:/usr/local/go/bin


Backend 

uvicorn main:app --reload


GoLang Desktop GUI

 go run main.go
 
 
 [Why GoLang ? Compatibility issue a lot with ARM64 Ubuntu and Platform issues and Python compatibility issues]
