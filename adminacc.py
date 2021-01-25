from tkinter import *
from tkinter import messagebox
root=Tk()
root.minsize(1366,786)

filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\op1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def admin():

    def get():
        N=name.get()
        A=age.get()
        M=mail.get()
        U=username.get()
        P=password.get()
     
        if len(N)==0 or A==0 or len(M)==0 or len(U)==0 or len(P)==0:
            messagebox.showinfo(title="ERROR",message="FILL ALL DETAILS")
                    
        elif len(N)!=0 or A!=0 or len(M)!=0 or len(U)!=0 or len(P)!=0:
            s=str(N)+' '+str(A)+' '+str(M)+' '+str(U)+' '+str(P)
            f=open('admin account.txt','a')
            a=f.write('\n'+s)
            messagebox.showinfo(title="quiz creation of account",message="creation of account is successful")
            root.destroy()
        else:
            pass
        
                     

    name=StringVar()
    age=IntVar()
    mail=StringVar()
    username=StringVar()
    password=StringVar()


    root.title("CREATE ADMIN'S ACCOUNT")

    t=Label(root,text="CREATE ADMIN'S ACCOUNT",font=('arial',14),bd=15,background="white")
    t.pack()

        
    nameL=Label(root,text="NAME",background="white",font=('arial',14),bd=10).place(x=60,y=60)
    ageL=Label(root,text="AGE",background="white",font=('arial',15),bd=10).place(x=60,y=100)
    maiL=Label(root,text="EMAIL ID",background="white",font=('arial',16),bd=10).place(x=60,y=140)
    userL=Label(root,text="USERNAME",background="white",font=('arial',16),bd=10).place(x=60,y=180)
    passL=Label(root,text="PASSWORD",background="white",font=('arial',16),bd=10).place(x=60,y=220)

    nameE=Entry(root,textvariable=name).place(x=200,y=75)
    ageE=Entry(root,textvariable=age).place(x=200,y=115)
    maiE=Entry(root,textvariable=mail).place(x=200,y=155)
    userE=Entry(root,textvariable=username).place(x=200,y=195)
    passE=Entry(root,textvariable=password,show='*').place(x=200,y=235)

    create=Button(root,text="CREATE ACCOUNT",background="white",command=get).place(x=300,y=300)
admin()
