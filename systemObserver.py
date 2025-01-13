import os
import sys
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
        extension: make directory if extension has not been read before
        '''

        entry = str(event.src_path)
        ext = os.path.splitext(entry)[-1][1:]
        file_name = os.path.basename(entry)

        target_dir = f'/Users/joels/Documents/test_destination/{ext}'
        target_path = f'{target_dir}/{file_name}'

        print(f'file extension: {ext}')

        if ext in directory_dict:
            # MOVE FILE TO '/DEDICATED PATH/ {ext}'
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                print(f'Directory created: {target_dir}')

            if os.path.exists(f'{target_path}'):
                print("already a file in this directory with the same name!")
            else:
                os.replace(entry, target_path)
                print(f'file was moved to {target_path}')
        else:
            # create a directory with the current extension as the name
            os.makedirs(target_dir, exist_ok=True)
            print(f'{file_name} was moved to {target_path}')
            os.replace(entry, target_path)
            directory_dict[ext] = 1


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/Users/joels/Downloads', recursive=Fals e)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
