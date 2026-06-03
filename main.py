import machine
import time

ledver =  machine.Pin(17, machine.Pin.OUT)
ledvr =   machine.Pin(14, machine.Pin.OUT)
ledblue = machine.Pin(12, machine.Pin.OUT)

butaover  = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
butaovr =   machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
butaoblue = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)

while(True):

    estado  = butaover.value()
    estado2 = butaovr.value()
    estado3 = butaoblue.value()


    if (estado == 0):
        ledver.on()
    else:
        ledver.off()


    if (estado3 == 0):
        ledvr.on()
    else:
        ledvr.off()


    if (estado2 == 0):
        ledblue.on()
    else:
        ledblue.off()

    time.sleep(0.15)
