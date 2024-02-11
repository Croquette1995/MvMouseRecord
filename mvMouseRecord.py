#!/usr/bin/env python3

import time, pynput, datetime, re, os  # Import necessary modules

startExec = datetime.datetime.now()   # Record starting execution time

listFile = []                         # Initialize an empty list to store log filenames
path = r"C:\Users\Coren\Nextcloud\Bac Info\BAC 2\[SE] Systèmes d'Exploitation\ExerciceMouseRecordPython"
filename = "kikou.txt"
extension = ".log"

mouse = pynput.mouse.Controller()      # Create a mouse controller object from pynput module
execTime = float(input("Veuillez indiquer le temps d'execution du script désiré : \n"))

# Define function to check existing files with today's date and .log extension
def checkExistingFile(listFile):
    for file in os.listdir(path):       # Iterate through all files in path directory
        if file.endswith(extension):    # Check if the file has .log extension
            detect = re.search(time.strftime("%Y-%m-%d"), file)  # Search for today's date format in the filename
            if detect:                   # If found, add it to the list
                listFile.append(file)
    return listFile

# Define function to rename the current log file based on number of existing ones with same date
def renameFile(listFile):
    if len(listFile) != 0:           # If there are existing files
        os.rename(os.path.join(path, filename), os.path.join(path, "mv" + str(len(listFile))+"-" +time.strftime("%Y-%m-%d") + extension))
                                      # Rename the new one according to their count
    else:                             # Otherwise
        os.rename(os.path.join(path, filename), os.path.join(path, "mv-" + time.strftime("%Y-%m-%d") + extension))
                                      # Just add "-date" to its name without counting

# Open or create the initial log file
with open(os.path.join(path, filename), 'w') as f:
    f.write("Script débuté à : {0}.\n".format(startExec.strftime("%H:%M:%S")))          # Write start time
    while execTime > 0:                # Run until desired execution time elapses (user input at beginning)
        f.write("Position de la souris : {0} à {1}.\n".format(mouse.position, time.strftime("%H:%M:%S")))
                                      # Log mouse position every 0.1 seconds
        time.sleep(0.1)
        execTime -= 0.1
    endExec = datetime.datetime.now()  # Get ending execution time after loop ends
    f.write("Durée d'execution du script : {0} secondes.\n".format((endExec-startExec).total_seconds()))
                                      # Add total duration to log
f.close()

# Call defined functions
checkExistingFile(listFile)
renameFile(listFile)


