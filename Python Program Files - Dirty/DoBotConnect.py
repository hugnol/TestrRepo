import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}

#---Connect To Dobot---#
def connectToDobot(api):
    state = dType.ConnectDobot(api, "", 115200)[0]

    boolState = True
    #If DoBot causes no error and is available
    if (state == dType.DobotConnect.DobotConnect_NoError):
        print("Connect status:",CON_STR[state])
        #Clean Command Queued
        dType.SetQueuedCmdClear(api)

        #Async Motion Params Setting
        dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
        dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
        dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

        #Async Home
        dType.SetHOMECmd(api, temp = 0, isQueued = 1)
    else:
        boolState = False
    return boolState

#---DoBot Disconnect---#
def disconnectToDoBot(api,dType):
    dType.DisconnectDobot(api)
#------------------------------------------------------
