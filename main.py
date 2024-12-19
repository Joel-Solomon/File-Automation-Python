import os


'''
Write down the logical objective and then GOOGLE!!
1. Triggered when a new item is added to downloads 
2. It must scan all entering files in downloads 
3. depending on the file type (img, mpv4, doc, pdf) it will sort into the corresponding folders
4. If the file type is DISTINCT and DOESNT ALREADY EXIST it will create a new file
'''





#how to check when a new download has been added - the trigger#

#---------------------------------------
#os.listdir(.C:\Users\joels\Downloads) returns just the contents of a file / directory but not the file type 
file_list = os.scandir('/Users/joels/Downloads') # returns the file type ASWELL as the files in the directory


num_of_files = 0

for entry in file_list:
    num_of_files += 1
    if entry.is_file():
        print(entry.name)
print(num_of_files)
print(type(file_list))
#print(len(file_list))


#! function hasDownloadsBeenIncreased():
#this is a test for a pull 


