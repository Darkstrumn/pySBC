#!/usr/bin/python
from os import system, name
from time import sleep
import usb.core
import usb.util
import array as arr

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


# 0a7b:d000
VID = 0x0a7b
PID = 0xd000
dev = usb.core.find(idVendor=VID, idProduct=PID)
if not dev:
    print "Could not find SBC :("
    exit(1)
print "SBC - Detected!"
# first endpoint
interface = 0
endpoint = dev[0][(0,0)][0]
# if the OS kernel already claimed the device, which is most likely true
# thanks to http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
if dev.is_kernel_driver_active(interface) is True:
    # tell the kernel to detach
    print "Disengaging kernel mode driver for user mode driver"
    dev.detach_kernel_driver(interface)
    # claim the device
    print "Engaging user mode driver"
    usb.util.claim_interface(dev, interface)
collected = 0
attempts = 50000
prevdata = None
# data model: array('B', [0, 26, 0, 0, 0, 0, 252, 0, 128, 100, 0, 86, 128, 254, 64, 3, 0, 253, 64, 0, 64, 37, 192, 0, 1, 5])
# data model:            ["00", "1A", "Buttons0", "Buttons1", "Buttons2", "Buttons3", "FC", "00", 128, 100, 0, 86, 128, 254, 64, 3, 0, 253, 64, 0, 64, 37, 192, 0, 1, 5])
model = ["Const_00", "SBC_Id", "Buttons0", "Buttons1", "Buttons2", "Buttons3", "ToggleSwitches", "Const_00", "Aiming_X1", "Aiming_x2", "Aiming_Y1", "Aiming_Y2", "Rotation1", "Rotation2", "Sight_X1", "Sight_X2", "Sight_Y1", "Sight Y2", "S_Bias", "Strafe", "B_Bias", "Brake", "T_Bias", "Throttle", "TunerDial", "Gear"]

activeModel = ["Const_00", "SBC_Id", "Buttons0", "Buttons1", "Buttons2", "Buttons3", "ToggleSwitches", "Const_00", "Aiming_X1", "Aiming_x2", "Aiming_Y1", "Aiming_Y2", "Rotation1", "Rotation2", "Sight_X1", "Sight_X2", "Sight_Y1", "Sight Y2", "S_Bias", "B_Bias", "T_Bias"]


while True :#collected < attempts :
    try:
        data = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
        collected += 1
        if data != prevdata:
	    clear()
            for val in activeModel:
                index = model.index(val)
                print(val, data[index])
        prevdata = data
    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            continue
# release the devices
print "Releasing user mode driver"
usb.util.release_interface(dev, interface)
print "Re-engaging kernel mode driver"
# reattach the device to the OS kernel
dev.attach_kernel_driver(interface)
exit(0)
