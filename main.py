import os
from hashlib import md5

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
            
def compareFolder(folder, sync):
    files = os.listdir(folder)
    syncFiles = os.listdir(sync)

    if len(files) != len(syncFiles):
        print("not the same if1")
    
    for file in files:
        print("im here")
        if file in syncFiles:
            if compareFiles(folder+'/'+file, sync+'/'+file):
                print("same")
            else:
                print("not the same1")
        else:
            print("not the same")
        


folder = 'd:/Projects/folder-sync/folder'
sync = 'd:/Projects/folder-sync/sync'


compareFolder(folder, sync)
#print(os.listdir(folder))