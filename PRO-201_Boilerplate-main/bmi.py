from cgitb import text
from tkinter import *
from unittest import result 
window = Tk()

window.title('BMI Calculator ')

window.geometry('380x400')
window.configure(bg = 'white')

def calculate_bmi():
    weight = int(weight_frame.get())
    height = int(height_frame.get())/100
    bmi = weight/(height*height)
    bmi = round(bmi, 1)
    name = username.get()
    result_label.destroy()
    msg = ''
    if bmi < 18.5:
        msg = 'You are Under Weight'
    elif bmi > 18.5 and bmi <= 24.9:
        msg = 'You have a Normal BMI'
    elif bmi > 25 and bmi <= 29.9:
        msg = 'You are Over Weight'   
    elif bmi > 30:
        msg = 'You are Obese' 
    else:
        msg = 'Something Went Wrong !'
    output_msg = Label(result_frame, text = name+', Your BMI is '+str(bmi)+' and '+msg,fg = 'black', bg = 'white', font = ('Arial', 12), width = 40)
    output_msg.place(x = 20, y = 40)
    output_msg.pack()        

app_label = Label(window, text='BMI Calculator ', fg = 'black', bg = 'white', font = ('Arial', 20), bd = 5)
app_label.place(x = 50, y = 20)

name_label = Label(window, text='Your name ', fg = 'black', bg = 'white', font = ('Arial', 12), bd = 1)
name_label.place(x = 20, y = 90)

height_label = Label(window, text='Enter Your Height (cm)', fg = 'black', bg = 'white', font = ('Arial', 12), bd = 5)
height_label.place(x = 20, y = 140)

weight_label = Label(window, text='Enter Your Weight (kg) ', fg = 'black', bg = 'white', font = ('Arial', 12), bd = 5)
weight_label.place(x = 20, y = 180)

username = Entry(window, text = '', bd= 2, width = 20)
username.place(x = 180, y = 90)

height_frame = Entry(window, text = '', bd= 2, width = 15)
height_frame.place(x = 180, y = 140)

weight_frame = Entry(window, text = '', bd= 2, width = 15)
weight_frame.place(x = 180, y = 180)

calculate_button = Button(window, text = 'Calculate', fg = 'black', bg = 'white', bd = 4, command=calculate_bmi)
calculate_button.place(x = 20, y = 250)

result_frame = LabelFrame(window, text = 'result', fg = 'black', bg = 'white', font = ('Arial', 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x = 20, y = 300)

result_label = Label(result_frame, text = ' ', fg = 'black', bg = 'white', font = ('Arial', 12))
result_label.place(x = 20, y = 20)
result_label.pack()

window.mainloop()
