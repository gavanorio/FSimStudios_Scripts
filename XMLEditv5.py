import ctypes
import os
import sys
import fileinput
import xml.etree.cElementTree as ET
from os.path import join
from winreg import *
from shutil import copyfile
import shutil

from ctypes.wintypes import MAX_PATH

dll = ctypes.windll.shell32
buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
    print(buf.value)
else:
    print("Failure!")

docsdirectory = buf.value
p3daddons = "\Prepar3D v5 Add-ons"
fsimstudios = "\FSimStudios - CYVR"
xmlfile = "\\add-on.txt"
xmldirectory = buf.value + p3daddons + fsimstudios + xmlfile
tempdirectory = buf.value + p3daddons + fsimstudios + "\\temp.txt"
xmlcompdirectory = buf.value + p3daddons + fsimstudios + "\\add-on.xml"

mypath = os.getcwd()
print(mypath)
mypathsubs = mypath

with open(xmldirectory, 'r') as f:
    temp= open(tempdirectory,"w+")

    f_contents=f.read(330)
    temp.write(f_contents + mypathsubs + "\\scenery")
    f_contents = f.read(92)
    temp.write(f_contents + mypathsubs + "\\texture")
    f_contents = f.read(92)
    temp.write(f_contents + mypathsubs + "\\effects")
    f_contents = f.read(92)
    temp.write(f_contents)

temp.close()
f.close()

with open(tempdirectory) as f:
    rd=f.readlines()
    with open (xmlcompdirectory,"w") as v:
        for i in rd:
            print (i)
            v.write(i)




print("Script Successfully completed")
