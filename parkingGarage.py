class Customer():
    def __init__(self):
        self.name = "name"
        self.customerInfo = {}

    def Park(self):
        response = input("What's your name?").lower()
        self.customerInfo['name'] = response
        self.customerInfo['tckNumb'] = 1
        self.customerInfo['parkingSpace'] = 1



class ParkingGarage():
    def __init__(self):
        self.tickets = []
        self.parkingSpaces = list(range(20))
        self.currentTickets = {}

    def takeTicket(self):
        if len(self.parkingSpaces) > 0:
            print("TICKT TAKEN")
            print(self.parkingSpaces)
        else:
            print("NO TIX")


    def payForParking(self):
        pass

    def leaveGarage(self):
        pass


park = ParkingGarage()

park.takeTicket()
