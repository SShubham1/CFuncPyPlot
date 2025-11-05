import ctypes
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Detect platform and load the correct library

if sys.platform.startswith("linux"):
    libname = "./libfunction_data.so"
elif sys.platform == "darwin":
    libname = "./libfunction_data.dylib"
elif sys.platform == "win32":
    libname = "./function_data.dll"
else:
    raise Exception("Unsupported OS")

lib = ctypes.CDLL(libname)

# Defining types of argument and return value

lib.x_array.restype = ctypes.POINTER(ctypes.c_double)
lib.y_array.restype = ctypes.POINTER(ctypes.c_double)
lib.free_array.argtypes = [ctypes.POINTER(ctypes.c_double)]

# C arrays to numpy arrays

x_arr = np.ctypeslib.as_array(lib.x_array(), shape=(10000,))
y_arr = np.ctypeslib.as_array(lib.y_array(), shape=(10000,))

# Plot

plt.plot(x_arr, y_arr)
plt.xlabel("x")
plt.ylabel("y = f(x)")
plt.title("Function plot from C data")
plt.grid(True)

plt.show()

# Free memory
lib.free_array(x_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
lib.free_array(y_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
