import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

directory_dict = {
    'txt': 1,
    'jpeg': 1
}


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'file{event.src_path} has been created')
        '''
        apon creation the extension must be checked 
        then moved to the correct directory 
        extension: make directory is extension has not been read before
        '''

        entry = str(event.src_path)
        ext = (entry.split(".")[-1])
        file_name = (entry.split("/"[-1]))

        print(ext)

        '''
        if ext in directory_dict:
            #MOVE FILE TO '/DEDICATED PATH/ {ext}'
            if os.path.exists(f'/Users/joels/Documents/test_destination/{ext}/{file_name}'):
                print("already a file in this directory with the same name!")
            else:
                os.replace(entry, f"/Users/joels/Documents/test_destination/{ext}")
                print(entry + "was moved")
        else:
            pass # create a directory with the current extension as the name
        '''


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/Users/joels/Downloads', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
