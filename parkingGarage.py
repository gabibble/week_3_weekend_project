from datetime import datetime, timedelta
from time import sleep
import time
import sys

now = datetime.now()
current_time=now.strftime("%I:%M")
# print(current_time)
# print(datetime.strftime(now + timedelta(hours=3),"%I:%M"))

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def dots(x):
    for z in range(x):
        print('.', end=' ', flush=True)
        time.sleep(0.5)

class Customer():
    def __init__(self):
        self.name = "name"
        self.customerInfo = {}

    def park(self, ticket):
        response = input("What's your name? ").lower()
        self.customerInfo["name"] = response
        self.customerInfo["ticket"] = ticket
        self.customerInfo["hasTicket"] = True

class ParkingGarage():
    def __init__(self):
        self.tickets = list(range(1, 7))
        self.parkingSpaces = 6
        self.customers = []

    def takeTicket(self):
        if self.parkingSpaces > 0:
            customer = Customer()
            customer.park(self.tickets.pop(0))
            self.customers.append(customer.customerInfo)
            self.parkingSpaces -= 1
            delay_print(f"Your ticket number is {self.customers[-1]['ticket']}\n")
            # self.hasTicket == True
        else:
            delay_print("Sorry, the parking lot is full")
        
    def payForParking(self):
        delay_print("Parking prices: $1.00 per 1 hour of parking\n")
        response = float(input(f"It's currently {current_time}. How many hours would you like to park for? "))
        delay_print(f'You owe ${response}0. Your ticket will expire at {datetime.strftime(now + timedelta(hours=response),"%I:%M")}\n')
        self.customers[-1]['hoursPaid'] = response

    def leaveGarage(self):
        if not self.customers:
            delay_print("Sorry, you can't leave an empty parking lot!\n")
        else:
            response = input("Thanks for parking visiting Julia and Nick's parking Emporium. Enter your name: ").lower()
            for x in self.customers:
                if x['name'] == response.lower():
                    stay = float(input("How many hours did you stay? "))
                    if stay > x['hoursPaid']:
                        delay_print(f"Sorry, didn't pay for {stay} hours. You owe us $200. The feds are on the way!\n")
                    self.tickets.append(x["ticket"])
                    self.customers.remove(x)
                    self.parkingSpaces += 1
                    delay_print("Have a good day!\n")
                else:
                    delay_print("Hey! How did you sneak past the ticket booth? We gotta fire Larry. He keeps sleeping on the job!")
                    dots(7)
                    delay_print("\nYou owe a $200 fee! Respect the rules of the parking king next time!")


park = ParkingGarage()
while True:
    dots(3)
    delay_print(f"\n\nHello! Welcome to the ticket booth! Parking spaces available: {park.parkingSpaces}\n")
    sleep(0.5)
    delay_print("\nAre you arriving or leaving?")
    response = input("\n(type '1' for parking or '2' if you are leaving 'q' for quit) \n")
    if response.lower() == "1":
        park.takeTicket()
        park.payForParking()
    elif response.lower() == "2":
        park.leaveGarage()
    elif response.lower() == "q":
        delay_print("Thanks for stopping by!")
        break
    else:
        delay_print("Invalid input. Please try again!")
# customer = Customer()

# customer.park()