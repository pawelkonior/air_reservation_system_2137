class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_model(self):
        return self.airplane.get_airplane_model()


class Airplane:
    def get_seats_no(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)


class AirbusA380(Airplane):
    @staticmethod
    def get_airplane_model():
        return "Airbus A380"

    @staticmethod
    def get_seating_plan():
        return range(1, 26), 'ABCDEG'


class Boeing737Max(Airplane):
    @staticmethod
    def get_airplane_model():
        return "Boeing 737 Max"

    @staticmethod
    def get_seating_plan():
        return range(1, 46), 'ABCDEGHJK'


plane = Airplane()
airbus = AirbusA380()
boeing = Boeing737Max()
f = Flight('LO127', boeing)
# print(boeing.get_seating_plan())
# print(f.get_airline())
# print(f.get_number())
# print(f.get_model())
print(boeing.get_seats_no())
print(airbus.get_seats_no())
