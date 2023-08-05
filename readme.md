# A unique DoorBell system with a Keyless Unlock System

This project uses a knock sensor that detects vibrations from the knocks on the door and sends a signal to a sound module to ring a calling Bell Sound. I used a keyless Wi-Fi Based Authentication to unlock the door and a Live Camera footage

All of this runs on a Raspberry Pi Zero 2 W

## Components Used

- Raspberry Pi zero 2 w
- Raspberry pi camera module
- Tap/Knock Sensor
- Solenoid lock
- speaker/Buzzer for alarm purposes

## setup

- paste the HTML folder into the directory ```/var/www``` and host it in an apache server on local Host and make it run on startup
- copy the ```knock.py``` file into any one of the $PATH folder to make it executable
- run ```echo $PATH``` to find the suitable directories in your linux OS
- copy ```/pi``` folder into ```/Home``` directory or ```/desktop```
- To make ```knock.py``` run on startup add ```knock.py``` into ```.bashrc``` file such that it will be running on startup

### Webcam Streaming

- depending upon the type of camera forward the port  ```554``` or  ```443``` to any port forwarding site to access the camera in realtime from anywhere as long as the RPi is running 

### Notification Setup

- Create an account in pushbullet and get their API for python
- install Pushbullet in your desired Mobile Device and get the Device name
- Install pushbullet library in python using ```pip install pushbullet.py==0.9.1```
- edit the file ```Pi\notifications\__init__.py``` and replace the ```Your API here``` with your API key and ```Your Device here``` with your device name

## Unlocking Door

- once all done and everthing is up and running , access the IP of the RPI in your local network and click the unlock button to unlock the door, this will be safe as long as your home Wi-Fi is safe and scales with its security

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details