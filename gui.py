from tkinter import messagebox
import tkinter
import fractal

top = tkinter.Tk()

def callSolution():
   messagebox.showinfo( "Solutioning...", "This will take time")
   fractal.fractalSolution()
   print("doing it bro")

B = tkinter.Button(top, text ="Solve", command = callSolution)

B.pack()
top.mainloop()


