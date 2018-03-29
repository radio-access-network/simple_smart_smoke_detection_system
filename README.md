# simple_smart_smoke_detection_system
a simple system to query smoke detectors via Ethernet

18/3/29

I'm planning to add some smoke detectors in my house, but the smart ones, which you can query via Internet or App are expensive and only work via WLAN or Zigbee, etc.
These are not a reliable choice as radio connections can be "jammed" e.g. loosing WLAN-Connection on a little too far away client. 
Also as the house is a little bigger, i won't hear the detectors, if they are on, when i'm e.g. in the living room. 
So i need a centralized alarm system that shows an alarm and position for each connected detector.
Therefore i'll add some [cheap smoke detectors](http://www.eielectronics.de/rauchwarnmelder/rauchwarnmelder-ei605c.html), whose alarm-bus i'll query 
with an Arduino via an optocoupler once per detector. The Arduino has a Ethernet module/ temperatur sensor connected and runs a webserver, 
that shows temperature and alarm signal of the detector on a certain IP.
I've written a small program that queries the webserver and reads the data into a GUI on my Raspberry Pi 3. 
An alarm from the Arduino will flash lights or ring a bell in my house.
Also i'll add a small touch screen in the hallway, where you can view the current alarm state.

Later i'm planning to run a server on the Pi (e.g. with a python script) and let the Arduinos connect as Clients, so i don't have to use polling for querying the detectors.