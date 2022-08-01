#---------
def getConfigDataStructure_dictionary(self):
	"""Define the config for finding the SBC and talking to it"""
	return {
	        "author" : "Darkstrumn"
	        ,"version" : "0.6"
	        ,"vendor_id" : 0x0a7b
	        ,"product_id" : 0xd000
	        ,"usb_sbc_configuration" : 0
	        ,"usb_sbc_interface" : 0
	        ,"usb_sbc_setting" : 0
	        ,"usb_endpoint_reader" : 0
	        ,"usb_endpoint_writer" : 1
	        ,"normal_intensity" : 1
	        ,"bold_intensity" : 7
	        ,"emergency_intensity" : 15
	        ,"refresh_rate" : 60
	        }
#---------

def getDataPacketStructure_dictionary(self):
	"""Define the usb data packet particulars"""
	packets = (
		"Const_00_0"
		, "Const_1A"
		, "Buttons0"
		, "Buttons1"
		, "Buttons2"
		, "Buttons3"
		, "Buttons4"
		, "Const_00_1"
		, "Aiming_X1"
		, "Aiming_X2"
		, "Aiming_Y1"
		, "Aiming_Y2"
		, "Rotation1"
		, "Rotation2"
		, "SightChange_X1"
		, "SightChange_X2"
		, "SightChange_Y1"
		, "SightChange_Y2"
		, "Sidestep1"
		, "Sidestep2"
		, "Brake1"
		, "Brake2"
		, "Throttle1"
		, "Throttle2"
		, "Tuner"
		, "Gear"
		, "Const_00_2"
		, "Const_00_3"
		, "Const_00_4"
		, "Const_00_5"
		, "Const_00_6"
		, "Const_00_7"
		)
        # Enumerate and make into dictionary for consistancey
	result = { str( x + 1 ) : str( packets[x] ) for x, _ in enumerate(packets) }
	return result
#---------

def getControllerDataStructure_dictionary(self):
	"""Define the basic controller datastructure and particulars"""
	controller = {
        "RightJoythumbTrigger" : { "Section" : "Triggers", "Group" : "RightJoystick", "Control" : "Main Weapon", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 7}
        ,"RightJoyfingerTrigger" : { "Section" : "Triggers", "Group" : "RightJoystick", "Control" : "Secondary Weapon", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 6 }
        ,"RightJoylockOn" : { "Section" : "Triggers", "Group" : "RightJoystick", "Control" : "Lock-On", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 5 }

        ,"Eject" : { "Section" : "Button", "Group" : "CommandColumn", "Control" : "Eject", "Id" : None, "Led" : { "Id" : 3, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 4 }
        ,"CockpitHatch" : {  "Section" : "Buttons", "Group" : "CommandColumn", "Control" : "Cockpit Hatch", "Id" : None, "Led" : { "Id" : 4, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 3 }
        ,"Ignition" : {  "Section" : "Buttons", "Group" : "CommandColumn", "Control" : "Ignition", "Id" : None, "Led" : { "Id" : 5, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"Start"  : {  "Section" : "Buttons", "Group" : "CommandColumn", "Control" : "Start", "Id" : None, "Led" : { "Id" : 6, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons"  ), "DataFormat" : "08b", "mask" : 1 }

        ,"MmcOpenClose" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Open/Close", "Id" : None, "Led" : { "Id" :  7, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 0 }
        ,"MmcMapZoomInOut" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Map Zoom In/Out", "Id" : None, "Led" : { "Id" : 8, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 7 }
        ,"MmcModeSelect" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Mode Select", "Id" : None, "Led" : { "Id" : 9, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 6 }
        ,"MmcSubMonitor" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Sub Monitor Mode Select", "Id" : None, "Led" : { "Id" : 10, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 5 }
        ,"MmcZoomIn" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Zoom In", "Id" : None, "Led" : { "Id" : 11, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 4 }
        ,"MmcZoomOut" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Zoom Out", "Id" : None, "Led" : { "Id" : 12, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 3 }

        ,"FxForcastShootingSystem" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "FSS - Forcast Shooting System", "Id" : None, "Led" : { "Id" : 13, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"FxManipulator" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Manipulator", "Id" : None, "Led" : { "Id" : 15, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 1 }
        ,"FxLineColourChange" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Line Colour Change", "Id" : None, "Led" : { "Id" : 16, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 0 }

        ,"WcWashing" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Washing", "Id" : None, "Led" : { "Id" : 17, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 7 }
        ,"WcExstinguisher" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Exstinguisher", "Id" : None, "Led" : { "Id" : 18, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 6 }
        ,"WcChaff" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Chaff", "Id" : None, "Led" : { "Id" : 19, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 5 }

        ,"FxTankDetach" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Tank Detach", "Id" : None, "Led" : { "Id" : 20, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 4 }
        ,"FxOverride" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Override", "Id" : None, "Led" : { "Id" : 21, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 3 }
        ,"FxNightScope" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Night Scope", "Id" : None, "Led" : { "Id" : 22, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"FxFunctionF1" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "F1", "Id" : None, "Led" : { "Id" : 23, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 1 }
        ,"FxFunctionF2" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "F2", "Id" : None, "Led" : { "Id" : 24, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 0 }
        ,"FxFunctionF3" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "F3", "Id" : None, "Led" : { "Id" : 25, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 7 }

        ,"WcMain" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Main", "Id" : None, "Led" : { "Id" : 26, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 6 }
        ,"WcSub" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Sub", "Id" : None, "Led" : { "Id" : 27, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 5 }
        ,"WcMagazineChange" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Magazine Change", "Id" : None, "Led" : { "Id" : 28, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 4 }

        ,"Comm1" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 1", "Id" : None, "Led" : { "Id" : 29, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 3 }
        ,"Comm2" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 2", "Id" : None, "Led" : { "Id" : 30, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"Comm3" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 3", "Id" : None, "Led" : { "Id" : 31, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 1 }
        ,"Comm4" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 4", "Id" : None, "Led" : { "Id" : 32, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 0 }
        ,"Comm5" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 5", "Id" : None, "Led" : { "Id" : 33, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 7 }

        ,"ToggleFilter" : { "Section" : "Toggles", "Group" : "", "Control" : "Filter Control System", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 4 }
        ,"ToggleOxygenSupply" : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "Oxygen Supply System", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 5 }
        ,"ToggleFuelFlowRate" : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "Fuel Flow Rate", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 3 }
        ,"ToggleBufferMaterial" : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "Buffer Material", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"ToggleVTLocation"  : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "VT-Location Measurement", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 1 }

        ,"LeftJoySightChange" : { "Section" : "Analogs", "Group" : "LeftJoystick", "Control" : "Sight Change", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "SightChange_X1", "SightChange_X2", "SightChange_Y1", "SightChange_Y2" ), "DataFormat" : "08b", "mask" : None }
        ,"LeftJoyRotation" : { "Section" : "Analogs", "Group" : "LeftJoystick", "Control" : "Rotation", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Rotation1", "Rotation2" ), "DataFormat" : "08b", "mask" : None }
        ,"RightJoyAiming" : { "Section" : "Analogs", "Group" : "RightJoystick", "Control" : "Aiming", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Aiming_X1", "Aiming_X2", "Aiming_Y1", "Aiming_Y2" ), "DataFormat" : "08b", "mask" : None }

        ,"SidestepPedal" : { "Section" : "Analogs", "Group" : "Pedals", "Control" : "Side step", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Sidestep1", "Sidestep2" ), "DataFormat" : "d", "mask" : 0 }
        ,"BrakePedal" : { "Section" : "Analogs", "Group" : "Pedals", "Control" : "Brake", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Brake1", "Brake2"  ), "DataFormat" : "d", "mask" : 0 }
        ,"ThrottlePedal" : { "Section" : "Analogs", "Group" : "Pedals", "Control" : "Throttle", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Throttle1", "Throttle2" ), "DataFormat" : "d", "mask" : 0 }

        ,"Tuner" : { "Section" : "Tuner", "Group" : "Tuner", "Control" : "Tuner Dial", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Tuner"  ), "DataFormat" : "d", "mask" : 0 }

        ,"Gear" : { "Section" : "Gear", "Group" : "Gear", "Control" : "Gear Shifter", "Id" : None, "Min" : -2, "Max" : 5, "packets" : ( "Gear"  ), "DataFormat" : "d", "mask" : 0
                ,"Gears" : {
                        "5" : { "Gear" : "5", "Led" : { "Id" : 41, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "5", "To" : "5", "packet" : "Gear" } },
                        "4" : { "Gear" : "4", "Led" : { "Id" : 40, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "4", "To" : "4", "packet" : "Gear" } },
                        "3" : { "Gear" : "3", "Led" : { "Id" : 39, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "3", "To" : "3", "packet" : "Gear" } },
                        "2" : { "Gear" : "2", "Led" : { "Id" : 38, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "2", "To" : "2", "packet" : "Gear" } },
                        "1" : { "Gear" : "1", "Led" : { "Id" : 37, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "1", "To" : "1", "packet" : "Gear" } },
                        "-1" : { "Gear" : "N", "Led" : { "Id" : 36, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "-1", "To" : "N", "packet" : "Gear" } },
                        "-2" : { "Gear" : "R", "Led" : { "Id" : 35, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" :  { "From" : "-2", "To" : "R", "packet" : "Gear" } }
                        }
                }
        }

	enumId = 0

	for control in controller:
		# Enumerate the model
		enumId += 1
		controller[control]["Id"] = enumId
		
		# Add state properties to the following control types
		for controlType in ("Buttone", "Triggers", "Toggles"):

			if( controller[control]["Section"] == controlType ):
				controller[control]["State"] = { "enum" : enumId, "CurrentState" : False, "Changed" : False }
			else:
				controller[control]["State"] = { "enum" : enumId, "CurrentState" : None, "Changed" : False }

	return controller
#---------

def get_sbc_model_dictionary(self):
	"""Define the model for the SBC device"""
	return {
        "config" : get_config_data_structure_dictionary()
        ,"data_dackets": get_data_packet_structure_dictionary()
        ,"dontroller" : get_controller_data_structure_dictionary()
		,"dev" : {
			"device" : None
			, "usb_sbc_configuration" : None
			, "usb_endpoint_reader" : None
			, "usb_endpoint_writer" : None
			, "void" : None,}
        }
#---------


#---------
#---------
#---------
#---------

#Diagnostics
def diagnostics_Test():
    """Diagnostics"""

    sbc = get_sbc_model_dictionary()
    print("! Steel Battalions Controller- v " + sbc["config"]["version"] + " - Driver written by: " + sbc["config"]["author"] + " !") 
    for item in list( map( lambda x: "(" + str(x) + "):" + str(sbc["data_packets"][x]), sbc["data_packets"] ) ):
        print ( str(item) )
#	for model in sbc:
#		#print ( "Model:\\" + str(model) + "::")
#		print ( "-----------------------------")
#		for modelNode in sbc[model]:
#			print ( "Model:\\" + str(model) + "\\\\" + str(modelNode) + "::" + str(sbc[model][modelNode]))
#---------

diagnostics_Test()

class Steel_Battalions_Controller:
	"""
	Steel Battalions Controller Driver - Will make the SBC behave like a real-time datasource
	"""

    def __init__(self):
		"""Init SBC"""
        self.sbc = self.get_sbc_model_dictionary()

		#Real sbc - device
        #self.sbc["dev"]["device"] = usb.core.find(idVendor=self.sbc["config"]["vendor_id"], idProduct=self.sbc["config"]["product_id"])
        #self.sbc["dev"]["usb_sbc_configuration"] = self.sbc["dev"]["device"].get_active_configuration()

		#Mock sbc - device
        self.sbc["dev"]["device"] = {
				#endpoint = dev[0][(0,0)][0]
				0 : {
						(0, 0) : {
								0 : "usb_sbc_configuration, usb_sbc_interface, usb_sbc_setting, usb_endpoint_reader"
								, 1 : "usb_sbc_configuration, usb_sbc_interface, usb_sbc_setting, usb_endpoint_writer"
						}
					}
			}

        self.sbc["dev"]["usb_endpoint_reader"] = self.sbc["dev"]["device"][self.sbc["config"]["usb_sbc_configuration"]][(self.sbc["config"]["usb_sbc_interface"], self.sbc["config"]["usb_sbc_setting"])][self.sbc["config"]["usb_endpoint_reader"]]
        self.sbc["dev"]["usb_endpoint_writer"] = self.sbc["dev"]["device"][self.sbc["config"]["usb_sbc_configuration"]][(self.sbc["config"]["usb_sbc_interface"], self.sbc["config"]["usb_sbc_setting"])][self.sbc["config"]["usb_endpoint_writer"]]

        # if the OS kernel already claimed the device, which is most likely true
        # thanks to http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
        if self.sbc["dev"]["device"].is_kernel_driver_active(self.sbc["config"]["usb_sbc_interface"]) is True:
            # tell the kernel to detach
            print("Disengaging kernel mode driver for user mode driver")
            self.sbc["dev"]["device"].detach_kernel_driver(self.sbc["config"]["usb_sbc_interface"])
            # claim the device
            print("Engaging user mode driver")
            usb.util.claim_interface(self.sbc["dev"]["device"], self.sbc["config"]["usb_sbc_interface"])

        #print("Leds::", self.modeldict["leds"])
        #return False

        self.led_test()

    def program(self):
        self.release_sbc()
        exit(0)

        self.clear()
        if not self.model["dev"]:
            print("Could not find SBC :(")
            exit(1)
        print("SBC - Detected!")
        self.parse_loop()
        self.release_sbc()
        exit(0)

    def parse_loop(self):
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
        self.endpoint_writer(cmd)
        
    def refresh_led_state(self):
        raw_led_data = arr.array("B",[])
        #for i in range(34):
            #raw_led_data.append(0x00)

        for led_index in self.modeldict["leds"]:
            #print("led_index", led_index)
            #print("refresh_led_state ", self.modeldict["leds"][led_index])
            #raw_led_data[self.modeldict["leds"][led_index]["byte_pos"]] = self.modeldict["leds"][led_index]["intensity"]
            
            #byte_pos = int(self.modeldict["leds"][led_index]["byte_pos"])
            #print("***byte_pos:: ", byte_pos)
            #raw_led_data[byte_pos] = self.modeldict["leds"][led_index]["intensity"]
            raw_led_data.append(self.modeldict["leds"][led_index]["intensity"])
            #print("rld: ", raw_led_data)
        self.endpoint_writer.write(raw_led_data)
        
    def set_led_state(self, led_id, intensity, refresh_state):
        led = self.modeldict["leds"][led_id]
        
        if led == None: return
        
        hex_pos = int(led_id % 2)
        print("___hex_pos: ", hex_pos)
        byte_pos = self.modeldict["leds"][led_id]["byte_pos" ]
        print("___byte_pos: ", byte_pos)
        intensity = 0x0f if intensity > 0x0f else intensity
        #self.modeldict["leds"][led_id]["byte_pos" ] = byte_pos
        self.modeldict["leds"][led_id]["intensity"] &= (0x0F if hex_pos == 1 else 0xF0)
        self.modeldict["leds"][led_id]["intensity"] += (intensity * (0x10 if hex_pos == 1 else 0x01))
        if refresh_state:
            self.refresh_led_state()

    def get_led_state(self, led_id):
        led_index = self.modeldict["leds"].find(led_id)

        if led == None: return
        
        hex_pos = int(led_id % 2)
        byte_pos = int(led_id - hex_pos) / 2
        intensity = 0x0f if intensity > 0x0f else intensity
        return self.modeldict["leds"][led_index]["intensity"] & (0x0F if hex_pos == 1 else 0xF0) /  (0x01 if hex_pos == 1 else 0x10)

    def led_test2(self, index):
        led = self.modeldict["leds"].get(index)
        led_id = led["id"]
        for intensity in range(0x0f):
            self.set_led_state(led_id, intensity, True)
        led = self.modeldict["leds"].get(index)
        led_id = led["id"]
        for intensity in range(0x10, -1, -1):
            self.set_led_state(led_id, intensity, True)
        self.set_led_state(led_id, 0x00, True)

    def led_test(self):
        self.refresh_led_state()
        for x in range(2):
            for index in self.modeldict["leds"]:
                self.led_test2(index)
        self.refresh_led_state()

    def read_sbc(self, model, active_model, collected, attempts, prev_data):
        try:
            data = self.model["dev"].read(self.endpoint_reader.bEndpointAddress,self.endpoint_reader.wMaxPacketSize)
            #noted that the second read pull the last data, so there seems to be hosticall buffer, oor possibly a hardware smoothing (2 cycle read)
            #shadow_data = self.model["dev"].read(self.endpoint.bEndpointAddress,self.endpoint.wMaxPacketSize)
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
                ,"Fx1x1" : self.translate(format(data[model.index("Buttons3")],'08b')[1])
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
                self.modeldict["model"]["sight"]["x"] = format(data[model.index("Sight_X1")],'d') + " : " + format(data[model.index("Sight_X2")],'d')
                self.modeldict["model"]["sight"]["y"] = format(data[model.index("Sight_Y1")],'d') + " : " + format(data[model.index("Sight_Y2")],'d')
                self.modeldict["model"]["rotation"] = format(data[model.index("Rotation1")],'d') + " : " + format(data[model.index("Rotation2")],'d')
                self.modeldict["model"]["aiming"]["x"] = format(data[model.index("Aiming_X1")],'d') + " : " + format(data[model.index("Aiming_X2")],'d')
                self.modeldict["model"]["aiming"]["y"] = format(data[model.index("Aiming_Y1")],'d') + " : " + format(data[model.index("Aiming_Y2")],'d')
                
                self.modeldict["model"]["sidestep"]["drift_offset"] = data[model.index("Sidestep")] if self.modeldict["model"]["sidestep"]["drift_offset"] == -1  else self.modeldict["model"]["sidestep"]["drift_offset"]
                self.modeldict["model"]["sidestep"]["value"] = format(data[model.index("S_Bias")],'d') + " : " + format((lambda x, y: x - self.modeldict["model"]["sidestep"]["drift_offset"] if x + (-1 * self.modeldict["model"]["sidestep"]["drift_offset"]) > -1 and (y == 64 or y ==128 or y == 0 and y == 192) else x)(data[model.index("Sidestep")], data[model.index("S_Bias")]),'d')
                #self.modeldict["model"]["sidestep"]["value"] = format(data[model.index("S_Bias")],'d') + " : " + format(data[model.index("Sidestep")],'d')
                
                self.modeldict["model"]["brake"]["drift_offset"] = data[model.index("Brake")] if self.modeldict["model"]["brake"]["drift_offset"] == -1 else self.modeldict["model"]["brake"]["drift_offset"]
                self.modeldict["model"]["brake"]["value"] = format(data[model.index("B_Bias")],'d') + " : " + format((lambda x, y: x - self.modeldict["model"]["brake"]["drift_offset"] if x + (-1 * self.modeldict["model"]["brake"]["drift_offset"]) > -1 and (y == 64 or y ==128 or y == 0 and y != 192) else x)(data[model.index("Brake")], data[model.index("B_Bias")]),'d')
                
                self.modeldict["model"]["throttle"]["drift_offset"] = data[model.index("Throttle")] if self.modeldict["model"]["throttle"]["drift_offset"] == -1 else self.modeldict["model"]["throttle"]["drift_offset"]
                self.modeldict["model"]["throttle"]["value"] = format(data[model.index("T_Bias")],'d') + " : " + format((lambda x, y: x - self.modeldict["model"]["throttle"]["drift_offset"] if x + (-1 * self.modeldict["model"]["throttle"]["drift_offset"]) > -1 and (y == 64 or y ==128 or y == 0 and y != 192) else x)(data[model.index("Throttle")], data[model.index("T_Bias")]),'d')
                #
                #for val in active_model:
                #    index = model.index(val)
                #    if index - 8 > 0:
                #        self.modeldict["buffers"][index] = (self.modeldict["buffers"][index] + data[index]) / self.modeldict["rates"][index]
                #
        except usb.core.USBError as e:
            data = None
            if e.args == ('Operation timed out',):
                print("*****(1)Attempt({0} - Read error: {1}.", collected, e.args)
        return data

    def translate(self,value):
        ret = re.sub("0", "-- ", value)
        ret = re.sub("1", "ON", ret)
        return ret

    def display_data(self, model):
        self.clear()
        print(model)

    def release_sbc(self):
        # release the devices
        print("Releasing user mode driver")
        usb.util.release_interface(self.model["dev"], self.model["interface"])
        print("Re-engaging kernel mode driver")
        # reattach the device to the OS kernel
        self.model["dev"].attach_kernel_driver(self.model["interface"])

    # define our clear function 
    def clear(self): 
  
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
  
     #for ma    c and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear')

def getConfigDataStructure_dictionary(self):
	"""Define the config for finding the SBC and talking to it"""
	return {
	        "author" : "Darkstrumn"
	        ,"version" : "0.6"
	        ,"vendor_id" : 0x0a7b
	        ,"product_id" : 0xd000
	        ,"usb_sbc_configuration" : 0
	        ,"usb_sbc_interface" : 0
	        ,"usb_sbc_setting" : 0
	        ,"usb_endpoint_reader" : 0
	        ,"usb_endpoint_writer" : 1
	        ,"normal_intensity" : 1
	        ,"bold_intensity" : 7
	        ,"emergency_intensity" : 15
	        ,"refresh_rate" : 60
	        }
#---------

def getDataPacketStructure_dictionary(self):
	"""Define the usb data packet particulars"""
	packets = (
		"Const_00_0"
		, "Const_1A"
		, "Buttons0"
		, "Buttons1"
		, "Buttons2"
		, "Buttons3"
		, "Buttons4"
		, "Const_00_1"
		, "Aiming_X1"
		, "Aiming_X2"
		, "Aiming_Y1"
		, "Aiming_Y2"
		, "Rotation1"
		, "Rotation2"
		, "SightChange_X1"
		, "SightChange_X2"
		, "SightChange_Y1"
		, "SightChange_Y2"
		, "Sidestep1"
		, "Sidestep2"
		, "Brake1"
		, "Brake2"
		, "Throttle1"
		, "Throttle2"
		, "Tuner"
		, "Gear"
		, "Const_00_2"
		, "Const_00_3"
		, "Const_00_4"
		, "Const_00_5"
		, "Const_00_6"
		, "Const_00_7"
		)
        # Enumerate and make into dictionary for consistancey
	result = { str( x + 1 ) : str( packets[x] ) for x, _ in enumerate(packets) }
	return result
#---------

def getControllerDataStructure_dictionary(self):
	"""Define the basic controller datastructure and particulars"""
	controller = {
        "RightJoythumbTrigger" : { "Section" : "Triggers", "Group" : "RightJoystick", "Control" : "Main Weapon", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 7}
        ,"RightJoyfingerTrigger" : { "Section" : "Triggers", "Group" : "RightJoystick", "Control" : "Secondary Weapon", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 6 }
        ,"RightJoylockOn" : { "Section" : "Triggers", "Group" : "RightJoystick", "Control" : "Lock-On", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 5 }

        ,"Eject" : { "Section" : "Button", "Group" : "CommandColumn", "Control" : "Eject", "Id" : None, "Led" : { "Id" : 3, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 4 }
        ,"CockpitHatch" : {  "Section" : "Buttons", "Group" : "CommandColumn", "Control" : "Cockpit Hatch", "Id" : None, "Led" : { "Id" : 4, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 3 }
        ,"Ignition" : {  "Section" : "Buttons", "Group" : "CommandColumn", "Control" : "Ignition", "Id" : None, "Led" : { "Id" : 5, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"Start"  : {  "Section" : "Buttons", "Group" : "CommandColumn", "Control" : "Start", "Id" : None, "Led" : { "Id" : 6, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons"  ), "DataFormat" : "08b", "mask" : 1 }

        ,"MmcOpenClose" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Open/Close", "Id" : None, "Led" : { "Id" :  7, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons0"  ), "DataFormat" : "08b", "mask" : 0 }
        ,"MmcMapZoomInOut" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Map Zoom In/Out", "Id" : None, "Led" : { "Id" : 8, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 7 }
        ,"MmcModeSelect" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Mode Select", "Id" : None, "Led" : { "Id" : 9, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 6 }
        ,"MmcSubMonitor" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Sub Monitor Mode Select", "Id" : None, "Led" : { "Id" : 10, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 5 }
        ,"MmcZoomIn" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Zoom In", "Id" : None, "Led" : { "Id" : 11, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 4 }
        ,"MmcZoomOut" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Zoom Out", "Id" : None, "Led" : { "Id" : 12, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 3 }

        ,"FxForcastShootingSystem" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "FSS - Forcast Shooting System", "Id" : None, "Led" : { "Id" : 13, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"FxManipulator" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Manipulator", "Id" : None, "Led" : { "Id" : 15, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 1 }
        ,"FxLineColourChange" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Line Colour Change", "Id" : None, "Led" : { "Id" : 16, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons1"  ), "DataFormat" : "08b", "mask" : 0 }

        ,"WcWashing" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Washing", "Id" : None, "Led" : { "Id" : 17, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 7 }
        ,"WcExstinguisher" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Exstinguisher", "Id" : None, "Led" : { "Id" : 18, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 6 }
        ,"WcChaff" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Chaff", "Id" : None, "Led" : { "Id" : 19, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 5 }

        ,"FxTankDetach" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Tank Detach", "Id" : None, "Led" : { "Id" : 20, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 4 }
        ,"FxOverride" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Override", "Id" : None, "Led" : { "Id" : 21, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 3 }
        ,"FxNightScope" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Night Scope", "Id" : None, "Led" : { "Id" : 22, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"FxFunctionF1" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "F1", "Id" : None, "Led" : { "Id" : 23, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 1 }
        ,"FxFunctionF2" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "F2", "Id" : None, "Led" : { "Id" : 24, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons2"  ), "DataFormat" : "08b", "mask" : 0 }
        ,"FxFunctionF3" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "F3", "Id" : None, "Led" : { "Id" : 25, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 7 }

        ,"WcMain" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Main", "Id" : None, "Led" : { "Id" : 26, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 6 }
        ,"WcSub" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Sub", "Id" : None, "Led" : { "Id" : 27, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 5 }
        ,"WcMagazineChange" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Magazine Change", "Id" : None, "Led" : { "Id" : 28, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 4 }

        ,"Comm1" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 1", "Id" : None, "Led" : { "Id" : 29, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 3 }
        ,"Comm2" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 2", "Id" : None, "Led" : { "Id" : 30, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"Comm3" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 3", "Id" : None, "Led" : { "Id" : 31, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 1 }
        ,"Comm4" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 4", "Id" : None, "Led" : { "Id" : 32, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons3"  ), "DataFormat" : "08b", "mask" : 0 }
        ,"Comm5" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 5", "Id" : None, "Led" : { "Id" : 33, "Init" : 1, "Intensity" : 1, "State" : "0" }, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 7 }

        ,"ToggleFilter" : { "Section" : "Toggles", "Group" : "", "Control" : "Filter Control System", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 4 }
        ,"ToggleOxygenSupply" : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "Oxygen Supply System", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 5 }
        ,"ToggleFuelFlowRate" : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "Fuel Flow Rate", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 3 }
        ,"ToggleBufferMaterial" : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "Buffer Material", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 2 }
        ,"ToggleVTLocation"  : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "VT-Location Measurement", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Buttons4"  ), "DataFormat" : "08b", "mask" : 1 }

        ,"LeftJoySightChange" : { "Section" : "Analogs", "Group" : "LeftJoystick", "Control" : "Sight Change", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "SightChange_X1", "SightChange_X2", "SightChange_Y1", "SightChange_Y2" ), "DataFormat" : "08b", "mask" : None }
        ,"LeftJoyRotation" : { "Section" : "Analogs", "Group" : "LeftJoystick", "Control" : "Rotation", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Rotation1", "Rotation2" ), "DataFormat" : "08b", "mask" : None }
        ,"RightJoyAiming" : { "Section" : "Analogs", "Group" : "RightJoystick", "Control" : "Aiming", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Aiming_X1", "Aiming_X2", "Aiming_Y1", "Aiming_Y2" ), "DataFormat" : "08b", "mask" : None }

        ,"SidestepPedal" : { "Section" : "Analogs", "Group" : "Pedals", "Control" : "Side step", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Sidestep1", "Sidestep2" ), "DataFormat" : "d", "mask" : 0 }
        ,"BrakePedal" : { "Section" : "Analogs", "Group" : "Pedals", "Control" : "Brake", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Brake1", "Brake2"  ), "DataFormat" : "d", "mask" : 0 }
        ,"ThrottlePedal" : { "Section" : "Analogs", "Group" : "Pedals", "Control" : "Throttle", "Id" : None, "Min" : -32767, "Max" : 32768, "packets" : ( "Throttle1", "Throttle2" ), "DataFormat" : "d", "mask" : 0 }

        ,"Tuner" : { "Section" : "Tuner", "Group" : "Tuner", "Control" : "Tuner Dial", "Id" : None, "Min" : 0, "Max" : 1, "packets" : ( "Tuner"  ), "DataFormat" : "d", "mask" : 0 }

        ,"Gear" : { "Section" : "Gear", "Group" : "Gear", "Control" : "Gear Shifter", "Id" : None, "Min" : -2, "Max" : 5, "packets" : ( "Gear"  ), "DataFormat" : "d", "mask" : 0
                ,"Gears" : {
                        "5" : { "Gear" : "5", "Led" : { "Id" : 41, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "5", "To" : "5", "packet" : "Gear" } },
                        "4" : { "Gear" : "4", "Led" : { "Id" : 40, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "4", "To" : "4", "packet" : "Gear" } },
                        "3" : { "Gear" : "3", "Led" : { "Id" : 39, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "3", "To" : "3", "packet" : "Gear" } },
                        "2" : { "Gear" : "2", "Led" : { "Id" : 38, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "2", "To" : "2", "packet" : "Gear" } },
                        "1" : { "Gear" : "1", "Led" : { "Id" : 37, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "1", "To" : "1", "packet" : "Gear" } },
                        "-1" : { "Gear" : "N", "Led" : { "Id" : 36, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" : { "From" : "-1", "To" : "N", "packet" : "Gear" } },
                        "-2" : { "Gear" : "R", "Led" : { "Id" : 35, "Init" : 1, "Intensity" : 1, "State" : "0" }, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1, "Transform" :  { "From" : "-2", "To" : "R", "packet" : "Gear" } }
                        }
                }
        }

	enumId = 0

	for control in controller:
		# Enumerate the model
		enumId += 1
		controller[control]["Id"] = enumId
		
		# Add state properties to the following control types
		for controlType in ("Buttone", "Triggers", "Toggles"):

			if( controller[control]["Section"] == controlType ):
				controller[control]["State"] = { "enum" : enumId, "CurrentState" : False, "Changed" : False }
			else:
				controller[control]["State"] = { "enum" : enumId, "CurrentState" : None, "Changed" : False }

	return controller
#---------

def get_sbc_model_dictionary(self):
	"""Define the model for the SBC device"""
	return {
        "config" : get_config_data_structure_dictionary()
        ,"data_dackets": get_data_packet_structure_dictionary()
        ,"dontroller" : get_controller_data_structure_dictionary()
		,"dev" : {
			"device" : None
			, "usb_sbc_configuration" : None
			, "usb_endpoint_reader" : None
			, "usb_endpoint_writer" : None
			, "" : None,}
        }
#---------
#-------------------------------------------------------------------------------
