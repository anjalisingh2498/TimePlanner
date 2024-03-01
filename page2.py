import winsound
from tkinter import *
import datetime
import time
import winsound
# from playsound import playsound
from threading import *
from tkinter import messagebox
from PIL import ImageTk, Image

ws = Tk()
ws.geometry('1200x500')
ws.title('Alarm')
ws['bg']='white'

f = ("Times bold", 14)
def Threading():
    t1=Thread(target=alarm)
    t1.start()
    
def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
 
        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            messagebox.showinfo("Time up","Time to Wake up")
            # Playing sound
            
            

Label(ws,text="Alarm Clock",
    background='white',
    foreground='dark slate gray',
    font=('Times 50 bold italic')).grid(column=1,row=0,sticky=N)

img = ImageTk.PhotoImage(Image.open("abc.png"))
label = Label(ws, image = img)
label.grid(column=0,row=1,sticky=W)


Label(ws,text="    set alarm",
    background='white',
    foreground='green',
    font=('Times 30 bold italic')).grid(row=1,column=1,sticky=N)


frame = Frame(ws,bg='white')
frame.grid(column=1,row=1,sticky='W',padx=200)

hour = StringVar(ws)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.config(bg="cadet blue",fg="white")
hrs.grid(column=1,row=1)
 
minute = StringVar(ws)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.grid(column=2,row=1)
mins.config(bg="cadet blue",fg='white')
 
second = StringVar(ws)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.grid(column=3,row=1)
secs.config(bg="cadet blue",fg="white")
 
Button(frame,text="Set Alarm",font=("Times 15"),bg="cadet blue",fg="white",command=Threading).grid(column=4,row=1,padx=10)

def nextPage1():
    ws.destroy()
    import pomobag
    
def nextPage():
    ws.destroy()
    import todo


def prevPage():
    ws.destroy()
    import page1


# Create an object of tkinter ImageTk


# Create a Label Widget to display the text or Image
Button(
    ws,
    text="home",
    font='Times',
    command=prevPage,
    background='cadet blue',
    height=2, width=9,
foreground='white'
    ).grid(column=0,row=2)
Button(
    ws,
    text="Task planner",
    font='Times',
    command=nextPage,
    background='cadet blue',
    foreground='white',
    height=2, width=9
    ).grid(column=1,row=2)
Button(
    ws,
    text="pomodoro",
    font='Times',
    command=nextPage1,
    background='cadet blue',
    foreground='white',
    height=2, width=9
    ).grid(column=2,row=2)

ws.mainloop()