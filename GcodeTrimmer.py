# GCodeTrimmer made by Ángel L.M. 17/01/2018
# Special mention to StackOverflow as this script is basically merged copy-paste of several answered python programming questions.

# Shared under a Creative Commons Attribution-ShareAlike 4.0 International License

import sys
import time

if len(sys.argv)<4:
    sys.exit("Not enough arguments. Please check it.")
if len(sys.argv)>4:
    sys.exit("Too many arguments. Please check it.")
if not sys.argv[1].replace(".", "", 1).isdigit():
    sys.exit("The first argument does not contain only a digits. Check it.")
if sys.argv[2].find('.gcode')==-1:
    sys.exit("Not .gcode file extension found on origin file argument. Check it.")
if sys.argv[3].find('.gcode')==-1:
    sys.exit("Not .gcode file extension found on destination file argument. Check it.")

start_time = time.time()

FirstZMoveString = "G1 Z15.0 F1200          ;move the platform down 15mm"
EndOfStartGcodeString = "M106 S255"
ZeroExtrudeLenghtString = "G92 E0                  ;zero the extruded length again"

Zstring = "Z"+ str(sys.argv[1])
ZmoveFirst = "Z"+ str((float(sys.argv[1])+5))

try:
    fread = open(sys.argv[2], 'r')

except:
    sys.exit("Origin gcode file not found. Check it.")

originalgcode = (fread.read())
fread.close()

newsplitted=originalgcode.split("\n")
matching = [s for s in newsplitted if Zstring in s]
indexmatch = newsplitted.index(matching[0])

Xmatch = newsplitted[indexmatch].split(" ")[1]
Ymatch = newsplitted[indexmatch].split(" ")[2]
Zmatch = newsplitted[indexmatch].split(" ")[3]

indexFirstZMove = newsplitted.index(FirstZMoveString)
FirstZMoveStringSplitted=FirstZMoveString.split(" ")
newsplitted[indexFirstZMove]=FirstZMoveStringSplitted[0]+" "+ZmoveFirst+" "+FirstZMoveStringSplitted[2]

indexEndStartGcode = newsplitted.index(EndOfStartGcodeString)

indexResetExtrude = newsplitted.index(ZeroExtrudeLenghtString)
for i in range(1,10):
    if newsplitted[indexmatch-i].find(' E')!=-1:
        Ematch=newsplitted[indexmatch-i].split(" ")[3]
        newsplitted[indexResetExtrude]= "G92 "+Ematch
        break

for x in reversed(range(indexEndStartGcode+1, indexmatch)):
    newsplitted.pop(x)

newJoined='\n'.join(newsplitted)

fwrite = open(sys.argv[3], 'w+')
fwrite.write(newJoined)
fwrite.close()

print ("Done in " + str(time.time()-start_time) + " seconds!")
