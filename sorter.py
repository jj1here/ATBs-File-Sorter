#! /usr/env/python
# sorts all the files with the same extenstion (.txt , .xlsx, .py. etc.)

import re, os, shutil
from pathlib import Path

def fileSort(folder) :

    folder = os.path.abspath(folder) #gets absolute path for folder
    #walks through folder
    for folderName, subfolder, fileNames in os.walk(folder) : 
        #keeps track of the new folders
        newFolders = []
        for file in fileNames :
            # makes new folders based off of the file extensions
            fileExtent = Path(file).suffix
            if str(fileExtent) not in newFolders :
                newFolders.append(fileExtent)
            pathing = os.path.join(folder, fileExtent)
            os.makedirs(pathing, exist_ok=True)
        # goes through the new folders
        for i in  newFolders:
            extFolder = os.path.basename(i)
            #search the files for extentsions that match the current folder
            regex = rf"(([a-zA-z0-9]+)({extFolder}))"
            mo = re.findall(regex, str(fileNames))
            #goes through matches and copies them to the folder
            for extent in mo :
                if extent[2] == extFolder :
                    folderPath = os.path.join(folder, extFolder)
                    filePath = (os.path.join(folder, extent[0]))
                    finalPath = os.path.join(folderPath, extent[0])
                    if os.path.exists(finalPath) == False :
                        shutil.copy(filePath, folderPath)
                        # could do for permanent 
                        # shutil.move(filePath, folderPath)
    #all done
    print("Done")

print("\nWhat file would you like to sort? \n")
#asks for folder
folder = input()
fileSort(folder)


