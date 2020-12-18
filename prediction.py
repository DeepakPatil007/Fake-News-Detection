import pickle
import tkinter
from tkinter import *

window = Tk()
window.configure(bg="light grey")
window.geometry("640x640")
window.maxsize(640, 640)

global labelString1
global labelString2
global labelString3
global name
global slider

labelString1 = StringVar()
labelString2 = StringVar()
labelString3 = StringVar()
name = StringVar()
slider = 1

def update(ind):
    frame = frames[ind % 1]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


def getData():
    ind = entry.index
    name = entry.get('1.0', END)

    #function call to detecting_fake_news
    detecting_fake_news(name)


#function to run for prediction
def detecting_fake_news(var):    
    #retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    
    temp = str(prediction[0])
    if temp == 'True':
        label2.configure(fg = 'green')
    else:
        label2.configure(fg = 'red')

    labelString2.set("The given statement is " + temp)
    slider = (prob[0][1])
    temp = str(prob[0][1])
    labelString3.set("The truth probability score is " + temp)

    

    for x in range(0,round(slider * 300)):
        r = x*2 if x < 128 else 255
        g = 255 if x < 128 else 255 - (x-128)*2
        gradient2.create_rectangle(x*2, 0, x*2 + 2, 35, fill=rgb(g,r,0), 
            outline=rgb(g,r,0))           
    window.update()

def rgb(r, g, b):
        return "#%s%s%s" % tuple([hex(c)[2:].rjust(2, "0") for c in (r, g, b)])


#initialization

frames = [PhotoImage(file='news.png')]
label = Label(window, width=600, height=320)
label.pack()


label1 = Label(window, textvariable=labelString1, bg='light grey')
label1.config(font=("Courier", 15), fg='black')
labelString1.set('Please Enter the News Text You want to Verify: ')
label1.pack()

entry = Text(window, width = 50, height = 3)
entry.config(font=("Courier", 15), fg='black', relief = RAISED)
entry.pack()

btn = Button(window, text = 'Validate News', bd = '10', command = getData, bg = 'black', fg = 'white')
btn.pack()

label2 = Label(window, textvariable=labelString2, bg='light grey')
label2.config(font=("Courier", 20), fg='black')
labelString2.set('')
label2.pack()

label3 = Label(window, textvariable=labelString3, bg='light grey')
label3.config(font=("Courier", 15), fg='black')
labelString3.set('')
label3.pack()

gradient2 = tkinter.Canvas(window, width=255*2, height=35)
gradient2.pack()


window.after(0, update, 0)

window.mainloop()




