import machine # RPI Pico library functions
import utime # standrd time functions 

# POT is connected to GP26
potentiometer = machine.ADC(26)

while True:
    voltage = potentiometer.read_u16() # read the current state of the POT
    print(voltage)
    utime.sleep(2) #' wait 2 seconds
