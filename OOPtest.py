import tkinter as tk
from Classes101 import EnterBox
from Classes101 import InvisTextLabel
import madplotlib
window = tk.Tk()
window.title("Graphing Calc")
window.geometry("800x520")
window.configure(bg="#676767")




#UI
xAxis = EnterBox(window,"0.12","0.12","0.2","0.1")
xAxisLabel = InvisTextLabel(window,"0.12","0.07","0.1","0.05","X Axis")
xAxis.construct()
xAxisLabel.construct()

yAxis = EnterBox(window,"0.12","0.28","0.2","0.1")
yAxisLabel = InvisTextLabel(window,"0.12","0.23","0.1","0.05","Y Axis")
yAxis.construct()
yAxisLabel.construct()

XPPA = EnterBox(window,"0.12","0.44","0.2","0.1")
yAxisLabel = InvisTextLabel(window,"0.12","0.39","0.1","0.05","XPPA")
XPPA.construct()
yAxisLabel.construct()

YPPA = EnterBox(window,"0.12","0.60","0.2","0.1")
yAxisLabel = InvisTextLabel(window,"0.12","0.55","0.1","0.05","YPPA")
YPPA.construct()
yAxisLabel.construct()

#Window Initilization
window.mainloop()

#testy testo pesto