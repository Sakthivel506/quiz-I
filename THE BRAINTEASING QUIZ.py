#Error-1
import turtle,time,csv,random,os,tkinter
from tkinter import *
import mysql.connector as abc
import mysql.connector
from tkinter import messagebox
running=True
def ADMINSPART():
    def dell():
        def deleting(FILE):
            global file,sno
            file = FILE
            root=tkinter.Tk()
            root.title("DELETING QUESTIONS")
            root['bg']='black'
            root.minsize(1366,768)
            def print1():
                def NE():
                    root.destroy()
                    try:
                        turtle.clearscreen()
                        adm('yes')
                    except:
                        adm('yes')
                root=tkinter.Tk()
                root['bg']='black'
                root.minsize(1366,768)
                with open(file,newline="") as f:
                        reader=csv.reader(f)
                        e=0
                        for col in reader:
                            d=0
                            for row in col:
                                if d==1:
                                    x=90
                                else:
                                    x=20
                                label=tkinter.Label(root,width=x,height=2,text=row,relief=tkinter.RIDGE,fg='white',background='black')
                                label.grid(row=e,column=d)
                                d+=1
                            e+=1
                        N=Button(root,text='next',command=NE,background='grey',fg='orange',height=1,width=15).place(x=1150,y=600)
                        #file.close()
            def check():                
                global sno,file
                a=sno.get()
                win=open(file,'r')
                s=len(list(csv.reader(win)))
                win.close()
                if a<=0 or a>=s:
                    messagebox.showinfo(title="deleting questions",message="enter correct number")
                else:
                    root.destroy()
                    open1 = open(file,"r")
                    csv_reader = csv.reader(open1)
                    open2 = open("project2.csv","w",newline = '')
                    csv_writer = csv.writer(open2,delimiter=',')
                    for i in csv_reader :
                        if csv_reader.line_num == 1 : 
                            csv_writer.writerow(i)
                        else :
                            if i == [] or int(i[0]) == a:
                                continue
                            else :
                                csv_writer.writerow(i)
                    open1.close()
                    open2.close()
                    os.remove(file)
                    os.rename('project2.csv',file)

                    open3 = open(file,'r')
                    csv_reader1 = csv.reader(open3)
                    open4 = open('project3.csv','w',newline= '')
                    csv_writer1 = csv.writer(open4,delimiter=',')
                    for i in csv_reader1 :
                        if csv_reader1.line_num != 1 :
                            if a < int(i[0]):
                                p = int(i[0])
                                list2 = [str(p-1),i[1],i[2],i[3],i[4],i[5],i[6]]
                                csv_writer1.writerow(list2)
                            elif a > int(i[0]):
                                csv_writer1.writerow(i)
                            else :
                                continue
                        else:
                            csv_writer1.writerow(i)

                    open3 = open(file,'r')
                    csv_reader1 = csv.reader(open3)
                    open4 = open('project3.csv','w',newline= '')
                    csv_writer1 = csv.writer(open4,delimiter=',')

                    open3.close()
                    open4.close()
                    os.remove(file)
                    os.rename('project3.csv',file)
                    print1()

            with open(file,newline="") as f:
                sno=tkinter.IntVar()
                
                reader=csv.reader(f)
                r=0
                for col in reader:
                    c=0
                    for row in col:
                        if c==1:
                            x=90
                        else:
                            x=20
                        label=tkinter.Label(root,width=x,height=2,text=row,relief=tkinter.RIDGE,fg='white',background='black')
                        label.grid(row=r,column=c)
                        c+=1
                    r+=1
                a=tkinter.Label(root,text="Enter The Sno Of The Question To Be Deleted",fg="white",background='black',font='Times').place(x=100,y=600)
                entry=tkinter.Entry(root,width=15,textvariable=sno).place(x=400,y=600)
                button=tkinter.Button(root,text='ENTER',command=check,font='Times',background='grey').place(x=250,y=650)
                #file.close()
            root.mainloop()

        def deleting1(FILE):
            global file,sno
            file = FILE
            root=tkinter.Tk()
            root.title("DELETING QUESTIONS")
            root['bg']='black'
            root.minsize(1366,768)
            #global sno
            def print1():
                def NE():
                    root.destroy()
                    try:
                        turtle.clearscreen()
                        adm('yes')
                    except:
                        adm('yes')
                root=tkinter.Tk()
                root['bg']='black'
                root.minsize(1366,768)
                with open(file,newline="") as f:
                        reader=csv.reader(f)
                        e=0
                        for col in reader:
                            d=0
                            for row in col:
                                if d==1:
                                    x=90
                                else:
                                    x=20
                                label=tkinter.Label(root,width=x,height=2,text=row,relief=tkinter.RIDGE,fg='white',background='black')
                                label.grid(row=e,column=d)
                                d+=1
                            e+=1
                        N=Button(root,text='next',command=NE,background='grey',fg='orange',height=1,width=15).place(x=1150,y=600)
                #file.close()
            def check():                
                global sno,file
                a=sno.get()
                win=open(file,'r')
                s=len(list(csv.reader(win)))
                win.close()
                if a<=1 or a>=s:
                    messagebox.showinfo(title="deleting questions",message="enter correct number")
                else:
                    root.destroy()
                    open1 = open(file,"r")
                    csv_reader = csv.reader(open1)
                    open2 = open("project2.csv","w",newline = '')
                    csv_writer = csv.writer(open2,delimiter=',')
                    for i in csv_reader :
                        if csv_reader.line_num == 1 : 
                            csv_writer.writerow(i)
                        else :
                            if i == [] or int(i[0]) == a:
                                continue
                            else :
                                csv_writer.writerow(i)
                    open1.close()
                    open2.close()
                    os.remove(file)
                    os.rename('project2.csv',file)

                    open3 = open(file,'r')
                    csv_reader1 = csv.reader(open3)
                    open4 = open('project3.csv','w',newline= '')
                    csv_writer1 = csv.writer(open4,delimiter=',')
                    for i in csv_reader1 :
                        if csv_reader1.line_num != 1 :
                            if a < int(i[0]):
                                p = int(i[0])
                                list2 = [str(p-1),i[1],i[2]]
                                csv_writer1.writerow(list2)
                            elif a > int(i[0]):
                                csv_writer1.writerow(i)
                            else :
                                continue
                        else:
                            csv_writer1.writerow(i)

                    open3 = open(file,'r')
                    csv_reader1 = csv.reader(open3)
                    open4 = open('project3.csv','w',newline= '')
                    csv_writer1 = csv.writer(open4,delimiter=',')

                    open3.close()
                    open4.close()
                    os.remove(file)
                    os.rename('project3.csv',file)
                    print1()

            with open(file,newline="") as f:
                sno=tkinter.IntVar()
                
                reader=csv.reader(f)
                r=0
                for col in reader:
                    c=0
                    for row in col:
                        if c==1:
                            x=90
                        else:
                            x=20
                        label=tkinter.Label(root,width=x,height=2,text=row,relief=tkinter.RIDGE,fg='white',background='black')
                        label.grid(row=r,column=c)
                        c+=1
                    r+=1
                a=tkinter.Label(root,text="Enter The Sno Of The Question To Be Deleted",fg="white",background='black',font='Times').place(x=100,y=600)
                entry=tkinter.Entry(root,width=15,textvariable=sno).place(x=400,y=600)
                button=tkinter.Button(root,text='ENTER',command=check,font='Times',background='grey').place(x=250,y=650)
            #file.close()
            root.mainloop()
            
        a=turtle.Turtle()
        b=turtle.Screen()
        a.hideturtle()
        b.setup(width=1366,height=768)

        b.title('DELETING')
        b.bgpic('type.png')
        b.bgcolor('medium slate blue')
        a.pencolor('brown')
        a.penup()
        a.goto(-400,250)
        a.write('CHOOSE THE TYPE FOR RANKING', font=('Arial',40,'normal'),align='left')
        a.goto(-280,20)
        a.pencolor('grey')
        a.write('GENERAL KNOWLEDGE QUIZ', font=('Arial',20,'normal'),align='left')
        a.goto(-280,-60)
        a.write('TRUE OR FALSE', font=('Arial',20,'normal'),align='left')


        tr= turtle.Turtle()
        tr.penup()
        tr.goto(-295,35)
        tr.speed(0)
        tr.shape('arrow')
        tr.color('chartreuse')

        tr.direction='stop'

        def go_up():
            if tr.ycor()<35:
                tr.direction ='up'
            else:
                tr.sety(-45)

        def go_down():
            if tr.ycor()>-45:
                tr.direction ='down'
            else:
                tr.sety(35)

        def click():
            if tr.xcor()==-295 and tr.ycor()==35:
                turtle.clearscreen()
                #general knowledge quiz
                b.title('DELETING')
                b.bgpic('rank.png')
                #b.bgcolor('yellow')
                a.pencolor('white')
                a.penup()
                a.goto(-400,300)
                a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                a.goto(-300,80)
                a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Arial',20,'normal'),align='left')
                a.goto(-300,20)
                a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-40)
                a.write('SPACE',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-100)
                a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-160)
                a.write('INCREDIBLE INDIA',font=('Arial',20,'normal'),align='left')

                ar= turtle.Turtle()
                ar.penup()
                ar.goto(-315,95)
                ar.speed(0)
                ar.shape('arrow')
                ar.color('green')
                ar.direction='stop'
                        

                def go_up():
                    if ar.ycor()<95:
                        ar.direction ='up'
                    else:
                        ar.sety(-145)

                def go_down():
                    if ar.ycor()>-145:
                        ar.direction ='down'
                    else:
                        ar.sety(95)

                def move():
                    if ar.direction =='up':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() +60)
                        ar.direction='stop'
                            
                    elif ar.direction =='down':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() -60)
                        ar.direction='stop'
                            
                def clicks():
                    if ar.xcor()==-315 and ar.ycor()==95 :
                        turtle.clearscreen()
                        ##print('c3 (mcq)')
                        turtle.bye()
                        running=False
                        deleting('C3questionsop.csv')

                    elif ar.xcor()==-315 and ar.ycor()==35:
                        turtle.clearscreen()
                        ##print('movies (mcq)')
                        turtle.bye()
                        running=False
                        deleting('moviequestionsop.csv')

                    elif ar.xcor()==-315 and ar.ycor()==-25:
                        turtle.clearscreen()
                        ##print('space (mcq)')
                        turtle.bye()
                        running=False
                        deleting('Spacequestionsop.csv')


                    elif ar.xcor()==-315 and ar.ycor()==-85:
                        turtle.clearscreen()
                        ##print('sports (mcq)')
                        turtle.bye()
                        running=False
                        deleting('sportquestionsop.csv')#sportquestionsop


                    elif ar.xcor()==-315 and ar.ycor()==-145:
                        turtle.clearscreen()
                        ##print('india (mcq)')
                        turtle.bye()
                        running=False
                        deleting('Indquestionsop.csv')

                                

                b.listen()
                b.onkeypress(go_up,'w')
                b.onkeypress(go_down,'s')
                b.onkeypress(clicks,'x')

                while True:
                    try:
                        b.update()
                        move()
                            
                    except:
                        move()
                        break

                            

                                
            elif tr.xcor()==-295 and tr.ycor()==-45:
                turtle.clearscreen()
                #true or false
                b.title('RANKING')
                #b.bgcolor('yellow')
                b.bgpic('rank.png')
                a.pencolor('white')
                a.penup()
                a.goto(-400,300)
                a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                a.goto(-300,80)
                a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Arial',20,'normal'),align='left')
                a.goto(-300,20)
                a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-40)
                a.write('SPACE',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-100)
                a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-160)
                a.write('INDIA',font=('Arial',20,'normal'),align='left')

                ar= turtle.Turtle()
                ar.penup()
                ar.goto(-315,95)
                ar.speed(0)
                ar.shape('arrow')
                ar.color('green')
                ar.direction='stop'
                        

                def go_up():
                    if ar.ycor()<95:
                        ar.direction ='up'
                    else:
                        ar.sety(-145)

                def go_down():
                    if ar.ycor()>-145:
                        ar.direction ='down'
                    else:
                        ar.sety(95)

                def move():
                    if ar.direction =='up':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() +60)
                        ar.direction='stop'
                            
                    elif ar.direction =='down':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() -60)
                        ar.direction='stop'
                            
                def clicks():
                    if ar.xcor()==-315 and ar.ycor()==95:
                        turtle.clearscreen()
                        ##print('c3 (t/f)')
                        turtle.bye()
                        running=False
                        deleting1('C3questtof.csv')

                    elif ar.xcor()==-315 and ar.ycor()==35:
                        turtle.clearscreen()
                        ##print('movies (t/f)')
                        turtle.bye()
                        running=False
                        deleting1('moviesquesttof.csv')

                    elif ar.xcor()==-315 and ar.ycor()==-25:
                        turtle.clearscreen()
                        ##print('space (t/f)')
                        turtle.bye()
                        running=False
                        deleting1('spacequesttof.csv')
                            

                    elif ar.xcor()==-315 and ar.ycor()==-85:
                        turtle.clearscreen()
                        ##print('sports (t/f)')
                        turtle.bye()
                        running=False
                        deleting1('sportsquesttof.csv')
                           

                    if ar.xcor()==-315 and ar.ycor()==-145:
                        turtle.clearscreen()
                        ##print('india (t/f)')
                        turtle.bye()
                        running=False
                        deleting1('Indquesttof.csv')
                            
                                

                b.listen()
                b.onkeypress(go_up,'w')
                b.onkeypress(go_down,'s')
                b.onkeypress(clicks,'x')

                while True:
                    try:
                        b.update()
                        move()
                            
                    except:
                        move()
                        break

                         

                                
        def move():
            if tr.direction =='up':
                time.sleep(0.1)
                tr.sety(tr.ycor() +80)
                tr.direction='stop'
                            
            elif tr.direction =='down':
                time.sleep(0.1)
                tr.sety(tr.ycor() -80)
                tr.direction='stop'

        b.listen()
        b.onkeypress(go_up,'w')
        b.onkeypress(go_down,'s')
        b.onkeypress(click,'x')

        while True:
            try:
                b.update()
                move()
                            
            except:
                move()
                break

    def addquest():
        def choose():
            a=turtle.Turtle()
            b=turtle.Screen()
            a.hideturtle()
            b.setup(width=1366,height=768)
            b.title('CHOOSE TYPE OF QUIZ')
            #b.bgpic('choose.png')
            b.bgpic('add.png')
            b.bgcolor('medium slate blue')
            a.pencolor('orange')
            a.penup()
            a.goto(-400,250)
            a.write('CHOOSE THE TYPE OF QUIZ', font=('Arial',40,'normal'),align='left')
            a.goto(-280,20)
            a.pencolor('grey')
            a.write('GENERAL KNOWLEDGE QUIZ', font=('Arial',20,'normal'),align='left')
            a.goto(-280,-60)
            a.write('TRUE OR FALSE', font=('Arial',20,'normal'),align='left')


            tr= turtle.Turtle()
            tr.penup()
            tr.goto(-295,35)
            tr.speed(0)
            tr.shape('arrow')
            tr.color('chartreuse')

            tr.direction='stop'

            def go_up():
                if tr.ycor()<35:
                    tr.direction ='up'
                else:
                    tr.sety(-45)

            def go_down():
                if tr.ycor()>-45:
                    tr.direction ='down'
                else:
                    tr.sety(35)

            def click():
                if tr.xcor()==-295 and tr.ycor()==35:
                    turtle.clearscreen()
                    b.bgpic('type.png')
                    #general knowledge quiz
                    b.title('CHOOSE THE CATEGORY OF THE QUIZ')
                    #b.bgcolor('orange')
                    a.pencolor('grey')
                    a.penup()
                    a.goto(-400,300)
                    a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                    a.goto(-300,80)
                    a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Arial',20,'normal'),align='left')
                    a.goto(-300,20)
                    a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                    a.goto(-300,-40)
                    a.write('SPACE',font=('Arial',20,'normal'),align='left')
                    a.goto(-300,-100)
                    a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                    a.goto(-300,-160)
                    a.write('INDIA',font=('Arial',20,'normal'),align='left')

                    ar= turtle.Turtle()
                    ar.penup()
                    ar.goto(-315,95)
                    ar.speed(0)
                    ar.shape('arrow')
                    ar.color('green')
                    ar.direction='stop'
                

                    def go_up():
                        if ar.ycor()<95:
                            ar.direction ='up'
                        else:
                            ar.sety(-145)

                    def go_down():
                        if ar.ycor()>-145:
                            ar.direction ='down'
                        else:
                            ar.sety(95)
                            '''
                    def ch():
                        print(tr.xcor(),tr.ycor())
                            '''
                    def move():
                        if ar.direction =='up':
                            time.sleep(0.1)
                            ar.sety(ar.ycor() +60)
                            ar.direction='stop'
                    
                        elif ar.direction =='down':
                            time.sleep(0.1)
                            ar.sety(ar.ycor() -60)
                            ar.direction='stop'
                    
                    def clicks():
                        if ar.xcor()==-315 and ar.ycor()==95:
                            turtle.clearscreen()
                            #print('c3 (mcq)')
                            turtle.bye()
                            running=False
                            filename('C3questionsop.csv','C3 QUESTIONS MCQ')
                        elif ar.xcor()==-315 and ar.ycor()==35:
                            turtle.clearscreen()
                            #print('movies (mcq)')
                            turtle.bye()
                            running=False
                            filename('moviequestionsop.csv','MOVIES QUESTIONS MCQ')
                        elif ar.xcor()==-315 and ar.ycor()==-25:
                            turtle.clearscreen()
                            #print('space (mcq)')
                            turtle.bye()
                            running=False
                            filename('Spacequestionsop.csv','SPACE QUESTIONS MCQ')

                        elif ar.xcor()==-315 and ar.ycor()==-85:
                            turtle.clearscreen()
                            #print('sports (mcq)')
                            turtle.bye()
                            running=False
                            filename('sportquestionsop.csv','SPORTS QUESTIONS MCQ')

                        if ar.xcor()==-315 and ar.ycor()==-145:
                            turtle.clearscreen()
                            #print('india (mcq)')
                            turtle.bye()
                            running=False
                            filename('Indquestionsop.csv','INDIA QUESTIONS MCQ')
                        

                    b.listen()
                    b.onkeypress(go_up,'w')
                    b.onkeypress(go_down,'s')
                    b.onkeypress(clicks,'x')

                    while True:
                        try:
                            b.update()
                            move()
                    
                        except:
                            move()
                            break

                    

                        
                elif tr.xcor()==-295 and tr.ycor()==-45:
                    turtle.clearscreen()
                    #true or false
                    b.bgpic('type.png')
                    b.title('CHOOSE THE CATEGORY OF THE QUIZ')
                    #b.bgcolor('yellow')
                    a.pencolor('grey')
                    a.penup()
                    a.goto(-400,300)
                    a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                    a.goto(-300,80)
                    a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Arial',20,'normal'),align='left')
                    a.goto(-300,20)
                    a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                    a.goto(-300,-40)
                    a.write('SPACE',font=('Arial',20,'normal'),align='left')
                    a.goto(-300,-100)
                    a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                    a.goto(-300,-160)
                    a.write('INDIA',font=('Arial',20,'normal'),align='left')

                    ar= turtle.Turtle()
                    ar.penup()
                    ar.goto(-315,95)
                    ar.speed(0)
                    ar.shape('arrow')
                    ar.color('green')
                    ar.direction='stop'
                

                    def go_up():
                        if ar.ycor()<95:
                            ar.direction ='up'
                        else:
                            ar.sety(-145)

                    def go_down():
                        if ar.ycor()>-145:
                            ar.direction ='down'
                        else:
                            ar.sety(95)
                            '''
                    def ch():
                        print(tr.xcor(),tr.ycor())
                            '''
                    def move():
                        if ar.direction =='up':
                            time.sleep(0.1)
                            ar.sety(ar.ycor() +60)
                            ar.direction='stop'
                    
                        elif ar.direction =='down':
                            time.sleep(0.1)
                            ar.sety(ar.ycor() -60)
                            ar.direction='stop'
                    
                    def clicks():
                        if ar.xcor()==-315 and ar.ycor()==95:
                            turtle.clearscreen()
                            #print('c3 (t/f)')
                            turtle.bye()
                            running=False
                            filename1('C3questtof.csv','C3 (TRUE/FALSE) QUIZ')
                        elif ar.xcor()==-315 and ar.ycor()==35:
                            turtle.clearscreen()
                            #print('movies (t/f)')
                            turtle.bye()
                            running=False
                            filename1('moviesquesttof.csv','MOVIES (TRUE/FALSE) QUIZ')
                        elif ar.xcor()==-315 and ar.ycor()==-25:
                            turtle.clearscreen()
                            #print('space (t/f)')
                            turtle.bye()
                            running=False
                            filename1('spacequesttof.csv','SPACE (TRUE/FALSE) QUIZ')

                        elif ar.xcor()==-315 and ar.ycor()==-85:
                            turtle.clearscreen()
                            #print('sports (t/f)')
                            turtle.bye()
                            running=False
                            filename1('sportsquesttof.csv','SPORTS (TRUE/FALSE) QUIZ')

                        if ar.xcor()==-315 and ar.ycor()==-145:
                            turtle.clearscreen()
                            #print('india (t/f)')
                            turtle.bye()
                            running=False
                            filename1('Indquesttof.csv','INDIA (TRUE/FALSE) QUIZ')
                        

                    b.listen()
                    b.onkeypress(go_up,'w')
                    b.onkeypress(go_down,'s')
                    b.onkeypress(clicks,'x')

                    while True:
                        try:
                            b.update()
                            move()
                    
                        except:
                            move()
                            break

                 

                        
            def move():
                
                if tr.direction =='up':
                    time.sleep(0.1)
                    tr.sety(tr.ycor() +80)
                    tr.direction='stop'
                    
                elif tr.direction =='down':
                    time.sleep(0.1)
                    tr.sety(tr.ycor() -80)
                    tr.direction='stop'

            b.listen()
            b.onkeypress(go_up,'w')
            b.onkeypress(go_down,'s')
            b.onkeypress(click,'x')

            while True:
                try:
                    b.update()
                    move()
                    
                except:
                    move()
                    break


        def filename(Filename,name):
            fil=open(Filename,'r')
            z=list(csv.reader(fil))
            fil.close()
            top=Tk()
            top.minsize(1366,786)
            filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\op1.png")
            background_label = Label(top, image=filename)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            #top.geometry("450x300")
            lbl=Label(top,text=name,font=("Verdana",30),background='white',bd=15)
            lbl.pack()

            quest=StringVar()
            op1=StringVar()
            op2=StringVar()
            op3=StringVar()
            op4=StringVar()
            ans=StringVar()

            def check():
                a=quest.get()
                b=op1.get()
                g=op2.get()
                d=op3.get()
                e=op4.get()
                f=ans.get()
                c=len(z)
                f1=open(Filename,'a',newline='')
                w=csv.writer(f1)
                if len(a)==0 or len(b)==0 or len(g)==0 or len(d)==0 or len(e)==0 or len(f)==0:
                    messagebox.showinfo(title="APPENDING QUESTIONS",message="enter all the fields")
                elif len(a)!=0 or len(b)!=0 or len(g)!=0 or len(d)!=0 or len(e)!=0 or len(f)!=0:
                    w.writerow([c,a,b,g,d,e,f])
                    f1.close()
                    messagebox.showinfo(title="APPENDING QUESTIONS",message="successfully appended")
                    top.destroy()
                    try:
                        turtle.clearscreen()
                        adm('yes')
                    except:
                        adm('yes')
                f1.close()
                
                #print(a,b,c,d,e)
                
            q1=Label(top,text="QUESTION:",background='white').place(x=40,y=60)
            o1=Label(top,text="OPTION-A:",background='white').place(x=40,y=100)
            o2=Label(top,text="OPTION-B:",background='white').place(x=40,y=140)
            o3=Label(top,text="OPTION-C:",background='white').place(x=40,y=180)
            o4=Label(top,text="OPTION-D:",background='white').place(x=40,y=220)
            ansa=Label(top,text="ANSWER:",background='white').place(x=40,y=260)



            q1a=Entry(top,width=30,textvariable=quest).place(x=110,y=60)
            q2a=Entry(top,width=30,textvariable=op1).place(x=110,y=100)
            q3a=Entry(top,width=30,textvariable=op2).place(x=110,y=140)
            q4a=Entry(top,width=30,textvariable=op3).place(x=110,y=180)
            q5a=Entry(top,width=30,textvariable=op4).place(x=110,y=220)
            ansa=Entry(top,width=30,textvariable=ans).place(x=110,y=260)


            submit=Button(top,text=" SUBMIT ",command=check,background='white',).place(x=240,y=300)
            top.mainloop()

        def filename1(Filename,name):
            fil=open(Filename,'r')
            z=list(csv.reader(fil))
            fil.close()
            top=Tk()
            top.minsize(1366,786)
            filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\op1.png")
            background_label = Label(top, image=filename)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            #top.geometry("450x300")
            lbl=Label(top,text=name,font=("Verdana",30),background='white',bd=15)
            lbl.pack()

            quest=StringVar()
            ans=StringVar()

            def check():
                a=quest.get()
                f=ans.get()
                c=len(z)
                f1=open(Filename,'a',newline='')
                w=csv.writer(f1)
                if len(a)==0 or len(f)==0:
                    messagebox.showinfo(title="APPENDING QUESTIONS",message="enter all the fields")
                elif len(a)!=0 or len(f)!=0:
                    w.writerow([c,a,f])
                    f1.close()
                    messagebox.showinfo(title="APPENDING QUESTIONS",message="successfully appended")
                    top.destroy()
                    try:
                        turtle.clearscreen()
                        adm('yes')
                    except:
                        adm('yes')
                f1.close()
                #print(a,b,c,d,e)
                
            q1=Label(top,text="QUESTION:",background='white').place(x=40,y=60)
            ansa=Label(top,text="ANSWER:",background='white').place(x=40,y=100)



            q1a=Entry(top,width=30,textvariable=quest).place(x=110,y=60)
            ansa=Entry(top,width=30,textvariable=ans).place(x=110,y=100)


            submit=Button(top,text=" SUBMIT ",command=check,background='white').place(x=240,y=150)
            top.mainloop()
        choose()
    #addquest()      
    def quest():
        def go_up2():
            if ar.ycor()<65:
                ar.direction ='up'
            else:
                ar.sety(15)

        def go_down2():
            if ar.ycor()>15:
                    ar.direction ='down'
            else:
                ar.sety(65)

        pen=turtle.Turtle()
        p=turtle.Screen()
        p.setup(width=1366,height=768)
        pen.hideturtle()
        p.bgpic('ranking.png')
        pen.pencolor('yellow')
        pen.penup()
        time.sleep(0.01)      
        pen.goto(-200,280)
        pen.write(w,font=('Belluccia',40,'bold'),align='left')
        time.sleep(0.01)     
        pen.goto(-100,50)
        pen.write('ADD QUESTIONS',font=('Comic Sans',20,'normal'),align='left')
        time.sleep(0.01)
        pen.goto(-100,0)
        pen.write('DELETE QUESTIONS',font=('Comic Sans',20,'normal'),align='left')

        ar= turtle.Turtle()
        ar.speed(0)
        ar.penup()
        ar.shape('arrow')
        ar.color('Chartreuse')
        ar.penup()

        ar.goto(-120.0,65.0)
        ar.direction='stop'
        def click3(x,y):
            turtle.clearscreen()
            if x==-120 and y==65:
                pass
                #addquest()
            elif x==-120 and y==15:
                pass
                #dell()

        def click1():
            click3(ar.xcor(),ar.ycor())



        def move():
            if ar.direction =='up':
                time.sleep(0.1)
                ar.sety(ar.ycor() +50)
                ar.direction='stop'
                        
            elif ar.direction =='down':
                time.sleep(0.1)
                ar.sety(ar.ycor() -50)
                ar.direction='stop'

        p.listen()
        p.onkeypress(click1,'x')
        p.onkeypress(go_up2,'w')
        p.onkeypress(go_down2,'s')

        while True:
            try:
                p.update()
                move()
                        
            except:
                move()
                break
    def adminacc():
        def NE():
            root.destroy()
            try:
                turtle.clearscreen()
                adm('yes')
            except:
                adm('yes')
        root=tkinter.Tk()
        root.minsize(1366,768)
        f=open('admin account.txt')
        a=f.read().split()
        x=20
        r=0
        root['bg']='black'
        c=0
        for i in range(len(a)):
            if c==2:
                x=50
            else :
                x=20
            if c<4:
                label=tkinter.Label(root,width=x,height=2,text=a[i],relief=tkinter.RIDGE,fg='white',background='black')
                label.grid(row=r,column=c)
                c+=1
            elif c>4:
                c=0
                #r+=1
                label=tkinter.Label(root,width=x,height=2,text=a[i],relief=tkinter.RIDGE,fg='white',background='black')
                label.grid(row=r,column=c)
                
            elif c==4:
                
                label=tkinter.Label(root,width=x,height=2,text=a[i],relief=tkinter.RIDGE,fg='white',background='black')
                label.grid(row=r,column=c)
                r+=1
                c=0
            else:
                label=tkinter.Label(root,width=x,height=2,text=a[i],relief=tkinter.RIDGE,fg='white',background='black')
                label.grid(row=r,column=c)
                c+=1
        N=Button(root,text='next',command=NE,background='grey',fg='orange',height=1,width=15).place(x=1150,y=600)
    def details():
        def playersdetails():
            def NE():
                root.destroy()
                try:
                    turtle.clearscreen()
                    adm('yes')
                except:
                    adm('yes')
            root=tkinter.Tk()
            root.title("players details")
            root.minsize(1366,768)
            root['bg']='black'
            mydb=mysql.connector.connect(host="localhost",user="root",password="Admin@123456",database="project")
            cur=mydb.cursor()
            cur.execute('select * from playersdetails')
            reader=cur
            r=0
            c=0
            label=tkinter.Label(root,width=20,height=2,text='SNO',relief=tkinter.RIDGE,fg='white',background='grey')
            label.grid(row=r,column=c)
            r=0
            c=1
            label=tkinter.Label(root,width=20,height=2,text='NAME',relief=tkinter.RIDGE,fg='white',background='grey')
            label.grid(row=r,column=c)
            r=0
            c=2
            label=tkinter.Label(root,width=20,height=2,text='AGE',relief=tkinter.RIDGE,fg='white',background='grey')
            label.grid(row=r,column=c)
            r=0
            c=3
            label=tkinter.Label(root,width=70,height=2,text='EMAIL',relief=tkinter.RIDGE,fg='white',background='grey')
            label.grid(row=r,column=c)
            r=0
            c=4
            label=tkinter.Label(root,width=20,height=2,text='USERNAME',relief=tkinter.RIDGE,fg='white',background='grey')
            label.grid(row=r,column=c)
            r=0
            c=5
            label=tkinter.Label(root,width=20,height=2,text='PASSWORD',relief=tkinter.RIDGE,fg='white',background='grey')
            label.grid(row=r,column=c)
            r=1
            for col in reader:
                c=0
                
                for row in col:
                    if c==3:
                        x=70
                    else:
                        x=20
                    label=tkinter.Label(root,width=x,height=2,text=row,relief=tkinter.RIDGE,fg='white',background='black')
                    label.grid(row=r,column=c)
                    c+=1
                r+=1
            N=Button(root,text='next',command=NE,background='grey',fg='orange',height=1,width=15).place(x=1150,y=600)
            root.mainloop()
        def go_up2():
            if ar.ycor()<65:
                ar.direction ='up'
            else:
                ar.sety(15)

        def go_down2():
            if ar.ycor()>15:
                ar.direction ='down'
            else:
                ar.sety(65)

        pen=turtle.Turtle()
        p=turtle.Screen()
        p.setup(width=1366,height=768)
        pen.hideturtle()
        #p.bgcolor('MediumSlateBlue')
        p.bgpic('ranking.png')
        w='  '
        pen.pencolor('grey')
        pen.penup()
        time.sleep(0.01)      
        pen.goto(-200,280)
        pen.write(w,font=('Belluccia',40,'bold'),align='left')
        time.sleep(0.01)     
        pen.goto(-100,50)
        pen.write('PLAYERS DETAILS',font=('Comic Sans',20,'normal'),align='left')
        time.sleep(0.01)
        pen.goto(-100,0)
        pen.write('ADMINS DETAILS',font=('Comic Sans',20,'normal'),align='left')

        ar= turtle.Turtle()
        ar.speed(0)
        ar.penup()
        ar.shape('arrow')
        ar.color('Chartreuse')
        ar.penup()

        ar.goto(-120.0,65.0)
        ar.direction='stop'
        def click3(x,y):
            if x==-120 and y==65:
                turtle.clearscreen()
                turtle.bye()
                running=False
                playersdetails()
            elif x==-120 and y==15:
                turtle.clearscreen()
                turtle.bye()
                adminacc()

        def click1():
            click3(ar.xcor(),ar.ycor())

        def move():
            
            if ar.direction =='up':
                time.sleep(0.1)
                ar.sety(ar.ycor() +50)
                ar.direction='stop'
                
            elif ar.direction =='down':
                time.sleep(0.1)
                ar.sety(ar.ycor() -50)
                ar.direction='stop'

        p.listen()
        p.onkeypress(click1,'x')
        p.onkeypress(go_up2,'w')
        p.onkeypress(go_down2,'s')

        while True:
            try:
                p.update()
                move()
                
            except:
                move()
                break
    def quest():
        def go_up2():
            if ar.ycor()<65:
                ar.direction ='up'
            else:
                ar.sety(15)

        def go_down2():
            if ar.ycor()>15:
                ar.direction ='down'
            else:
                ar.sety(65)

        pen=turtle.Turtle()
        p=turtle.Screen()
        p.setup(width=1366,height=768)
        pen.hideturtle()
        p.bgpic('ranking.png')
        w='  '
        pen.pencolor('yellow')
        pen.penup()
        time.sleep(0.01)      
        pen.goto(-200,280)
        pen.write(w,font=('Belluccia',40,'bold'),align='left')
        time.sleep(0.01)     
        pen.goto(-100,50)
        pen.write('ADD QUESTIONS',font=('Comic Sans',20,'normal'),align='left')
        time.sleep(0.01)
        pen.goto(-100,0)
        pen.write('DELETE QUESTIONS',font=('Comic Sans',20,'normal'),align='left')

        ar= turtle.Turtle()
        ar.speed(0)
        ar.penup()
        ar.shape('arrow')
        ar.color('Chartreuse')
        ar.penup()

        ar.goto(-120.0,65.0)
        ar.direction='stop'
        def click3(x,y):
            turtle.clearscreen()
            if x==-120 and y==65:
                addquest()
            elif x==-120 and y==15:
                dell()

        def click1():
            click3(ar.xcor(),ar.ycor())



        def move():
            if ar.direction =='up':
                time.sleep(0.1)
                ar.sety(ar.ycor() +50)
                ar.direction='stop'
                    
            elif ar.direction =='down':
                time.sleep(0.1)
                ar.sety(ar.ycor() -50)
                ar.direction='stop'

        p.listen()
        p.onkeypress(click1,'x')
        p.onkeypress(go_up2,'w')
        p.onkeypress(go_down2,'s')

        while True:
            try:
                p.update()
                move()
                    
            except:
                move()
                break
    def rank1():
        def ranking1(x):
            def NE():
                w.destroy()
                try:
                    turtle.clearscreen()
                    adm('yes')
                except:
                    adm('yes')
            w=Tk()
            w.geometry("400x250")
            w.minsize(1366,786)
            w['bg']='black'
            filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\ranking.png")
            background_label = Label(w, image=filename)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            mydb=abc.connect(host="localhost",user="root",password="Admin@123456",database="project")
            cur=mydb.cursor()
            cur.execute(x)
            i=0
            k=0
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'Rank')
            k=1
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'Username')
            k=2
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'Name')
            k=3
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'Last Game Score')
            k=4
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'Highest Game Score')
            #k=0
            i=1
            count=1
            for j in cur:
                c=0
                for k in range(len(j)):
                    if k==0:
                        e=Entry(w,width=30,fg="white",background='black',font='Arial')
                        e.grid(row=i,column=k)
                        e.insert(END,count)
                        c+=1
                        count+=1
                    else:
                        e=Entry(w,width=30,fg="white",background='black',font='Arial')
                        e.grid(row=i,column=k)
                        e.grid(row=i,column=k)
                        e.insert(END,j[k])
                        c+=1
                i+=1
                N=Button(w,text='next',command=NE,background='grey',fg='orange',height=1,width=15).place(x=1150,y=600)
            w.mainloop()
        a=turtle.Turtle()
        b=turtle.Screen()
        a.hideturtle()
        b.setup(width=1366,height=768)

        b.title('RANKING')
        b.bgpic('type.png')
        b.bgcolor('medium slate blue')
        a.pencolor('brown')
        a.penup()
        a.goto(-400,250)
        a.write('CHOOSE THE TYPE FOR RANKING', font=('Arial',40,'normal'),align='left')
        a.goto(-280,20)
        a.pencolor('grey')
        a.write('GENERAL KNOWLEDGE QUIZ', font=('Arial',20,'normal'),align='left')
        a.goto(-280,-60)
        a.write('TRUE OR FALSE', font=('Arial',20,'normal'),align='left')


        tr= turtle.Turtle()
        tr.penup()
        tr.goto(-295,35)
        tr.speed(0)
        tr.shape('arrow')
        tr.color('chartreuse')
        tr.direction='stop'

        def go_up():
            if tr.ycor()<35:
                tr.direction ='up'
            else:
                tr.sety(-45)

        def go_down():
            if tr.ycor()>-45:
                tr.direction ='down'
            else:
                tr.sety(35)

        def click():
            if tr.xcor()==-295 and tr.ycor()==35:
                turtle.clearscreen()
                #general knowledge quiz
                b.title('RANKING')
                b.bgpic('rank.png')
                #b.bgcolor('yellow')
                a.pencolor('white')
                a.penup()
                a.goto(-400,300)
                a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                a.goto(-300,80)
                a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Arial',20,'normal'),align='left')
                a.goto(-300,20)
                a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-40)
                a.write('SPACE',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-100)
                a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-160)
                a.write('INCREDIBLE INDIA',font=('Arial',20,'normal'),align='left')

                ar= turtle.Turtle()
                ar.penup()
                ar.goto(-315,95)
                ar.speed(0)
                ar.shape('arrow')
                ar.color('green')
                ar.direction='stop'
                        

                def go_up():
                    if ar.ycor()<95:
                        ar.direction ='up'
                    else:
                        ar.sety(-145)

                def go_down():
                    if ar.ycor()>-145:
                        ar.direction ='down'
                    else:
                        ar.sety(95)

                def move():
                    if ar.direction =='up':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() +60)
                        ar.direction='stop'
                            
                    elif ar.direction =='down':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() -60)
                        ar.direction='stop'
                            
                def clicks():
                    if ar.xcor()==-315 and ar.ycor()==95 :
                        turtle.clearscreen()
                        ##print('c3 (mcq)')
                        turtle.bye()
                        running=False
                        ranking1('select* from c3op order by highestscore desc limit 0,10')

                    elif ar.xcor()==-315 and ar.ycor()==35:
                        turtle.clearscreen()
                        #print('movies (mcq)')
                        turtle.bye()
                        running=False
                        ranking1('select* from moviesop order by highestscore desc limit 0,10')

                    elif ar.xcor()==-315 and ar.ycor()==-25:
                        turtle.clearscreen()
                        #print('space (mcq)')
                        turtle.bye()
                        unning=False
                        ranking1('select* from spaceop order by highestscore desc limit 0,10')


                    elif ar.xcor()==-315 and ar.ycor()==-85:
                        turtle.clearscreen()
                        #print('sports (mcq)')
                        turtle.bye()
                        running=False
                        ranking1('select* from sportsop order by highestscore desc limit 0,10')


                    elif ar.xcor()==-315 and ar.ycor()==-145:
                        turtle.clearscreen()
                        #print('india (mcq)')
                        turtle.bye()
                        running=False
                        ranking1('select* from indiaop order by highestscore desc limit 0,10')

                                

                b.listen()
                b.onkeypress(go_up,'w')
                b.onkeypress(go_down,'s')
                b.onkeypress(clicks,'x')

                while True:
                    try:
                        b.update()
                        move()
                            
                    except:
                        move()
                        break

                            

                                
            elif tr.xcor()==-295 and tr.ycor()==-45:
                turtle.clearscreen()
                #true or false
                b.title('RANKING')
                #b.bgcolor('yellow')
                b.bgpic('rank.png')
                a.pencolor('white')
                a.penup()
                a.goto(-400,300)
                a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                a.goto(-300,80)
                a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Arial',20,'normal'),align='left')
                a.goto(-300,20)
                a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-40)
                a.write('SPACE',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-100)
                a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-160)
                a.write('INDIA',font=('Arial',20,'normal'),align='left')

                ar= turtle.Turtle()
                ar.penup()
                ar.goto(-315,95)
                ar.speed(0)
                ar.shape('arrow')
                ar.color('green')
                ar.direction='stop'
                        

                def go_up():
                    if ar.ycor()<95:
                        ar.direction ='up'
                    else:
                        ar.sety(-145)

                def go_down():
                    if ar.ycor()>-145:
                        ar.direction ='down'
                    else:
                        ar.sety(95)

                def move():
                    if ar.direction =='up':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() +60)
                        ar.direction='stop'
                            
                    elif ar.direction =='down':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() -60)
                        ar.direction='stop'
                            
                def clicks():
                    if ar.xcor()==-315 and ar.ycor()==95:
                        turtle.clearscreen()
                        #print('c3 (t/f)')
                        turtle.bye()
                        running=False
                        ranking1('select* from c3tof order by highestscore desc limit 0,10')

                    elif ar.xcor()==-315 and ar.ycor()==35:
                        turtle.clearscreen()
                        #print('movies (t/f)')
                        turtle.bye()
                        running=False
                        ranking1('select* from moviestof order by highestscore desc limit 0,10')

                    elif ar.xcor()==-315 and ar.ycor()==-25:
                        turtle.clearscreen()
                        #print('space (t/f)')
                        turtle.bye()
                        running=False
                        ranking1('select* from spacetof order by highestscore desc limit 0,10')
                            

                    elif ar.xcor()==-315 and ar.ycor()==-85:
                        turtle.clearscreen()
                        #print('sports (t/f)')
                        turtle.bye()
                        running=False
                        ranking1('select* from sportstof order by highestscore desc limit 0,10')
                           

                    if ar.xcor()==-315 and ar.ycor()==-145:
                        turtle.clearscreen()
                        #print('india (t/f)')
                        turtle.bye()
                        running=False
                        ranking1('select* from indiatof order by highestscore desc limit 0,10')
                            
                                

                b.listen()
                b.onkeypress(go_up,'w')
                b.onkeypress(go_down,'s')
                b.onkeypress(clicks,'x')

                while True:
                    try:
                        b.update()
                        move()
                            
                    except:
                        move()
                        break

                         

                                
        def move():
            if tr.direction =='up':
                time.sleep(0.1)
                tr.sety(tr.ycor() +80)
                tr.direction='stop'
                            
            elif tr.direction =='down':
                time.sleep(0.1)
                tr.sety(tr.ycor() -80)
                tr.direction='stop'

        b.listen()
        b.onkeypress(go_up,'w')
        b.onkeypress(go_down,'s')
        b.onkeypress(click,'x')

        while True:
            try:
                b.update()
                move()
                            
            except:
                move()
                break
    def adm(t):
        while t=='yes':
            t='no'
            def go_up2():
                if ar.ycor()<65:
                    ar.direction ='up'
                else:
                    ar.sety(-85)

            def go_down2():
                if ar.ycor()>-85:
                    ar.direction ='down'
                else:
                    ar.sety(65)

            pen=turtle.Turtle()
            p=turtle.Screen()
            p.setup(width=1366,height=768)
            pen.hideturtle()
            #p.bgcolor('MediumSlateBlue')
            p.bgpic('play.png')
            w='ADMINS PART'   
            p.bgpic('play.png')
            pen.pencolor('grey')
            pen.penup()
            time.sleep(0.01)      
            pen.goto(-200,280)
            pen.write(w,font=('Times',40,'bold'),align='left')
            time.sleep(0.01)     
            pen.goto(-100,50)
            pen.write('EDIT QUESTIONS',font=('Times',20,'normal'),align='left')
            time.sleep(0.01)
            pen.goto(-100,0)
            pen.write('VIEW DETAILS',font=('Times',20,'normal'),align='left')
            pen.goto(-100,-50)
            pen.write('RANKING',font=('Times',20,'normal'),align='left')
            pen.goto(-100,-100)
            pen.write('QUIT',font=('Times',20,'normal'),align='left')
            ar= turtle.Turtle()
            ar.speed(0)
            ar.penup()
            ar.shape('arrow')
            ar.color('Chartreuse')
            ar.penup()

            ar.goto(-120.0,65.0)
            ar.direction='stop'
            def click3(x,y):
                if x==-120 and y==65:
                    turtle.clearscreen()
                    quest()

                elif x==-120 and y==15:
                    turtle.clearscreen()
                    details()
                elif x==-120 and y==-35:
                    turtle.clearscreen()
                    rank1()
                elif x==-120 and y==-85:
                    turtle.clearscreen()
                    p.bgpic('exit.png')
                    #p.bgcolor('blue')
                    pen.color('purple')
                    pen.goto(-250,150)
                    pen.write('THANK YOU', font=('Lucida Handwriting',60,'normal'),align='left')
                    pen.goto(80,-20)
                    pen.pencolor('yellow')
                    pen.write('DONE BY:', font=('Lucida Handwriting',40,'normal'),align='left')
                    pen.goto(160,-100)
                    pen.write('ARUL PRAKASH.K', font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(160,-140)
                    pen.write('JEEVA SHRIRAM.G', font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(160,-180)
                    pen.write('SAKTHIVEL.B', font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(160,-220)
                    pen.write('THEJAS ADITHYAA.T', font=('Lucida Handwriting',20,'normal'),align='left')
                    def ne(x,y):
                        turtle.clearscreen()
                        turtle.bye()
                        running=False
                    turtle.onscreenclick(ne,3)

            def click1():
                click3(ar.xcor(),ar.ycor())

            def move():
                if ar.direction =='up':
                    time.sleep(0.1)
                    ar.sety(ar.ycor() +50)
                    ar.direction='stop'
                        
                elif ar.direction =='down':
                    time.sleep(0.1)
                    ar.sety(ar.ycor() -50)
                    ar.direction='stop'

            p.listen()
            p.onkeypress(click1,'x')
            p.onkeypress(go_up2,'w')
            p.onkeypress(go_down2,'s')

            while True:
                try:
                    p.update()
                    move()
                        
                except:
                    move()
                    break
    root = Tk()
    root.minsize(1366,786)

    filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\op11.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def connect(NAME,PASSWORD):
        f=open('admin account.txt','r')
        a=f.readlines()
        c=0

        for i in range(1,len(a)):
            b=a[i].split()
            if b[-1]==PASSWORD and b[-2]==NAME:
                messagebox.showinfo(title="quiz login",message="LOGIN SUCCESSFUL")
                c+=1
                root.destroy()
                try:
                    turtle.clearscreen()
                    adm('yes')
                    break
                except:
                    #turtle.clearscreen()
                    adm('yes')
                break
            else:
                pass
        if c==0:
            messagebox.showinfo(title="quiz login",message="enter correct username and password")
                          
    def check():
        name=un.get()
        password=pw.get()
        data=connect(name,password)

    un=StringVar()
    pw=StringVar()
    root.title("ADMIN'S LOGIN PAGE")
    t=Label(root,text="ADMIN'S LOGIN FORM",font=('arial',14),bd=15,background="white")
    t.pack()
    nameL=Label(root,text="USERNAME",background="white",font=('arial',14),bd=10).place(x=40,y=100)
    passL=Label(root,text="PASSWORD",background="white",font=('arial',15),bd=10).place(x=40,y=140)
    nameE=Entry(root,textvariable=un,background="white").place(x=180,y=115)
    passE=Entry(root,textvariable=pw,show="*",background="white").place(x=180,y=155)
    login=Button(root,text="LOGIN",command=check,background="white").place(x=200,y=200)
    root.mainloop()

def player(name):
    ##print(name)
    #from itertools import repeat, chain
    global tof1,tof2,tof3,tof4,tof5,mcq1,mcq2,mcq3,mcq4,mcq5,NA,file1
    tof1=tof2=tof3=tof4=tof5=mcq1=mcq2=mcq3=mcq4=mcq5=0
    NA=name
    def rank():
        def ranking(x):
            def NE():
                w.destroy()
                try:
                    turtle.clearscreen()
                    opt('yes')
                except:
                    opt('yes')
            w=Tk()
            w.geometry("400x250")
            w.minsize(1366,786)
            w['bg']='black'
            filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\ranking.png")
            background_label = Label(w, image=filename)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            mydb=abc.connect(host="localhost",user="root",password="Admin@123456",database="project")
            cur=mydb.cursor()
            cur.execute(x)
            i=0
            k=0
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'RANK')
            k=1
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'Username')
            k=2
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'Name')
            k=3
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'Last Game Score')
            k=4
            e=Entry(w,width=30,fg="white",background='grey',font='Arial')
            e.grid(row=i,column=k)
            e.insert(END,'Highest Game Score')
            k=0
            i=1
            count=1
            for j in cur:
                c=0
                for k in range(len(j)):
                    if k==0:
                        e=Entry(w,width=30,fg="white",background='black',font='Arial')
                        e.grid(row=i,column=k)
                        e.insert(END,count)
                        c+=1
                        count+=1
                    else:
                        e=Entry(w,width=30,fg="white",background='black',font='Arial')
                        e.grid(row=i,column=k)
                        e.insert(END,j[k])
                        c+=1  
                        
                i+=1
            N=Button(w,text='next',command=NE,background='grey',fg='orange',height=1,width=15).place(x=1150,y=600)
            w.mainloop()
        a=turtle.Turtle()
        b=turtle.Screen()
        a.hideturtle()
        b.setup(width=1366,height=768)

        b.title('RANKING')
        b.bgpic('type.png')
        b.bgcolor('medium slate blue')
        a.pencolor('brown')
        a.penup()
        a.goto(-400,250)
        a.write('CHOOSE THE TYPE FOR RANKING', font=('Arial',40,'normal'),align='left')
        a.goto(-280,20)
        a.pencolor('grey')
        a.write('GENERAL KNOWLEDGE QUIZ', font=('Arial',20,'normal'),align='left')
        a.goto(-280,-60)
        a.write('TRUE OR FALSE', font=('Arial',20,'normal'),align='left')


        tr= turtle.Turtle()
        tr.penup()
        tr.goto(-295,35)
        tr.speed(0)
        tr.shape('arrow')
        tr.color('chartreuse')

        tr.direction='stop'

        def go_up():
            if tr.ycor()<35:
                tr.direction ='up'
            else:
                tr.sety(-45)

        def go_down():
            if tr.ycor()>-45:
                tr.direction ='down'
            else:
                tr.sety(35)

        def click():
            if tr.xcor()==-295 and tr.ycor()==35:
                turtle.clearscreen()
                #general knowledge quiz
                b.title('RANKING')
                b.bgpic('rank.png')
                #b.bgcolor('yellow')
                a.pencolor('white')
                a.penup()
                a.goto(-400,300)
                a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                a.goto(-300,80)
                a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Arial',20,'normal'),align='left')
                a.goto(-300,20)
                a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-40)
                a.write('SPACE',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-100)
                a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-160)
                a.write('INCREDIBLE INDIA',font=('Arial',20,'normal'),align='left')

                ar= turtle.Turtle()
                ar.penup()
                ar.goto(-315,95)
                ar.speed(0)
                ar.shape('arrow')
                ar.color('green')
                ar.direction='stop'
                    

                def go_up():
                    if ar.ycor()<95:
                        ar.direction ='up'
                    else:
                        ar.sety(-145)

                def go_down():
                    if ar.ycor()>-145:
                        ar.direction ='down'
                    else:
                        ar.sety(95)

                def move():
                    if ar.direction =='up':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() +60)
                        ar.direction='stop'
                        
                    elif ar.direction =='down':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() -60)
                        ar.direction='stop'
                        
                def clicks():
                    if ar.xcor()==-315 and ar.ycor()==95 :
                        turtle.clearscreen()
                        ##print('c3 (mcq)')
                        turtle.bye()
                        running=False
                        ranking('select* from c3op order by highestscore desc limit 0,10')

                    elif ar.xcor()==-315 and ar.ycor()==35:
                        turtle.clearscreen()
                        #print('movies (mcq)')
                        turtle.bye()
                        running=False
                        ranking('select* from moviesop order by highestscore desc limit 0,10')

                    elif ar.xcor()==-315 and ar.ycor()==-25:
                        turtle.clearscreen()
                        #print('space (mcq)')
                        turtle.bye()
                        running=False
                        ranking('select* from spaceop order by highestscore desc limit 0,10')


                    elif ar.xcor()==-315 and ar.ycor()==-85:
                        turtle.clearscreen()
                        #print('sports (mcq)')
                        turtle.bye()
                        running=False
                        ranking('select* from sportsop order by highestscore desc limit 0,10')


                    if ar.xcor()==-315 and ar.ycor()==-145:
                        turtle.clearscreen()
                        #print('india (mcq)')
                        turtle.bye()
                        running=False
                        ranking('select* from indiaop order by highestscore desc limit 0,10')

                            

                b.listen()
                b.onkeypress(go_up,'w')
                b.onkeypress(go_down,'s')
                b.onkeypress(clicks,'x')

                while True:
                    try:
                        b.update()
                        move()
                        
                    except:
                        move()
                        break

                        

                            
            elif tr.xcor()==-295 and tr.ycor()==-45:
                turtle.clearscreen()
                #true or false
                b.title('RANKING')
                #b.bgcolor('yellow')
                b.bgpic('rank.png')
                a.pencolor('white')
                a.penup()
                a.goto(-400,300)
                a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                a.goto(-300,80)
                a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Arial',20,'normal'),align='left')
                a.goto(-300,20)
                a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-40)
                a.write('SPACE',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-100)
                a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                a.goto(-300,-160)
                a.write('INDIA',font=('Arial',20,'normal'),align='left')

                ar= turtle.Turtle()
                ar.penup()
                ar.goto(-315,95)
                ar.speed(0)
                ar.shape('arrow')
                ar.color('green')
                ar.direction='stop'
                    

                def go_up():
                    if ar.ycor()<95:
                        ar.direction ='up'
                    else:
                        ar.sety(-145)

                def go_down():
                    if ar.ycor()>-145:
                        ar.direction ='down'
                    else:
                        ar.sety(95)

                def move():
                    if ar.direction =='up':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() +60)
                        ar.direction='stop'
                        
                    elif ar.direction =='down':
                        time.sleep(0.1)
                        ar.sety(ar.ycor() -60)
                        ar.direction='stop'
                        
                def clicks():
                    if ar.xcor()==-315 and ar.ycor()==95:
                        turtle.clearscreen()
                        #print('c3 (t/f)')
                        turtle.bye()
                        running=False
                        ranking('select* from c3tof order by highestscore desc limit 0,10')

                    elif ar.xcor()==-315 and ar.ycor()==35:
                        turtle.clearscreen()
                        #print('movies (t/f)')
                        turtle.bye()
                        running=False
                        ranking('select* from moviestof order by highestscore desc limit 0,10')

                    elif ar.xcor()==-315 and ar.ycor()==-25:
                        turtle.clearscreen()
                        #print('space (t/f)')
                        turtle.bye()
                        running=False
                        ranking('select* from spacetof order by highestscore desc limit 0,10')
                        

                    elif ar.xcor()==-315 and ar.ycor()==-85:
                        turtle.clearscreen()
                        #print('sports (t/f)')
                        turtle.bye()
                        running=False
                        ranking('select* from sportstof order by highestscore desc limit 0,10')
                       

                    if ar.xcor()==-315 and ar.ycor()==-145:
                        turtle.clearscreen()
                        #print('india (t/f)')
                        turtle.bye()
                        running=False
                        ranking('select* from indiatof order by highestscore desc limit 0,10')
                        
                            

                b.listen()
                b.onkeypress(go_up,'w')
                b.onkeypress(go_down,'s')
                b.onkeypress(clicks,'x')

                while True:
                    try:
                        b.update()
                        move()
                        
                    except:
                        move()
                        break

                     

                            
        def move():
            if tr.direction =='up':
                time.sleep(0.1)
                tr.sety(tr.ycor() +80)
                tr.direction='stop'
                        
            elif tr.direction =='down':
                time.sleep(0.1)
                tr.sety(tr.ycor() -80)
                tr.direction='stop'

        b.listen()
        b.onkeypress(go_up,'w')
        b.onkeypress(go_down,'s')
        b.onkeypress(click,'x')

        while True:
            try:
                b.update()
                move()
                        
            except:
                move()
                break
    def play():
        global s,i,j,o,l,h,tof1,tof2,tof3,tof4,tof5,mcq1,mcq2,mcq3,mcq4,mcq5
        s=0
        i=1
        j=0
        o=-1
        l=[]
        def score1(score):
            conn=abc.connect(host='localhost',user='root',passwd='Admin@123456',database='project')
            global Na,file1
            #print(NA,file1)
            root=Tk()
            root.minsize(1366,768)
            
            root['bg']='black'
            #filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\score.png")
            #background_label = Label(root, image=filename)
            #background_label.place(x=0, y=0, relwidth=1, relheight=1)
            s="Your Final Score Is : "+str(score)
            def next():
                root.destroy()
                try:
                    turtle.clearscreen()
                    opt('yes')
                except:
                    opt('yes')
                            
                    
            def update():
                if file1=='C3questionsop.csv':
                    
                    query="select * from c3op"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update c3op set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update c3op set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                                
                            else:
                                next()

                        else:
                            i+=1
                            
                elif file1=='moviequestionsop.csv':
                    
                    query="select * from moviesop"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update moviesop set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update moviesop set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                            else:
                                next()

                        else:
                            i+=1
                elif file1=='Indquestionsop.csv':
                    
                    query="select * from indiaop"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update indiaop set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update indiaop set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                            else:
                                next()

                        else:
                            i+=1
                elif file1=='Spacequestionsop.csv':
                    
                    query="select * from spaceop"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update spaceop set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update spaceop set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                            else:
                                next()

                        else:
                            i+=1
                elif file1=='sportquestionsop.csv':
                    
                    query="select * from sportsop"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update sportsop set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update sportsop set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                            else:
                                next()

                        else:
                            i+=1
                elif file1=='C3questtof.csv':
                    
                    query="select * from c3tof"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update c3tof set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update c3tof set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                            else:
                                next()

                        else:
                            i+=1
                elif file1=='Indquesttof.csv':
                    
                    query="select * from indiatof"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update indiatof set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update indiatof set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                            else:
                                next()

                        else:
                            i+=1
                elif file1=='moviesquesttof.csv':
                    
                    query="select * from moviestof"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update moviestof set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update moviestof set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                            else:
                                next()

                        else:
                            i+=1
                elif file1=='spacequesttof.csv':
                    
                    query="select * from spacetof"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update spacetof set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update spacetof set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                            else:
                                next()

                        else:
                            i+=1
                elif file1=='sportsquesttof.csv':
                    
                    query="select * from sportstof"
                    c=conn.cursor()
                    c.execute(query)
                    x=c.fetchall()
                    i=0
                    while True:
                        if x[i][1]==NA:
                            #c.execute("update  set total=total+(total*%s/100) where
                            ##print('yes')
                            c.execute("update sportstof set lastgamescore=%s where username=%s",(score,NA))
                            conn.commit()
                            #break

                            max=x[i][-1]
                            if max<score:
                                c.execute("update sportstof set highestscore=%s where username=%s",(score,NA))
                                conn.commit()
                                next()
                            else:
                                next()

                        else:
                            i+=1
                 
            

            
            
                
            scor=Label(root,text=s,background='black',font=('Times',40),bd=40,fg='white').place(x=300,y=100)
            if score<=10:
                p='Better Luck Next Time'
                sa=Label(root,text=p,background='black',font=('Times',30),bd=30,fg='white').place(x=350,y=300)
            elif score>10 and score<=20:
                p='Okay'
                sa=Label(root,text=p,background='black',font=('Times',30),bd=30,fg='white').place(x=350,y=300)
            elif score>20 and score<=30:
                p='Good'
                sa=Label(root,text=p,background='black',font=('Times',30),bd=30,fg='white').place(x=350,y=300)
            elif score>30 and score<=40:
                p='Very Good'
                sa=Label(root,text=p,background='black',font=('Times',30),bd=30,fg='white').place(x=350,y=300)
            elif score>40 and score<50:
                p='Excellent'
                sa=Label(root,text=p,background='black',font=('Times',30),bd=30,fg='white').place(x=350,y=300)
            elif score==50:
                p='Full Marks!!!'
                sa=Label(root,text=p,background='black',font=('Times',30),bd=30,fg='white').place(x=350,y=300)

            
                
                
            button=Button(root,text='Next',background='black',height=1,width=15,command=update,font='Times',fg='white').place(x=1150,y=600)
            
        def fnb(x,v,n,m,w,t,y):
            global op1,op2,op3,op4,s,k,co,j
            co=0
            root=Tk()
            root.minsize(1366,768)
            root.title('QUIZ')
            root['bg']='black'

            #filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\score.png")
            #background_label = Label(root, image=filename)
            #background_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            def NEXT():
                global j,file,k,co,s
                
                    
                if co==0:
                    ui=messagebox.askquestion(title="warning!!",message="Do You Want To Skip This Question?")
                    if ui=='yes':
                        if j<9:
                            root.destroy()
                            j+=1
                            filename(file1)
                        elif j==9:
                            root.destroy()
                            ##print(s)
                            score1(s)
                    if ui=='no':
                        #messagebox.showinfo('Return','You will now return to the question')
                        pass

                elif j==9:
                    root.destroy()
                    ##print(s)
                    score1(s)
                        
                elif co==1 and j<9:
                    root.destroy()
                    j+=1
                    filename(file1)

                    

                
            def check():
                global s,op1,op4,co
                s=s-1
                op2.configure(bg='green',command=NONE,activebackground='green')
                op1.configure(bg='red',command=NONE,activebackground='red')
                op3.configure(command=NONE,activebackground='white')
                op4.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1160,y=0)
                co+=1
            def chec():
                global s,op2,op4,co
                s=s+5
                op1.configure(command=NONE,activebackground='white')
                op2.configure(bg='green',command=NONE,activebackground='green')
                op3.configure(command=NONE,activebackground='white')
                op4.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1160,y=0)
                co+=1
            def che():
                global s,op3,op4,co
                s=s-1
                op3.configure(bg='red',command=NONE,activebackground='red')
                op2.configure(bg='green',command=NONE,activebackground='green')
                op4.configure(command=NONE,activebackground='white')
                op1.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1160,y=0)
                co+=1
            def ch():
                global s,op4,co
                s-=1
                op1.configure(command=NONE,activebackground='white')
                op2.configure(bg='green',command=NONE,activebackground='green')
                op3.configure(command=NONE,activebackground='white')
                op4.configure(bg='red',command=NONE,activebackground='red')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1160,y=0)
                co+=1

            Label(root,text=str(j+1)+') '+v,font=('Times',15),bd=15,background="black",fg='white').place(x=100,y=50)
            ##print((y,z,a,b))
            op1=Button(root,text=n,command=check,height=1,width=25,background='grey',fg='white',font='Times')
            op1.place(x=600,y=300)
            op2=Button(root,text=m,command=chec,height=1,width=25,background='grey',fg='white',font='Times')
            op2.place(x=600,y=350)
            op3=Button(root,text=w,command=che,height=1,width=25,background='grey',fg='white',font='Times')
            op3.place(x=600,y=400)
            op4=Button(root,text=t,command=ch,height=1,width=25,background='grey',fg='white',font='Times')
            op4.place(x=600,y=450)
            score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
            next=Button(root,text='Next',command=NEXT,background='grey',fg='white',height=1,width=15,font='Times').place(x=1150,y=600)
        def fna(x,v,n,m,w,t,y):
            
            global op1,op2,op3,op4,s,k,co,j
            co=0
            root=Tk()
            root.minsize(1366,768)
            root.title("INDIA QUIZ")
            root['bg']='black'
            #filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\score.png")
            #background_label = Label(root, image=filename)
            #background_label.place(x=0, y=0, relwidth=1, relheight=1)

                                   
            def NEXT():
                global j,file,k,co,s
                

                if co==0:
                    ui=messagebox.askquestion(title="warning!!",message="Do You Want To Skip This Question?")
                    ##print(ui)
                    if ui=='yes':
                       if j<9:
                            root.destroy()
                            j+=1
                            filename(file1)
                       elif j==9:
                           root.destroy()
                           ##print(s)
                           score1(s)

                    elif ui=='no':
                        #messagebox.showinfo('Return','You will now return to the application screen')
                        pass
                elif j==9 :
                    root.destroy()
                    ##print(s)
                    score1(s)
                        
                    
                elif co==1 and j<9:
                    root.destroy()
                    j+=1
                    filename(file1)

                    

            def check():
                global s,op1,op4,co
                s=s+5
                op1.configure(bg='green',command=NONE,activebackground='green')
                op2.configure(command=NONE,activebackground='white')
                op3.configure(command=NONE,activebackground='white')
                op4.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            def chec():
                global s,op2,op4,co
                s=s-1
                op2.configure(bg='red',command=NONE,activebackground='red')
                op1.configure(bg='green',command=NONE,activebackground='green')
                op3.configure(command=NONE,activebackground='white')
                op4.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            def che():
                global s,op3,op4,co
                s=s-1
                op3.configure(bg='red',command=NONE,activebackground='red')
                op1.configure(bg='green',command=NONE,activebackground='green')
                op4.configure(command=NONE,activebackground='white')
                op2.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            def ch():
                global s,op4,co
                s-=1
                op2.configure(command=NONE,activebackground='white')
                op1.configure(bg='green',command=NONE,activebackground='green')
                op3.configure(command=NONE,activebackground='white')
                op4.configure(bg='red',command=NONE,activebackground='red')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1

            Label(root,text=str(j+1)+') '+v,font=('Times',15),bd=15,background="black",fg='white').place(x=100,y=50)
            ##print((y,z,a,b))
            op1=Button(root,text=n,command=check,height=1,width=25,background='grey',font='Times')
            op1.place(x=600,y=300)
            op2=Button(root,text=m,command=chec,height=1,width=25,background='grey',font='Times')
            op2.place(x=600,y=350)
            op3=Button(root,text=w,command=che,height=1,width=25,background='grey',font='Times')
            op3.place(x=600,y=400)
            op4=Button(root,text=t,command=ch,height=1,width=25,background='grey',font='Times')
            op4.place(x=600,y=450)
            score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
            next=Button(root,text='Next',command=NEXT,background='grey',fg='white',height=1,width=15,font='Times').place(x=1150,y=600)
        def fnc(x,v,n,m,w,t,y):
            
            global op1,op2,op3,op4,s,k,co,j
            co=0
            root=Tk()
            root.minsize(1366,768)
            root.title("INDIA QUIZ")
            root['bg']='black'
            #filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\score.png")
            #background_label = Label(root, image=filename)
            #background_label.place(x=0, y=0, relwidth=1, relheight=1)

            def NEXT():
                global j,file,k,s
                
                    
                if co==0:
                    ui=messagebox.askquestion(title="warning!!",message="Do You Want To Skip This Question?")
                    ##print(ui)
                    if ui=='yes':
                        if j<9:
                            root.destroy()
                            j+=1
                            filename(file1)
                        elif j==9:
                            root.destroy()
                            ##print(s)
                            score1(s)
                    elif ui=='no':
                        #messagebox.showinfo('Return','You will now return to the application screen')
                        pass
                elif j==9:
                    root.destroy()
                    ##print(s)
                    
                    score1(s)
                        

                elif co==1 and j<9:
                    root.destroy()
                    j+=1
                    filename(file1)

                    

            def check():
                global s,op1,op4,co
                s=s-1
                op1.configure(bg='red',command=NONE,activebackground='red')
                op2.configure(command=NONE,activebackground='white')
                op3.configure(bg='green',command=NONE,activebackground='green')
                op4.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            def chec():
                global s,op2,op4,co
                s=s-1
                op2.configure(bg='red',command=NONE,activebackground='red')
                op3.configure(bg='green',command=NONE,activebackground='green')
                op1.configure(command=NONE,activebackground='white')
                op4.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            def che():
                global s,op3,op4,co
                s=s+5
                op4.configure(command=NONE,activebackground='white')
                op3.configure(bg='green',command=NONE,activebackground='green')
                op1.configure(command=NONE,activebackground='white')
                op2.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            def ch():
                global s,op4,co
                s-=1
                op1.configure(command=NONE,activebackground='white')
                op3.configure(bg='green',command=NONE,activebackground='green')
                op2.configure(command=NONE,activebackground='white')
                op4.configure(bg='red',command=NONE,activebackground='red')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1

            Label(root,text=str(j+1)+') '+v,font=('Times',15),bd=15,background="black",fg='white').place(x=100,y=50)
            ##print((y,z,a,b))
            op1=Button(root,text=n,command=check,height=1,width=25,background='grey',font='Times')
            op1.place(x=600,y=300)
            op2=Button(root,text=m,command=chec,height=1,width=25,background='grey',font='Times')
            op2.place(x=600,y=350)
            op3=Button(root,text=w,command=che,height=1,width=25,background='grey',font='Times')
            op3.place(x=600,y=400)
            op4=Button(root,text=t,command=ch,height=1,width=25,background='grey',font='Times')
            op4.place(x=600,y=450)
            score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
            next=Button(root,text='Next',command=NEXT,background='grey',fg='white',height=1,width=15).place(x=1150,y=600)
        def fn(x,v,n,m,w,t,y):
            global op1,op2,op3,op4,s,k,co,j
            co=0
            root=Tk()
            root.minsize(1366,768)
            root.title("INDIA QUIZ")
            root['bg']='black'
            #filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\score.png")
            #background_label = Label(root, image=filename)
            #background_label.place(x=0, y=0, relwidth=1, relheight=1)
                    
            def NEXT():
                global j,file,k,co,s
                
                    
                if co==0:
                    ui=messagebox.askquestion(title="warning!!",message="Do You Want To Skip This Question?")
                    ##print(ui)
                    if ui=='yes':
                        if j<9:
                            root.destroy()
                            j+=1
                            filename(file1)
                        elif j==9:
                            root.destroy()
                            ##print(s)
                            score1(s)
                        
                    elif ui=='no':
                        #messagebox.showinfo('Return','You will now return to the application screen')
                        pass
                elif j==9:
                    root.destroy()
                    ##print(s)
                    score1(s)
                        
                elif co==1 and j<9:
                    root.destroy()
                    j+=1
                    filename(file1)

                    

                
                
            def check():
                global s,op1,op4,co
                s=s-1
                op1.configure(bg='red',command=NONE,activebackground='red')
                op2.configure(command=NONE,activebackground='white')
                op4.configure(bg='green',command=NONE,activebackground='green')
                op3.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            def chec():
                global s,op2,op4,co
                s=s-1
                op2.configure(bg='red',command=NONE,activebackground='red')
                op4.configure(bg='green',command=NONE,activebackground='green')
                op1.configure(command=NONE,activebackground='white')
                op3.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
             
           

            def che():
                global s,op3,op4,co
                s=s-1
                op3.configure(bg='red',command=NONE,activebackground='red')
                op4.configure(bg='green',command=NONE,activebackground='green')
                op1.configure(command=NONE,activebackground='white')
                op2.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1




            def ch():
                global s,op4,co
                s+=5
                op1.configure(command=NONE,activebackground='white')
                op4.configure(bg='green',command=NONE,activebackground='green')
                op2.configure(command=NONE,activebackground='white')
                op3.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1

            Label(root,text=str(j+1)+') '+v,font=('Times',15),bd=15,background="black",fg='white').place(x=100,y=50)
            ##print((y,z,a,b))
            op1=Button(root,text=n,command=check,height=1,width=25,background='grey',font='Times')
            op1.place(x=600,y=300)
            op2=Button(root,text=m,command=chec,height=1,width=25,background='grey',font='Times')
            op2.place(x=600,y=350)
            op3=Button(root,text=w,command=che,height=1,width=25,background='grey',font='Times')
            op3.place(x=600,y=400)
            op4=Button(root,text=t,command=ch,height=1,width=25,background='grey',font='Times')
            op4.place(x=600,y=450)
            score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
            next=Button(root,text='Next',command=NEXT,background='grey',fg='white',height=1,width=15).place(x=1150,y=600)

            
        def filename(file):
            global file1,o,l
            file1=file
            f=open(file,'r')
            a=list(csv.reader(f))
            ##print(a)
            
            while len(l)!=10:
                k=random.randint(1,len(a)-2)
                if len(l)==10:
                    break
                if k in l:
                    pass
                elif k not in l:
                    l.append(k)
                    ##print(l)
            if o==-1:
                random.shuffle(l)
                ##print(l)
                o+=1
            else:
                pass
            ##print(j)
            i=l[j]    
            #k=len(a)-1
            A=a[i][0]
            b=a[i][1]
            c=a[i][2]
            d=a[i][3]
            e=a[i][4]
            f=a[i][5]
            g=a[i][6]
            
            ##print(g)
            if g=='D':
                fn(A,b,c,d,e,f,g)
            elif g=='C':
                fnc(A,b,c,d,e,f,g)
            elif g=='B':
                fnb(A,b,c,d,e,f,g)
            elif g=='A':
                fna(A,b,c,d,e,f,g)

        def fnt(z,x,v):
            
            global op1,op2,s,co,j
            co=0
            root=Tk()
            root.minsize(1366,768)
            root.title("INDIA QUIZ")
            root['bg']='black'
            #filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\score.png")
            #background_label = Label(root, image=filename)
            #background_label.place(x=0, y=0, relwidth=1, relheight=1)
            def NEXT():
                global j,file,s
                
                    
                if co==0:
                    ui=messagebox.askquestion(title="warning!!",message="Do You Want To Skip This Question?")
                    #print(ui)
                    if ui=='yes':
                        if j<9:
                            root.destroy()
                            j+=1
                            filename1(file1)
                        elif j==9:
                            root.destroy()
                            score1(s)
                        
                    elif ui=='no':
                        #messagebox.showinfo('Return','You will now return to the application screen')
                        pass
                elif j==9:
                    root.destroy()
                    score1(s)
                elif co==1 and j<9:
                    root.destroy()
                    j+=1
                    filename1(file1)

            def check():
                global s,op1,op2,co
                s=s+5
                op1.configure(bg='green',command=NONE,activebackground='green')
                op2.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            
            def chec():
                global s,op2,op1,co
                s=s-1
                op2.configure(bg='red',command=NONE,activebackground='red')
                op1.configure(bg='green',command=NONE,activebackground='green')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
                
            Label(root,text=str(j+1)+') '+x,font=('Times',15),bd=15,background="black",fg='white').place(x=100,y=50)

            op1=Button(root,text='TRUE',command=check,height=1,width=15,background='grey',font='Times',fg='white')
            op1.place(x=600,y=300)
            op2=Button(root,text='FALSE',command=chec,height=1,width=15,background='grey',font='Times',fg='white')
            op2.place(x=600,y=350)
            
            score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
            next=Button(root,text='Next',command=NEXT,background='grey',fg='orange',height=1,width=15,font='Times').place(x=1150,y=600)

        def fnf(z,x,v):
            
            global op1,op2,s,co,j
            co=0
            root=Tk()
            root.minsize(1366,768)
            root.title("QUIZ")
            root['bg']='black'
            #filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\score.png")
            #background_label = Label(root, image=filename)
            #background_label.place(x=0, y=0, relwidth=1, relheight=1)
                
            def NEXT():
                global j,file,co,s
                
                
                
                    
                if co==0:
                    ui=messagebox.askquestion(title="warning!!",message="Do You Want To Skip This Question?")
                    #print(ui)
                    if ui=='yes':
                        if j<9:
                            root.destroy()
                            j+=1
                            filename1(file1)
                        elif j==9:
                            root.destroy()
                            score1(s)
                        
                    elif ui=='no':
                        #messagebox.showinfo('Return','You will now return to the application screen')
                        pass
                elif j==9:
                    root.destroy()
                    score1(s)
                elif co==1 and j<9:
                    root.destroy()
                    j+=1
                    filename1(file1)

            def check():
                global s,op1,op2,co
                s=s-1
                op1.configure(bg='red',command=NONE,activebackground='red')
                op2.configure(bg='green',command=NONE,activebackground='green')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            def chec():
                global s,op2,op1,co
                s=s+5
                op2.configure(bg='green',command=NONE,activebackground='green')
                op1.configure(command=NONE,activebackground='white')
                score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
                co+=1
            Label(root,text=str(j+1)+') '+x,font=('Times',15),bd=18,background="black",fg='white').place(x=100,y=50)

            op1=Button(root,text='TRUE',command=check,height=1,width=15,background='grey',fg='white',font='Times')
            op1.place(x=600,y=300)
            op2=Button(root,text='FALSE',command=chec,height=1,width=15,background='grey',fg='white',font='Times')
            op2.place(x=600,y=350)
            
            score=Label(root,text='SCORE:'+str(s),background='black',font=('forte',30),bd=30,fg='green').place(x=1150,y=0)
            next=Button(root,text='Next',command=NEXT,background='grey',fg='orange',height=1,width=15,font='Times').place(x=1150,y=600)

        def filename1(file):
            global file1,o
            file1=file
            f=open(file,'r')
            a=list(csv.reader(f))
            while len(l)!=10:
                k=random.randint(1,len(a)-2)
                if len(l)==10:
                    break
                if k in l:
                    pass
                elif k not in l:
                    l.append(k)
                    ##print(l)
            if o==-1:
                random.shuffle(l)
                ##print(l)
                o+=1
            else:
                pass
            ##print(j)
            i=l[j]    
            A=a[i][0]
            b=a[i][1]
            c=a[i][2]
            ##print(A,b,c)
            if c=='F':
                fnf(A,b,c)
            elif c=='T':
                fnt(A,b,c)

          
            ##print(a)
        def choose():
            a=turtle.Turtle()
            b=turtle.Screen()
            a.hideturtle()
            b.setup(width=1366,height=768)
            b.title('CHOOSE TYPE OF QUIZ')
            #b.bgpic('choose.png')
            #b.bgcolor('medium slate blue')
            a.pencolor('brown')
            b.bgpic('type.png')
            a.penup()
            a.goto(-400,250)
            a.write('CHOOSE THE TYPE OF QUIZ', font=('Lucida Handwriting',40,'normal'),align='left')
            a.goto(-280,20)
            a.pencolor('white')
            if mcq1==1 and mcq2==1 and mcq3==1 and mcq4==1 and mcq5==1:
                a.write('\u0336'.join('GENERAL KNOWLEDGE QUIZ')+'\u0336', font=('Lucida Handwriting',20,'normal'),align='left')
            else:
                a.write('GENERAL KNOWLEDGE QUIZ',font=('Lucida Handwriting',20,'normal'),align='left')
            a.goto(-280,-60)
            if tof1==1 and tof2==1 and tof3==1 and tof4==1 and tof5==1:
                a.write('\u0336'.join('TRUE OR FALSE')+'\u0336', font=('Lucida Handwriting',20,'normal'),align='left')
            else:
                a.write('TRUE OR FALSE', font=('Lucida Handwriting',20,'normal'),align='left')


            tr= turtle.Turtle()
            tr.penup()
            tr.goto(-295,35)
            tr.speed(0)
            tr.shape('arrow')
            tr.color('chartreuse')

            tr.direction='stop'

            def go_up():
                if tr.ycor()<35:
                    tr.direction ='up'
                else:
                    tr.sety(-45)

            def go_down():
                if tr.ycor()>-45:
                    tr.direction ='down'
                else:
                    tr.sety(35)

            def click():
                global mcq1,mcq2,mcq3,mcq4,mcq5,tof1,tof2,tof3,tof4,tof5
                if tr.xcor()==-295 and tr.ycor()==35:
                    
                    #general knowledge quiz
                    if mcq1==0 and mcq2==0 and mcq3==0 and mcq4==0 and mcq5==0:
                        turtle.clearscreen()
                        b.title('CHOOSE THE CATEGORY OF THE QUIZ')
                        b.bgpic('cate.png')
                        #b.bgcolor('yellow')
                        a.pencolor('white')
                        a.penup()
                        a.goto(-400,300)
                        a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Lucida Handwriting',40,'normal'),align='left')
                        a.goto(-300,80)
                        a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Lucida Handwriting',20,'normal'),align='left')
                        a.goto(-300,20)
                        a.write('MOVIES',font=('Lucida Handwriting',20,'normal'),align='left')
                        a.goto(-300,-40)
                        a.write('SPACE',font=('Lucida Handwriting',20,'normal'),align='left')
                        a.goto(-300,-100)
                        a.write('SPORTS',font=('Lucida Handwriting',20,'normal'),align='left')
                        a.goto(-300,-160)
                        a.write('INCREDIBLE INDIA',font=('Lucida Handwriting',20,'normal'),align='left')

                        ar= turtle.Turtle()
                        ar.penup()
                        ar.goto(-315,95)
                        ar.speed(0)
                        ar.shape('arrow')
                        ar.color('green')
                        ar.direction='stop'
       
                        def go_up():
                            if ar.ycor()<95:
                                ar.direction ='up'
                            else:
                                ar.sety(-145)

                        def go_down():
                            if ar.ycor()>-145:
                                ar.direction ='down'
                            else:
                                ar.sety(95)
                                '''
                        def ch():
                            #print(tr.xcor(),tr.ycor())
                                '''
                        def move():
                            if ar.direction =='up':
                                time.sleep(0.1)
                                ar.sety(ar.ycor() +60)
                                ar.direction='stop'
                        
                            elif ar.direction =='down':
                                time.sleep(0.1)
                                ar.sety(ar.ycor() -60)
                                ar.direction='stop'
                                

                        
                        def clicks():
                            global mcq1,mcq2,mcq3,mcq4,mcq5
                            if ar.xcor()==-315 and ar.ycor()==95 :
                                turtle.clearscreen()
                                ##print('c3 (mcq)')
                                turtle.bye()
                                running=False
                                mcq1+=1
                                filename('C3questionsop.csv')#,'C3 QUESTIONS MCQ'
                            elif ar.xcor()==-315 and ar.ycor()==35:
                                turtle.clearscreen()
                                #print('movies (mcq)')
                                turtle.bye()
                                running=False
                                mcq2+=1
                                filename('moviequestionsop.csv')#,'MOVIES QUESTIONS MCQ'
                            elif ar.xcor()==-315 and ar.ycor()==-25:
                                turtle.clearscreen()
                                #print('space (mcq)')
                                turtle.bye()
                                running=False
                                mcq3+=1
                                filename('Spacequestionsop.csv')#,'SPACE QUESTIONS MCQ'

                            elif ar.xcor()==-315 and ar.ycor()==-85:
                                turtle.clearscreen()
                                #print('sports (mcq)')
                                turtle.bye()
                                running=False
                                mcq4+=1
                                filename('sportquestionsop.csv')#,'SPORTS QUESTIONS MCQ'

                            if ar.xcor()==-315 and ar.ycor()==-145:
                                turtle.clearscreen()
                                #print('india (mcq)')
                                turtle.bye()
                                running=False
                                mcq5+=1
                                filename('Indquestionsop.csv')#,'INDIA QUESTIONS MCQ'
                        b.listen()
                        b.onkeypress(go_up,'w')
                        b.onkeypress(go_down,'s')
                        b.onkeypress(clicks,'x')
                        
                        while True:
                            try:
                                b.update()
                                move()
                        
                            except:
                                move()
                                break
                            
                    elif mcq1==1 and mcq2==1 and mcq3==1 and mcq4==1 and mcq5==1:
                        messagebox.showinfo(title="Error",message="You have attended all Categories from this Type once")
                        
                    elif mcq1==0 or mcq2==0 or mcq3==0 or mcq4==0 or mcq5==0:
                        turtle.clearscreen()
                        b.title('CHOOSE THE CATEGORY OF THE QUIZ')
                        b.bgpic('cate.png')
                        b.bgcolor('yellow')
                        a.pencolor('white')
                        a.penup()
                        a.goto(-400,300)
                        a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                        a.goto(-300,80)
                        if mcq1==1:
                            a.write('\u0336'.join('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)')+'\u0336',font=('Lucida Handwriting',20,'normal'),align='left')
                        elif mcq1==0:
                            a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES)',font=('Lucida Handwriting',20,'normal'),align='left')
                        a.goto(-300,20)
                        if mcq2==0:
                            a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                        elif mcq2==1:
                            a.write('\u0336'.join('MOVIES')+'\u0336',font=('Lucida Handwriting',20,'normal'),align='left')
                        a.goto(-300,-40)
                        if mcq3==0:
                            a.write('SPACE',font=('Lucida Handwriting',20,'normal'),align='left')
                        elif mcq3==1:
                            a.write('\u0336'.join('SPACE')+'\u0336',font=('Lucida Handwriting',20,'normal'),align='left')
                        a.goto(-300,-100)
                        if mcq4==0:
                            a.write('SPORTS',font=('Lucida Handwriting',20,'normal'),align='left')
                        elif mcq4==1:
                            a.write('\u0336'.join('SPORTS')+'\u0336',font=('Lucida Handwriting',20,'normal'),align='left')
                        a.goto(-300,-160)
                        if mcq5==0:
                            a.write('INCREDIBLE INDIA',font=('Lucida Handwriting',20,'normal'),align='left')
                        elif mcq5==1:
                            a.write('\u0336'.join('INCREDIBLE INDIA')+'\u0336',font=('Lucida Handwriting',20,'normal'),align='left')
                            

                        ar= turtle.Turtle()
                        ar.penup()
                        ar.goto(-315,95)
                        ar.speed(0)
                        ar.shape('arrow')
                        ar.color('green')
                        ar.direction='stop'
               
                        def go_up():
                            if ar.ycor()<95:
                                ar.direction ='up'
                            else:
                                ar.sety(-145)

                        def go_down():
                            if ar.ycor()>-145:
                                ar.direction ='down'
                            else:
                                ar.sety(95)

                        def move():
                            if ar.direction =='up':
                                time.sleep(0.1)
                                ar.sety(ar.ycor() +60)
                                ar.direction='stop'
                                
                            elif ar.direction =='down':
                                time.sleep(0.1)
                                ar.sety(ar.ycor() -60)
                                ar.direction='stop'
                                        

                                
                        def clicks():
                            global mcq1,mcq2,mcq3,mcq4,mcq5
                            if ar.xcor()==-315 and ar.ycor()==95 :
                                if mcq1==0:
                                    turtle.clearscreen()
                                    ##print('c3 (mcq)')
                                    turtle.bye()
                                    running=False
                                    mcq1+=1
                                    try:
                                        filename('C3questionsop.csv')#,'C3 QUESTIONS MCQ'
                                    except:
                                        filename('C3questionsop.csv')#,'C3 QUESTIONS MCQ'
                                else:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")
                            elif ar.xcor()==-315 and ar.ycor()==35:
                                if mcq2==0:
                                    turtle.clearscreen()
                                    ##print('movies (mcq)')
                                    turtle.bye()
                                    running=False
                                    mcq2+=1
                                    try:
                                        filename('moviequestionsop.csv')#,'MOVIES QUESTIONS MCQ'
                                    except:
                                        filename('moviesquestionop.csv')#,'MOVIES QUESTION MCQ'
                                else:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")
                            elif ar.xcor()==-315 and ar.ycor()==-25:
                                if mcq3==0:
                                    turtle.clearscreen()
                                    ##print('movies (mcq)')
                                    turtle.bye()
                                    running=False
                                    mcq3+=1
                                    try:
                                        filename('Spacequestionsop.csv')#,'MOVIES QUESTIONS MCQ'
                                    except:
                                        filename('Spacequestionsop.csv')#,'MOVIES QUESTIONS MCQ'
                                else:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")

                            elif ar.xcor()==-315 and ar.ycor()==-85:
                                if mcq4==0:
                                    turtle.clearscreen()
                                    ##print('movies (mcq)')
                                    turtle.bye()
                                    running=False
                                    mcq4+=1
                                    try:
                                        filename('sportquestionsop.csv')#,'MOVIES QUESTIONS MCQ'
                                    except:
                                        filename('sportquestionsop.csv')#,'MOVIES QUESTIONS MCQ'
                                else:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")

                            if ar.xcor()==-315 and ar.ycor()==-145:
                                if mcq5==0:
                                    turtle.clearscreen()
                                    ##print('movies (mcq)')
                                    turtle.bye()
                                    running=False
                                    mcq5+=1
                                    try:
                                        filename('Indquestionsop.csv')#,'MOVIES QUESTIONS MCQ'
                                    except:
                                        filename('Indquestionsop.csv')#,'MOVIES QUESTIONS MCQ'
                                else:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")
                                        
                                    
                                    

                        b.listen()
                        b.onkeypress(go_up,'w')
                        b.onkeypress(go_down,'s')
                        b.onkeypress(clicks,'x')
                        while True:
                            try:
                                b.update()
                                move()
                                
                            except:
                                move()
                                break
                        
                    

                        
                elif tr.xcor()==-295 and tr.ycor()==-45:
                    ##print(tof1,tof2,tof3,tof4,tof4,tof5)
                    if tof1==0 and tof2==0 and tof3==0 and tof4==0 and tof5==0:
                        turtle.clearscreen()
                        #true or false
                        b.title('CHOOSE THE CATEGORY OF THE QUIZ')
                        b.bgpic('cate.png')
                        b.bgcolor('yellow')
                        a.pencolor('white')
                        a.penup()
                        a.goto(-400,300)
                        a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                        a.goto(-300,80)
                        a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES',font=('Arial',20,'normal'),align='left')
                        a.goto(-300,20)
                        a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                        a.goto(-300,-40)
                        a.write('SPACE',font=('Arial',20,'normal'),align='left')
                        a.goto(-300,-100)
                        a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                        a.goto(-300,-160)
                        a.write('INDIA',font=('Arial',20,'normal'),align='left')

                        ar= turtle.Turtle()
                        ar.penup()
                        ar.goto(-315,95)
                        ar.speed(0)
                        ar.shape('arrow')
                        ar.color('green')
                        ar.direction='stop'
                    

                        def go_up():
                            if ar.ycor()<95:
                                ar.direction ='up'
                            else:
                                ar.sety(-145)

                        def go_down():
                            if ar.ycor()>-145:
                                ar.direction ='down'
                            else:
                                ar.sety(95)
                                '''
                        def ch():
                            #print(tr.xcor(),tr.ycor())
                                '''
                        def move():
                            if ar.direction =='up':
                                time.sleep(0.1)
                                ar.sety(ar.ycor() +60)
                                ar.direction='stop'
                        
                            elif ar.direction =='down':
                                time.sleep(0.1)
                                ar.sety(ar.ycor() -60)
                                ar.direction='stop'
                        
                        def clicks():
                            global tof1,tof2,tof3,tof4,tof5
                            if ar.xcor()==-315 and ar.ycor()==95:
                                turtle.clearscreen()
                                #print('c3 (t/f)')
                                turtle.bye()
                                running=False
                                tof1+=1
                                filename1('C3questtof.csv')#,'C3 (TRUE/FALSE) QUIZ'
                            elif ar.xcor()==-315 and ar.ycor()==35:
                                turtle.clearscreen()
                                #print('movies (t/f)')
                                turtle.bye()
                                running=False
                                tof2+=1
                                filename1('moviesquesttof.csv')#,'MOVIES (TRUE/FALSE) QUIZ'
                            elif ar.xcor()==-315 and ar.ycor()==-25:
                                turtle.clearscreen()
                                #print('space (t/f)')
                                turtle.bye()
                                running=False
                                tof3+=1
                                filename1('spacequesttof.csv')#,'SPACE (TRUE/FALSE) QUIZ'

                            elif ar.xcor()==-315 and ar.ycor()==-85:
                                turtle.clearscreen()
                                #print('sports (t/f)')
                                turtle.bye()
                                running=False
                                tof4+=1
                                filename1('sportsquesttof.csv')#,'SPORTS (TRUE/FALSE) QUIZ'

                            if ar.xcor()==-315 and ar.ycor()==-145:
                                turtle.clearscreen()
                                #print('india (t/f)')
                                turtle.bye()
                                running=False
                                tof5+=1
                                filename1('Indquesttof.csv')#'INDIA (TRUE/FALSE) QUIZ'
                            

                        b.listen()
                        b.onkeypress(go_up,'w')
                        b.onkeypress(go_down,'s')
                        b.onkeypress(clicks,'x')

                        while True:
                            try:
                                b.update()
                                move()
                        
                            except:
                                move()
                                break
                
                    elif tof1==1 and tof2==1 and tof3==1 and tof4==1 and tof5==1:
                        messagebox.showinfo(title="Error!",message="You have attended all the Categories of this Type once")
                    elif tof1>=0 or tof2>=0 or tof3>=0 or tof4>=0 or tof5>=0:
                        turtle.clearscreen()
                        #true or false
                        b.title('CHOOSE THE CATEGORY OF THE QUIZ')
                        b.bgpic('cate.png')
                        b.bgcolor('yellow')
                        a.pencolor('white')
                        a.penup()
                        a.goto(-400,300)
                        a.write('CHOOSE CATEGORY OF YOUR TYPE', font=('Arial',40,'normal'),align='left')
                        a.goto(-300,80)
                        if tof1==1:
                            a.write('\u0336'.join('C3(COUNTRIES ,CAPITALS AND CURRENCIES')+'\u0336',font=('Arial',20,'normal'),align='left')
                        elif tof1==0:
                            a.write('C3 (COUNTRIES ,CAPITALS AND CURRENCIES',font=('Arial',20,'normal'),align='left')
                        a.goto(-300,20)
                        if tof2==0:
                            a.write('MOVIES',font=('Arial',20,'normal'),align='left')
                        elif tof2==1:
                            a.write('\u0336'.join('MOVIES')+'\u0336',font=('Arial',20,'normal'),align='left')
                        a.goto(-300,-40)
                        if tof3==0:
                            a.write('SPACE',font=('Arial',20,'normal'),align='left')
                        elif tof3==1:
                            a.write('\u0336'.join('SPACE')+'\u0336',font=('Arial',20,'normal'),align='left')
                        a.goto(-300,-100)
                        if tof4==0:
                            a.write('SPORTS',font=('Arial',20,'normal'),align='left')
                        elif tof4==1:
                            a.write('\u0336'.join('SPORTS')+'\u0336',font=('Arial',20,'normal'),align='left')
                        a.goto(-300,-160)
                        if tof5==0:
                            a.write('INCREDIBLE INDIA',font=('Arial',20,'normal'),align='left')
                        elif tof5==1:
                             a.write('\u0336'.join('INCREDIBLE INDIA')+'\u0336',font=('Arial',20,'normal'),align='left')
                            

                        ar= turtle.Turtle()
                        ar.penup()
                        ar.goto(-315,95)
                        ar.speed(0)
                        ar.shape('arrow')
                        ar.color('green')
                        ar.direction='stop'
                    

                        def go_up():
                            if ar.ycor()<95:
                                ar.direction ='up'
                            else:
                                ar.sety(-145)

                        def go_down():
                            if ar.ycor()>-145:
                                ar.direction ='down'
                            else:
                                ar.sety(95)
                                '''
                        def ch():
                            #print(tr.xcor(),tr.ycor())
                                '''
                        def move():
                            if ar.direction =='up':
                                time.sleep(0.1)
                                ar.sety(ar.ycor() +60)
                                ar.direction='stop'
                        
                            elif ar.direction =='down':
                                time.sleep(0.1)
                                ar.sety(ar.ycor() -60)
                                ar.direction='stop'
                        
                        def clicks():
                            global tof1,tof2,tof3,tof4,tof5
                            if ar.xcor()==-315 and ar.ycor()==95:
                                if tof1==0:
                                    turtle.clearscreen()
                                    ##print('c3 (t/f)')
                                    turtle.bye()
                                    running=False
                                    tof1+=1
                                    filename1('C3questtof.csv')#,'C3 (TRUE/FALSE) QUIZ'
                                elif tof1==1:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")
                            elif ar.xcor()==-315 and ar.ycor()==35:
                                if tof2==0:
                                    turtle.clearscreen()
                                    ##print('movies (t/f)')
                                    turtle.bye()
                                    running=False
                                    tof2+=1
                                    filename1('moviesquesttof.csv')#,'MOVIES (TRUE/FALSE) QUIZ'
                                elif tof2==1:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")
                            elif ar.xcor()==-315 and ar.ycor()==-25:
                                if tof3==0:
                                    turtle.clearscreen()
                                    ##print('space (t/f)')
                                    turtle.bye()
                                    running=False
                                    tof3+=1
                                    filename1('spacequesttof.csv')#,'SPACE (TRUE/FALSE) QUIZ'
                                elif tof3==1:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")

                            elif ar.xcor()==-315 and ar.ycor()==-85:
                                if tof4==0:
                                    turtle.clearscreen()
                                    ##print('sports (t/f)')
                                    turtle.bye()
                                    running=False
                                    tof4+=1
                                    filename1('sportsquesttof.csv')#,'SPORTS (TRUE/FALSE) QUIZ'
                                elif tof4==1:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")

                            if ar.xcor()==-315 and ar.ycor()==-145:
                                if tof5==0:
                                    turtle.clearscreen()
                                    ##print('india (t/f)')
                                    turtle.bye()
                                    running=False
                                    tof5+=1
                                    filename1('Indquesttof.csv')#'INDIA (TRUE/FALSE) QUIZ'
                                elif tof5==1:
                                    messagebox.showinfo(title="Error!",message="You have attended this category once")
                            

                        b.listen()
                        b.onkeypress(go_up,'w')
                        b.onkeypress(go_down,'s')
                        b.onkeypress(clicks,'x')

                        while True:
                            try:
                                b.update()
                                move()
                        
                            except:
                                move()
                                break

                        
            def move():
                
                if tr.direction =='up':
                    time.sleep(0.1)
                    tr.sety(tr.ycor() +80)
                    tr.direction='stop'
                    
                elif tr.direction =='down':
                    time.sleep(0.1)
                    tr.sety(tr.ycor() -80)
                    tr.direction='stop'

            b.listen()
            b.onkeypress(go_up,'w')
            b.onkeypress(go_down,'s')
            b.onkeypress(click,'x')

            while True:
                try:
                    b.update()
                    move()
                    
                except:
                    move()
                    break
        choose()
        #play and check
    def opt(t):
        global tof1,tof2,tof3,tof4,tof5,mcq1,mcq2,mcq3,mcq4,mcq5
        while t=='yes':
            t='no'
            def go_up2():
                if ar.ycor()<65:
                    ar.direction ='up'
                else:
                    ar.sety(-85)

            def go_down2():
                if ar.ycor()>-85:
                    ar.direction ='down'
                else:
                    ar.sety(65)

            pen=turtle.Turtle()
            p=turtle.Screen()
            p.setup(width=1366,height=768)
            pen.hideturtle()
            p.bgpic('play.png')
            #p.bgcolor('MediumSlateBlue')
            w='  '
            pen.pencolor('grey')
            pen.penup()
            time.sleep(0.01)      
            pen.goto(-200,280)
            pen.write(w,font=('Belluccia',40,'bold'),align='left')
            time.sleep(0.01)     
            pen.goto(-100,50)
            a=['Lucida Handwriting','Showcard Gothic']
            random.shuffle(a)
            font1=a[0]
            if mcq1==1 and mcq2==1 and mcq3==1 and mcq4==1 and mcq5==1 and tof1==1 and tof2==1 and tof3==1 and tof4==1 and tof5==1:
                pen.write('\u0336'.join('PLAY')+'\u0336',font=(font1,20,'normal'),align='left')
            else:   
                pen.write('PLAY',font=(font1,20,'normal'),align='left')
            #time.sleep(0.01)
            pen.goto(-100,0)
            pen.write('ABOUT(SYNOPSIS)',font=(font1,20,'normal'),align='left')
            pen.goto(-100,-50)
            pen.write('RANKING',font=(font1,20,'normal'),align='left')
            pen.goto(-100,-100)
            pen.write('QUIT',font=(font1,20,'normal'),align='left')

            ar= turtle.Turtle()
            ar.speed(0)
            ar.penup()
            ar.shape('arrow')
            ar.color('Chartreuse')
            ar.penup()

            ar.goto(-120.0,65.0)
            ar.direction='stop'
            def click3(x,y):
                global tof1,tof2,tof3,tof4,tof5,mcq1,mcq2,mcq3,mcq4,mcq5
                
                #print(x,y)
                if x==-120 and y==65:
                    
                    if mcq1==1 and mcq2==1 and mcq3==1 and mcq4==1 and mcq5==1 and tof1==1 and tof2==1 and tof3==1 and tof4==1 and tof5==1:
                        messagebox.showinfo(title="Error!",message="You have attended all types and all categories once")
                    else:
                        turtle.clearscreen()
                        play()
                if x==-120 and y==15:
                    turtle.clearscreen()
                    #turtle.bye()
                    #running=False
                    p.bgpic('synopsis.png')
                    pen.pencolor('black')
                    pen.penup()
                    def quit1(x,y):
                        pen.clear()
                        turtle.clearscreen()
                        turtle.bye()
                        running=False
                        try:
                            opt('yes')
                        except:
                            opt('yes')
                    def next7(x,y):
                        pen.clear()
                        pen.goto(-650,300)
                        pen.write("CREATION OF ADMIN ACCOUNT:",font=('Times',25,'bold'),align='left')
                        pen.goto(-650,280)
                        pen.write("-------------------------------------------------",font=('times',25,'bold'),align='left')
                        pen.goto(-600,240)
                        pen.write("* YOU CAN ADD ADMIN ACCOUNTS OR USER ACCOUNTS. ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,200)
                        pen.write("* TO ADD YOU MUST FIRST CHOOSE ADMIN OR PLAYER. IF YOU CHOOSE ADMIN ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,160)
                        pen.write("  YOU CAN CREATE AN ADMIN ACCOUNT AND IF YOU CHOOSE PLAYER YOU CAN   ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,120)
                        pen.write("  CREATE A PLAYER ACCOUNT.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,80)
                        pen.write("* AFTER CHOOSING ADMIN OR PLAYER YOU MUST SELECT THE CREATE ACCOUNT  ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,40)
                        pen.write("  OPTION . AFTER CHOOSING IT YOU MUST GIVE THE NECESSARY",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,0)
                        pen.write("  DETAILS(NAME,AGE,EMAIL ID,USERNAME,PASSWORD).",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-40)
                        pen.write("* IF YOU DON'T GIVE THE DETAILS PROPERLY, THEN YOU WILL BE GIVEN AN",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-80)
                        pen.write("  ERROR MESSAGE TO FILL IT PROPERLY.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-120)
                        pen.write("*  AFTER FILLING ALL THE DETAILS, SELECT THE CREATE BUTTON AND THE ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-160)
                        pen.write("   ACCOUNT WILL BE CREATED AND IT’S DETAILS WILL BE STORED IN A ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-200)
                        pen.write("  TABLE ALONG WITH THE OTHER ACCOUNTS.",font=('Lucida Handwriting',20,'normal'),align='left')
                        turtle.onscreenclick(quit1,3)
                    def next6(x,y):
                        pen.clear()
                        pen.goto(-600,300)
                        pen.write("* YOU WILL BE DISPLAYED A TABLE OF THE CONTENT OF THE FILE WHICH ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,260)
                        pen.write("  CONTAINS THE QUESTIONS FROM THE PARTICULAR TYPE AND CATEGORY.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,220)
                        pen.write("   EACH QUESTION WILL HAVE A SERIAL NUMBER AT THE START.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,180)
                        pen.write("* YOU MUST TYPE IN THE SERIAL NUMBER OF THE QUESTION YOU WANT",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,140)
                        pen.write("  TO DELETE IN THE GIVEN FIELD.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,100)
                        pen.write("*  AFTER SELECTING DELETE, THE QUESTION GETS DELETED AND YOU WILL",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,60)
                        pen.write("   BE DISPLAYED THE UPDATED FILE OF THE QUESTIONS IN TABLE FORM.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-650,0)
                        pen.write("RANKING:",font=('Times',25,'bold'),align='left')
                        pen.goto(-650,-20)
                        pen.write("---------------",font=('times',25,'bold'),align='left')
                        pen.goto(-600,-60)
                        pen.write("* THE SCORE RANKING OF THE GAME CAN BE VIEWED BY BOTH PLAYERS AND ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-100)
                        pen.write("  ADMINS. EACH TYPE AND CATEGORY HAS IT’S OWN RANKING TABLES.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-140)
                        pen.write("* TO VIEW THE RANKING YOU MUST SELECT THE RANKING OPTION. YOU MUST",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-180)
                        pen.write("  THEN SELECT THE TYPE AND CATEGORY OF QUESTIONS FOR WHICH YOU WANT",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-220)
                        pen.write("  TO SEE THE RANKING.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-260)
                        pen.write("* YOU CAN THEN SEE THE RANKING.PLAYERS ARE RANKED BASED ON THE",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-300)
                        pen.write("  HIGHEST SCORE THEY GOT IN THAT PARTICULAR TYPE AND CATEGORY.",font=('Lucida Handwriting',20,'normal'),align='left')
                        turtle.onscreenclick(next7,3)
                    def next5(x,y):
                        pen.clear()
                        pen.goto(-600,300)
                        pen.write("  IF IT'S ,THEN FILL IN THE ANSWER FIELD WITH B,AND SO ON",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,260)
                        pen.write("* IF YOU CHOOSE TRUE OR FALSE .YOU WILL BE ASKED TO FILL IN THE ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,220)
                        pen.write("  QUESTION AND THE ANSWER.IF THE ANSWER IS TRUE ,THEN FILL IN THE ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,180)
                        pen.write("  ANSWER FIELD WITH T AND IF THEIF THE ANSWER IS FALSE ,THEN FILL",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,140)
                        pen.write("  IN THE ANSWER FIELD WITH F",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,100)
                        pen.write("* AFTER SELECTING THE ADD BUTTON,THE QUESTIONS GETS ADDED TO THE FILE",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,60)
                        pen.write("  AND CAN APPEAR WHILE PLAYING",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-650,0)
                        pen.write("DELETING QUESTION:",font=('Times',25,'bold'),align='left')
                        pen.goto(-650,-20)
                        pen.write("---------------------------------",font=('Times',25,'bold'),align='left')
                        pen.goto(-600,-60)
                        pen.write("* ADMINS CAN DELETE QUESTIONS AS WELL.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-100)
                        pen.write("* TO DELETE A QUESTION, YOU MUST SELECT DELETE QUESTION OPTION IN THE",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-140)
                        pen.write("  ADMIN PAGE.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-180)
                        pen.write("* AFTER SELECTING IT, YOU WILL BE ASKED TO CHOOSE THE TYPE OF QUESTION",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-220)
                        pen.write("   FROM WHICH YOU WANT TO DELETE(MCQ OR TRUE Or FALSE).",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-260)
                        pen.write("* AFTER SELECTING IT, YOU MUST SELECT THE CATEGORY WHICH HAS THE ",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-300)
                        pen.write("  QUESTION YOU WANT TO DELETE.",font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-340)
                        pen.write("*  AFTER SELECTING THE CATEGORY, YOU CAN DELETE THE QUESTION.",font=('Lucida Handwriting',20,'normal'),align='left')
                        turtle.onscreenclick(next6,3)
                    def next4(x,y):
                        pen.clear()
                        pen.goto(-650,300)
                        pen.write('ADMIN:',font=('Times',25,'bold'),align='left')
                        pen.goto(-650,280)
                        pen.write('-----------',font=('Times',25,'bold'),align='left')
                        pen.goto(-600,240)
                        pen.write('* ADMIN IS THE ONLY ONE WHO CAN ADD OR DELETE QUESTIONS WHERE THEY',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,200)
                        pen.write('  HAVE APPOPRIATE SPACE TO ADD OR DELETE QUESTIONS,AND VIEW THE DETAILS',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,160)
                        pen.write('  OF PLAYERS AND ADMINS',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,100)
                        pen.write('ADDING QUESTIONS:' ,font=('Times',25,'bold'),align='left')
                        pen.goto(-600,80)
                        pen.write('-------------------------------',font=('Times',25,'bold'),align='left')
                        pen.goto(-550,40)
                        pen.write('* ADMINS CAN ADD ONE QUESTION AT A TIME' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,0)
                        pen.write('* TO ADD A QUESTION YOU MUST SELECT ADD QUESTION OPTION IN THE ADMIN' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-40)
                        pen.write('   PAGE' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-80)
                        pen.write('* AFTER SELECTING IT ,YOU WILL BE ASKED TO CHOOSE THE TYPE OF  ' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-120)
                        pen.write('  QUESTIONS (MCQ OR TRUE/FALSE)' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-160)
                        pen.write('* AFTER SELECTING IT ,YOU MUST SELECT THE CATEGORY TO WHICH YOU  ' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-200)
                        pen.write('  WANT TO ADD ' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-240)
                        pen.write('* AFTER SELECTING CATEGORY,YOU CAN ADD THE QUESTION.IF YOU CHOOSE',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-280)
                        pen.write('  MCQ ,YOU WILL BE ASKED TO FILL IN THE QUESTION,THE 4 OPTIONS' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-320)
                        pen.write('  (A,B,C AND D),AND THE ANSWER.IF THE ANSWER IS A ,YOU MUST FILL IN A, ' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        turtle.onscreenclick(next5,3)
                    def next3(x,y):
                        pen.clear()
                        pen.goto(-600,300)
                        pen.write('* ONLY ADMINS CAN ACCESS ADMINS FEATURES .ADMINS,AFTER SELECTING',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,260)
                        pen.write('  LOGIN OR CREATING ACCOUNT ,ADMINS MUST ENTER APPROPRIATE PASSWORD',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,220)
                        pen.write('  FOR VERIFICATION',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,180)
                        pen.write('* IF YOU DONT HAVE AN ACCOUNT, THEN YOU MUST CREATE ONE BY' ,font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,140)
                        pen.write('  CHOOSING CREATE ACCOUNT. ONCE YOU CREATED AN ACCOUNT,YOUR ',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,100)
                        pen.write('  DETAILS WILL BE STORED.',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,60)
                        pen.write('* AFTER LOGGING IN, YOU CAN PLAY THE GAME BY SELETING ANY',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,20)
                        pen.write('  1 OF THE TYPE OF QUESTION AND IN THAT YOU CAN SELECT ANY',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-20)
                        pen.write('  ONE OF THE CATEGORY .',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-60)
                        pen.write('* FOR EACH CORRECT ANSWER,THE YOU WILL BE AWARDED 5 MARKS AND',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-100)
                        pen.write('  FOR EACH INCORRECT ANSWER YOU WILL BE AWARDED -1 MARK.',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-140)
                        pen.write('* IF THE ANSWER YOU CHOSE IS CORRECT,IT WILL BE REFLECTED BY GREEN ',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-180)
                        pen.write('  COLOUR.IF THE ANSWER IS INCORRECT,IT WILL BE REFLECTED WITH RED',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-220)
                        pen.write('  COLOUR AND ALONG WITH THE CORRECT ANSWER.',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-260)
                        pen.write('*  FINALLY YOU WILL GET YOUR SCORE WHICH WILL BE COMPARED WITH THE',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-300)
                        pen.write('   SCORES OF ALL THE PLAYERS AND YOU WILL BE GIVEN YOUR RESPECTIVE',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-340)
                        pen.write('  RANK FOR EACH CATEGORY',font=('Lucida Handwriting',20,'normal'),align='left')
                        turtle.onscreenclick(next4,3)
                    def next2(x,y):
                        pen.clear()
                        pen.goto(-600,300)
                        pen.write('THERE WILL BE FIVE CATEGORIES IN EACH TYPE:',font=('Lucida Handwriting',20,'bold'),align='left')
                        pen.goto(-550,260)
                        pen.write('* C3 (COUNTRIES,CURRENCIES,CAPITALS)',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,220)
                        pen.write('* MOVIES',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,180)
                        pen.write('* SPACE',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,140)
                        pen.write('* SPORTS',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,100)
                        pen.write('* INDIA',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-650,40)
                        pen.write('FUNCTIONING OF QUIZ:',font=('Times',25,'bold'),align='left')
                        pen.goto(-650,20)
                        pen.write('------------------------------------',font=('Times',25,'bold'),align='left')
                        pen.goto(-600,-20)
                        pen.write('LETS SEE HOW THE QUIZ WORKS:',font=('Lucida Handwriting',20,'bold'),align='left')
                        pen.goto(-550,-60)
                        pen.write('* BEFORE YOU START TO PLAY THE QUIZ,YOU WILL BE ASKED IF YOU ARE',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-100)
                        pen.write('  AN ADMIN OR A PLAYER OR A PLAYER ',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-140)
                        pen.write('* AFTER CHOOSING PLAYER OR ADMIN,YOU WILL ENTER THE PAGE WHERE YOU',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-180)
                        pen.write('  CAN LOGIN WITH AN EXISTING ACCOUNT OR CREATE A NEW ACCOUNT',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-220)
                        pen.write('* AFTER CHOOSING LOGIN ,YOU WILL LOGIN WITH YOUR USERNAME AND',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-260)
                        pen.write('  PASSWORD IN THE PROVIDED SPACE',font=('Lucida Handwriting',20,'normal'),align='left')
                        turtle.onscreenclick(next3,3)
                    def next1(x,y):
                        pen.clear()
                        pen.goto(-600,300)
                        pen.write('*  BOTH PLAYERS AND ADMINS CAN VIEW THE RANKING. RANKING DISPLAYS  ',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,260)
                        pen.write('   HIGHEST SCORE OF THE PLAYER AS WELL AS THE SCORE OF THE MOST RECENT ',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,220)
                        pen.write('   ATTEMPT FOR EACH CATEGORY ',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-650,160)
                        pen.write('CONCEPTS USED: ',font=('Times',25,'bold'),align='left')
                        pen.goto(-650,140)
                        pen.write('--------------------------',font=('Times',25,'bold'),align='left')
                        pen.goto(-600,100)
                        pen.write('* USER DEFINED FUNCTIONS',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,60)
                        pen.write('* LIBRARIES(TKINTER,TURTLE)',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,20)
                        pen.write('* MODULES(TIME,RANDOM)',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-20)
                        pen.write('* PACKAGES',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-60)
                        pen.write('* FILES(CSV, TEXT)',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-600,-100)
                        pen.write('* SQL CONNECTOR',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-650,-160)
                        pen.write('TYPES AND CATEGORIES USED IN QUIZ:',font=('Times',25,'bold'),align='left')
                        pen.goto(-650,-180)
                        pen.write('-----------------------------------------------------------',font=('Times',25,'bold'),align='left')
                        pen.goto(-600,-220)
                        pen.write('THERE WILL BE TWO TYPES OF QUESTIONS ASKED:',font=('Lucida Handwriting',20,'bold'),align='left')
                        pen.goto(-550,-260)
                        pen.write('* MCQ',font=('Lucida Handwriting',20,'normal'),align='left')
                        pen.goto(-550,-300)
                        pen.write('* TRUE/FALSE',font=('Lucida Handwriting',20,'normal'),align='left')
                        turtle.onscreenclick(next2,3)

                    pen.goto(-150,290)
                    pen.write('SYNOPSIS',font=('Times',40,'bold'),align='left')
                    pen.goto(-150,270)
                    pen.write('---------------',font=('Times',40,'bold'),align='left')
                    pen.goto(-650,220)
                    pen.write('ABOUT:',font=('Times',25,'bold'),align='left')
                    pen.goto(-650,200)
                    pen.write('-----------',font=('Times',25,'bold'),align='left')
                    pen.goto(-600,160)
                    pen.write('*  OUR PROJECT IS AN INTERESTING QUIZ GAME . OUR GAME HAS 2 DIFFERENT ',font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(-600,120)
                    pen.write('   TYPE OF QUESTIONS AND 5 DIFFERENT CATEGORIES IN EACH.THE PLAYER',font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(-600,80)
                    pen.write('   MUST LOGIN BEFORE PLAYING THE QUIZ SO THAT THEIR USERNAME AND',font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(-600,40)
                    pen.write('   PASSWORD WILL BE STORED AND CAN BE USED AGAIN LATER',font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(-600,-20)
                    pen.write("*  THE PLAYER CAN PLAY A CATEGORY ONLY ONCE.THEY CAN'T PLAY THE SAME ",font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(-600,-60)
                    pen.write('   CATEGORY ONCE AGAIN.',font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(-600,-120)
                    pen.write('*  ADMINS ONLY VIEW THE DETAILS OF THE PLAYERS WHO HAVE CREATED ',font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(-600,-160)
                    pen.write('   AN ACCOUNT. ADMINS CAN ALSO ADD OR DELETE QUESTIONS IF THEY WISH',font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(-600,-200)
                    pen.write("   BUT PLAYERS CAN'T.THESE QUESTIONS WILL BE STORED IN A CSV FILE.",font=('Lucida Handwriting',20,'normal'),align='left')
                    turtle.onscreenclick(next1,3)
                    #synopsis()
                if x==-120 and y==-35:
                    turtle.clearscreen()
                    rank()
                if x==-120 and y==-85:
                    turtle.clearscreen()
                    p.bgpic('exit.png')
                    #p.bgcolor('blue')
                    pen.color('purple')
                    pen.goto(-250,150)
                    pen.write('THANK YOU', font=('Lucida Handwriting',60,'normal'),align='left')
                    pen.goto(80,-20)
                    pen.pencolor('yellow')
                    pen.write('DONE BY:', font=('Lucida Handwriting',40,'normal'),align='left')
                    pen.goto(160,-100)
                    pen.write('ARUL PRAKASH.K', font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(160,-140)
                    pen.write('JEEVA SHRIRAM.G', font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(160,-180)
                    pen.write('SAKTHIVEL.B', font=('Lucida Handwriting',20,'normal'),align='left')
                    pen.goto(160,-220)
                    pen.write('THEJAS ADITHYAA.T', font=('Lucida Handwriting',20,'normal'),align='left')
                    def ne(x,y):
                        turtle.clearscreen()
                        turtle.bye()
                        running=False
                    turtle.onscreenclick(ne,3)
            def click1():
                click3(ar.xcor(),ar.ycor())



            def move():
                
                if ar.direction =='up':
                    time.sleep(0.1)
                    ar.sety(ar.ycor() +50)
                    ar.direction='stop'
                    
                elif ar.direction =='down':
                    time.sleep(0.1)
                    ar.sety(ar.ycor() -50)
                    ar.direction='stop'

            p.listen()
            p.onkeypress(click1,'x')
            p.onkeypress(go_up2,'w')
            p.onkeypress(go_down2,'s')

            while True:
                try:
                    p.update()
                    move()
                    
                except:
                    move()
                    break

    opt('yes')




def LOG():
    root = Tk()#className='LOGIN PAGE'
    root.minsize(1366,786)

    #C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "C:\\Users\\Welcome\\Desktop\\prj1\\op11.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    def connect(NAME,PASSWORD):
        conn=abc.connect(host='localhost',user='root',passwd='Admin@123456',database='project')
        query="select * from playersdetails"
        c=conn.cursor()
        c.execute(query)
        x=c.fetchall()
        #print(x,len(x))
        i=0
        while True:
            
            if str(x[i][-2])==str(NAME) and str(x[i][-1])==str(PASSWORD):
                messagebox.showinfo(title="quiz login",message="login successful")
                #print('success')
                root.destroy()
                try:
                    player(NAME)
                except:
                    turtle.clearscreen()
                    player(NAME)
                break
                '''
                try:
                    import choos
                except:
                    import choos
                    break
                '''
            elif i==len(x)-1:
                messagebox.showinfo(title="quiz login",message="enter correct username and password")
                break
            else:
                i+=1            
    def check():
        name=un.get()
        password=pw.get()
        data=connect(name,password)

    a=' '
    #   CREATING LOGIN PAGE
    #root =Tk()
    #root.configure(bg='blue')
    un=StringVar()
    pw=StringVar()
    #root.geometry("300x300") 
    root.title("LOGIN PAGE")
    t=Label(root,text='LOGIN FORM',font=('arial',14),bd=15,background="white")
    t.pack()
    #form=Frame(root)
    #form.pack(side=TOP,fill=X)
    nameL=Label(root,text="USERNAME",background="white",font=('arial',14),bd=10).place(x=40,y=100)
    passL=Label(root,text="PASSWORD",background="white",font=('arial',15),bd=10).place(x=40,y=140)
    '''
    nameL.grid(row=40)
    passL.grid(row=45)
    '''
    nameE=Entry(root,textvariable=un,background="white").place(x=180,y=115)
    passE=Entry(root,textvariable=pw,show="*",background="white").place(x=180,y=155)
    '''
    nameE.grid(row=40,column=30)
    passE.grid(row=45,column=30)
    '''
    login=Button(root,text="LOGIN",command=check,background="white").place(x=200,y=200)
    
    #login.pack()
    

    root.mainloop()
def go_up():
    if tr.ycor()<65:
        tr.direction ='up'
    else:
        tr.sety(15)

def go_down():
    if tr.ycor()>15:
        tr.direction ='down'
    else:
        tr.sety(65)

pen=turtle.Turtle()
p=turtle.Screen()
p.setup(width=1366,height=768)
pen.hideturtle()
p.bgpic('open.png')
#p.bgcolor('darkblue')
w='THE BRAINTEASING QUIZ'
pen.pencolor('orange')
pen.penup()
time.sleep(0.01)      
pen.goto(-400,280)
pen.write(w,font=('Lucida Handwriting',40,'bold'),align='left')
time.sleep(0.01)     
pen.goto(-100,50)
pen.write('ADMIN',font=('Lucida Handwriting',20,'normal'),align='left')
time.sleep(0.01)
pen.goto(-100,0)
pen.write('PLAYER',font=('Lucida Handwriting',20,'normal'),align='left')

tr= turtle.Turtle()
tr.speed(0)
tr.penup()
#tr.goto(-300.0,100.0)
tr.shape('arrow')
#tr.shapesize(1.8,2,0)
tr.color('Chartreuse')
tr.penup()

tr.goto(-120.0,65.0)
tr.direction='stop'
def click4(x,y):
    if x==-120 and y==65:
        #admin
        p.clearscreen()
        def go_up2():
            if ar.ycor()<65:
                ar.direction ='up'
            else:
                ar.sety(15)

        def go_down2():
            if ar.ycor()>15:
                ar.direction ='down'
            else:
                ar.sety(65)
        pen.hideturtle()
        p.bgpic('log.png')
        #p.bgcolor('MediumSlateBlue')
        w='ADMIN ACCOUNT'
        pen.pencolor('orange')
        pen.penup()
        time.sleep(0.01)      
        pen.goto(-200,280)
        pen.write(w,font=('Lucida Handwriting',40,'bold'),align='left')
        time.sleep(0.01)     
        pen.goto(-100,50)
        a='A) 10-10-2020'
        pen.write('LOGIN',font=('Lucida Handwriting',20,'normal'),align='left')
        time.sleep(0.01)
        pen.goto(-100,0)
        pen.write('CREATE ACCOUNT',font=('Lucida Handwriting',20,'normal'),align='left')

        ar= turtle.Turtle()
        ar.speed(0)
        ar.penup()
        ar.shape('arrow')
        ar.color('Chartreuse')
        ar.penup()

        ar.goto(-120.0,65.0)
        ar.direction='stop'
        def click3(x,y):
            if x==-120 and y==65:
                turtle.clearscreen()
                turtle.bye()
                running=False
                root=Tk()
                root.minsize(250,30)
                password=StringVar()
                def check():
                    c=password.get()
                    if c=='abc':
                        messagebox.showinfo(title="ADMIN PASSWORD",message="login successful")
                        root.destroy()
                        ADMINSPART()
                    else:
                        messagebox.showinfo(title="ADMIN PASSWORD",message="enter correct password")    
                a=Label(root,text="PASSWORD",fg="black").place(x=40,y=100)
                entry=Entry(root,width=15,textvariable=password,show="*").place(x=120,y=100)
                button=Button(root,text='ENTER',command=check).place(x=80,y=140)
                #LOGIN()
            elif x==-120 and y==15:
                turtle.clearscreen()
                turtle.bye()
                running=False
                root=Tk()
                root.minsize(250,30)
                password=StringVar()
                def check():
                    c=password.get()
                    if c=='abc':
                        messagebox.showinfo(title="ADMIN PASSWORD",message="SUCCESS")
                        root.destroy()
                        import adminacc
                    else:
                        messagebox.showinfo(title="ADMIN PASSWORD",message="enter correct password")    
                a=Label(root,text="PASSWORD",fg="black").place(x=40,y=100)
                entry=Entry(root,width=15,textvariable=password,show="*").place(x=120,y=100)
                button=Button(root,text='ENTER',command=check).place(x=80,y=140)
                
        def click1():
            click3(ar.xcor(),ar.ycor())

        def move():
            
            if ar.direction =='up':
                time.sleep(0.1)
                ar.sety(ar.ycor() +50)
                ar.direction='stop'
                
            elif ar.direction =='down':
                time.sleep(0.1)
                ar.sety(ar.ycor() -50)
                ar.direction='stop'

        p.listen()
        p.onkeypress(click1,'x')
        p.onkeypress(go_up2,'w')
        p.onkeypress(go_down2,'s')

        while True:
            try:
                p.update()
                move()
                
            except:
                move()
                break

    elif x==-120 and y==15:
        #player
        p.clearscreen()
        def go_up2():
            if ar.ycor()<65:
                ar.direction ='up'
            else:
                ar.sety(15)

        def go_down2():
            if ar.ycor()>15:
                ar.direction ='down'
            else:
                ar.sety(65)
        pen.hideturtle()
        p.bgpic('log.png')
        #p.bgcolor('MediumSlateBlue')
        w='PLAYERS ACCOUNT'
        pen.pencolor('orange')
        pen.penup()
        time.sleep(0.01)      
        pen.goto(-200,280)
        pen.write(w,font=('Lucida Handwriting',40,'bold'),align='left')
        time.sleep(0.01)     
        pen.goto(-100,50)
        pen.write('LOGIN',font=('Lucida Handwriting',20,'normal'),align='left')
        time.sleep(0.01)
        pen.goto(-100,0)
        pen.write('CREATE ACCOUNT',font=('Lucida Handwriting',20,'normal'),align='left')

        ar= turtle.Turtle()
        ar.speed(0)
        ar.penup()
        ar.shape('arrow')
        ar.color('Chartreuse')
        ar.penup()

        ar.goto(-120.0,65.0)
        ar.direction='stop'
        def click3(x,y):
            if x==-120 and y==65:
                turtle.clearscreen()
                turtle.bye()
                running=False
                LOG()
            elif x==-120 and y==15:
                turtle.clearscreen()
                turtle.bye()
                running=False
                import cracc

        def click1():
            click3(ar.xcor(),ar.ycor())

        def move():
            
            if ar.direction =='up':
                time.sleep(0.1)
                ar.sety(ar.ycor() +50)
                ar.direction='stop'
                
            elif ar.direction =='down':
                time.sleep(0.1)
                ar.sety(ar.ycor() -50)
                ar.direction='stop'

        p.listen()
        p.onkeypress(click1,'x')
        p.onkeypress(go_up2,'w')
        p.onkeypress(go_down2,'s')

        while True:
            try:
                p.update()
                move()
                
            except:
                move()
                break

def click2():
    click4(tr.xcor(),tr.ycor())

def move():
    
    if tr.direction =='up':
        time.sleep(0.1)
        tr.sety(tr.ycor() +50)
        tr.direction='stop'
        
    elif tr.direction =='down':
        time.sleep(0.1)
        tr.sety(tr.ycor() -50)
        tr.direction='stop'

p.listen()

p.onkeypress(go_up,'w')
p.onkeypress(go_down,'s')
p.onkeypress(click2,'x')

while True:
    try:
        p.update()
        move()
        
    except:
        move()
        break

