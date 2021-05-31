from tkinter import * 
from win32com.client import Dispatch # for speaking anything
import datetime
import random
import tkinter.messagebox as message
import os
import time
import smtplib


# homepage function
def homepage():
    global root_homepage
    root_homepage = Tk()
    root_homepage.geometry("520x400")
    root_homepage.title("Kavyansh - Hotel")
    root_homepage.config(bg="yellow")

    #Title Of The GUI
    Label(root_homepage, text="Welcome To Kavyansh-Hotel", font="algerian 20 bold", bg="light blue").grid(row=1, column=0)

    #Buttons
    checkin = Button(root_homepage, text="Check In", font="comicsansMS 20 bold", bg="red", command=checkinbutton)
    checkin.grid(row=2, column=0)

    checkout = Button(root_homepage, text="Check Out", font="comicsansMS 20 bold", bg="red", command=checkoutbutton)
    checkout.grid(row=3, column=0)

    guestlist = Button(root_homepage, text="Guest List", font="comicsansMS 20 bold", bg="red", command=GuestList)
    guestlist.grid(row=4, column=0)

    gueststatus = Button(root_homepage, text="Guest Status", font="comicsansMS 20 bold", bg="red", command=in_or_out)
    gueststatus.grid(row=5, column=0)

    exit = Button(root_homepage, text="Exit", font="comicsansMS 20 bold", bg="red", command=quit)
    exit.grid(row=6, column=0)

    Label(root_homepage, text="Hotel Management By\nKavyansh", font="comicsansMS 20 bold", bg="green").grid()
    root_homepage.mainloop()

# check in button (submit button in check in function)
def checkinbutton():
    root_homepage.destroy()
    checkIn()
 
# ok button (ok button in roomkey function)
def okbutton():
    root_list.destroy()
    homepage()


# full check in function
def checkIn():
    global root
    root = Tk()
    root.configure(bg="light blue")
    root.geometry("800x550")
    root.title("Travel Agency")

    var2 = StringVar()
    var2.set("Payment")

    #entries for our form
    Label(root, text="Check IN:- ", font="comicsansms 30 bold", bg="light green").grid(row=0, column=2)
    name = Label(root, text="Name", fg="red", font="classic 20 underline").grid(row=1, column=2)
    email = Label(root, text="Email", fg="red", font="classic 20 underline").grid(row=2, column=2)
    phone = Label(root, text="Phone Number", fg="red", font="classic 20 underline").grid(row=3, column=2)
    gender = Label(root, text="Gender", fg="red", font="classic 20 underline").grid(row=4, column=2)
    aadhar = Label(root, text="Aadhar Number", fg="red", font="classic 20 underline").grid(row=5, column=2)
    dayss = Label(root, text="Days", fg="red", font="classic 20 underline").grid(row=6, column=2)

    Thanks = Label(root, text="Thanks for visiting our Hotle", fg="light blue", bg="light blue", font="classic 17 bold").grid(row=7, column=2)

    #Payment Mode
    Label(root, text="Payment Mode:- ", font="normal 20", bg="black", fg="white").grid(row=8, column=2)

    payment = Radiobutton(root, text="Google Pay?", variable = var2, pady="5", font="normal 12", value="Google Pay")
    payment.grid(row=9, column=2)
    payment = Radiobutton(root, text="Credit Card?", variable = var2, pady="5", font="normal 12", value="Credit Card")
    payment.grid(row=10, column=2)
    payment = Radiobutton(root, text="Cash?", variable = var2, pady="5", font="normal 12", value="Cash")
    payment.grid(row=11, column=2)

    # Tkinter variable for storing entries
    global namevalue
    global gendervalue
    global daysvalue
    namevalue = StringVar()
    phonevalue = StringVar()
    gendervalue = IntVar()
    emailvalue = StringVar()
    aadharvalue = IntVar()
    daysvalue = IntVar()
    # paymentmodevalue = StringVar()
    global var
    var = StringVar()
    var.set("Room") 

    #Entries for our form
    nameentry = Entry(root, textvariable=namevalue, font="normal 20")
    phoneentry = Entry(root, textvariable=phonevalue, font="normal 20")
    genderentry = Entry(root, textvariable=gendervalue, font="normal 20")
    emailentry = Entry(root, textvariable=emailvalue, font="normal 20")
    aadharentry = Entry(root, textvariable=aadharvalue, font="normal 20")
    day = Entry(root, textvariable=daysvalue, font="normal 20")
    
    # paymentmodeentry = Entry(root, textvariable=paymentmodevalue, font="normal 20")

    # Packing the Entries
    nameentry.grid(row=1, column=3)
    phoneentry.grid(row=2, column=3)
    genderentry.grid(row=3, column=3)
    emailentry.grid(row=4, column=3)
    aadharentry.grid(row=5, column=3)
    day.grid(row=6, column=3)
    # paymentmodeentry.grid(row=5, column=3)

    #Checkbox & Packing it
    Label(root, text="Which Room:- ", font="normal 20", bg="black", fg="white").grid(row=8, column=3)
    room = Radiobutton(root, text="Delux Room?", variable = var, pady="5", font="normal 12", value="Delux Room")
    room.grid(row=9, column=3)
    room = Radiobutton(root, text="Super Delux Room?", variable = var, pady="5", font="normal 12", value="Super Delux Room")
    room.grid(row=10, column=3)
    room = Radiobutton(root, text="Normal Room?", variable = var, pady="5", font="normal 12", value="Normal Room")
    room.grid(row=11, column=3)

    
    
    
 # errorinput (shows error if any one of the entries is empty)
    def errorinput():
        
        
    
        if namevalue.get()=="" or phonevalue.get()=="" or gendervalue.get()=="" or emailvalue.get()=="" or aadharvalue.get()=="":
            message.showerror("Error", "Invalid Input!!\nPlease fill the missing\ninformation")
            root.destroy()
            checkIn()
                
        else:
            pass

    

 # getvals (saves the info in different files)
    def getvals():
        if namevalue.get()=="" or phonevalue.get()=="" or gendervalue.get()=="" or emailvalue.get()=="" or aadharvalue.get()=="":
            errorinput()

        else:
            def sendEmail(to, content):
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('kavimaheshwari609@gmail.com', 'Kavya@123')
                server.sendmail('kavimahehswari609@gmail.com', to, content)
                server.close()
    
            from datetime import date
            today = date.today()
            today_date = today.strftime("%B %d, %Y")
            print("Submitting Form Sir/Maam")  

            with open("Guest List.txt", "a") as f:
                f.write(f"Name - {namevalue.get()}\nGender - {emailvalue.get()}\nDate - {today_date}\n-----------------------------------------------------------------------------------------\n")

            print(f"{namevalue.get(),  phonevalue.get(), gendervalue.get()}",
                f"{emailvalue.get(), var2.get(), var.get(), today_date}")
            
            with open("Hotel Check In List.txt", "a") as f:
                f.write(f"\nName - {namevalue.get()}\nEmail - {phonevalue.get()}\nContact Number - {gendervalue.get()}\nGender - {emailvalue.get()}\nAadhar Number - {aadharvalue.get()}\nDays - {daysvalue.get()}\nPayment Mode - {var2.get()}\nRoom Type - {var.get()}\nDate - {today_date}\n")
        
        if var.get() == "Normal Room": 
            message.showinfo("Payment", f"You need to pay Rs.{daysvalue.get()*2000} for check In")

        elif var.get() == "Delux Room": 
            message.showinfo("Payment", f"You need to pay Rs.{daysvalue.get()*6000} for check In")

        elif var.get() == "Super Delux Room": 
            message.showinfo("Payment", f"You need to pay Rs.{daysvalue.get()*10000} for check In")

        try:
            global otp
            otp = random.randint(1000, 9999)
            content = f"You have checked In\nThankyou for booking our hotel\n{namevalue.get()}\nYour OTP is - {otp}"
            to = f"{phonevalue.get()}"
            sendEmail(to, content)

            def speak(str):
                speak = Dispatch(("SAPI.SpVoice"))
                speak.Speak(str)

            if __name__ == '__main__':
                speak(f"Email has been sent")
                print(f"Email has been sent")


        except Exception as error:
            print(error)

            def speak(str):
                speak = Dispatch(("SAPI.SpVoice"))
                speak.Speak(str)

            if __name__ == '__main__':
                speak("Sorry sir because of some problem, email has not send")
                print("Sorry sir because of some problem, email has not send")
    
        
        root.destroy()
        roomkey()
        

    #Button & packing it and assigning it a command
    Button(root, text="Submit", command=getvals, bg="red", fg="yellow", pady="5", font="normal 15").grid(row=12, column=3)
    Button(root, text="Quit", command=quitcheckin, bg="red", fg="yellow", pady="5", font="normal 15").grid(row=12, column=2, ipadx=13)

    
    root.mainloop()

    


# roomkey (it randomly generates no. and display it)

def roomkey():
    
    global root_list
    root_list = Tk()
    root_list.config(bg="pink")
    root_list.geometry("230x150")
    root_list.title("Room Key")

    global room_key
    room_key = random.randint(100, 1000)

    with open("Hotel Check In List.txt", "a") as f:
        f.write(f"Room Number - {room_key}\n-----------------------------------------")

    Label(root_list, text="Your room key is:- ", font="comicsans 20", bg="pink", fg="dark blue").grid(row=0, column=2)
    Label(root_list, text=room_key, font="comicsans 20", bg="pink", fg="dark blue").grid(row=1, column=2)
    
    Button(root_list, text="Ok", font="comicsans 20", bg="pink", fg="dark blue", command=okbutton).grid(row=3, column=2)
    def speak(str):
                speak = Dispatch(("SAPI.SpVoice"))
                speak.Speak(str)

    if __name__ == '__main__':
        speak("Hope you will enjoy")
        speak(f"Your roomkey is {room_key}")
    
    root_list.mainloop()


def in_or_out():
    root_inout = Tk()
    root_inout.geometry("400x200")
    root_inout.config(bg="light green")
    root_inout.title("Checked In or Checked Out")

    Label(root_inout, text="Room Number ", font="comicsans 20 bold", bg="pink", fg="dark blue").grid(row=2, column=0)
    Label(root_inout, text="Name", font="comicsans 20 bold", bg="pink", fg="dark blue").grid(row=1, column=0)

    global name_value
    global roomno_value
    name_value = StringVar()
    roomno_value = StringVar()

    name_entry = Entry(root_inout, textvariable=name_value, font="normal 20")
    room_entry = Entry(root_inout, textvariable=roomno_value, font="normal 20")

    name_entry.grid(row=1, column=2)
    room_entry.grid(row=2, column=2)

    Button(root_inout, text="Submit", font="comicsansMS", bg="light green", command=check_in_out).grid(row=3, column=2)
   
    root_inout.mainloop()

def check_in_out():
    with open("Hotel Check Out List.txt", "r") as f:
        filecontent = f.read()
    if roomno_value.get() and name_value.get() in filecontent.lower():
        message.showinfo("", "This user is checked out")

   
    with open("Hotel Check In List.txt", "r") as f:
        filecontent = f.read()
    if roomno_value.get() and name_value.get() in filecontent.lower():
        message.showinfo("", "This user is currently checked in")
        
        

# exitwindow (checks in the check out window that the user is typing valid info)
def exitwindow():
    
    nowdate = datetime.date.today()
    time = datetime.datetime.now()
    currenttime = time.strftime("%H:%M:%S")


    with open("Hotel Check In List.txt", "r") as f:
        filecontent = f.read()
        
    if contactvalue.get() and name_outvalue.get() and aadharvalue2.get() and roomvalue.get() in filecontent.lower():
        message.showinfo("Thankyou", "You have successfully checked\nout. Thankyou for coming our\nHotel\nPlease come Again\nThankyou,\nKavyansh[Hotel Owner]")
        root_out.destroy()

        with open("Hotel Check Out List.txt", "a") as f:
            f.write(f"Name - {name_outvalue.get()}\nContact Number - {contactvalue.get()}\nAadhar number - {aadharvalue2.get()}\nDate - {nowdate}\nTime - {currenttime}\nRoom Number - {roomvalue.get()}\n--------------------------------------------------------------\n")
    
    else:

        message.showerror("Error", "You can't do check out because of invalid information")
        root_out.destroy()
        homepage()
           
    def feedbackus():
        global feed
        feed = Tk()
        feed.geometry("500x400")
        feed.title("Feedback")
        feed.config(bg="DeepSkyBlue2")

        Label(feed, text="Feedback", font="comicsansMS 30 bold").grid(row=1, column=3)

        global text
        text = StringVar()

        entry = Entry(feed, textvar=text, font="Arial 25 bold")
        entry.grid(row=2, column=3)

        submitfeedback = Button(feed, text="Submit", font="comicsansMS 25 bold", bg="SeaGreen1", command=thanks).grid(row=4, column=3)
        exitfeedback = Button(feed, text="Exit", font="comicsansMS 25 bold", bg="SeaGreen1", command=exitbutton).grid(row=5, column=3)
        
        feed.mainloop()
    def exitbutton():
        feed.destroy()
        homepage()

    def thanks():
        with open("Feedback.txt", "a") as f:
            f.write(f"Feedback - {text.get()}\n------------------------------------------\n")

        message.showinfo("Thank You", "Thanks For Your Feedback")
        feed.destroy()
        homepage()
    feedbackus()
    

#  
def checkoutbutton():
   
            
    root_homepage.destroy()
    global root_out
    root_out = Tk()
    root_out.geometry("550x300")
    root_out.title("Check Out")
    root_out.config(bg="yellow")

   
    Label(root_out, text="Check Out:-", bg="yellow", fg="red", font="algerian 20 bold").grid()
    name = Label(root_out, text="Name", fg="red", font="classic 20 underline").grid(row=1, column=0)
    name = Label(root_out, text="Phone Number", fg="red", font="classic 20 underline").grid(row=2, column=0)
    name = Label(root_out, text="Aadhar Number", fg="red", font="classic 20 underline").grid(row=3, column=0)
    name = Label(root_out, text="Room Number", fg="red", font="classic 20 underline").grid(row=4, column=0)


    # all entries
    global name_outvalue
    global contactvalue
    global aadharvalue2
    global roomvalue
    name_outvalue = StringVar()
    contactvalue = StringVar()
    aadharvalue2 = StringVar()
    roomvalue = StringVar()

    nameentry = Entry(root_out, textvariable=name_outvalue, font="normal 20")
    contactentry = Entry(root_out, textvariable=contactvalue, font="normal 20")
    aadharentry2 = Entry(root_out, textvariable=aadharvalue2, font="normal 20")
    roomentry = Entry(root_out, textvariable=roomvalue, font="normal 20")
    # packing the entries
    nameentry.grid(row=1, column=2)   
    contactentry.grid(row=2, column=2)
    aadharentry2.grid(row=3, column=2)
    roomentry.grid(row=4, column=2)

    
    # button
    Button(root_out, text="Check Out", bg="black", fg="white", pady="5", font="normal 15", command=exitwindow).grid(row=5, column=2)
    Button(root_out, text="Quit", bg="black", fg="white", pady="5", font="normal 15", command=quitcheckout).grid(row=6, column=2)
    
def quitcheckout():
    root_out.destroy()
    homepage()

# guestlist (displays the guest list to the user)
def GuestList():
        os.startfile('D:\\PycharmProjects\\Guest List.txt')


# quitcheckin (exits the checkin window if by mistakly opened)
def quitcheckin():
    root.destroy()
    homepage()

homepage()