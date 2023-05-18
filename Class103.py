import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the directory to monitor
directory = "C:/Users/prade/Downloads"

# Define the event handler for file system events
class FileChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            print(f"File created: {event.src_path}")
        elif event.event_type == 'modified':
            print(f"File modified: {event.src_path}")
        elif event.event_type == 'deleted':
            print(f"File deleted: {event.src_path}")

# Create an observer and attach the event handler
observer = Observer()
observer.schedule(FileChangeHandler(), path=directory, recursive=True)

# Start the observer
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

# Wait for the observer to complete
observer.join()
