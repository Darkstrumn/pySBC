#---------
def getConfigDataStructure_Dictionary():
	"""Define the config for finding the SBC and talking to it"""
	return {
	        "Author" : "Darkstrumn"
	        ,"Version" : "0.6"
	        ,"_VENDORID" : 0x0a7b
	        ,"_PRODUCTID" : 0xd000
	        ,"_INTERFACE_SBC" : 0
	        ,"_SETTING_SBC" : 0
	        ,"_ENDPOINT_READER" : 0
	        ,"_ENDPOINT_WRITER" : 1
	        ,"normalIntensity" : 1
	        ,"boldIntensity" : 7
	        ,"normalIntensity" : 15
	        ,"boldIntensity" : 15
	        ,"emergencyIntensity" : 15
	        ,"refreshRate" : 60
	        }
#---------

def getDataPacketStructure_Dictionary():
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

def getControllerDataStructure_Dictionary():
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
#		print ( str(control) )
		# Enumerate the model
		enumId += 1
		controller[control]["Id"] = enumId
		
		# Add state properties to the following control types
		for controlType in ("Buttone", "Triggers", "Toggles"):

			if( controller[control]["Section"] == controlType ):
				controller[control]["State"] = { "enum" : enumId, "CurrentState" : False, "Changed" : False }
			else:
				controller[control]["State"] = { "enum" : enumId, "CurrentState" : None, "Changed" : False }

		# diagnostics
#		for attribute in controller[control]:
#
#			if(controller[control]["Section"] == "Buttons"):
#				print ( "       :\\" + str(attribute) + ":: " + str(controller[control][attribute]) )

	return controller
#---------

def getSbcModel_Dictionary():
	"""Define the model for the SBC device"""
	return {
        "Config" : getConfigDataStructure_Dictionary()
        ,"DataPackets": getDataPacketStructure_Dictionary()
        ,"Controller" : getControllerDataStructure_Dictionary()
        }
#---------


#---------
#---------
#---------
#---------

#Diagnostics
def diagnostics_Test():
    """Diagnostics"""

    sbc = getSbcModel_Dictionary()
    print("! Steel Battalions Controller- v " + sbc["Config"]["Version"] + " - Driver written by: " + sbc["Config"]["Author"] + " !") 
    for item in list( map( lambda x: "(" + str(x) + "):" + str(sbc["DataPackets"][x]), sbc["DataPackets"] ) ):
        print ( str(item) )
#	for model in sbc:
#		#print ( "Model:\\" + str(model) + "::")
#		print ( "-----------------------------")
#		for modelNode in sbc[model]:
#			print ( "Model:\\" + str(model) + "\\\\" + str(modelNode) + "::" + str(sbc[model][modelNode]))
#---------

diagnostics_Test()

