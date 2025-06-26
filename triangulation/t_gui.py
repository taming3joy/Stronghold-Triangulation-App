import tkinter as tk
from . import t_math as tm

root = tk.Tk()
root.title("Triangulation")
root.geometry("300x135")


def on_click():
    try:
        measurement1=[float(x) for x in str(entry1.get()).split(" ")]
        measurement2=[float(x) for x in str(entry2.get()).split(" ")]
        stronghold_coordinates_overworld = tm.triangulate(measurement1,measurement2)
        stronghold_coordinates_nether = tuple([x//8 for x in stronghold_coordinates_overworld])
        overworld.config(text = f"Overworld = {stronghold_coordinates_overworld}" )
        nether.config(text=f"Nether = {stronghold_coordinates_nether}")
    except:
        overworld.config(text="Invalid input(s)")
        nether.config(text="")

Heading = tk.Label(root,text="Format: X-coordinate Z-coordinate Angle")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

button = tk.Button(root,text="Find coordinates",command=on_click)
overworld = tk.Label(root,text="")
nether = tk.Label(root,text="")



#structure
Heading.pack()
entry1.pack()
entry2.pack()
button.pack()
overworld.pack()
nether.pack()

root.mainloop()

#Add use of F3+C
#Add distance to stronghold