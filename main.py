#importação do tkinter
from tkinter import *
from tkinter import ttk


#colors
color1 = "#1e1f1e" # black
color2 = "#feffff" #white
color3 = "#38576b"  #blue charge
color4 = "#ECEFF1" #grey
color5 = "#FFAB40" #orange


window = Tk()
window.title("Calculator")
window.geometry("235x310")
window.config(bg=color1)

#frames
frame_display = Frame(window, width=235, height=50, bg=color3) 
frame_display.grid(row = 0, column = 0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row = 1, column = 0)


#Labels
app_label = Label(frame_display, text="123456789", width=16,height=2, padx=7, relief=FLAT,anchor="e",justify=RIGHT, font=("Ivy 18"), bg=color3,fg= color2 )
app_label.place(x=0,y=0)


#----buttons----
#first line
b_1 = Button(frame_body, text="C", width=11, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_1.place(x = 0, y = 0)

b_2 = Button(frame_body, text="%", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b_2.place(x = 118, y = 0)

b_3 = Button(frame_body, text="/", width=5, height=2, bg=color5, fg=color2, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE )
b_3.place(x = 177, y = 0) #orange button


#second line
b_4 = Button(frame_body, text="7", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_4.place(x = 0, y = 52)

b_5 = Button(frame_body, text="8", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_5.place(x = 59, y = 52)

b_6 = Button(frame_body, text="9", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_6.place(x = 118, y = 52)

b_7 = Button(frame_body, text="*", width=5, height=2, bg=color5, fg=color2, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_7.place(x = 177, y = 52) #orange button

#third line
b_8 = Button(frame_body, text="4", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_8.place(x = 0, y = 104)

b_9 = Button(frame_body, text="5", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_9.place(x = 59, y = 104)

b_10 = Button(frame_body, text="6", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_10.place(x = 118, y = 104)

b_10 = Button(frame_body, text="-", width=5, height=2, bg=color5, fg=color2, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_10.place(x = 177, y = 104) #orange button

#fouth line
b_11 = Button(frame_body, text="1", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_11.place(x = 0, y = 156)

b_12 = Button(frame_body, text="2", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_12.place(x = 59, y = 156)

b_13 = Button(frame_body, text="3", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_13.place(x = 118, y = 156)

b_14 = Button(frame_body, text="+", width=5, height=2, bg=color5, fg=color2, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_14.place(x = 177, y = 156) #orange button

#fifith
b_15 = Button(frame_body, text="0", width=11, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE) 
b_15.place(x = 0, y = 208)

b_16 = Button(frame_body, text=".", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b_16.place(x = 118, y = 208)

b_17 = Button(frame_body, text="=", width=5, height=2, bg=color5,fg=color2, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE )
b_17.place(x = 177, y = 208) #orange button


window.mainloop()