import smtplib
from win32com.client import Dispatch
print("Welcome to Travel Agency of Kavyansh!!!")
name = str(input("What is your full name ?\n"))
print()

gmail = input("What is your Gmail ?\n")
print()

age = int(input(f"What is your age {name} ?\n"))
if age>=18:
    print("You are allowed")
elif age<18: 
    print("You are not allowed.")
    print("You are not 18+ (Adult)")
    exit()
elif age>100:
    exit()    
print()
contact = int(input("What is your emergency contact no.?\n"))
print()
place = str(input("Which place do you want to go ?\n1.Shimla\n2.Kerela\n3.Goa\n4.Manali\n"))
print()
budget = int(input("What is your budget ?\nper person\n1. 4000\n2. 7000\n3. 13000\n"))
print("About your destination-:\n\n")

if place=="1":
    print("Detail of Shimla-:\nShimla is home to a number of buildings that are styled in the Tudorbethanand neo-Gothic architectures dating from the colonial era, as well as multiple temples and churches.\nThe colonial architecture and churches, the temples, and the natural environment of the city attracts tourists.Attractions include the Viceregal Lodge, the Christ Church, the Jakhu Temple, the Mall Road,the Ridge and Annadale.\n")
elif place=="2":
     print("Detail of Kerela-:\nKerala, a state situated on the tropical Malabar Coast of southwestern India,\n is one of the most popular tourist destinations in the country.\n Named as one of the ten paradises of the world by National Geographic Traveler,\nKerala is famous especially for its ecotourism initiatives and beautiful backwaters.\n")
elif place=="3":
    print("Detail of Goa-:\nGoa is one of the most favorite destination among Indian tourists due to its pristine\n beaches. ... Every beach has its specialty, beauty, and serenity where tourists enjoy their\n best. Famous beaches in Goa: Baga, Candolim, Calangute, Morjim, Arambol, Anjuna, etc.\n")
elif place=="4":
    print("Detail of Manali-:\nManali is a resort and tourist town nestled in the mountains\n of the Indian state of Himachal Pradesh near the northern end of the Kullu Valley in the\n Beas River Valley.It is located in the Kullu district\n")
else:
    print("Invalid Input")

cab = str(input("Do you want to book a cab ? (y/n)\n"))
 
if cab=="y":
    members = int(input(f"How many members are there with you {name} ?\n"))
    if members<=5:
        if cab=="y":
            cars = str(input("Which car do you want ?\n1.Etios- Rs.3000\n2.Swift Desire- Rs.2200\n3.Indica Vista- Rs.1500\n"))
            print("Ok we have booked a cab for you.\n\n\n")
            print()

            if cars=="1":
                var1 = 3000
                print(f"Total price for transport is - {var1}\n" ) 
                print("Your total price for the tour is is - ", budget*members+var1)
                print("Your subtotal is:", budget*members+var1)
            elif cars=="2":
                var1 = 2200
                print(f"Total price for transport is - {var1}\n" ) 
                print("Your total price for the tour is is - ", budget*members+var1)
                print("Your subtotal is:", budget*members+var1)

            elif cars=="3":
                var1 = 1500
                print(f"Total price for transport is - {var1}\n" ) 
                print("Your total price for the tour is is - ", budget*members+var1)
                print("Your subtotal is:", budget*members+var1)
                
        elif cab=="n":
            print("Ok then we will not book a cab for you.\n")    
        else:
            exit()


        

    elif members<=7:
        if cab=="y":
            car = str(input("Which car do you want ?\n1.Scorpio- Rs.5000\n2.Tavera- Rs.4000\n3.Toyoto- Rs.2500\n"))

        if car=="1":
            var1 = 5000
            print(f"Total price for transport is - {var1}\n" ) 
            print("Your total price for the tour is is - ", (budget*members)+var1)
            print("Your subtotal is:", budget*members+var1)

        elif car=="2":
            var1 = 4000
            print(f"Total price for transport is - {var1}\n" )
            print("Your total price for the tour is is - ", budget*members+var1)
            print("Your subtotal is:", budget*members+var1)

        elif car=="3":
            var1 = 2500
            print(f"Total price for transport is - {var1}\n" ) 
            print("Your total price for the tour is is - ", budget*members+var1)
            print("Your subtotal is:", budget*members+var1)         



    else:
        print("We have booked a nice travellor for you")

else:
    pass





print("\nYour information is saved\n")
print("Thankyou for visiting Travel Agency of Kavyansh!!!\n")  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kavimaheshwari609@gmail.com', 'Kavya@123')
    server.sendmail('kavimahehswari609@gmail.com', to, content)
    server.close()
try:
    content = f" Sir/Maam Thankyou for booking a tour from us{name}\nThankyou For Visiting\nPlease Visit Again"
    to = f"{gmail}"
    sendEmail(to, content)

    def speak(str):
        speak = Dispatch(("SAPI.SpVoice"))
        speak.Speak(str)

    if __name__ == '__main__':
        print(f"We Have Sent a mail to you {name}")
        speak(f"We Have Sent a mail to you {name}")


except Exception as error:
    def speak(str):
        speak = Dispatch(("SAPI.SpVoice"))
        speak.Speak(str)

    if __name__ == '__main__':
        print(f"Sorry {name} because of some problem, email has been not send") 
        speak(f"Sorry {name} because of some problem, email has been not send")

f = open("travelagency.txt", "a")
f.write(f"name = {name}\n")
f.write(f"age = {age}\n")
f.write(f"contact = {contact}\n")
f.write(f"members = {members}\n")
f.write(f"cab = {cab}\n")
f.write(f"place = {place}\n")
f.write(f"budget = {budget}\n")
f.write("--------------------------------------------\n")
f.close()