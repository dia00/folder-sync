import os
from hashlib import md5
import shutil

# function for writing operations in log file
def log(message):
    with open('log.txt', 'w') as f:
        f.write(message)

# function for comparing files
def compareFiles(file1, file2):
    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            if(f1.read() == f2.read()):
                return True
            else:
                return False

# function for coparing folders       
def compareFolder(folder, sync):
    files = os.listdir(folder)
    syncFiles = os.listdir(sync)

    if len(files) != len(syncFiles):
        return False
    
    for file in files:
        if file in syncFiles:
            if compareFiles(folder+'/'+file, sync+'/'+file):
                return True
            else:
                return False
        else:
            return False
    
folderPath = 'd:/Projects/folder-sync/folder'
syncPath = 'd:/Projects/folder-sync/sync'

folderFiles = os.listdir('d:/Projects/folder-sync/folder')
syncFiles = os.listdir('d:/Projects/folder-sync/sync')

for file in folderFiles:
    if file in syncFiles:
        #check if our files are the same
        if compareFiles(folderPath+'/'+file, syncPath+'/'+file):
             print("folders up to date")
        else:
            os.remove(syncPath+'/'+file)
            shutil.copy(folderPath+'/'+file, syncPath)
    else:
        shutil.copy(folderPath+'/'+file, syncPath)
        print("updated folder")


