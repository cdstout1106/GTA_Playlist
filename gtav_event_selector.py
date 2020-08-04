import random

vehicleClassList = ["MotorCycles","Compacts","Coupes","Sedans","Sports","Sports Classics","Super","Muscle","Off-Road","SUVs","Vans","Industrial","Commercial","Utility","Military","Boats","Planes","Helicopters","Cycles","Service"]
raceList = []
numberOfLaps = [1,2,3,4,5,6,7,8,9,10]
numberOfRounds = [1,2,3,4,5]
eventSelectionList = []
TrafficSelectionList = ["Default","Off","Low","Medium","High"]
weatherSelectionList = ["Current","Bright","Raining","Smog","Clear","Clouds","Overcast","Thunder","Foggy"]
raceType = ["Standard","GTA","Rally","Non-Contact","Default"]
timeOfDay = ["Current","Default","Morning","Noon","Night"]
wantedLevels = ["On","Off","Default"]
customVehicles = ["On","Off","Default"]
cameraLock = ["Default","First Person","Third Person"]




print(random.choice(vehicleClassList))