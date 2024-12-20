import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileCreatedEvent


'''
Write down the logical objective and then GOOGLE!!
1. Triggered when a new item is added to downloads 
2. It must scan all entering files in downloads 
3. depending on the file type (img, mpv4, doc, pdf) it will sort into the corresponding folders
4. If the file type is DISTINCT and DOESNT ALREADY EXIST it will create a new file
'''

if __name__ == "__main__":
    # Set the format for logging info
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Set format for displaying path
    #path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = "/Users/joels/Downloads"

    # Initialize logging event handler
    event_handler = LoggingEventHandler()
    #file_creation_handler = FileCreatedEvent('/Users/joels/Downloads')

    # Initialize Observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    #observer.schedule(file_creation_handler, path, recursive=True)

    # Start the observer
    observer.start()
    try:
        while True:
            # Set the thread sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()





#how to check when a new download has been added - the trigger#



#---------------------------------------
#os.listdir(.C:\Users\joels\Downloads) returns just the contents of a file / directory but not the file type
file_list = os.scandir('/Users/joels/Downloads') # returns the file type ASWELL as the files in the directory

num_of_files = 0

for entry in file_list:
    num_of_files += 1
    os.path.split
    if entry.is_file():
        entry = str(entry.name)
        print(entry.split(".")[-1])


print(num_of_files)
print(type(file_list))

#os.scandir returns a class object thus


#! function hasDownloadsBeenIncreased():
#this is a test for a pull
#how about this push test


