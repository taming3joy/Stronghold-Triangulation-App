import tkinter as tk
from tkinter import ttk,messagebox
from pyperclip import paste
from t_math import triangulate

class gui:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Temp Gui Structure")
        self.root.geometry("515x250")

        #Top Frame

        self.top_frame = tk.Frame(self.root,bg="grey",width=515,height=50)
        self.top_frame.pack(anchor="nw")
        self.top_frame.pack_propagate(False)

        self.m1_label1=tk.Label(self.top_frame,text="Measurement 1",font=("Arial",17),bg="grey")
        self.m1_label1.pack(side="left",padx=10)

        self.seperator1=ttk.Separator(self.top_frame,orient="vertical")
        self.seperator1.pack(side="left",fill='y',padx=5)
        
        self.button1=tk.Button(self.top_frame,text="paste",font=("Arial",12),command=self.onclick_button1)
        self.button1.pack(side="left",ipady=3,padx=10)

        self.m1_label2=tk.Label(self.top_frame,text="x: - z: - yaw: - °",font=("Arial",14),bg="grey")
        self.m1_label2.pack(side="left")

        self.m1_values=None
        self.m1_valid=False

        #Middle Frame

        self.middle_frame = tk.Frame(self.root,bg="grey",width=515,height=50)
        self.middle_frame.pack(anchor="nw")
        self.middle_frame.pack_propagate(False)

        self.m2_label1=tk.Label(self.middle_frame,text="Measurement 2",font=("Arial",17),bg="grey")
        self.m2_label1.pack(side="left",padx=10)

        self.seperator2=ttk.Separator(self.middle_frame,orient="vertical")
        self.seperator2.pack(side="left",fill='y',padx=5)

        self.button2=tk.Button(self.middle_frame,text="paste",font=("Arial",12),command=self.onclick_button2)
        self.button2.pack(side="left",ipady=3,padx=10)

        self.m2_label2=tk.Label(self.middle_frame,text="x: - z: - yaw: - °",font=("Arial",14),bg="grey")
        self.m2_label2.pack(side="left")

        self.m2_values=None
        self.m2_valid=False

        #Bottom Frame

        self.bottom_frame=tk.Frame(self.root,width=515,height=150,bg="white")
        self.bottom_frame.pack(anchor="nw")
        self.bottom_frame.pack_propagate(False)

        self.distance_label=tk.Label(self.bottom_frame,text="Distance to Stronghold = - Blocks",font=("Arial",17),bg="white")
        self.distance_label.pack(pady=10)

        self.o_label=tk.Label(self.bottom_frame,text="Overworld = (_,_)",font=("Arial",17),bg="white")
        self.o_label.pack(pady=5)
        self.o_coords=None

        self.n_label=tk.Label(self.bottom_frame,text="Nether = (_,_)",font=("Arial",17),bg="white")
        self.n_label.pack(pady=10)
        self.n_coords=None

        self.root.mainloop()
    
    #methods

    def extract_measurements(self):
        clip_board=paste()
        clip_board=clip_board.split(" ")
        measurements = [float(x) for x in [clip_board[6],clip_board[8],clip_board[9]]]
        return (tuple(measurements))
    
    def check_valids(self):
        if self.m1_valid and self.m2_valid:
            self.o_coords=triangulate(self.m1_values,self.m2_values)
            self.o_label.config(text=f"Overworld = {self.o_coords}")
            self.n_label.config(text=f"Nether = {tuple([x//8 for x in self.o_coords])}") #Add this method to t_math later

    def onclick_button1(self):
        try:
            self.m1_values=self.extract_measurements()
            self.m1_valid=True
            x,z,yaw=self.m1_values
            self.m1_label2.config(text=f"x: {x:.0f} z: {z:.0f} yaw: {yaw:.1f}°")
            self.check_valids()
        except:
            self.m1_valid=False
            messagebox.showerror(title="Input error",message="Error in your input")
            raise

    def onclick_button2(self):
        try:
            self.m2_values=self.extract_measurements()
            self.m2_valid=True
            x,z,yaw=self.m2_values
            self.m2_label2.config(text=f"x: {x:.0f} z: {z:.0f} yaw: {yaw:.1f}°")
            self.check_valids()
        except:
            self.m2_valid=False
            messagebox.showerror(title="Input error",message="Error in your input")
            raise
            


gui()