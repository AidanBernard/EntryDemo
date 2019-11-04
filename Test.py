from tkinter import*
root = Tk()


#### MODEL (Data and Methods) ####
count = 0

def countpresses():
    global count
    count +=1
    display.insert(END, "The button has been pressed " + str(count) + " times.\n")
    display.see(END)

def greeting():
    display.insert(END, "Welcome " + name.get() + "!\n")
    display.see(END)

#### CONTROLLERS (Widgets that can change the data) ####
greetingLabel = Label(root, text = "Enter Name")
greetingLabel.grid(row=0,column=0,sticky="E")


name = Entry(root, width = 20)
name.grid(row=0,column=1, sticky = "W")

greet = Button(root,text="Greet",fg="green",width = 20, command = greeting)
greet.grid(row=1,column=0)

counter = Button(root,text="Press to Get Count",fg="green", width = 20, command = countpresses)
counter.grid(row=1,column=1)

erase = Button(root, text="Erase Text", fg= "red", bg = "black")
erase.grid(row = 1, column = 2)

#### VIEW (Widgets which display the data) ####
display = Text(root,fg="green",bg="white")
display.grid(row=2,column=0,columnspan=2)

root.mainloop()