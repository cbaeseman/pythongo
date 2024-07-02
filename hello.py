import ctypes

# Load the shared library
lib = ctypes.CDLL('./hello.so')

# Define the argument and return types for the HelloWorld function
lib.HelloWorld.argtypes = [ctypes.c_char_p]
lib.HelloWorld.restype = None

def hello_world(name):
    lib.HelloWorld(name.encode('utf-8'))

if __name__ == "__main__":
    hello_world("World")

