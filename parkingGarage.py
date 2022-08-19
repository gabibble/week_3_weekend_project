class Customer():
    def __init__(self):
        self.name = "name"
        self.customerInfo = {}
        self.hasTicket = False

    def park(self, ticket):
        response = input("What's your name?").lower()
        self.customerInfo[response] = ticket
        # name = ticket
        # self.customerInfo['tckNumb'] = 1
        # self.customerInfo['parkingSpace'] = 1
        print(self.customerInfo)



class ParkingGarage():
    def __init__(self):
        self.tickets = list(range(1, 4))
        self.parkingSpaces = 3
        self.currentTickets = {}

    def takeTicket(self):
        if self.parkingSpaces > 0:
            print("TICKT TAKEN")
            print(self.parkingSpaces)
            customer = Customer()
            customer.park(self.tickets.pop())
            self.parkingSpaces -= 1
            print(self.tickets)
            # self.hasTicket == True
        else:
            print("NO TIX")
        
    def payForParking(self):
        pass

    def leaveGarage(self):
        pass

park = ParkingGarage()

park.takeTicket()
park.takeTicket()
park.takeTicket()
park.takeTicket()
park.takeTicket()

# customer = Customer()

# customer.park()