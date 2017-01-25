from tkinter import *
import serial

top = Tk()
w, h = 540, 420#top.winfo_screenwidth(), top.winfo_screenheight()
top.geometry("%dx%d+0+0" % (w, h))

clap_settings = ['1 slide forward		   ', '1 slide backward		  ', '2 slides forward', '2 slides backward', 'End presentation		 ', 'Restart presentation',]
clap2_settings = ['Pause						', 'Rewind					   ', 'Forward					  ', 'Mute						   ']

#send messages to arduino
def talkToArduino(clap1_var, clap2_var, clap3_var, clap4_var, sensitivity_var, input_range_var):
	arduinoSerialPort = serial.Serial("COM4", 9600) #connect to arduino
	while True:
		print arduinoSerialPort.readline()
	'''clap1_ard = 'a' + str(clap_settings.index(clap1_var.get()))
	clap2_ard = 'b' + str(clap_settings.index(clap2_var.get()))
	clap3_ard = 'c' + str(clap_settings.index(clap3_var.get()))
	clap4_ard = 'd' + str(clap_settings.index(clap4_var.get()))
	sens_ard = 's' + str(sensitivity_var)
	input_ard = 'i' + str(input_range_var)
	arduinoSerialPort.write(clap1_ard.encode('utf-8'))
	arduinoSerialPort.write(clap2_ard.encode('utf-8'))
	arduinoSerialPort.write(clap3_ard.encode('utf-8'))
	arduinoSerialPort.write(clap4_ard.encode('utf-8'))
	arduinoSerialPort.write(sens_ard.encode('utf-8'))
	arduinoSerialPort.write(input_ard.encode('utf-8'))'''


top["bg"]="white"

# show "PrezGo" at the top
top.title("PrezGo")

#position variables
PrezGo_x = 180
PrezGo_y = 1

presentation_x=50
presentation_y=PrezGo_y+ 60
video_x=390
video_y=PrezGo_y+ 60

clap1_x = 20
clap1_y = presentation_y + 30
clap2_x = clap1_x
clap2_y = clap1_y + 40
clap3_x = clap2_x
clap3_y = clap2_y + 40
clap4_x = clap3_x
clap4_y = clap3_y + 40

clap21_x = 100 + 190
clap21_y = presentation_y + 30
clap22_x = clap21_x
clap22_y = clap21_y + 40
clap23_x = clap22_x
clap23_y = clap22_y + 40
clap24_x = clap23_x
clap24_y = clap23_y + 40

sensitivity_x = clap4_x + 120
sensitivity_y = clap4_y + 50
input_range_x = sensitivity_x
input_range_y = sensitivity_y + 50
save_x = input_range_x + 30
save_y = input_range_y + 50
canvas_x=sensitivity_x+130
canvas_y=sensitivity_y-170



#set up title PrezGo
PrezGo_label = Label(top, text="PrezGo", bg="white")
PrezGo_label.config(font=("Courier", 44))
PrezGo_label.pack()
PrezGo_label.place(x=PrezGo_x, y=PrezGo_y)



#widgets
presentation_label = Label(top, text="Presentation", bg="white")
presentation_label.config(font=("Courier", 15))
presentation_label.pack()
presentation_label.place(x=presentation_x, y=presentation_y)

video_label = Label(top, text="Video", bg="white")
video_label.config(font=("Courier", 15))
video_label.pack()
video_label.place(x=video_x, y=video_y)

clap1_label = Label(top, text="One Clap: ", bg="white")
clap1_label.pack()
clap1_label.place(x=clap1_x, y=clap1_y)
clap1_var = StringVar(top)
clap1_var.set(clap_settings[0])
clap1 = OptionMenu(top, clap1_var, clap_settings[0], clap_settings[1], clap_settings[-2], clap_settings[-1])
clap1["menu"].config(bg="white")
clap1.config(bg="white")
clap1.pack()
clap1.place(x=clap1_x+70, y=clap1_y)
clap2_label = Label(top, text="Two Claps: ", bg="white")
clap2_label.pack()
clap2_label.place(x=clap2_x, y=clap2_y)
clap2_var = StringVar(top)
clap2_var.set(clap_settings[1])
clap2 = OptionMenu(top, clap2_var, clap_settings[1], clap_settings[2], clap_settings[3], clap_settings[-2], clap_settings[-1])
clap2["menu"].config(bg="white")
clap2.config(bg="white")
clap2.pack()
clap2.place(x=clap2_x+70, y=clap2_y)
clap3_label = Label(top, text="Three Claps: ", bg="white")
clap3_label.pack()
clap3_label.place(x=clap3_x, y=clap3_y)
clap3_var = StringVar(top)
clap3_var.set(clap_settings[4])
clap3 = OptionMenu(top, clap3_var, clap_settings[-2], clap_settings[-1])
clap3["menu"].config(bg="white")
clap3.config(bg="white")
clap3.pack()
clap3.place(x=clap3_x+70, y=clap3_y)
clap4_label = Label(top, text="Four Claps: ", bg="white")
clap4_label.pack()
clap4_label.place(x=clap4_x, y=clap4_y)
clap4_var = StringVar(top)
clap4_var.set(clap_settings[-1])
clap4 = OptionMenu(top, clap4_var, clap_settings[-2], clap_settings[-1])
clap4["menu"].config(bg="white")
clap4.config(bg="white")
clap4.pack()
clap4.place(x=clap4_x+70, y=clap4_y)

w = Canvas(top, width=2, height=150, background="black", highlightcolor="black")
w.pack()
w.place(x=canvas_x, y=canvas_y)


clap21_label = Label(top, text="One Clap: ", bg="white")
clap21_label.pack()
clap21_label.place(x=clap21_x, y=clap21_y)
clap21_var = StringVar(top)
clap21_var.set(clap2_settings[0])
clap21 = OptionMenu(top, clap21_var, clap2_settings[0], clap2_settings[1], clap2_settings[-2], clap2_settings[-1])
clap21["menu"].config(bg="white")
clap21.config(bg="white")
clap21.pack()
clap21.place(x=clap21_x+70, y=clap21_y)
clap22_label = Label(top, text="Two Claps: ", bg="white")
clap22_label.pack()
clap22_label.place(x=clap22_x, y=clap22_y)
clap22_var = StringVar(top)
clap22_var.set(clap2_settings[1])
clap22 = OptionMenu(top, clap22_var, clap2_settings[0], clap2_settings[1], clap2_settings[-2], clap2_settings[-1])
clap22["menu"].config(bg="white")
clap22.config(bg="white")
clap22.pack()
clap22.place(x=clap22_x+70, y=clap22_y)
clap23_label = Label(top, text="Three Claps: ", bg="white")
clap23_label.pack()
clap23_label.place(x=clap23_x, y=clap23_y)
clap23_var = StringVar(top)
clap23_var.set(clap2_settings[2])
clap23 = OptionMenu(top, clap23_var, clap2_settings[0], clap2_settings[1], clap2_settings[-2], clap2_settings[-1])
clap23["menu"].config(bg="white")
clap23.config(bg="white")
clap23.pack()
clap23.place(x=clap23_x+70, y=clap23_y)
clap24_label = Label(top, text="Four Claps: ", bg="white")
clap24_label.pack()
clap24_label.place(x=clap24_x, y=clap24_y)
clap24_var = StringVar(top)
clap24_var.set(clap2_settings[-1])
clap24 = OptionMenu(top, clap24_var, clap2_settings[0], clap2_settings[1], clap2_settings[-2], clap2_settings[-1])
clap24["menu"].config(bg="white")
clap24.config(bg="white")
clap24.pack()
clap24.place(x=clap24_x+70, y=clap24_y)

sensitivity_label = Label(top, text="Sensitivity:", bg="white")
sensitivity_label.pack( side = LEFT)
sensitivity_label.place(x=sensitivity_x, y=sensitivity_y)
sensitivity_var = 0
sensitivity = Scale(top, variable = sensitivity_var, from_=1, to_=3, resolution=1, orient=HORIZONTAL, length=120, bg="white", highlightbackground="white")

sensitivity.pack()
sensitivity.place(x=sensitivity_x + 75, y=sensitivity_y - 13)

input_range_label = Label(top, text="Input Range:", bg="white")
input_range_label.pack( side = LEFT)
input_range_label.place(x=input_range_x, y=input_range_y)
input_range_var = 1
input_range = Scale(top, variable = input_range_var, from_=1, to_=3, resolution=1, orient=HORIZONTAL, length=120, bg="white", highlightbackground="white") 
input_range.pack()
input_range.place(x=input_range_x+75, y=input_range_y-13)

save = Button(top, text ="Save Settings", command = lambda:talkToArduino(clap1_var, clap2_var, clap3_var, clap4_var, sensitivity_var, input_range_var))
save.pack()
save.place(x=save_x + 55, y=save_y)


#launch screen
top.mainloop()
