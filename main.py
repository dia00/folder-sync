import os
import shutil
import time

# function for writing operations in log file
def log(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    with open('log.txt', 'a') as f:
        f.write(current_time+": "+message)
        f.write('\n')

# function for comparing files
def compareFiles(file1, file2):
    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            if(f1.read() == f2.read()):
                return True
            else:
                return False

# function for comparing folders       
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
    return True
    
folderPath = input("Please input your source file path: ") 
#'d:/Projects/folder-sync/folder'
syncPath = input("Please input your sync file path: ") 
#'d:/Projects/folder-sync/sync'

folderFiles = os.listdir(folderPath)
syncFiles = os.listdir(syncPath)

log("Start")

while True:
    if compareFolder(folderPath, syncPath):
        log("Folder up to date")
        print("Folder up to date")
        time.sleep(120)
        continue

    for file in folderFiles:
        if file in syncFiles:
            #check if our files are the same
            if compareFiles(folderPath+'/'+file, syncPath+'/'+file):
                #if file is the same, write to log and console
                log(file+" is up to date")
                print(file+" is up to date")
            else:
                #if not the same, remove file and recopy with correct version
                os.remove(syncPath+'/'+file)
                shutil.copy(folderPath+'/'+file, syncPath) #or os.system("cp " +folderPath+'/'+file+' '+backup), but not on windows
                log(file+" was updated")
                print(file+" was updated")
        else:
            #if file not found in sync folder, copy it
            shutil.copy(folderPath+'/'+file, syncPath)
            log(file+" was copied")
            print(file+" was copied")

    for file in syncFiles:
        if file not in folderFiles:
            #if file from sync folder not in src folder, remove it
            os.remove(syncPath+'/'+file)
            log(file+" was removed")
            print(file+" was removed")
    
    print("Folder up to date")
    log("Folder up to date")
    time.sleep(120)
   
