import os
import shutil

def swapFileData():
    file1 = input("enter source folder name:- ")
    file2 = input('enter destination folder name:- ')
    with open(file1, 'r') as a:
        data_a = a.read() 
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)
    
swapFileData()



# source = input("enter source folder name:- ")
# destination = input('enter destination folder name:- ')

# source = source + '/'
# destination = destination + '/'


# list_of_files = os.listdir(source)
# for file in list_of_files:
#     shutil.move((source+file), destination)
