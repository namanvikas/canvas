from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Canvas")
root.geometry("600x600")

fillcolour=["green","blue","yellow","red","orange"]
colour_dropdown=ttk.Combobox(root,state="redonly" ,values=fillcolour,width=10)
         
stratx=Label(root,text="startx")
starx.place( relx=0.8,rely=0.9,anchor=CENTER)

d1 = ttk.Combobox(root,state="readonly" ,values=coordinates_value, width= 10)
coordinates_values= [0,50,100,200,300,400,500,600,500,600,700,800,900]

canvas=Canvas(root,width=590,height=510,bg="white",highlightbackground="lightgray")
canvas.pack()

img=ImageTk.PhotoImage(Image.open("start_point1.png"))
my_image=canvas.create_image(50,50,image=img)








                                               
keypress=""
oidx=50
oldy=50
newy=50
newx=50

def triangle(event):
    global newx
    global newy
    global oldx
    global oldy
    global keypress
    oldx=newx
    oldy=newy
    newx=newx+5
    keypress="t"
    draw(keypress,oldx,oldy,newx,newy)
    
   
def rectangle(event):
    global newx
    global newy
    global oldx
    global oldy
    global keypress
    oldx=newx
    oldy=newy
    newx=newx-5
    keypress="r"
    draw(keypress,oldx,oldy,newx,newy) 
    
    
def square(event):
    global newx
    global newy
    global oldx
    global oldy
    global keypress
    oldx=newx
    oldy=newy
    newy=newy-5
    keypress="s"
    draw(keypress,oldx,oldy,newx,newy)
    
 
def circle(event):
    global newx
    global newy
    global oldx
    global oldy
    global keypress
    oldx=newx
    oldy=newy
    newy=newy+5
    keypress="c"
    draw(keypress,oldx,oldy,newx,newy)   
    
    
def draw(keypress,oldx,oldy,newx,newy) :
    fill_color=enter_word.get()
    if(keypress == "c"):
        draw_circle=canvas.create_circle(oldx,oldy,newx,newy,width=3,fill=fill_color)
    
    if(keypress == "s"):
        draw_square=canvas.create_square(oldx,oldy,newx,newy,width=3,fill=fill_color)
        
    if(keypress == "r"):
        draw_rectangle=canvas.create_rectangle(oldx,oldy,newx,newy,width=3,fill=fill_color)
        
    if(keypress == "t"):
        draw_tectangle=canvas.create_triangle(oldx,oldy,newx,newy,width=3,fill=fill_color)
    
root.bind("<c>",circle)
root.bind("<s>",square)
root.bind("<r>",rectangle)
root.bind("<t>",triangle)

root.mainloop()