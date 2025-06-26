import tkinter as tk
from tkinter import ttk

class gui:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Temp Gui Structure")
        self.root.geometry("450x250")

        #Top Frame

        self.top_frame = tk.Frame(self.root,bg="grey",width=450,height=50)
        self.top_frame.pack(anchor="nw")
        self.top_frame.pack_propagate(False)

        self.m1_label=tk.Label(self.top_frame,text="Measurement 1",font=("Arial",17),bg="grey")
        self.m1_label.pack(side="left",padx=10)

        self.seperator1=ttk.Separator(self.top_frame,orient="vertical")
        self.seperator1.pack(side="left",fill='y',padx=5)
        
        self.button1=tk.Button(self.top_frame,text="paste",font=("Arial",12))
        self.button1.pack(side="left",ipady=3,padx=10)

        self.measurements1=tk.Label(self.top_frame,text="x: - z: - yaw: - °",font=("Arial",17),bg="grey")
        self.measurements1.pack(side="left",padx=10)

        #Middle Frame

        self.middle_frame = tk.Frame(self.root,bg="grey",width=450,height=50)
        self.middle_frame.pack(anchor="nw")
        self.middle_frame.pack_propagate(False)

        self.m2_label=tk.Label(self.middle_frame,text="Measurement 2",font=("Arial",17),bg="grey")
        self.m2_label.pack(side="left",padx=10)

        self.seperator2=ttk.Separator(self.middle_frame,orient="vertical")
        self.seperator2.pack(side="left",fill='y',padx=5)

        self.button2=tk.Button(self.middle_frame,text="paste",font=("Arial",12))
        self.button2.pack(side="left",ipady=3,padx=10)

        self.measurements2=tk.Label(self.middle_frame,text="x: - z: - yaw: - °",font=("Arial",17),bg="grey")
        self.measurements2.pack(side="left",padx=10)

        #Bottom Frame

        self.bottom_frame=tk.Frame(self.root,width=450,height=150,bg="white")
        self.bottom_frame.pack(anchor="nw")
        self.bottom_frame.pack_propagate(False)

        self.distance_label=tk.Label(self.bottom_frame,text="Distance to Stronghold = - Blocks",font=("Arial",17),bg="white")
        self.distance_label.pack(pady=10)

        self.o_coords=tk.Label(self.bottom_frame,text="Overworld = (_,_)",font=("Arial",17),bg="white")
        self.o_coords.pack(pady=5)

        self.n_coords=tk.Label(self.bottom_frame,text="Nether = (_,_)",font=("Arial",17),bg="white")
        self.n_coords.pack(pady=10)

        self.root.mainloop()
    
    # def onclick_button1(self):


gui()