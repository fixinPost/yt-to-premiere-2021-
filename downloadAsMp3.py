import os
from pathlib import Path
import sys
import pymiere



os.chdir(r'C:\Users\J\Desktop\mb testing 21\python\changing names\footageFolder')
before = os.listdir()
vid = input("enter your youtube url")
os.system(' youtube-dl -x --audio-format mp3 ' +vid)

after = (os.listdir())
import glob

#os.chdir(directory)
myClip = set(after) - set(before)
from pathlib import Path

print(myClip)

element = list(myClip)[0]
print(element)
#myClip = Path(myClip)
y = element.replace("'","")
y = y.replace('"','')
os.rename(element,y)
z = str(os.getcwd()) + '\\' + y
print(z)
pymiere.objects.app.project.importFiles([z], True, pymiere.objects.app.project.rootItem, False)
