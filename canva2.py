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








                                               
direction=""
oidx=50
oldy=50
newy=50
newx=50

def right_dir(event):
    global newx
    global newy
    global oldx
    global oldy
    global direction
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="right"
    draw(direction,oldx,oldy,newx,newy)
    
   
def left_dir(event):
    global newx
    global newy
    global oldx
    global oldy
    global direction
    oldx=newx
    oldy=newy
    newx=newx-5
    direction="left"
    draw(direction,oldx,oldy,newx,newy) 
    
    
def up_dir(event):
    global newx
    global newy
    global oldx
    global oldy
    global direction
    oldx=newx
    oldy=newy
    newy=newy-5
    direction="up"
    draw(direction,oldx,oldy,newx,newy)
    
 
def down_dir(event):
    global newx
    global newy
    global oldx
    global oldy
    global direction
    oldx=newx
    oldy=newy
    newy=newy+5
    direction="down"
    draw(direction,oldx,oldy,newx,newy)   
    
    
def draw(direction,oldx,oldy,newx,newy) :
    fill_color=enter_word.get()
    if(direction == "right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    
    if(direction == "left"):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
        
    if(direction == "down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
        
    if(direction == "up"):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)

root.mainloop()