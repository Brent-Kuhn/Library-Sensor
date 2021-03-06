# Library-Sensor
This is a repository for creating a sensor for my mom's library.

My mom wanted a sensor that sits inside of something and says hello and good bye as people enter and exit her library.  This is the repository I used to transfer the information from one raspberrypi to the other.  

While testing I used royalty free downloaded sound files (analog-watch-alarm_daniel-simion.wav and fire-truck-air-horn_daniel-simion.wav) from soundbible.com set to only play for 1 second, but any .wav file can be used for the sounds, just ensure that you change the play time accordingly.

# For making the enterExit.py project run on start:

    sudo nano ~/.config/lxsession/LXDE-pi/autostart
Add the following line at the end of the file and save:

    @sudo python3 enterExit.py
  
# Adding the sensors to the py:

Using GPIO as BCM the below image is the layout for the pin numbers for connecting the sensors and calling them in the python script.

![GPIO](https://elinux.org/images/8/80/Pi-GPIO-header-26-sm.png)

Above image source [ELinux RPi Hub](https://elinux.org/RPi_Hub)

For sensor 1 (enter) I used 23 and 24.

For sensor 2 (exit) I used 25 and 8.

Using the GPIO numbers you chose in the python script, set up your sensor as follows:

![Sensor Setup](https://www.modmypi.com/image/data/tutorials/hc-sr04/hc-sr04-tut-2.png)

Above image source [ModMyPi](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)
