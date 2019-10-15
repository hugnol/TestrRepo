#--Functions--

def startMessage():
    print("\nDoBot Application 1.2")
    print("--Fast Input--")
    print("q:    Exit Application ")
    print("home: 250,0")
    print("---------------")
    print("\n--Enter Requested Coordinates in format x,y--")

#----------------<Input Functions>-----------------#

#1. -------Check if Input is in range-------#
def rangeCheck(splitCoordinates):
    if(int(splitCoordinates[0])):
        splitCoordinates[0] = int(splitCoordinates[0],10)
        if(splitCoordinates[0] > 250 or splitCoordinates[0] < 70):
            return False
    if(int(splitCoordinates[1])):
        splitCoordinates[1] = int(splitCoordinates[1],10)
        if(splitCoordinates[1] > 200 or splitCoordinates[1] < -200):
            return False
    else:
        return False
    return True

#2. -------Get User Input-------#
def getXY():
    while True:
        inputCoordinates = input("\n$ ")
        if(inputCoordinates == "q"):
            return inputCoordinates

        if "," not in inputCoordinates:
            print("\n$ Invalid Input")
            continue

        splitCoordinates = inputCoordinates.split(",")
        if(rangeCheck(splitCoordinates)):
            splitCoordinates = [int(i) for i in splitCoordinates]
            return splitCoordinates
        else:
            print("\n$ Invalid Input")
#---------------------------------------------------#


#----Robot Movement Functions----#

def suctionEnable(api,dType):
    lastIndex = dType.SetEndEffectorSuctionCup(api, True, True, isQueued = 0)[0]

    dType.SetQueuedCmdStartExec(api)
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(200)
    dType.SetQueuedCmdStopExec(api)

def suctionDisable(api,dType):
    lastIndex = dType.SetEndEffectorSuctionCup(api, True, False, isQueued = 0)[0]

    dType.SetQueuedCmdStartExec(api)
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(200)
    dType.SetQueuedCmdStopExec(api)

def pick(api,dType,currentX,currentY,action):
    if(action == 1):
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, currentX, currentY, -60, 0)[0]

        dType.SetQueuedCmdStartExec(api)
        while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
            dType.dSleep(100)
            dType.SetQueuedCmdStopExec(api)

    elif(action == 0):
        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, currentX, currentY, 50, 0)[0]

        dType.SetQueuedCmdStartExec(api)
        while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
            dType.dSleep(100)
            dType.SetQueuedCmdStopExec(api)

#--Move To X,Y--#
def moveArmXY(api,dType,x, y):
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x, y, 50, 0)[0]

    dType.SetQueuedCmdStartExec(api)
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)
    dType.SetQueuedCmdStopExec(api)
#----------#


#--Enter Manual Mode--
def manualMode(api,dType):
    startMessage()
    while True:
        splitCoordinates = getXY()
        if(splitCoordinates == "q"):
            moveArmXY(api,dType,250,0)
            return
        moveArmXY(api,dType,splitCoordinates[0],splitCoordinates[1])
    return

#--Automatic Mode--
def automaticMode():
    print("PlaceHolder")
    return
#------------------
#-------Test Functions------#

def succtionTest(api, dType):
    moveArmXY(api,dType,250,0)
    moveArmXY(api,dType,250,100)
    pick(api,dType,250,100, 1)
    suctionEnable(api,dType)
    pick(api,dType,250,100, 0)
    moveArmXY(api,dType,250,0)
    pick(api,dType,250,0, 1)
    suctionDisable(api,dType)
    pick(api,dType,250,0, 0)
