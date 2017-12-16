# Library-Sensor
This is a repository for creating a sensor for my mom's library.

My mom wanted a sensor that sits inside of something and says hello and good bye as people enter and exit her library.  This is the repository I used to transfer the information from one raspberrypi to the other.  

While testing I used royalty free downloaded sound files (analog-watch-alarm_daniel-simion.wav and fire-truck-air-horn_daniel-simion.wav) from soundbible.com set to only play for 1 second, but any .wav file can be used for the sounds, just ensure that you change the play time accordingly.

For making the enterExit.py project run on start:
  sudo nano ~/.config/lxsession/LXDE-pi/autostart
Add the following line at the end of the file and save:
  @sudo python3 enterExit.py
  
Adding the sensors to the py:
![gpiopins](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/images/gpio-numbers-pi2.png)

