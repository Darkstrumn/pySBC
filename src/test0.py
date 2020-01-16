index = 0
inputs = {
	"buttons" : {
    "RightJoystick" : {
    	"RightJoythumb_trigger" : {}
    	,"RightJoyfinger_trigger" : {}
    	,"RightJoylock_on" : {}
    	}
    ,"CommandColumn" : {
        "Eject" : { "Led" : 3 }
        ,"CockpitHatch" : { "Led" : 4 }
        ,"Ignition" : { "Led" : 5 }
        ,"Start"  : { "Led" : 6 }
    	}
    ,"MultiMonitorControls" : {
        "MmcOpenClose" : { "Led" :  7}
        ,"MmcMapZoomInOut" : { "Led" : 8 }
        ,"MmcModeSelect" : { "Led" : 9 }
        ,"MmcSubMonitor" : { "Led" : 10 }
        ,"MmcZoomIn" : { "Led" : 11 }
        ,"MmcZoomOut" : { "Led" : 12 }
    	}
    ,"Functions" : {
        "FxForcastShootingSystem" : { "Led" : 13 }
        ,"FxManipulator" : { "Led" : 15 }
        ,"FxLineColourChange" : { "Led" : 16 }
        ,"FxTankDetach" : { "Led" : 20 }
        ,"FxOverride" : { "Led" : 21 }
        ,"FxNightScope" : { "Led" : 22 }
        ,"FxFunctionF1" : { "Led" : 23 }
        ,"FxFunctionF2" : { "Led" : 24 }
        ,"FxFunctionF3" : { "Led" : 25 }
    	}
    ,"ToggleSwitches" : {
    	"ToggleOxygenSupply" : {}
    	,"ToggleFilter" : {}
    	,"ToggleFuelFlowRate" : {}
    	,"ToggleBufferMaterial" : {}
    	,"ToggleVTLocation"  : {}
    	}
    ,"Comms" : {
        "Comm1" : { "Led" : 29 }
        ,"Comm2" : { "Led" : 30 }
        ,"Comm3" : { "Led" : 31 }
        ,"Comm4" : { "Led" : 32 }
        ,"Comm5"  : { "Led" : 33 }
    	}
    ,"WeaponControls" : {
        "WcWashing" : { "Led" : 17 }
        ,"WcExstinguisher" : { "Led" : 18 }
        ,"WcChaff" : { "Led" : 19 }
        ,"WcMain" : { "Led" : 26 }
        ,"WcSub" : { "Led" : 27 }
        ,"WcMagazineChange" : { "Led" : 28 }
    	}
		}
	,"Analogs" : {
		"LeftJoystick" : {
                    "LeftJoyRotation" : { "Min" : 0, "Max" : "" }
			,"LeftJoySight" : {}
			},
		"RightJoystick" : {
			"RightJoyAiming" : {}
			},
		"Tuner" : {
			"Tuner_dial" : {}
			},
		"Shifter" : {
			"GearLever" : {
                            "Gear5" : { "Gear" : "5", "Led" : 41, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                            "Gear4" : { "Gear" : "4", "Led" : 40, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                            "Gear3" : { "Gear" : "3", "Led" : 39, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                            "Gear2" : { "Gear" : "2", "Led" : 38, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                            "Gear1" : { "Gear" : "1", "Led" : 37, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                            "GearN" : { "Gear" : "N", "Led" : 36, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                            "GearR" : { "Gear" : "R", "Led" : 35, "DefaultIntensity" : 1, "Intensity" : 1, "Min" : 0, "Max" : 1 },
                            }
			},
		"Pedals" : {
			"SidestepPedal" : {}
			,"BrakePedal" : {}
			,"ThrottlePedal" : {}
			}
		}
	}
#    inputs[item]={item: { "Name" : "\"" + item + "\"" } for x in item}
for section in inputs:
    print ("\n***Inputs: " + section)
    print ("------------------------")
    for group in inputs[section]:
        print ("   []" + group)
        for control in inputs[section][group]:
            print ("        :" + control)
            inputs[section][group][control]["Name"] = control
            if(str(inputs[section][group][control].get("Led")) != "None"):
                inputs[section][group][control]["Led"] = inputs[section][group][control]["Led"]
                inputs[section][group][control]["DefaultIntensity"] = 1
                inputs[section][group][control]["Intensity"] = 1
                inputs[section][group][control]["Min"] = 0
                inputs[section][group][control]["Max"] = 1

            else:
                inputs[section][group][control]["Led"] = None
                inputs[section][group][control]["DefaultIntensity"] = None
                inputs[section][group][control]["Intensity"] = None
                if(str(section) != "Button"):
                    inputs[section][group][control]["Min"] = 0
                    inputs[section][group][control]["Max"] = 1
                if(str(section) != "Analog"):
                    if(str(group) != ""):
                        inputs[section][group][control]["Min"] = 0
                        inputs[section][group][control]["Max"] = 255
                

            for attribute in inputs[section][group][control]:
                print ("            +" + attribute + " = " + str(inputs[section][group][control].get(attribute)))

#for x in mydict:
#	print (x)
#	for y in mydict[x]:
#		print (y)
