class FlightBooking:
    def book_flight(self, destination):
        print(f"Flight booked to {destination}")

class HotelBooking:
    def book_hotel(self, destination):
        print(f"Hotel booked in {destination}")

class CarRental:
    def book_car(self, destination):
        print(f"Car rented in {destination}")

class TravelFacade:
    def __init__(self):
        self.flight = FlightBooking()
        self.hotel = HotelBooking()
        self.car = CarRental()

    def book_complete_trip(self, destination):
        self.flight.book_flight(destination)
        self.hotel.book_hotel(destination)
        self.car.book_car(destination)

# Client code
travel = TravelFacade()
travel.book_complete_trip("Hawaii")
