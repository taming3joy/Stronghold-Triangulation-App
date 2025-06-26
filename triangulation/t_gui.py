import tkinter as tk
from .t_math import triangulate

class triangulation_gui():
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Stronghold Triangulation")
        self.root.geometry("450x200")

        self.heading = tk.Label(self.root,text="Format: X-coordinate Z-coordinate Angle",font=('Arial',15))
        self.heading.pack(pady=10)

        self.entry1 = tk.Entry(self.root,font=("Arial",12))
        self.entry1.pack()

        self.entry2 = tk.Entry(self.root,font=("Arial",12))
        self.entry2.pack(pady=5)

        self.button = tk.Button(self.root,text="Find coordinates",command=self.on_click,font=("Arial",12))
        self.button.pack(pady=5)

        self.overworld = tk.Label(self.root,text="",font=("Arial",12))
        self.overworld.pack()

        self.nether = tk.Label(self.root,text="",font=("Arial",12))
        self.nether.pack()

        self.root.mainloop()

    def on_click(self):
        try:
            measurement1=[float(x) for x in str(self.entry1.get()).split(" ")]
            measurement2=[float(x) for x in str(self.entry2.get()).split(" ")]
            stronghold_coordinates_overworld = triangulate(measurement1,measurement2)
            stronghold_coordinates_nether = tuple([x//8 for x in stronghold_coordinates_overworld])
            self.overworld.config(text = f"Overworld = {stronghold_coordinates_overworld}" )
            self.nether.config(text=f"Nether = {stronghold_coordinates_nether}")
        except:
            self.overworld.config(text="Invalid input(s)")
            self.nether.config(text="")
