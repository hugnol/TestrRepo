# Dobot Maigician with Python - Starter Guide

*Disclaimer: This guide will cover starting out with the DoBot Magician using Windows. No other operating system is guaranteed to work with the method bellow, but it will be similar.*

The [DoBot Magician](https://www.dobot.cc/dobot-magician/product-overview.html) is a fun mechanical arm with alot of functionallity. Thanks to the large array of peripherals available it can do many tasks if operated correctly. The main means of controling the DoBot Magician is the [Magician Studio](https://www.dobot.cc/downloadcenter/dobot-magician.html#most-download) application and it is easy to use for people of any age. 

This guide will not focus on how to operate the DoBot Magician through the Magician Studio, but instead through Python. Using your own code to control the DoBot Magician opens up for much more freedom, allowing things like automation and very calibrated movements for intricate tasks. If you are not familiar with Python, don't worry! It is powerfull but easy to learn.

## Starting Out

To get started you'll need an IDE which you can use to work with Python. There is no need to use a specific one so go with the IDE that you are the most comfortable with and has support for Python. For the functions created in this guide [Atom](https://atom.io/) was used, but it is not necessary.

To communicate with the DoBot we need to download the API supplied by DOBOT for the DoBot Magician. The file you are looking for is Dobot Demo v2.0 and can be found [here](https://www.dobot.cc/downloadcenter/dobot-magician.html?sub_cat=72#sub-download).

You will also need a copy of [Python](https://www.python.org/). Python is also available for download through the Microsoft Store. 

## Your first program

After extracting the contents of the DobotDemoV2.0 folder we find a list of more folders. The one we are going to use in this guide is the DobotDemoForPython. In this folder we can find a file called DobotControl.py. This file contains a test program which uses a connection to the Dobot through USB to make it do a couple of gestures. If you have installed Python correctly you should be able to run the file without any problems, as long as you are connected to the Dobot through any of your USB ports.
