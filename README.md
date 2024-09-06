# PiRemoteWipe
This project aims to allow you to remotely wipe a raspberry pi so that it can be installed in a inviroment where it cannot be recovered from without risking the safety of user.

![IMG_20240819_171411741 (1)](https://github.com/user-attachments/assets/49817168-1072-48e3-b8d6-7cf3415c618d)

wire your gpio, relay and sd card
Gpio connects to relay
relay acts as power switch for + voltage and ground is made common between power source and pi
Download the python file
Make sure you have the packages
run chmod +x relayt.py
now whenever ./relayt.py is run the relay will be opened and 9v or your power suppy of choice will be dumped into the sd card

Cool things you could you add: use the pogo pins and make it into a case. use a supercap or step up converter to make the sd card definitely fried
