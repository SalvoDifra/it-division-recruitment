
'''

message-printer.py

This script reads a messages from the named pipe and prints on the standard output.

'''


def main():

    pipe_path = "./named_pipe"
    print(f"Reading from {pipe_path} named_pipe:")

    try:
        with open(pipe_path, "r") as named_pipe:
            while True:
                    msg = named_pipe.readline()
                    if msg:
                        print(msg)
    
    except FileNotFoundError:
        print(f"message-printer error: named pipe {pipe_path} does not exist.")
    except OSError as e:
        print(f"message-printer error: failed to read data from named pipe {pipe_path}")
        print(f"{e}")



if __name__ == "__main__":
    main()