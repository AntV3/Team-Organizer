from tkinter import *
from tkinter import ttk
import tkinter as tk




class Organizer():
    def __init__(self):
        self.checkIn= "CHECK IN"
        self.mood= "MOOD"
        
        employee= Organizer()
        non_employee = Organizer()
        intern = Organizer()
        temporary_employee= Organizer()


        employee.checkIn= 100
        if (employee.checkIn <= 99):
            print (" You're Late")
        non_employee.checkIn = 0
        intern.checkIn = 100
        if (intern.checkIn <= 99):
            print("You're Late")
        temporary_employee.checkIn=100
        if (temporary_employee.checkIn <= 99):
            print ("You're Late")
            

        employee.mood= 100
        if (employee.mood <=100):
            print ("If you need to talk to a Supervisor or Lead please do-so, or contact HR")
        non_employee.mood = 100
        if (non_employee.mood <= 100):
            print ("Please consult with a professional/therapist")
        intern.mood= 100
        if (intern.mood <= 100):
            print ("If you need to talk to a Supervisor or Lead please do-so, or contact HR")
        temporary_employee.mood = 100
        if (temporary_employee.mood <= 100):
            print ("If you need to talk to a Supervisor or Lead please do-so, or contact HR")



# GUI BUILD
root = Tk()
root.title("Organizer")

top_frame=ttk.LabelFrame(root, text="Welcome")
top_frame.grid(row=0, column=0, padx=10, pady=10)

message_text= StringVar()
message_text.set("Welcome lets Organize your team")
message_label=ttk.Label(top_frame, textvariable=message_text, justify="center")
message_label.grid(row=0, column=1, padx=15, pady=15)

bottom_frame= ttk.LabelFrame(root, text="Who is your team")
bottom_frame.grid(row=1, column=0, padx=10, pady=5)

who = StringVar()
who.set("Lets name your team")
who_label=ttk.Label(bottom_frame, textvariable=who, justify="center")
who_label.grid(row=1, column=0, padx=10, pady=10)

window= tk.Button(root, text="Next Window", bg='White', fg='Black')
window_label=ttk.Label(bottom_frame, textvariable="Proceed", justify='left')
window_label.grid(row=3, column=4, padx=15, pady=15)

window.pack()
root.mainloop()













