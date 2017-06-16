# Raspberry-pi-motion-sersor-password-unlock

Required
Basic Knowledge of raspberry pi
1-raspberry pi3
1-active buzzer
1-matrix 4X4 keypad
1-PIR Movement Sensor
1-Transistor (S8050)
1- 1KOhm resistor

 
Keypad pin
-----◘◘◘◘◘◘  GPIO17
-----◘◘◘◘◘◘  GPIO18
-----◘◘◘◘◘◘  GPIO27
-----◘◘◘◘◘◘  GPIO22
-----------  GPIO23
-----------  GPIO24
-----------  GPIO25
-----------  GPIO04


PIR pin
positive to +5v
ground to gnd
out to GPIO12

Buzzer
connect positive of buzzer with +3V.
buzzers negative with transistors emitter.
transistors collector to Gnd.
1KOhm resistor from transistors base to GPIO05.
