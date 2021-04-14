import tkinter as tk
from tkinter import *
import random
import math
import sqlite3
import PIL




from tkinter import Button
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import OptionMenu
from tkinter import messagebox as msg
from tkinter import Radiobutton
from tkinter import Text
from tkinter import Canvas
from tkinter import Image
from tkinter import Listbox
from tkinter import Spinbox

global button

# pillow library for image

from PIL import Image, ImageFilter, ImageTk  

#global variables
win = None
frame = None
disabled = True



#########################################################################################################
####################################### HOME WINDOW GUI  ################################################
#########################################################################################################

#main function
def main():

    #set as global variables 
    global win
    global frame

    #cretae window
    win = tk.Tk()
    win.geometry("900x570")
    win.title("Combustion of Hydrocarbon")
    win.configure(background='lawn green')
    #create main menu
    createMainMenuGUI()
    #show window to user
    win.mainloop()

#create main menu function
    
def createMainMenuGUI():

    #set as global variables 
    global win
    global frame

    #if frame currently being shown in win- destroy it. clears window
    if(frame != None):
        frame.destroy()

    #create new frame object
    frame = Frame(win)
    frame.configure(background='lawn green')

    lab1 = Label(frame, text = "Combustion of Hydrocarbon", fg="black", bg="lawn green", font=("Comic Sans MS", 20))
    lab1.grid(padx=5, column = 2,)
    
    #create button 
    btnStart = Button(frame,text="Start",command=createSelectGUI , height = 5, width = 30,fg="black", bg="lime green", font=("Comic Sans MS", 10))
    btnStart.grid(column = 3,padx=3, pady = 5)

    btnUpdate = Button(frame,text="Update", command=loginGUI, height = 5, width = 30, fg="black", bg="lime green", font=("Comic Sans MS", 10))
    btnUpdate.grid(column = 3, pady = 5)
    
    btnInstruction = Button(frame, text="?", command=instructionGUI, height = 2, width = 10,fg="black", bg="lime green", font=("Comic Sans MS", 10))
    btnInstruction.grid(column=5, pady = 20)
    
    frame.grid()


#########################################################################################################
########################################### INSTRUCTION  ################################################
#########################################################################################################

def instructionGUI():

    try:
        #open textfile and read 
        with open("Instruction.txt") as fp: 
            message = fp.read()
    except IOError:
        #print message in messagebox
        message = 'No instructions available'
    msg.showinfo("Instructions", message)


#########################################################################################################
################################### LOGIN TO UPDATE GUI  ################################################
#########################################################################################################

def login(comment, username, password): 

    #open csv file in read mode to compare the username and passwords 
    loginFile = open("User.csv", "r")   
 
    #flag variable to store authentication
    authenticated = False   

   # go through every line and compare the correct details to the ones given
    for line in loginFile:
        loginRecord = line.split(",")

        if loginRecord[0].strip() == username and loginRecord[1].strip() == password:   #.strip() removes all white space
            authenticated = True
            comment.config(text="Successful login")
            frame.destroy()
            updateGUI()
                
        if authenticated == False:
            # have a label with comments whether they are successfully logged on or not to inform user 
            comment.config(text="unsucessful login")
            comment.config(text="Please try again")
        
def loginGUI():
    global win
    global frame


    if(frame != None):
        frame.destroy()

    #create new frame 
    frame = Frame(win, background='lawn green')
    lb1 = Label(frame, text="Teacher Login", fg="black", bg="lawn green", font=("Comic Sans MS", 20))
    lb1.pack(pady = 15)
    lb2 = Label(frame,text="Enter your username")
    lb2.configure(background='lime green')
    lb2.pack()

    TextEntry=Entry(frame,bd=5)
    TextEntry.pack()

    lbl3= Label(frame,text="Enter your password")
    lbl3.configure(background='lime green')
    lbl3.pack()

    TextEntry2=Entry(frame,bd=5)
    TextEntry2.pack()

    comment=Label(frame,text="")

    comment.configure(background='lime green')
    comment.pack(pady=10)

    # get given username and password and compare
    btnSubmit=Button(frame,text="Submit",height = 2, width = 8,  fg="black", bg="lime green", font=("Comic Sans MS", 10),command=lambda: login(comment, TextEntry.get(), TextEntry2.get()))
    btnSubmit.pack(pady=10)

    btnHome = Button(frame, text = "Home",command = createMainMenuGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnHome.pack(pady=10)
    
    frame.pack()

#########################################################################################################
############################################ UPDATE GUI  ################################################
#########################################################################################################


def updateGUI():
    
    global win
    global frame

    if(frame != None):
        frame.destroy()

    #create new frame 
    frame = Frame(win, background='lawn green')

    lab1 = Label(frame, text = "Update Hydrocarbon", fg="black", bg="lawn green", font=("Comic Sans MS", 20))
    lab1.pack()

    btnAdd = Button(frame, text = "Add hydrocarbon", height = 5, width = 50, command = addGUI, fg="black", bg="lime green", font=("Comic Sans MS", 10))
    btnAdd.pack(pady = 30)
 
    btnRemove = Button(frame, text = "Remove hydrocarbon", height = 5, width = 50, command = removeGUI, fg="black", bg="lime green", font=("Comic Sans MS", 10))
    btnRemove.pack(pady = 30)

    btnHome = Button(frame, text = "Home",command = createMainMenuGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnHome.pack()

    frame.pack()


#########################################################################################################
##################################### ADD NEW HYDROCARBON GUI  ##########################################
#########################################################################################################

def addGUI():

    global win
    global frame

    global newHydrocarbon
    global SpinCarbon
    global CO2
  
    newHydrocarbon= tk.StringVar()
    CO2=tk.IntVar()


    if(frame != None):
        frame.destroy()

    #create new frame 
    frame = Frame(win, background='lawn green')

    SpinCarbon=tk.StringVar()

    titleLbl = Label(frame, text="Add Hydrocarbon", fg="black", bg="lawn green", font=("Comic Sans MS", 20))
    titleLbl.pack()
    
    lb2 = Label(frame,text="name of hydrocarbon", fg="black", font=("Comic Sans MS", 10))
    lb2.configure(background='lime green')
    lb2.pack()

    newHydrocarbon=Entry(frame,bd=5)    
    newHydrocarbon.pack()
    #TextName.bind("<FocusOut>", lambda evt: strValidate(evt, TextName.get()))
    

    lb3 = Label(frame,text="number of carbon atoms", fg="black", font=("Comic Sans MS", 10))
    lb3.configure(background='lime green')
    lb3.pack()

    carbonNumber=Spinbox(frame, from_= 0, to = 50, textvariable=SpinCarbon)
    carbonNumber.pack()
    
    lb4 = Label(frame,text="Standard enthalpy change of formation of new hydrocarbon ", fg="black", font=("Comic Sans MS", 10))
    lb4.configure(background='lime green')
    lb4.pack()
    
    CO2=Entry(frame,bd=5)
    CO2.pack()
    CO2.bind("<FocusOut>", lambda evt: numValidate(evt, CO2.get()))

    global textbox
    textbox = Text(frame, width=100, height=10)
    textbox.pack()

    global button
    button=Button(frame,text="Submit",command=add, height = 2, width = 8,  fg="black", bg="lime green", font=("Comic Sans MS", 10))
    button.config(state='disabled')
    button.pack()
    

    btnHome = Button(frame, text = "Home",command = createMainMenuGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnHome.pack()

    frame.pack()

def numValidate(event, text):

    global button
    
    try:
        # VALIDATION - see if the value is an float
        float(text)
        button.config(state='active')
    except ValueError:
        # if it is not an integer then output messagebox until correct input is given 
        msg.showerror("Error", "The standard enthalpy change of hydrocarbon should be integer")
        button.config(state='disabled')
        #disable submit button
def add():

    global newHydrocarbon
    global SpinCarbon
    global CO2
    print(SpinCarbon.get())

    #n = Number of carbon from a spinbox
    n=float(SpinCarbon.get())

    #m = Number of hydrogen
    m=2*n+2

    Hydrocarbons= newHydrocarbon.get()


    duplicate = False


    #validate name is unique
   
    conn=sqlite3.connect("Theoretical_Method.db")
    cursor = conn.cursor()


    #get list of tuples containing all player names
    sql = "SELECT Hydrocarbon from Theoretical"
    cursor.execute(sql)
    playernames = cursor.fetchall()
    numplayers = len(playernames)

    sql2 = "SELECT number_Carbon from Theoretical"
    cursor.execute(sql2)
    numberCarbon = cursor.fetchall()
    numCarbons = len(numberCarbon)

    #change entered name to uppercase so cases match when comparing to names in database
    #Hydrocarbons = Hydrocarbons.upper()

    #go through every name to see if the new name is a duplicate
    for i in range(0,numplayers) and range(0,numCarbons):
        if Hydrocarbons == playernames[i][0]:
            duplicate = True
            msg.showinfo("Error", "Hydrocarbon already exits")
        elif n == numberCarbon[i][0]:
            duplicate = True
            msg.showinfo("Error", "Number already exits")   
    
    if not duplicate:                            # and float(CO2)
        DeltaH_CH4=CO2.get()
        DeltaH_CO2=n * -393.7
        Delta_H2O=(n+1)* -285.5
        Delta_O2=0
        Reactant="C" + str(n) + "H" + str(m) + "[g] + " + str(n+m/4) + "O2 [g]"
        Product=str(n) + "CO2[g] + " + str(m/2) + "H2O[I]"
        Intermediate=str(n) + "C[s] + " +  str(n+1) + "H2 [g]"
        Molar_mass=n*12.0107+m*1.00794
    
        cursor.execute("INSERT INTO Theoretical (Hydrocarbon, DeltaH_CH4, DeltaH_CO2, DeltaH_H2O, Delta_O2, Reactant, Product, Intermediate, Molar_mass, number_Carbon) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
        (Hydrocarbons, DeltaH_CH4, DeltaH_CO2, Delta_H2O, Delta_O2, Reactant, Product, Intermediate, Molar_mass, n))
    
        conn.commit()

        textbox.insert(tk.END,"\nstandard enthalpies of formation of hydrocarbon of " )
        textbox.insert(tk.END, Hydrocarbons )
        textbox.insert(tk.END,": ")
        textbox.insert(tk.END, DeltaH_CH4)
        textbox.insert(tk.END, " kJ mol-1")
        textbox.insert(tk.END,"\nstandard enthalpies of formation of carbon dioxide: ")
        textbox.insert(tk.END, DeltaH_CO2)
        textbox.insert(tk.END, " kJ mol-1")
        textbox.insert(tk.END,"\nstandard enthalpies of formation of water: ")
        textbox.insert(tk.END, Delta_H2O)
        textbox.insert(tk.END, " kJ mol-1")
        textbox.insert(tk.END, "\nmolar mass of hydrocarbon: ")
        textbox.insert(tk.END, Molar_mass)
        textbox.insert(tk.END, "\nformula of reactant: ")
        textbox.insert(tk.END, Reactant)
        textbox.insert(tk.END, "\nformula of product: ")
        textbox.insert(tk.END, Product)
        textbox.insert(tk.END, "\nformula of intermediate: ")
        textbox.insert(tk.END, Intermediate) 
        textbox.configure(state="disabled")



def removeGUI():
     
    global win
    global frame
    if(frame != None):
        frame.destroy()

    frame = Frame(win,background='lawn green')

    lab1 = Label(frame, text="Delete hydrocarbon", fg="black", bg="lawn green", font=("Comic Sans MS", 20))
    lab1.pack(pady = 10)

    # create a listbox
    lists = Listbox(frame, width=20, height=18, selectmode = tk.SINGLE)
    lists.pack()

    #on buttonclick moves to remove function 
    deleteBtn = Button(frame, text="Delete",height = 2, width = 8,  fg="black", bg="lime green", font=("Comic Sans MS", 10), command = lambda: remove(lists.get(tk.ACTIVE)))
    deleteBtn.pack()

    btnHome = Button(frame, text = "Home", command = createMainMenuGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnHome.pack()
    
    frame.pack()

    # connect to batabase    
    conn = sqlite3.connect('Theoretical_Method.db')
    c = conn.cursor()
 
    # go through every single hydrocarbon name column and compare to the chosen one 
    query = c.execute('SELECT Hydrocarbon FROM Theoretical').fetchall()
    for i in query:
        lists.insert(tk.END,i)


def remove(carbonSelection):
    #connect to the database
    conn = sqlite3.connect('Theoretical_Method.db')
    c = conn.cursor()

    # delete the chosen carbon (carbonSelection)
    delete= c.execute("DELETE FROM Theoretical WHERE Hydrocarbon =?", (carbonSelection))
    print(carbonSelection)
    conn.commit()



#########################################################################################################
################################# SELECT HYDROCARBON FROM DATABASE  #####################################
#########################################################################################################

def createSelectGUI():
   

    global win
    global frame
    global scrollbar

    if(frame != None):
        frame.destroy()

    frame = Frame(win,background='lawn green')

    lab1 = Label(frame, text="Combustion of hydrocarbon", fg="black", bg="lawn green", font=("Comic Sans MS", 20))
    lab1.pack(pady = 10)

######################################################
    
####    scrollbar = Scrollbar(win)
####    scrollbar.pack(side=RIGHT, fill=Y)
##    
##    # listbox with all the hydrocarbon from the database
##    #lists = Listbox(frame, width=20, height=18, selectmode = tk.SINGLE, bd=0, yscrollcommand=scrollbar.set)
##    #lists.pack()
##
    lists = Listbox(frame, width=20, height=18, selectmode = tk.SINGLE) #bd=0)# , yscrollcommand=scrollbar.set)
    lists.pack()
## 
##    scrollbar = Scrollbar(lists, orient="vertical")
##    scrollbar.pack(side=RIGHT, fill=Y)
##    scrollbar.config(command=lists.yview)
##    
##    lists.config(yscrollcommand=scrollbar.set)
#########################################
    #selectbutton
    selectBtn = Button(frame, text="Select",height = 2, width = 8, fg="black", bg="lime green", font=("Comic Sans MS", 10), command = lambda: createSelectMethodGUI(lists.get(tk.ACTIVE)))
    selectBtn.pack()

    btnHome = Button(frame, text = "Home", command = createMainMenuGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnHome.pack(pady=3)
    
    frame.pack()

    # connect to the database 
    conn = sqlite3.connect('Theoretical_Method.db')
    c = conn.cursor()

    # go through the database and print all the hydrocarbon names
    # get the selected hydrocabon and store as carbonSelection
    query = c.execute('SELECT Hydrocarbon FROM Theoretical').fetchall()
    for i in query:
        lists.insert(tk.END,i)

#########################################################################################################
############################ SELECT PRACTICAL OR THEORETCIAL METHOD #####################################
#########################################################################################################
    

def practicalValidate(event, text):

    try:
        # VALIDATION - see if the value is an integer
        float(text) 
    except ValueError:
        # if it is not an integer then output messagebox until correct input is given 
        msg.showerror("Error", "The number should be integer") 



def createSelectMethodGUI(carbonSelection): # pass a parameter 
     
    global win
    global frame
    global disabled

    disabled = False

    if(frame != None):
        frame.destroy()

    #create new frame 
    frame = Frame(win, background='lawn green')
    
    btnTheoretical = Button(frame, text = "Theoretical \n method", height = 5, width = 50, command = lambda: createTheoreticalGUI(carbonSelection), fg="black", bg="lime green", font=("Comic Sans MS", 10))
    btnTheoretical.pack(pady = 30) 
 
    btnPractical = Button(frame, text = "Practical \n method", height = 5, width = 50, command = lambda: createPracticalGUI(carbonSelection), fg="black", bg="lime green", font=("Comic Sans MS", 10))
    btnPractical.pack(pady = 30) 

    btnHome = Button(frame, text = "Home",command = createMainMenuGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnHome.pack()

    frame.pack()


#########################################################################################################
########################################  PRACTICAL METHOD GUI ##########################################
#########################################################################################################
    

def createPracticalGUI(carbonSelection):

    global win
    global frame
    global var2
    global var3
    global var4
    global var5
    global var
    global dh
    global radiovar
    global radiovar2
    global radiovar3

    if(frame != None):
        frame.destroy()
        
    # variables set for validation 
    var = tk.StringVar()
    var2 = tk.StringVar()
    var3 = tk.StringVar()
    var4 = tk.StringVar()
    var5 = tk.StringVar()
    radiovar = tk.IntVar()
    radiovar2 = tk.IntVar()
    radiovar3 = tk.IntVar()

    def calculation(carbonNames):

        global var
        global var2
        global var3
        global var4
        global var5
        global radiovar
        global radiovar2
        global radiovar3
        global textbox
        
        try:

            # assign varaible to every input for calculation in the end 
            massWater = float(var.get())
            temperatureBefore = float(var2.get())
            temperatureAfter = float(var3.get())
            massBefore = float(var4.get())
            massAfter = float(var5.get())

            # connect to the database 
            conn = sqlite3.connect('Theoretical_Method.db')
            c = conn.cursor()


            # molar mass
            molarMass= c.execute("SELECT Molar_mass FROM Theoretical WHERE Hydrocarbon = ?", carbonSelection).fetchone()[0]
            print(molarMass)

            # mass of water
            # have radiobuttons for the units
            # if kilogram given multiply by 1000 to get grams
            if radiovar.get() == 1:
                massWaterGram = massWater*1000
            else:
                massWaterGram = massWater

            textbox.insert(tk.END, "Molar Mass of Hydrocarbon: ")
            textbox.insert(tk.END, molarMass)
            textbox.insert(tk.END, "\nMass of water: ")
            textbox.insert(tk.END, massWaterGram)
            textbox.insert(tk.END, " grams")


        #temperature
            temperatureDifference=(temperatureAfter-temperatureBefore)
            
            textbox.insert(tk.END, "\nTemperature difference: " )
            textbox.insert(tk.END, temperatureDifference)
            textbox.insert(tk.END, "  Kelvin")


            #spirit burner
            # have radiobuttons for the units
            # if kilogram given multiply by 1000 to get grams
            if radiovar2.get() == 1:
                massBurnerBeforeGram=massBefore*1000
            else:
                massBurnerBeforeGram=massBefore

            if radiovar3.get() == 1:
                 massBurnerAfterGram=massAfter*1000
            else:
                massBurnerAfterGram=massAfter

            # difference in mass burner before and after
            # if the mass before is greater than the mass after: before - after
            # if the mass after is greater than the mass before: after - before
            
            if massBurnerBeforeGram > massBurnerAfterGram:
                massDifference=(massBurnerBeforeGram-massBurnerAfterGram)
            else:
                
                massDifference=(massBurnerAfterGram-massBurnerBeforeGram)
                
            textbox.insert(tk.END, "\nDifference in mass of spirit burner: ")
            textbox.insert(tk.END, massDifference)
            textbox.insert(tk.END, " grams")
                
        
            #Calculating Mole
            # use the molar mass from the database and the difference in mass calculated above find the mole
            moles=(massDifference/molarMass)
            textbox.insert(tk.END, "\nMoles (difference in mass of spirit burner/molar mass): ")
            textbox.insert(tk.END, moles)
            textbox.insert(tk.END, " moles")

            # calculate enery transferred using Q = mcDeltaT
            energyTransferredQ =((massWaterGram*4.184*temperatureDifference)/1000.0)
            textbox.insert(tk.END, "\nEnergy transferred: ")
            textbox.insert(tk.END, energyTransferredQ)
            textbox.insert(tk.END, "kJ")
        
            enthalpyChange=energyTransferredQ/moles
            textbox.insert(tk.END, "\nEnthalpy change of combustion: ")
            textbox.insert(tk.END, enthalpyChange )
            textbox.insert(tk.END, "kJ/mol")

            with open("Answer.txt", "w") as answer:
                answer.write(str(enthalpyChange))
            

            # find out if exothermic or endothermic reaction 
            if enthalpyChange > 0:
                textbox.insert(tk.END, "\n\nThis reaction is Endothermic")
                textbox.configure(state="disabled")
            else :
                textbox.insert(tk.END, "\n\nThis reaction is Exothermic")
                textbox.configure(state="disabled")
            
        except ValueError:
            pass
    
    #create new frame 
    frame = Frame(win, bg="lawn green")

    titleLbl = Label(frame, text="Practical method", fg="black", bg="lawn green", font=("Comic Sans MS", 20))
    titleLbl.pack()
    
    lbl = Label(frame,text="Enter mass of water",fg="black", font=("Comic Sans MS", 10))
    lbl.configure(background='lime green')
    lbl.pack()
    
    TextEntry=Entry(frame,bd=5, textvariable=var)
    TextEntry.pack()
    TextEntry.bind("<FocusOut>", lambda evt: practicalValidate(evt, TextEntry.get())) # when return key (enter key) is pressed the value will be checked 

    # VALIDATION - make sure the units are correct     
    rb = Radiobutton(frame, text="kilograms", fg="black", bg="lime green", font=("Comic Sans MS", 10), variable = radiovar, value=1)
    rb.place(x=600, y = 55)

    rb1 = Radiobutton(frame, text="grams",fg="black", bg="lime green", font=("Comic Sans MS", 10),  variable = radiovar, value=2)
    rb1.place(x=700, y=55)
    

    lb2 = Label(frame,text="Temperature of water before", fg="black", font=("Comic Sans MS", 10))
    lb2.configure(background='lime green')
    lb2.pack()

    TextEntry2=Entry(frame,bd=5, textvariable=var2)    
    TextEntry2.pack()
    TextEntry2.bind("<FocusOut>", lambda evt: practicalValidate(evt, TextEntry2.get()))                

    lb3 = Label(frame,text="Temperature of water after", fg="black", font=("Comic Sans MS", 10))
    lb3.configure(background='lime green')
    lb3.pack()

    TextEntry3=Entry(frame,bd=5, textvariable=var3)
    TextEntry3.pack()
    TextEntry3.bind("<FocusOut>", lambda evt: practicalValidate(evt, TextEntry3.get()))
        
    lb4 = Label(frame,text="Mass of spirit burner before", fg="black", font=("Comic Sans MS", 10))
    lb4.configure(background='lime green')
    lb4.pack()
    
    TextEntry4=Entry(frame,bd=5, textvariable=var4)
    TextEntry4.pack()
    TextEntry4.bind("<FocusOut>", lambda evt: practicalValidate(evt, TextEntry4.get()))

    radiovar2 = tk.IntVar()
    rb3 = Radiobutton(frame, text="kilograms", fg="black", bg="lime green", font=("Comic Sans MS", 10), variable = radiovar2, value=1)
    rb3.place(x=600, y = 210)

    rb4 = Radiobutton(frame, text="grams",fg="black", bg="lime green", font=("Comic Sans MS", 10),  variable = radiovar2, value=2)
    rb4.place(x=700, y=210)

    lb5 = Label(frame,text="Mass of spirit burner after", fg="black", font=("Comic Sans MS", 10))
    lb5.configure(background='lime green')
    lb5.pack()

    radiovar3 = tk. IntVar()
    rb3 = Radiobutton(frame, text="kilograms", fg="black", bg="lime green", font=("Comic Sans MS", 10), variable = radiovar3, value=1)
    rb3.place(x=600, y = 250)

    rb4 = Radiobutton(frame, text="grams",fg="black", bg="lime green", font=("Comic Sans MS", 10),  variable = radiovar3, value=2)
    rb4.place(x=700, y=250)

    TextEntry5=Entry(frame,bd=5, textvariable=var5)
    TextEntry5.pack()
    TextEntry5.bind("<FocusOut>", lambda evt: practicalValidate(evt, TextEntry5.get()))
    global textbox
    textbox = Text(frame, width=100, height=10)
    textbox.pack()

    button=Button(frame,text="Submit",command=lambda:calculation(carbonSelection), height = 2, width = 8,state='disabled',  fg="black", bg="lime green", font=("Comic Sans MS", 10))
    button.pack()

    button2=Button(frame,text="Canvas",command=canvas, height = 2, width = 8,state='disabled',  fg="black", bg="lime green", font=("Comic Sans MS", 10))
    button2.pack()

    btnHome = Button(frame, text = "Home",command = createMainMenuGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnHome.pack(padx=10 ,pady=0,side=RIGHT)
    
    var.trace("w",lambda *args: submitButton(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button))
    var2.trace("w",lambda *args: submitButton(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button))
    var3.trace("w",lambda *args: submitButton(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button))
    var4.trace("w",lambda *args: submitButton(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button))
    var5.trace("w",lambda *args: submitButton(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button))
    radiovar.trace("w",lambda *args: submitButton(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button))
    radiovar2.trace("w",lambda *args: submitButton(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button))
    radiovar3.trace("w",lambda *args: submitButton(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button))

    var.trace("w",lambda *args: submitButton1(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button, button2))
    var2.trace("w",lambda *args: submitButton1(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button, button2))
    var3.trace("w",lambda *args: submitButton1(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button, button2))
    var4.trace("w",lambda *args: submitButton1(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button, button2))
    var5.trace("w",lambda *args: submitButton1(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button, button2))
    radiovar.trace("w",lambda *args: submitButton1(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button, button2))
    radiovar2.trace("w",lambda *args: submitButton1(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button, button2))
    radiovar3.trace("w",lambda *args: submitButton1(var.get(), var2.get(), var3.get(), var4.get(), var5.get(), radiovar.get(), radiovar2.get(), radiovar3.get(), button, button2))

         
    frame.pack()

def submitButton(a, b, c, d, e, f, g, h, button):

    # disable submit button until all the entry boxes are filled correctly with the correct data types 
    if a and b and c and d and e and f and g and h :

        button.config(state='normal')
    else:

        button.config(state='disabled')

def submitButton1(a, b, c, d, e, f, g, h, button, button2):

    if a and b and c and d and e and f and g and h and button :

        button2.config(state='normal')
    else:

        button2.config(state='disabled')



#########################################################################################################
######################################  THEORETICAL METHOD GUI ##########################################
#########################################################################################################            
    

def createTheoreticalGUI(carbonSelection):

    global win
    global frame
    global disabled

    disabled = False

    if(frame != None):
        frame.destroy()

    
    frame = Frame(win, background='lawn green')

    # connect to database 
    conn = sqlite3.connect('Theoretical_Method.db')
    c = conn.cursor()

    # select rows from database and assign variable names to them to use during calculations 
    reactant= c.execute("SELECT Reactant FROM Theoretical WHERE Hydrocarbon = ?", carbonSelection).fetchone()[0]
    print(reactant)

    product= c.execute("SELECT Product FROM Theoretical WHERE Hydrocarbon = ?", carbonSelection).fetchone()[0]
    print(product)

    intermediate = c.execute("SELECT Intermediate FROM Theoretical WHERE Hydrocarbon = ?", carbonSelection).fetchone()[0]
    print(intermediate)

    enthalpyHydrocarbon = c.execute("SELECT DeltaH_CH4 FROM Theoretical WHERE Hydrocarbon = ?", carbonSelection).fetchone()[0]
    print(enthalpyHydrocarbon)

    enthalpyCarbondioxide = c.execute("SELECT DeltaH_CO2 FROM Theoretical WHERE Hydrocarbon = ?", carbonSelection).fetchone()[0]
    print(enthalpyCarbondioxide)

    enthalpyWater = c.execute("SELECT DeltaH_H2O FROM Theoretical WHERE Hydrocarbon = ?", carbonSelection).fetchone()[0]
    print(enthalpyWater)

        
    label1 = Label(frame, text="Hess' cycle", fg="black", bg="lawn green", font=("Comic Sans MS", 20))
    #label1.place(x=100, y=0)
    label1.pack(pady=10)
    #label1.grid(row = 0, column = 2)
    
    lb3 = Label(frame,text="Reactant", fg="black", font=("Comic Sans MS", 10))
    lb3.configure(background='lime green')
    lb3.pack(pady=5)

    text2 = Text(frame, width=30, height = 1, bg= "lime green")
    #text2.place(x=520, y=100)
    #text2.pack(padx=5, pady=20, side = tk.LEFT)
    #text2.grid(row=3, column = 6)
    text2.pack(pady=10)
    
    text2.delete(0.0, tk.END)
    text2.insert(tk.END, reactant)
    text2.configure(state="disabled")

    lb4 = Label(frame,text="Intermediate", fg="black", font=("Comic Sans MS", 10))
    lb4.configure(background='lime green')
    lb4.pack(pady=5)

    text3 = Text(frame, width=30, height = 1, bg= "lime green")
    #text3.place(x=370, y=250)
    text3.pack(pady=10)
    
    text3.delete(0.0, tk.END)
    text3.insert(tk.END, intermediate)
    text3.configure(state="disabled")

    lb2 = Label(frame,text="Product", fg="black", font=("Comic Sans MS", 10))
    lb2.configure(background='lime green')
    lb2.pack(pady=5)

    
    text1 = Text(frame, width=30, height = 1, bg= "lime green")
    #text1.place(x=200, y=100)
    #text1.pack(padx=100, pady=0, side = tk.LEFT)
    #text1.grid(row = 3, column = 3)
    text1.pack(pady=10)
    
    text1.delete(0.0, tk.END)
    text1.insert(tk.END, product)
    text1.configure(state="disabled")

    global textbox
    textbox = Text(frame, width=400, height=10)
    
    
    textbox.pack()
    enthalpyChange = float(enthalpyWater) + float(enthalpyCarbondioxide) - float(enthalpyHydrocarbon)
    print(enthalpyChange)

    with open("Answer.txt", "w") as answer:
        answer.write(str(enthalpyChange))

    textbox.insert(tk.END, "standard enthalpy change of formation of water: ")
    textbox.insert(tk.END, enthalpyWater)
    textbox.insert(tk.END, " kJ mol-1")
    textbox.insert(tk.END,"\nstandard enthalpies of formation of carbon dioxide: ")
    textbox.insert(tk.END, enthalpyCarbondioxide)
    textbox.insert(tk.END, " kJ mol-1")
    textbox.insert(tk.END,"\nstandard enthalpies of formation of hydrocarbon of " )
    textbox.insert(tk.END, carbonSelection)
    textbox.insert(tk.END, " kJ mol-1")
    textbox.insert(tk.END,": ")
    textbox.insert(tk.END, enthalpyHydrocarbon)
    textbox.insert(tk.END, " kJ mol-1")
    textbox.insert(tk.END, "\nformula = ΔHcombustion = Hproduct – Hreactant")
    textbox.insert(tk.END, "\nstandard enthalpy change of combustion: ")
    textbox.insert(tk.END, enthalpyChange)
    textbox.insert(tk.END, " kJ mol-1")
    textbox.configure(state="disabled")



    btnCanvas = Button(frame, text="Canvas", command = canvas, height = 2, width = 8, fg="black", bg="lime green", font=("Comic Sans MS", 10))
    #btnDone.place(x=3, y= 200)
    btnCanvas.pack()

    btnHome = Button(frame, text = "Home",command = createMainMenuGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnHome.pack()

    frame.pack()

#########################################################################################################
###############################################  CANVAS GUI #############################################
#########################################################################################################

def answerGUI():

    try:
        #open textfile and read 
        with open("Answer.txt") as fp: 
            message = fp.read()
    except IOError:
        #print message in messagebox
        message = 'No instructions available'
    msg.showinfo("The Enthalpy change is ", message)    

  
def canvas():
    global win
    global frame

    global x
    global y
    global x_vel
    global y_vel
    global a
    global b
    global a_vel
    global b_vel
    global m
    global n
    global m_vel
    global n_vel
    global r
    global s
    global r_vel
    global s_vel

    def move():

        # get random move for the bubbles
        x_vel = random.randint(-5, 5)
        y_vel = -5
        a_vel = random.randint(-7, 4)
        b_vel = -7
        m_vel = random.randint(-6, 5)
        n_vel = -2
        r_vel = random.randint(-4, 4)
        s_vel = -5

        canvas1.move(circle, x_vel, y_vel)
        canvas1.move(circle2, a_vel, b_vel)
        canvas1.move(circle3, m_vel, n_vel)
        canvas1.move(circle4, r_vel, s_vel)
        
        
        coordinates = canvas1.coords(circle)

        x = coordinates[0]
        y = coordinates[1]
        a = coordinates[0]
        b = coordinates[1]
        m = coordinates[0]
        n = coordinates[1]
        r = coordinates[0]
        s = coordinates[1]
        
        # if outside screen move to start position

        if y < -height:
            x = start_x
            y = start_y
            canvas1.coords(circle, x, y, x+width, y+height)

        #window.after(33, move)

        if b < -height:
            a = start_a
            b = start_b
            canvas1.coords(circle2, a, b, a+width2, b+height2)
        
        if s < -height:
            r = start_r
            s = start_s
            canvas1.coords(circle4, r, s, r+width4, s+height4)

        if n < -height:
            m = start_m
            n = start_n
            canvas1.coords(circle3, m, n, m+width3, n+height3)

        frame.after(30, move)

    # make bubbles start at different positions 
    start_x = 170
    start_y = 140

    start_a = 230
    start_b = 140

    start_m = 290
    start_n = 140

    start_r = 300
    start_s = 140

    x = start_x
    y = start_y
    a = start_a
    b = start_b
    m = start_m
    n = start_n
    r = start_r
    s = start_s

    # create different sized bubbles 
    width  = 20
    height = 20

    width2 = 29
    height2 = 29

    width3  = 15
    height3 = 15

    width4 = 30
    height4 = 30

    x_vel = 5
    y_vel = 5

    a_vel = 5
    b_vel = 5

    m_vel = 5
    n_vel = 5

    r_vel = 5
    s_vel = 5

    if(frame != None):
        frame.destroy()
 
    frame = Frame(win)

    #canvas
    canvas1 = tk.Canvas(frame, height=1000, width=1000)
    canvas1.grid(row=0, column=0, sticky='w')

    coord = [x, y, x+width, y+height]
    circle = canvas1.create_oval(coord, outline="light blue", fill="light blue")

    coord = [a, b, a+width2, b+height2]
    circle2 = canvas1.create_oval(coord, outline="cyan", fill="cyan")

    coord = [m, n, m+width3, n+height3]
    circle3 = canvas1.create_oval(coord, outline="DarkSlateGray1", fill="darkslategray1")

    coord = [r, s, r+width4, s+height4]
    circle4 = canvas1.create_oval(coord, outline="paleturquoise", fill="paleturquoise")

    coord = [x, y, x+160, y+10]
    rect2 = canvas1.create_rectangle(coord, outline="goldenrod", fill="goldenrod")

    coord = [150, 40, 170, 320]
    rect = canvas1.create_rectangle(coord, outline="Black", fill="Black")

    coord = [330, 40, 350, 310]
    rect1 = canvas1.create_rectangle(coord, outline="Black", fill="black")


    coord = [130, 310, 370, 320]
    rect2 = canvas1.create_rectangle(coord, outline="Blue", fill="Blue")

    coord = [230, 270, 270, 310]
    rect3 = canvas1.create_rectangle(coord, outline="purple", fill="purple")

    # reseize image using PILLOW library
    load = Image.open('flame1.png')
    load=load.resize((17, 27), Image.ANTIALIAS)  
    render = ImageTk.PhotoImage(load)

    # position image 
    img = Label(image=render)
    img.image= render
    img.place(x=240,y=240) 

    # reseize image 
    load1 = Image.open('termo.png')
    load1=load1.resize((17, 170), Image.ANTIALIAS)  
    render1 = ImageTk.PhotoImage(load1)

    # position image
    img1 = Label(image=render1)
    img1.image= render1
    img1.place(x=240,y=10)  

    btnHome = Button(frame, text = "Home",command = createMainMenuGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnHome.place(x= 320, y=330)
    btnAnswer = Button(frame, text = "ANSWER",command = answerGUI,  height = 2, width = 8, fg="black", bg="green4", font=("Comic Sans MS", 10))
    btnAnswer.place(x= 320, y=370)



    #top left x and y coordinates and bottom right x and y coordinates 
    coord = [200, 150, 210, 240] 
    rect4 = canvas1.create_rectangle(coord, outline="gray30", fill="gray30")

    coord = [210, 230, 300, 240]
    rect4 = canvas1.create_rectangle(coord, outline="gray30", fill="gray30")

    coord = [290, 150, 300, 240]
    rect4 = canvas1.create_rectangle(coord, outline="gray30", fill="gray30")

    coord = [240, 20, 260, 180]
    rect4 = canvas1.create_rectangle(coord, outline="Pink", fill="pink")

    move()

  
    

    frame.pack()
  
#call main
main()
