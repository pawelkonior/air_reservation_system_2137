from flight import Flight
from planes import AirbusA380, Boeing737Max
from helpers import card_printer


def main():
    airbus = AirbusA380()
    boeing = Boeing737Max()
    f = Flight('LO127', boeing)
    # print(boeing.get_seating_plan())
    # print(f.get_airline())
    # print(f.get_number())
    # print(f.get_model())
    # print(boeing.get_seats_no())
    f.allocate_passenger(passenger="Lech K", seat="12C")
    f.allocate_passenger(passenger="Jarosław K", seat="12B")
    f.allocate_passenger(passenger="Paweł K", seat="12A")
    f.relocate_passenger("12A", "25G")
    # print(f.get_empty_seat())
    # pp(f.seating_plan)
    f.print_tickets(card_printer)


if __name__ == '__main__':
    main()
