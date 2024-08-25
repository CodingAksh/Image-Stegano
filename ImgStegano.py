from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb # just install stegano

root = Tk()

root.title("Hide secret message inside your favourite image")

root.geometry("700x500+150+180")
root.resizable(True, True)
root.configure(bg="#444")

def showImage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="select image file",
                                          filetypes=(("PNG file", "*.png"), ("JPG file", "*.jpg"),
                                                     ("ALL file", "*.txt"))
                                          )
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250, height=250)
    lbl.image=img

def hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)
def show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def saveImage():
    secret.save("hidden.png")


#icon
image_icon = PhotoImage(file="minecraftheart.png")
root.iconphoto(False, image_icon)

#logo

logo= PhotoImage(file="minecraftheart.png")
Label(root,image=logo,bg="#444").place(x=10,y=10)

Label(root, text="Demo Text", bg="#430a72", fg="white",font="arial 25 bold").place(x=200, y=220)


#first Frame

f1=Frame(root,bd=3, bg="black", width=300, height=280, relief="groove")
f1.place(x=10,y=10)

lbl = Label(f1,bg="black")
lbl.place(x=40, y=10)

#second Frame
f2=Frame(root,bd=3, bg="white", width=300, height=280, relief=GROOVE)
f2.place(x=310,y=10)


text1 = Text(f2,font="Roboto 20", bg="white", fg="black", relief="groove",wrap=WORD)
text1.place(
    x=0, y=0, width=310, height=280
)

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=280,y=0,height=280)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


#third frame

frame3=Frame(root,bd=3, bg="#4C4E50", width=300, height=120, relief=RAISED)
frame3.place(x=10, y=300)


Button(frame3,text="Open Image",width=9, height=2, font="arial 15 bold", command=showImage).place(x=10, y=40)
Button(frame3,text="Save Image",width=9, height=2, font="arial 15 bold", command=saveImage).place(x=170, y=40)
Label(frame3, text="place, Images or photo files", bg="#333", fg="white",font="arial 12 bold").place(x=10, y=10)


#forth frame

frame4=Frame(root,bd=3, bg="#4C4E50", width=300, height=120, relief=RIDGE)
frame4.place(x=310, y=300)


Button(frame4,text="Hide Msg",width=9, height=2, font="arial 15 bold",command=hide).place(x=10, y=40)
Button(frame4,text="Show Msg",width=9, height=2, font="arial 15 bold",command=show).place(x=170, y=40)
Label(frame4, text="hide or show your message", bg="#333", fg="white",font="arial 12 bold").place(x=10, y=10)









root.mainloop()

