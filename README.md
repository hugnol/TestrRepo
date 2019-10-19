WHAT TO DO:

- Functions + Descriptions
- First program example.
- How to give commands.
- Image Processing



# Dobot Magician with Python - Starter Guide
*Disclaimer: This guide will cover starting out with the DoBot Magician using Windows. Using other operating systems won't guarantee that the methods used in this guide will work.*

The [DoBot Magician](https://www.dobot.cc/dobot-magician/product-overview.html) is a fun mechanical arm with alot of functionallity. Thanks to the large array of peripherals available it can do many tasks if operated correctly. The main means of controling the DoBot Magician is the [Magician Studio](https://www.dobot.cc/downloadcenter/dobot-magician.html#most-download) application and it is easy to use for people of any age. 

This guide will not focus on how to operate the DoBot Magician through the Magician Studio, but instead through Python. Using your own code to control the DoBot Magician opens up for much more freedom, allowing things like automation and very calibrated movements for intricate tasks. If you are not familiar with Python, don't worry! It is powerfull but easy to learn.

## Table of Content
* [Starting Out](#starting-out)
* [Test Program](#test-program)
* [Important Functions](#important-functions)
   * [Connect to the Dobot](#connect-to-the-dobot)
   * [Queue Manipulation](#queue-manipulation)
   * [Setting Parameters](#setting-parameters)
   * [Movement Commands](#movement-commands)
   * [Peripherals](#peripherals)
* [Download Links](#download-links)


## Starting Out
To get started you'll need an IDE which you can use to work with Python. There is no need to use a specific one so go with the IDE that you are the most comfortable with and has support for Python. For the functions created in this guide [Atom](https://atom.io/) was used, but it is not necessary as an IDE like Visual Studio Code or similar would also suffice.

To communicate with the DoBot we need to download the API supplied by DOBOT for the DoBot Magician. The file you are looking for is [DobotDemov2.0](https://www.dobot.cc/downloadcenter/dobot-magician.html?sub_cat=72#sub-download). From this website you're also required to download and install the [Magician Studio](https://www.dobot.cc/downloadcenter/dobot-magician.html). We will not use the application itself, but the installation process contains some dependencies required to communicate with the dobot from our third party application.

You will also need [Python](https://www.python.org/). Python is also available for download through the Microsoft Store.


## Test Program
After extracting the contents of the DobotDemoV2.0 folder we find a list of more folders. These are demos for the available languages which can be used to operate the Dobot. The one we are going to use in this guide is the DobotDemoForPython. In this folder we can find a file called DobotControl.py. This file contains a test program which uses a connection to the Dobot through USB which makes it do a couple of gestures. If you have installed Python and Magician Studio correctly you should be able to run the file without any problems, as long as you are connected to the Dobot through any of your USB ports. 


## Important Functions

To understand how to use the Dobot more efficiently we have to look into what types of commands you can use to control it. Many of these functions are accessable inside the DoBotControl file, but theres also alot of them inside the DLL file  which is not being used. Here we will briefly go through some of the most important ones to get you started. If you want more indepth information it can be found in the [DoBot Magician API Description](https://www.dobot.cc/downloadcenter.html?sub_cat=72#sub-download).

We will import the DobotDLLType file in python with the local name dType, as they have done in the DobotControl file. All of the DLL functions will be accessed with the help of this module name. The reason this local name is used to access the functions is to keep the guide in line with the DobotControl file to make it easier to understand.

To have access to the library containing the functions, we have to load it into an object in out code. The function ```dType.load()``` will load the platform specific library and return it into an object which we will call *api*.

**Syntax**:
```python
api = dType.load()
```

### Connect to the Dobot
To connect to the Dobot we use the function *dType.ConnectDobot()*. The arguments in this function are the api object created with the ```dType.load()``` function, the port name for the Dobot and the baudrate. The port name will only affect you if you use multiple Dobots connected to the computer and if you only have one Dobot Magician connected then the port name doesnt have to be specified. More information can be found in the documentation.

**Syntax**:
```python
dType.ConnectDobot(api, portName, baudrate)
```

**Default Example**:
```python
dType.ConnectDobot(api, "", 115200)
```


To disconnect the Dobot, the function ```dType.DisconnectDobot()``` is used.

**Syntax**
```python
dType.DisconnectDobot(api)
```

### Queue Manipulation
There are functions which manipulates the command queue and functions that issue commands to the Dobot. You can operate the Dobot using the command queue, or just issue them directly. The difference is that the command queue can be filled up with commands and then executed in order, while without it the command will be executed directly after being called. To start off we will go through the mcommand queue manipulation functions.

The function ```dType.SetQueuedCmdStartExec()``` will start executing the commands in the queue one after another in order of inputting them. If no commands are in the queue, nothing will happen.

**Syntax**: 
```python
dType.SetQueuedCmdStartExec()
```

To stop executing the commands in the queue, you have to call ```dType.SetQueuedCmdStopExec()```. This will stop quering the Dobot, but if a command is currently running when the function is called, the command will finish its execution. The function *dType.SetQueuedCmdForceStopExec()* however, will force the command being executed to be forced to stop.

**Syntax**: 
```python
dType.SetQueuedCmdStopExec()
dType.SetQueuedCmdForceStopExec()
```

The command queue can also be cleared using the function *dType.SetQueuedCmdClear()*.

**Syntax**: 
```python
dType.SetQueuedCmdClear(api)
```

More queue manipulation functions are available in the documentation.


### Setting Parameters
Before we start issuing movement commands we need to set some parameters which specifies the velocity and acceleration of the joints. This is done using the function ```dType.SetPTPCommonParams()```. The function takes some arguments to specify the above. The first argument is the *api* object created with the load function. The second specifies the velocity ratio. The third specifies the acceleration ratio, and the last argument specifies if the function should be queued or not.

**Syntax**:
```python
dType.SetPTPCommonParams(api, v, a, isQueued)
```

**Default Example**:
```python
dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)
```

The home parameter specifies where the default stance of the Dobot Magician. Calling the home function then returns to this position. The arguments specifies the X and Y coordinates of the home location. Z is the height of the arm at this location and R is the rotation of the peripheral to return to. You can play around with the coordinates to find where you want the position to be. To return to the home position, use ```dType.SetHomeCmd()```. If the home function is called before setting parameters, the dobot will return to the default home location, otherwise it will go to the user specified location.

**Syntax**:
```python
dType.SetHomeParams(api, x, y, z, r, isQueued)
dType.SetHomeCmd(api, homeCmd, isQueued)
```

**Default Example**:
```python
dType.SetHomeParams(api, 250, 0, 50, 0, isQueued = 1)
dType.SetHomeCmd(api, homeCmd = 0, isQueued = 1)
```

### Movement Commands
There are two major ways of moving the Dobot Magicians arm. The first is using X, Y and Z coordinates and the other is based on joint orientation. We will be using X, Y and Z in this guide, but if you want to use the joints please refer to the documentation.

The main way of moving the Dobot to a location is through the function ```dType.SetPTPCmd()```. This function requires X, Y, Z and R coordinates and rotation. We also specify which movement mode to be used in the function and if we want to queue it or not. Keep in mind that the Dobot Magician will lock up if you move the arm to a location which it's unable to reach.

**Syntax**:
```python
dType.SetPTPCmd(api, dType.movementMode, X, Y, Z, R, isQueued)
```

**Default Example**
```python
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, X, Y, Z, R, isQueued = 1)
```

After a command is issued, use the ```dType.QueuedCmdStartExec()``` function to start execution explained above. It is important when not using the queue to use the ```dType.dSleep()``` function to allow for commands to fully execute before forcing a new one, otherwise the outcome might not be satisfactory.


### Peripherals
The Dobot Magician has alot of different peripherals in its repository, allowing it to do a bunch of fun things. Thins like using a suction cup to grab items, or grabbing items with a claw and many, many more! To activate the suction cup we use the function ```dType.SetEndEffectorSuctionCup()```.

**Syntax**:
```python
dType.SetEndEffectorSuctionCup(api, enableControl, suction, isQueued)
```

The enableControl argument enables or disables the pump. Suction enables outtake or intake. For more peripheral information, refer to the documentation.


There file named DobotArm.py contains wrapper functions which can be used as an example when making your own program.


## Download Links
[Atom](https://atom.io/) - IDE referensed above.

[Magician Studio](https://www.dobot.cc/downloadcenter/dobot-magician.html) - Dobot Application and Driver

[DobotDemoV2.0](https://www.dobot.cc/downloadcenter/dobot-magician.html?sub_cat=72#sub-download) - Code Examples

[Dobot API Manual](https://www.dobot.cc/downloadcenter/dobot-magician.html?sub_cat=72#sub-download) - Manual for API 

[Python](https://www.python.org/) - Language used in this guide

*Python installation instructions are available at their website. Other languages are also available but won't be present in this guide.*




