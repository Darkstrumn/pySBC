#!/usr/bin/python3
from os import system, name
from time import sleep
import re
import usb.core
import usb.util
import array as arr

class Steel_Battalions_Controller:

    def __init__(self):
        # 0a7b:d000
        self.modeldict = {
#                "index" : 0
#                ,"rates" : [1,1,1,1,1,1,1,1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#                ,"buffers" : [0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                "model" : {
                    "header" : None
                    ,"buttons" : {
                        # cmd column
                        "Eject" : None
                        ,"Hatch" : None
                        ,"Ignition" : None
                        ,"Start" : None
                        # toggles switches
                        ,"Oxygen" : None
                        ,"Filt" : None
                        ,"Fuel" : None
                        ,"Buffer" : None
                        ,"Location" : None
                        # 1x5  buttons - communications (red)
                        ,"Ch1x1" : None
                        ,"Ch1x2" : None
                        ,"Ch1x3" : None
                        ,"Ch1x4" : None
                        ,"Ch1x5" : None
                        # 3x3 Buttons - functions (green 3x3)
                        ,"Fx1x1" : None
                        ,"Fx1x2" : None
                        ,"Fx1x3" : None
                        ,"Fx2x1" : None
                        ,"Fx2x2" : None
                        ,"Fx2x3" : None
                        ,"Fx3x1" : None
                        ,"Fx3x2" : None
                        ,"Fx3x3" : None
                        # 2x3 - Weapon Controls (green 2x3)
                        ,"Wc1x1" : None
                        ,"Wc1x2" : None
                        ,"Wc1x3" : None
                        ,"Wc2x1" : None
                        ,"Wc2x2" : None
                        ,"Wc2x3" : None
                        # 3x2 - Monitor Controls (green 3x2)
                        ,"Mc1x1" : None
                        ,"Mc1x2" : None
                        ,"Mc2x1" : None
                        ,"Mc2x2" : None
                        ,"Mc3x1" : None
                        ,"Mc3x2" : None
                        ,"finger_trigger" : None
                        ,"thumb_trigger" : None
                        ,"lock_on" : None
                        ,"SBC_Active" : 1
                        }#/buttons
                    ,"separator" : None
                    ,"sight" :  {}
                    ,"rotation" : None
                    ,"aiming" : {}
                    ,"tuner_dial" : None
                    ,"gear" : None
                    ,"sidestep" : {"drift_offset" : -1}
                    ,"brake" : {"drift_offset" : -1}
                    ,"throttle" : {"drift_offset" : -1}
                    }#/model
                ,"leds" : {
                        4 : { "name" : "EmergencyEject", "id" : 4, "intensity" : 0, "byte_pos" : (round(int(4 - (4 % 2)) / 2))},
                        5 : { "name" : "CockpitHatch", "id" : 5, "intensity" : 0, "byte_pos" : (round(int(5 - (5 % 2)) / 2))},
                        6 : { "name" : "Ignition", "id" : 6, "intensity" : 0, "byte_pos" : (round(int(6 - (6 % 2)) / 2))},
                        7 : { "name" : "Start", "id" : 7, "intensity" : 0, "byte_pos" : (round(int(7 - (7 % 2)) / 2))},
                        8 : { "name" : "OpenClose", "id" : 8, "intensity" : 0, "byte_pos" : (round(int(8 - (8 % 2)) / 2))},
                        9 : { "name" : "MapZoomInOut", "id" : 9, "intensity" : 0, "byte_pos" : (round(int(9 - (9 % 2)) / 2))},
                        10 : { "name" : "ModeSelect", "id" : 10, "intensity" : 0, "byte_pos" : (round(int(10 - (10 % 2)) / 2))},
                        11 : { "name" : "SubMonitorModeSelect", "id" : 11, "intensity" : 0, "byte_pos" : (round(int(11 - (11 % 2)) / 2))},
                        12 : { "name" : "MainMonitorZoomIn", "id" : 12, "intensity" : 0, "byte_pos" : (round(int(12 - (12 % 2)) / 2))},
                        13 : { "name" : "MainMonitorZoomOut", "id" : 13, "intensity" : 0, "byte_pos" : (round(int(13 - (13 % 2)) / 2))},
                        41 : { "name" : "Gear5", "id" : 41, "intensity" : 0, "byte_pos" : (round(int(41 - (41 % 2)) / 2))},
                        40 : { "name" : "Gear4", "id" : 40, "intensity" : 0, "byte_pos" : (round(int(40 - (40 % 2)) / 2))},
                        39 : { "name" : "Gear3", "id" : 39, "intensity" : 0, "byte_pos" : (round(int(39 - (39 % 2)) / 2))},
                        38 : { "name" : "Gear2", "id" : 38, "intensity" : 0, "byte_pos" : (round(int(38 - (38 % 2)) / 2))},
                        37 : { "name" : "Gear1", "id" : 37, "intensity" : 0, "byte_pos" : (round(int(37 - (37 % 2)) / 2))},
                        36 : { "name" : "GearN", "id" : 36, "intensity" : 0, "byte_pos" : (round(int(36 - (36 % 2)) / 2))},
                        35 : { "name" : "GearR", "id" : 35, "intensity" : 0, "byte_pos" : (round(int(35 - (35 % 2)) / 2))},
                        33 : { "name" : "Comm5", "id" : 33, "intensity" : 0, "byte_pos" : (round(int(33 - (33 % 2)) / 2))},
                        32 : { "name" : "Comm4", "id" : 32, "intensity" : 0, "byte_pos" : (round(int(32 - (32 % 2)) / 2))},
                        31 : { "name" : "Comm3", "id" : 31, "intensity" : 0, "byte_pos" : (round(int(31 - (31 % 2)) / 2))},
                        30 : { "name" : "Comm2", "id" : 30, "intensity" : 0, "byte_pos" : (round(int(30 - (30 % 2)) / 2))},
                        29 : { "name" : "Comm1", "id" : 29, "intensity" : 0, "byte_pos" : (round(int(29 - (29 % 2)) / 2))},
                        28 : { "name" : "MagazineChange", "id" : 28, "intensity" : 0, "byte_pos" : (round(int(28 - (28 % 2)) / 2))},
                        27 : { "name" : "SubWeaponControl", "id" : 27, "intensity" : 0, "byte_pos" : (round(int(27 - (27 % 2)) / 2))},
                        26 : { "name" : "MainWeaponControl", "id" : 26, "intensity" : 0, "byte_pos" : (round(int(26 - (26 % 2)) / 2))},
                        25 : { "name" : "F3", "id" : 25, "intensity" : 0, "byte_pos" : (round(int(25 - (25 % 2)) / 2))},
                        24 : { "name" : "F2", "id" : 24, "intensity" : 0, "byte_pos" : (round(int(24 - (24 % 2)) / 2))},
                        23 : { "name" : "F1", "id" : 23, "intensity" : 0, "byte_pos" : (round(int(23 - (23 % 2)) / 2))},
                        22 : { "name" : "NightScope", "id" : 22, "intensity" : 0, "byte_pos" : (round(int(22 - (22 % 2)) / 2))},
                        21 : { "name" : "Override", "id" : 21, "intensity" : 0, "byte_pos" : (round(int(21 - (21 % 2)) / 2))},
                        20 : { "name" : "TankDetach", "id" : 20, "intensity" : 0, "byte_pos" : (round(int(20 - (20 % 2)) / 2))},
                        19 : { "name" : "Chaff", "id" : 19, "intensity" : 0, "byte_pos" : (round(int(19 - (19 % 2)) / 2))},
                        18 : { "name" : "Extinguisher", "id" : 18, "intensity" : 0, "byte_pos" : (round(int(18 - (18 % 2)) / 2))},
                        17 : { "name" : "Washing", "id" : 17, "intensity" : 0, "byte_pos" : (round(int(17 - (17 % 2)) / 2))},
                        16 : { "name" : "LineColorChange", "id" : 16, "intensity" : 0, "byte_pos" : (round(int(16 - (16 % 2)) / 2))},
                        15 : { "name" : "Manipulator", "id" : 15, "intensity" : 0, "byte_pos" : (round(int(15 - (15 % 2)) / 2))},
                        14 : { "name" : "ForecastShootingSystem", "id" : 14, "intensity" : 0, "byte_pos" : (round(int(14 - (14 % 2)) / 2))}
                    }#/led
                }#/modeldict

        self.vid = 0x0a7b
        self.pid = 0xd000
        INTERFACE_SBC = 0
        SETTING_SBC = 0
        ENDPOINT_READER = 0
        ENDPOINT_WRITER = 1
        self.dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)
        self.dev.reset()
        self.configuration = self.dev.get_active_configuration()
#        print(self.configuration)

        self.interface = 0
        #self.configuration[(INTERFACE_SBC, SETTING_SBC)]
        #print(self.interface)

        self.endpoint_reader = self.dev[0][(INTERFACE_SBC, SETTING_SBC)][ENDPOINT_READER]
#        print(self.endpoint_reader)

        self.endpoint_writer = self.dev[0][(INTERFACE_SBC, SETTING_SBC)][ENDPOINT_WRITER]
#        print(self.endpoint_writer)

        # if the OS kernel already claimed the device, which is most likely true
        # thanks to http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
        if self.dev.is_kernel_driver_active(self.interface) is True:
            # tell the kernel to detach
            print("Disengaging kernel mode driver for user mode driver")
            self.dev.detach_kernel_driver(self.interface)
            # claim the device
            print("Engaging user mode driver")
            usb.util.claim_interface(self.dev, self.interface)

        print("Leds::", self.modeldict["leds"])
#        return False

        self.led_test()
        

    def program(self):
        print("* Program called.")
        self.release_sbc()
        exit(0)

        self.clear()
        if not self.dev:
            print("Could not find SBC :(")
            exit(1)
        print("SBC - Detected!")
        self.parse_loop()
        self.release_sbc()
        exit(0)

    def parse_loop(self):
        print("* parse_loop called.")
        collected = 0
        attempts = 10000
        prev_data = None
        # data model: array('B', [0, 26, 0, 0, 0, 0, 252, 0, 128, 100, 0, 86, 128, 254, 64, 3, 0, 253, 64, 0, 64, 37, 192, 0, 1, 5])
        # data model:            ["00", "1A", "Buttons0", "Buttons1", "Buttons2", "Buttons3", "FC", "00", 128, 100, 0, 86, 128, 254, 64, 3, 0, 253, 64, 0, 64, 37, 192, 0, 1, 5])

        model = ["Const_00", "SBC_Id", "Buttons0", "Buttons1", "Buttons2", "Buttons3", "Buttons4", "Const_01", "Aiming_X1", "Aiming_X2", "Aiming_Y1", "Aiming_Y2", "Rotation1", "Rotation2", "Sight_X1", "Sight_X2", "Sight_Y1", "Sight_Y2", "S_Bias", "Sidestep", "B_Bias", "Brake", "T_Bias", "Throttle", "Tuner_Dial", "Gear"]
    
        active_model = ["Aiming_X1", "Aiming_X2", "Aiming_Y1", "Aiming_Y2", "Rotation1", "Rotation2", "Sight_X1", "Sight_X2", "Sight_Y1", "Sight_Y2", "S_Bias", "Sidestep", "B_Bias", "Brake", "T_Bias", "Throttle","Const_00", "SBC_Id","Const_01"]


        while collected < attempts :
            try:
                prev_data = self.read_sbc(model,active_model,collected,attempts,prev_data)
                self.clear()
                print("Header:", self.modeldict["model"]["header"])
                print("Const 1:", self.modeldict["model"]["separator"])
                print("Buttons:", self.modeldict["model"]["buttons"])
                print("Tuner Dial:", self.modeldict["model"]["tuner_dial"])
                print("Gear:", self.modeldict["model"]["gear"])
                print("Rotation - Z:", self.modeldict["model"]["rotation"])
                print("Sight:", self.modeldict["model"]["sight"])
                print("Aiming:", self.modeldict["model"]["aiming"])
                print("SideStep:", self.modeldict["model"]["sidestep"])
                print("Brake", self.modeldict["model"]["brake"])
                print("Throttle", self.modeldict["model"]["throttle"])

            except usb.core.USBError as e:
                if e.args == ('Operation timed out',):
                    print("*****(0)Attempt({0} - Read error: {1}.", collected, e.args)
                    continue
            sleep(0.1)

    def cmd_sbc(self, cmd):
        print("* cmd_sbc called.")
        self.endpoint_writer(cmd)
        
    def refresh_led_state(self):
        raw_led_data = arr.array("B",[])
#        for i in range(34):
#            raw_led_data.append(0x00)

        for led_index in self.modeldict["leds"]:
            #print("led_index", led_index)
            print("refresh_led_state ", led_index,", ", self.modeldict["leds"][led_index])
            #raw_led_data[self.modeldict["leds"][led_index]["byte_pos"]] = self.modeldict["leds"][led_index]["intensity"]
            
            #byte_pos = int(self.modeldict["leds"][led_index]["byte_pos"])
            #print("***byte_pos:: ", byte_pos)
            #raw_led_data[byte_pos] = self.modeldict["leds"][led_index]["intensity"]
            raw_led_data.append(self.modeldict["leds"][led_index]["intensity"])
            #print("rld: ", raw_led_data)
        self.endpoint_writer.write(raw_led_data)
        
    def set_led_state(self, led_id, intensity, refresh_state):
        print("* set_led_state called.")
        led = self.modeldict["leds"][led_id]
        
        if led == None: return
        
        hex_pos = int(led_id % 2)
        byte_pos = self.modeldict["leds"][led_id]["byte_pos" ]

        print("set_led_state:___hex_pos: ", hex_pos," ___byte_pos: ",byte_pos, " intensity: ", intensity)

        intensity = 0x0f if intensity >= 0x0f else intensity
#        self.modeldict["leds"][led_id]["byte_pos" ] = byte_pos
        self.modeldict["leds"][led_id]["intensity"] &= (0x0F if hex_pos == 1 else 0xF0)
        self.modeldict["leds"][led_id]["intensity"] += (intensity * (0x10 if hex_pos == 1 else 0x01))
        if refresh_state:
            self.refresh_led_state()

    def get_led_state(self, led_id):
        print("* get_led_state called.")
        led_index = self.modeldict["leds"].find(led_id)

        if led == None: return
        
        hex_pos = int(led_id % 2)
        byte_pos = int(led_id - hex_pos) / 2
        intensity = 0x0f if intensity > 0x0f else intensity
        print("** intensity: ",intensity)
        return self.modeldict["leds"][led_index]["intensity"] & (0x0F if hex_pos == 1 else 0xF0) /  (0x01 if hex_pos == 1 else 0x10)

    def led_test2(self, index):
        print("* led_test2 called.")
        led = self.modeldict["leds"].get(index)
        led_id = led["id"]
        for intensity in range(0x0e):
            self.clearConsole()
            self.set_led_state(led_id, intensity, True)
            sleep(0.5)
        led = self.modeldict["leds"].get(index)
        led_id = led["id"]
#        for intensity in range(0x10, -1, -1):
#            self.set_led_state(led_id, intensity, True)
#            sleep(1)
#        self.set_led_state(led_id, 0x00, True)

    def led_test(self):
        print("* led_test called.")
        self.refresh_led_state()
        for x in range(2):
            for index in self.modeldict["leds"]:
                self.led_test2(index)
        self.refresh_led_state()

    def clearConsole(self):
        command = 'clear'
        system(command)


    def read_sbc(self, model, active_model, collected, attempts, prev_data):
        print("* read_sbc called.")
        try:
            data = self.dev.read(self.endpoint_reader.bEndpointAddress,self.endpoint_reader.wMaxPacketSize)
            #noted that the second read pull the last data, so there seems to be hosticall buffer, oor possibly a hardware smoothing (2 cycle read)
            #shadow_data = self.dev.read(self.endpoint.bEndpointAddress,self.endpoint.wMaxPacketSize)
            collected += 1

            if data != prev_data:
                self.modeldict["model"]["header"] = format(data[model.index("Const_00")],'08b') + format(data[model.index("SBC_Id")],'08b')
       	        buttons = (format(data[model.index("Buttons0")],'08b')
                        + format(data[model.index("Buttons1")],'08b')
                        + format(data[model.index("Buttons2")],'08b')
                        + format(data[model.index("Buttons3")],'08b')
                        + format(data[model.index("Buttons4")],'08b')
                        )
                print ("0000000000000000000000000000000010000000")
                print (buttons)
                if buttons != "0000000000000000000000000000000010000000":
                    print ("^^^0^^^^|^^^1^^^|^^^2^^^|^^^3^^^|^^^4^^^")
                    print ("0123456701234567012345670123456701234567")
                    print ("0000000000111111111122222222223333333333")
                    print ("0123456789012345678901234567890123456789")
                    exit(0)
                self.modeldict["model"]["buttons"] = {
                # cmd column
                "Eject" : self.translate(format(data[model.index("Buttons0")],'08b')[4])
                ,"Hatch" : self.translate(format(data[model.index("Buttons0")],'08b')[3])
                ,"Ignition" : self.translate(format(data[model.index("Buttons0")],'08b')[2])
                ,"Start" : self.translate(format(data[model.index("Buttons0")],'08b')[1])
                # toggles switches
                ,"Oxygen" : self.translate(format(data[model.index("Buttons4")],'08b')[5])
                ,"Filter" : self.translate(format(data[model.index("Buttons4")],'08b')[4])
                ,"Fuel" : self.translate(format(data[model.index("Buttons4")],'08b')[3])
                ,"Buffer" : self.translate(format(data[model.index("Buttons4")],'08b')[2])
                ,"Location" : self.translate(format(data[model.index("Buttons4")],'08b')[1])
                # X1xY5  buttons - communications (red)
                ,"Ch1x1" : self.translate(format(data[model.index("Buttons3")],'08b')[3])
                ,"Ch1x2" : self.translate(format(data[model.index("Buttons3")],'08b')[2])
                ,"Ch1x3" : self.translate(format(data[model.index("Buttons3")],'08b')[1])
                ,"Ch1x4" : self.translate(format(data[model.index("Buttons3")],'08b')[0])
                ,"Ch1x5" : self.translate(format(data[model.index("Buttons4")],'08b')[7])
                # X3xY3 Buttons - functions (green 3x3)
                ,"Fx1x1" : self.translate(format(data[model.index("Buttons2")],'08b')[1])
                ,"Fx1x2" : self.translate(format(data[model.index("Buttons2")],'08b')[4])
                ,"Fx1x3" : self.translate(format(data[model.index("Buttons1")],'08b')[2])
                ,"Fx2x1" : self.translate(format(data[model.index("Buttons2")],'08b')[0])
                ,"Fx2x2" : self.translate(format(data[model.index("Buttons2")],'08b')[3])
                ,"Fx2x3" : self.translate(format(data[model.index("Buttons1")],'08b')[1])
                ,"Fx3x1" : self.translate(format(data[model.index("Buttons3")],'08b')[7])
                ,"Fx3x2" : self.translate(format(data[model.index("Buttons2")],'08b')[2])
                ,"Fx3x3" : self.translate(format(data[model.index("Buttons1")],'08b')[0])
                # X2xY3 - Weapon Controls (green 2x3)
                ,"Wc1x1" : self.translate(format(data[model.index("Buttons2")],'08b')[7])
                ,"Wc1x2" : self.translate(format(data[model.index("Buttons2")],'08b')[6])
                ,"Wc1x3" : self.translate(format(data[model.index("Buttons2")],'08b')[5])
                ,"Wc2x1" : self.translate(format(data[model.index("Buttons3")],'08b')[6])
                ,"Wc2x2" : self.translate(format(data[model.index("Buttons3")],'08b')[5])
                ,"Wc2x3" : self.translate(format(data[model.index("Buttons3")],'08b')[4])
                # X3xY2 - Monitor Controls (green 3x2)
                ,"Mc1x1" : self.translate(format(data[model.index("Buttons0")],'08b')[0])
                ,"Mc1x2" : self.translate(format(data[model.index("Buttons1")],'08b')[7])
                ,"Mc2x1" : self.translate(format(data[model.index("Buttons1")],'08b')[6])
                ,"Mc2x2" : self.translate(format(data[model.index("Buttons1")],'08b')[5])
                ,"Mc3x1" : self.translate(format(data[model.index("Buttons1")],'08b')[4])
                ,"Mc3x2" : self.translate(format(data[model.index("Buttons1")],'08b')[3])
                ,"finger_trigger" : self.translate(format(data[model.index("Buttons0")],'08b')[6])
                ,"thumb_trigger" : self.translate(format(data[model.index("Buttons0")],'08b')[7])
                ,"lock_on" : self.translate(format(data[model.index("Buttons0")],'08b')[5])
                ,"SBC_Active" : self.translate(format(data[model.index("Buttons4")],'08b')[0])
                }
                self.modeldict["model"]["separator"] = format(data[model.index("Const_01")],'08b')
                self.modeldict["model"]["tuner_dial"] = format(data[model.index("Tuner_Dial")],'d')
                self.modeldict["model"]["gear"] = re.sub("255","N", re.sub("254","R", format(data[model.index("Gear")],'d')))
                self.modeldict["model"]["sight"]["x"] = format(data[model.index("Sight_X1")]+data[model.index("Sight_X2")],'d') + " : " + format(data[model.index("Sight_X2")],'d')
                self.modeldict["model"]["sight"]["y"] = format(data[model.index("Sight_Y1")]+data[model.index("Sight_Y2")],'d') + " : " + format(data[model.index("Sight_Y2")],'d')
                self.modeldict["model"]["rotation"] = format(data[model.index("Rotation1")],'d') + " : " + format(data[model.index("Rotation2")],'d')
                self.modeldict["model"]["aiming"]["x"] = format(data[model.index("Aiming_X1")],'d') + " : " + format(data[model.index("Aiming_X2")],'d')
                self.modeldict["model"]["aiming"]["y"] = format(data[model.index("Aiming_Y1")],'d') + " : " + format(data[model.index("Aiming_Y2")],'d')
                
                self.modeldict["model"]["sidestep"]["drift_offset"] = data[model.index("Sidestep")] if self.modeldict["model"]["sidestep"]["drift_offset"] == -1  else self.modeldict["model"]["sidestep"]["drift_offset"]
                self.modeldict["model"]["sidestep"]["value"] = format(data[model.index("S_Bias")],'d') + " : " + format((lambda x, y: x - self.modeldict["model"]["sidestep"]["drift_offset"] if x + (-1 * self.modeldict["model"]["sidestep"]["drift_offset"]) > -1 and (y == 64 or y ==128 or y == 0 and y == 192) else x)(data[model.index("Sidestep")], data[model.index("S_Bias")]),'d')
#                self.modeldict["model"]["sidestep"]["value"] = format(data[model.index("S_Bias")],'d') + " : " + format(data[model.index("Sidestep")],'d')
                
                self.modeldict["model"]["brake"]["drift_offset"] = data[model.index("Brake")] if self.modeldict["model"]["brake"]["drift_offset"] == -1 else self.modeldict["model"]["brake"]["drift_offset"]
                self.modeldict["model"]["brake"]["value"] = format(data[model.index("B_Bias")],'d') + " : " + format((lambda x, y: x - self.modeldict["model"]["brake"]["drift_offset"] if x + (-1 * self.modeldict["model"]["brake"]["drift_offset"]) > -1 and (y == 64 or y ==128 or y == 0 and y != 192) else x)(data[model.index("Brake")], data[model.index("B_Bias")]),'d')
                
                self.modeldict["model"]["throttle"]["drift_offset"] = data[model.index("Throttle")] if self.modeldict["model"]["throttle"]["drift_offset"] == -1 else self.modeldict["model"]["throttle"]["drift_offset"]
                self.modeldict["model"]["throttle"]["value"] = format(data[model.index("T_Bias")],'d') + " : " + format((lambda x, y: x - self.modeldict["model"]["throttle"]["drift_offset"] if x + (-1 * self.modeldict["model"]["throttle"]["drift_offset"]) > -1 and (y == 64 or y ==128 or y == 0 and y != 192) else x)(data[model.index("Throttle")], data[model.index("T_Bias")]),'d')
                #
#                for val in active_model:
#                    index = model.index(val)
#                    if index - 8 > 0:
#                        self.modeldict["buffers"][index] = (self.modeldict["buffers"][index] + data[index]) / self.modeldict["rates"][index]
                #
        except usb.core.USBError as e:
            data = None
            if e.args == ('Operation timed out',):
                print("*****(1)Attempt({0} - Read error: {1}.", collected, e.args)
        return data

    def translate(self,value):
        print("* translate called.")
        ret = re.sub("0", "-- ", value)
        ret = re.sub("1", "ON", ret)
        return ret

    def display_data(self, model):
        print("* display_data called.")
        self.clear()
        print(model)

    def release_sbc(self):
        print("* release_sbc called.")
        # release the devices
        print("Releasing user mode driver")
        usb.util.release_interface(self.dev, self.interface)
        print("Re-engaging kernel mode driver")
        # reattach the device to the OS kernel
        self.dev.attach_kernel_driver(self.interface)

    # define our clear function 
    def clear(self): 
        print("* clear called.")
  
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
  
    # for ma    c and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear')

#-------------------------------------------------------------------------------

def main():
    print("main called.")
    sbc = Steel_Battalions_Controller() 
    sbc.program()
    exit(0)


main()
