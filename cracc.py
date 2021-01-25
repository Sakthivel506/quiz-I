import mysql.connector as hang
#import time,turtle
from tkinter import *
from tkinter import messagebox
global a,p
p=3
#f=open('count.txt','r')
#a=f.read()

#f.close()

root=Tk()
root.minsize(1366,786)

filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\op1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def cr():
    
    def create():



        def get():
            global a,p
            N=name.get()
            A=age.get()
            M=mail.get()
            U=username.get()
            P=password.get()
            #print(N,A,M,U,P)
            if len(N)==0 or A==0 or len(M)==0 or len(U)==0 or len(P)==0:
                messagebox.showinfo(title="ERROR",message="FILL ALL DETAILS")
                
            elif len(N)!=0 or A!=0 or len(M)!=0 or len(U)!=0 or len(P)!=0:
                h=0
                
                c=hang.connect(host='localhost',user='root',password='Admin@123456',database='project')
                m=c.cursor()
                m.execute('select * from playersdetails')
                w=m.fetchall()
                p=len(w)+1
                #m.execute("INSERT INTO login(username,password) VALUES(%s,%s)",(U,P))           
                #m.execute("insert into details(name,age,mail) values(%s,%s,%s)",(N,A,M))          
                m.execute("insert into playersdetails values(%s,%s,%s,%s,%s,%s)",(p,N,A,M,U,P))
                m.execute("insert into c3op values(%s,%s,%s,%s,%s)",(p,U,N,int(h),int(h)))
                m.execute('insert into c3tof values(%s,%s,%s,%s,%s)',(p,U,N,int(h),int(h)))
                m.execute('insert into moviesop values(%s,%s,%s,0,0)',(p,U,N))
                m.execute('insert into moviestof values(%s,%s,%s,0,0)',(p,U,N))
                m.execute('insert into indiaop values(%s,%s,%s,0,0)',(p,U,N))
                m.execute('insert into indiatof values(%s,%s,%s,0,0)',(p,U,N))
                m.execute('insert into spaceop values(%s,%s,%s,0,0)',(p,U,N))
                m.execute('insert into spacetof values(%s,%s,%s,0,0)',(p,U,N))
                m.execute('insert into sportsop values(%s,%s,%s,0,0)',(p,U,N))
                m.execute('insert into sportstof values(%s,%s,%s,0,0)',(p,U,N))
                c.commit()
        
                messagebox.showinfo(title="quiz creation of account",message="creation of account is successful")
                root.destroy()
            else:
                pass
    
                 

        name=StringVar()
        age=IntVar()
        mail=StringVar()
        username=StringVar()
        password=StringVar()

        #root.geometry('300x300')
        root.title('CREATE ACCOUNT')
        #className='CREATE ACCOUNT'
        t=Label(root,text='CREATE ACCOUNT',font=('arial',14),bd=15,background="white")
        t.pack()
        #form=Frame(root)
        #form.pack(side=TOP,fill=X)
        a=' '
        nameL=Label(root,text="NAME",background="white",font=('arial',14),bd=10).place(x=60,y=60)
        ageL=Label(root,text="AGE",background="white",font=('arial',15),bd=10).place(x=60,y=100)
        maiL=Label(root,text="EMAIL ID",background="white",font=('arial',16),bd=10).place(x=60,y=140)
        userL=Label(root,text="USERNAME",background="white",font=('arial',16),bd=10).place(x=60,y=180)
        passL=Label(root,text="PASSWORD",background="white",font=('arial',16),bd=10).place(x=60,y=220)

        '''
        nameL.grid(row=60,sticky=W)
        ageL.grid(row=65,sticky=W)
        maiL.grid(row=70,sticky=W)
        userL.grid(row=75,sticky=W)
        passL.grid(row=80,sticky=W)
        '''
        nameE=Entry(root,textvariable=name).place(x=200,y=75)
        ageE=Entry(root,textvariable=age).place(x=200,y=115)
        maiE=Entry(root,textvariable=mail).place(x=200,y=155)
        userE=Entry(root,textvariable=username).place(x=200,y=195)
        passE=Entry(root,textvariable=password,show='*').place(x=200,y=235)
        '''
        nameE.grid(row=60,column=35)
        ageE.grid(row=65,column=35)
        maiE.grid(row=70,column=35)
        userE.grid(row=75,column=35)
        passE.grid(row=80,column=35)
        '''
        create=Button(root,text="CREATE ACCOUNT",background="white",command=get).place(x=300,y=300)
        #create.pack()
        #f=open('count.txt','w')
        #a=f.write(str(p))
        #f.close()
    create()
cr()

                          
