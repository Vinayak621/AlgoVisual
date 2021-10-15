from tkinter import *
from tkinter import ttk
import random
from colors import *
from bubblesort import bubble_sort


window=Tk()
window.title("visualiser")
window.maxsize(900,600)
window.config(bg=WHITE)

selected_alg=StringVar()
data=[]
def Drawdata(data,colorArray):
    canvas.delete("all")
    canvas_height=380
    canvas_width=600
    x_width=canvas_width/(len(data)+1)
    offset=30
    spacing=10
    normalizedData = [i / max(data) for i in data]
    for i,height in enumerate(normalizedData):
        x0=i*x_width+offset+spacing
        y0=canvas_height-height*340
        x1=(i+1)*x_width+offset
        y1=canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))
    window.update_idletasks()
def generate():
    global data
    minval=int(minEntry.get())
    maxval=int(maxEntry.get())
    size=int(sizeEntry.get())

    data=[]
    for _ in range(size):
        data.append(random.randrange(minval, maxval+1))

    Drawdata(data,['red' for x in range(len(data))])
def StartAlgorithm():
    global data
    bubble_sort(data,Drawdata, speeedscale.get())


ui_frame=Frame(window,width=600,height=200,bg='GREY')
ui_frame.grid(row=0,column=0,padx=10,pady=5)



canvas=Canvas(window,width=600,height=380,bg='WHITE')
canvas.grid(row=1,column=0,padx=10,pady=5)

Label(ui_frame,text="Algorithm",bg='GREY').grid(row=0,column=0,padx=5,pady=5,sticky=W)
alg_menu=ttk.Combobox(ui_frame,textvariable=selected_alg,values=['quick_sort','selection','insertion',
'bubble_sort'])
alg_menu.grid(row=0,column=1,padx=10,pady=5)
alg_menu.current(0)
speeedscale=Scale(ui_frame,from_=0.1, to=2.0, length=200,digits=2,resolution=0.2,orient=HORIZONTAL,label=" Select_speed[s]")
speeedscale.grid(row=0,column=2,padx=5,pady=5)
Button(ui_frame,text="start",command=StartAlgorithm,bg='red').grid(row=0,column=3,padx=5,pady=5)


sizeEntry=Scale(ui_frame,from_=3, to=30, resolution=1,orient=HORIZONTAL,label=" Data_size")
sizeEntry.grid(row=1,column=0,padx=5,pady=5)

minEntry=Scale(ui_frame,from_=0, to=10, resolution=1,orient=HORIZONTAL,label=" min_value")
minEntry.grid(row=1,column=1,padx=5,pady=5)

maxEntry=Scale(ui_frame,from_=10, to=100, resolution=1,orient=HORIZONTAL,label=" max_size")
maxEntry.grid(row=1,column=2,padx=5,pady=5)
Button(ui_frame,text="generate",command=generate,bg='red').grid(row=1,column=3,padx=5,pady=5)
window.mainloop()
