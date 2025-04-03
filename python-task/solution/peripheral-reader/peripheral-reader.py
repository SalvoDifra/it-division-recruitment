
'''

peripheral-reader.py

This script reads a message from the peripheral device file and writes on the named pipe.

'''


import posix
import time
from fpp import Peripheral, Notifier, Listener




class PipeWriter(Listener):

    def __init__(self, pipe_path):
        
        self.pipe_path = pipe_path
        try:
            posix.mkfifo(pipe_path)
        except FileExistsError:
            print(f"periperal-reader error: the named pipe {self.pipe_path} already exists.")
        except OSError as e:
            print(f"periperal-reader error: named pipe creation failed.")
            print(f"{e}")


    def on_message_received(self, msg):

        try:
            with open(self.pipe_path, "w") as named_pipe:
                named_pipe.write(msg)
                named_pipe.flush()
                print(f"peripheral-reader: device message sent written in the named pipe {self.pipe_path}.")
        except FileNotFoundError:
            print(f"peripheral-reader error: named pipe {self.pipe_path} does not exist.")
        except OSError as e:
            print(f"peripheral-reader error: failed to read data from named pipe {self.pipe_path}")
            print(f"{e}")



def main():

    device_path = "./device_file"
    peripheral = Peripheral(device_path)

    pipe_path = "./named_pipe"
    pipe_writer = PipeWriter(pipe_path)    

    notifier = Notifier(peripheral, [pipe_writer])

    while True:
        time.sleep(1)



if __name__ == "__main__":
    main()