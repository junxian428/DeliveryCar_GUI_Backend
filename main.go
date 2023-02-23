package main

import (
	"io/ioutil"
	"log"
	"net/http"

	"fyne.io/fyne/app"
	"fyne.io/fyne/widget"
)

func main() {

	app := app.New()

	w := app.NewWindow("Hello")
	w.SetContent(widget.NewVBox(
		widget.NewLabel("JetSon Nano 24V Car GUI for Control!"),
		widget.NewButton("Forward", func() {

			//cmd := exec.Command("rostopic pub stop_motor std_msgs/Empty --once")
			//_, err := exec.Command("/bin/sh", "run.sh").Output()
			//if err != nil {
			//	panic(err)
			//}
			//fmt.Println("Script executed successfully")
			RunMotor()

		}),
		widget.NewButton("Stop", func() {
			//cmd := exec.Command("rostopic pub stop_motor std_msgs/Empty --once")

			//cmd := exec.Command("rostopic pub stop_motor std_msgs/Empty --once")
			//_, err := exec.Command("/bin/sh", "stop.sh").Output()
			//if err != nil {
			//	panic(err)
			//}
			//sfmt.Println("Script executed successfully")
			StopMotor()
		}),
		widget.NewButton("Quit", func() {

			app.Quit()
		}),
	))

	w.ShowAndRun()
}

func RunMotor() {
	resp, err := http.Get("http://127.0.0.1:8000/motor_run")
	if err != nil {
		log.Fatalln(err)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}

	log.Println(string(body))
}

func StopMotor() {
	resp, err := http.Get("http://127.0.0.1:8000/motor_stop")
	if err != nil {
		log.Fatalln(err)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}

	log.Println(string(body))
}
