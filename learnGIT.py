from tkinter import *
import tkinter.messagebox as tmsg
def getvals():
        a = int(uservalue.get())
        for i in range (1,11):
            userdisplay.insert(END,(a),'\t',"x",'\t',(i),'\t',"=",'\t',(a*i))
            userdisplay.insert(END,'\n')
            
root = Tk()
root.resizable(0,0)
root.configure(background = "black")
root.title("Tables")
root.geometry("285x580")
user = Label(root, text="Enter Table Number " ,fg='red',bg='black',padx =10,pady = 20 ,font=('arial',20,'bold'),justify='center')
user.grid(row=0,column=0)
uservalue = IntVar()
userentry = Entry(root,textvariable=uservalue,bd=15,insertwidth=4,justify='center',
                  font=('arial',15,'bold'))
userentry.grid(row=1,column=0)
userdisplay = Text(root, width=15, height=10,fg="green", bg="black", bd=16, font=('arial',20,'bold'))
userdisplay.grid(row=3,column=0)
btn = Button(text = "SUBMIT",font=('arial',20,'bold'),width=10, height=0,
             pady = 6 ,bd=14,bg = 'gray',fg = 'red',command=getvals)
btn.grid(row=2,column=0)


root.mainloop()