dataPackets = ["Const_00_0", "Const_1A", "Buttons0", "Buttons1", "Buttons2", "Buttons3", "Buttons4", "Const_00_1", "Aiming_X1", "Aiming_X2", "Aiming_Y1", "Aiming_Y2", "Rotation1", "Rotation2", "Sight_X1", "Sight_X2", "Sight_Y1", "Sight_Y2", "Sidestep1", "Sidestep2", "Brake1", "Brake2", "Throttle1s", "Throttle2", "TunerDial", "GearShifter",["Const_00_2", ["Const_00_3", ["Const_00_4", ["Const_00_5", ["Const_00_6", ["Const_00_7"]
contoller = {
        "RightJoythumbTrigger" : { "Section" : "Triggers", "Group" : "RightJoystick", "Control" : "Main Weapon", "Id" : None, "Min" : 0, "Max" : 1 }
        ,"RightJoyfingerTrigger" : { "Section" : "Triggers", "Group" : "RightJoystick", "Control" : "Secondary Weapon", "Id" : None, "Min" : 0, "Max" : 1 }
        ,"RightJoylockOn" : { "Section" : "Triggers", "Group" : "RightJoystick", "Control" : "Lock-On", "Id" : None, "Min" : 0, "Max" : 1}
        ,"Eject" : { "Section" : "Button", "Group" : "CommandColumn", "Control" : "Eject", "Id" : None, "Led" : 3, "Min" : 0, "Max" : 1 }
        ,"CockpitHatch" : {  "Section" : "Buttons", "Group" : "CommandColumn", "Control" : "Cockpit Hatch", "Id" : None, "Led" : 4 }
        ,"Ignition" : {  "Section" : "Buttons", "Group" : "CommandColumn", "Control" : "Ignition", "Id" : None, "Led" : 5, "Min" : 0, "Max" : 1 }
        ,"Start"  : {  "Section" : "Buttons", "Group" : "CommandColumn", "Control" : "Start", "Id" : None, "Led" : 6, "Min" : 0, "Max" : 1 }
        ,"MmcOpenClose" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Open/Close", "Id" : None, "Led" :  7, "Min" : 0, "Max" : 1 }
        ,"MmcMapZoomInOut" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Map Zoom In/Out", "Id" : None, "Led" : 8, "Min" : 0, "Max" : 1 }
        ,"MmcModeSelect" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Mode Select", "Id" : None, "Led" : 9, "Min" : 0, "Max" : 1 }
        ,"MmcSubMonitor" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Sub Monitor Mode Select", "Id" : None, "Led" : 10, "Min" : 0, "Max" : 1 }
        ,"MmcZoomIn" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Zoom In", "Id" : None, "Led" : 11, "Min" : 0, "Max" : 1 }
        ,"MmcZoomOut" : {  "Section" : "Buttons", "Group" : "MultiMonitorControls", "Control" : "Zoom Out", "Id" : None, "Led" : 12, "Min" : 0, "Max" : 1 }
        ,"FxForcastShootingSystem" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "FSS - Forcast Shooting System", "Id" : None, "Led" : 13, "Min" : 0, "Max" : 1 }
        ,"FxManipulator" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Manipulator", "Id" : None, "Led" : 15, "Min" : 0, "Max" : 1 }
        ,"FxLineColourChange" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Line Colour Change", "Id" : None, "Led" : 16, "Min" : 0, "Max" : 1 }
        ,"WcWashing" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Washing", "Id" : None, "Led" : 17, "Min" : 0, "Max" : 1 }
        ,"WcExstinguisher" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Exstinguisher", "Id" : None, "Led" : 18, "Min" : 0, "Max" : 1 }
        ,"WcChaff" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Chaff", "Id" : None, "Led" : 19, "Min" : 0, "Max" : 1 }
        ,"FxTankDetach" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Tank Detach", "Id" : None, "Led" : 20, "Min" : 0, "Max" : 1 }
        ,"FxOverride" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Override", "Id" : None, "Led" : 21, "Min" : 0, "Max" : 1 }
        ,"FxNightScope" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "Night Scope", "Id" : None, "Led" : 22, "Min" : 0, "Max" : 1 }
        ,"FxFunctionF1" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "F1", "Id" : None, "Led" : 23, "Min" : 0, "Max" : 1 }
        ,"FxFunctionF2" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "F2", "Id" : None, "Led" : 24, "Min" : 0, "Max" : 1 }
        ,"FxFunctionF3" : {  "Section" : "Buttons", "Group" : "Functions", "Control" : "F3", "Id" : None, "Led" : 25, "Min" : 0, "Max" : 1 }
        ,"WcMain" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Main", "Id" : None, "Led" : 26, "Min" : 0, "Max" : 1 }
        ,"WcSub" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Sub", "Id" : None, "Led" : 27, "Min" : 0, "Max" : 1 }
        ,"WcMagazineChange" : {  "Section" : "Buttons", "Group" : "WeaponControls", "Control" : "Magazine Change", "Id" : None, "Led" : 28, "Min" : 0, "Max" : 1 }
        ,"Comm1" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 1", "Id" : None, "Led" : 29, "Min" : 0, "Max" : 1 }
        ,"Comm2" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 2", "Id" : None, "Led" : 30, "Min" : 0, "Max" : 1 }
        ,"Comm3" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 3", "Id" : None, "Led" : 31, "Min" : 0, "Max" : 1 }
        ,"Comm4" : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 4", "Id" : None, "Led" : 32, "Min" : 0, "Max" : 1 }
        ,"Comm5"  : {  "Section" : "Buttons", "Group" : "Comms", "Control" : "Comm 5", "Id" : None, "Led" : 33, "Min" : 0, "Max" : 1 }
        ,"LeftJoySightChange" : { "Section" : "Analogs", "Group" : "LeftJoystick", "Control" : "Sight Change", "Id" : None, "Min" : 0, "Max" : 1 }
        ,"ToggleFilter" : { "Section" : "Toggles", "Group" : "", "Control" : "Filter Control System", "Id" : None, "Min" : 0, "Max" : 1 }
        ,"ToggleOxygenSupply" : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "Oxygen Supply System", "Id" : None, "Min" : 0, "Max" : 1 }
        ,"ToggleFuelFlowRate" : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "Fuel Flow Rate", "Id" : None, "Min" : 0, "Max" : 1 }
        ,"ToggleBufferMaterial" : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "Buffer Material", "Id" : None, "Min" : 0, "Max" : 1 }
        ,"ToggleVTLocation"  : { "Section" : "Toggles", "Group" : "Toggles", "Control" : "VT-Location Measurement", "Id" : None, "Min" : 0, "Max" : 1 }
        ,"TunerDial" : { "Section" : "Tuner", "Group" : "Tuner", "Control" : "Tuner Dial", "Id" : None, "Min" : 0, "Max" : 1 }
	,"Shifter" : { "Section" : "Slider", "Group" : "Shifter", "Control" : "Gear", "Id" : None, "Min" : -2, "Max" : 5,
              "GearLever" : {
                  "5" : { "Gear" : "5", "Led" : 41, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                  "4" : { "Gear" : "4", "Led" : 40, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                  "3" : { "Gear" : "3", "Led" : 39, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                  "2" : { "Gear" : "2", "Led" : 38, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                  "1" : { "Gear" : "1", "Led" : 37, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                  "-1" : { "Gear" : "N", "Led" : 36, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                  "-2" : { "Gear" : "R", "Led" : 35, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 }
                  }
              }
        ,"LeftJoyRotation" : { "Section" : "Analogs", "Group" : "LeftJoystick", "Control" : "Rotation", "Id" : None, "Min" : -32767, "Max" : 32768 }
        ,"RightJoyAiming" : { "Section" : "Analogs", "Group" : "RightJoystick", "Control" : "Aiming", "Id" : None, "Min" : -32767, "Max" : 32768 }
        ,"SidestepPedal" : { "Section" : "Analogs", "Group" : "Pedals", "Control" : "Side step", "Id" : None, "Min" : -32767, "Max" : 32768 }
        ,"BrakePedal" : { "Section" : "Analogs", "Group" : "Pedals", "Control" : "Brake", "Id" : None, "Min" : -32767, "Max" : 32768 }
        ,"ThrottlePedal" : { "Section" : "Analogs", "Group" : "Pedals", "Control" : "Throttle", "Id" : None, "Min" : -32767, "Max" : 32768 }
        }

enumId = 0

for control in controller:

	enumId += 1
	print ( str(control) )

	if( controller[control].get("Led") != None ):
		temp = controller[control]["Led"]

		if(control == "Eject"):
			intensity = 15
		else:
			intensity = 1
		
		if(controller[control]["Group"] == "Comms"):
			intensity = 7

		controller[control]["Led"] = {"Led" : temp, "DefaultIntensity" : intensity, "Intensity" : intensity}

	for controlType in ("Buttone", "Triggers", "Toggles"):

		controller[control]["Id"] = enumId

		if( controller[control]["Section"] == controlType ):
			controller[control]["State"] = { "enum" : enumId, "CurrentState" : False, "Changed" : False }
		else:
			controller[control]["State"] = { "enum" : enumId, "CurrentState" : None, "Changed" : False }

	for attribute in controller[control]:

		print ( "	:\\" + str(attribute) + ":: " + str(controller[control][attribute]) )


#    for group in controller[section]:
#        print ("   []" + group)
#        for control in controller[section][group]:
#            print ("        :" + control)
#            controller[section][group][control]["Name"] = control
#            if(str(controller[section][group][control].get("Led")) != "None"):
#                controller[section][group][control]["Led"] = controller[section][group][control]["Led"]
#                controller[section][group][control]["DefaultIntensity"] = 1
#                controller[section][group][control]["Intensity"] = 1
#                controller[section][group][control]["Min"] = 0
#                controller[section][group][control]["Max"] = 1
#
#            else:
#                controller[section][group][control]["Led"] = None
#                controller[section][group][control]["DefaultIntensity"] = None
#                controller[section][group][control]["Intensity"] = None
#                if(str(section) != "Button"):
#                    controller[section][group][control]["Min"] = 0
#                    controller[section][group][control]["Max"] = 1
#                if(str(section) != "Analog"):
#                    if(str(group) != ""):
#                        controller[section][group][control]["Min"] = 0
#                        controller[section][group][control]["Max"] = 255


#            for attribute in controller[section][group][control]:
#                print ("            +" + attribute + " = " + str(controller[section][group][control].get(attribute)))

