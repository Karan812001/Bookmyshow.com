#Project Name : BookYourMovie.com
#Description : In this project I Made Book My Show Replica In Which you can book a Tickets,Show seats,Ticket Statistics.
#Code

class Bookyourmovie: 
    
    @staticmethod
    def Option():
        print("1.Show the seats")
        print("2.Buy a Ticket")
        print("3.Statistics")
        print("4.Show Booked Ticket user Info")
        print("0.Exit")

    @staticmethod
    def seats():
        for i in range(r):
            rl= []
            for j in range(c):
                rl.append("S")
            cl.append(rl)
        return cl

    @staticmethod
    def seat_structure():
        print("Cinema:")
        print(" ", end="  ")
        for seat in range(1, c + 1):
            if seat <= 9:
                print(seat, " ", end="")
            else:
                print(f'{seat:}', "", end="")
        print()
        for k in range(r):
            if k <= 9:
                print(f'{k + 1:=2}', end=" ")
            else:
                print(k + 1, end=" ")
            for seat in range(c):
                print(cl[k][seat], "", end=" ")
            print()

    @staticmethod
    def percentage():
        perc = (Book_seats / T_seat) * 100
        return perc


if __name__ == '__main__':
    r = int(input("Enter the number of rows:"))
    c = int(input("Enter the number of seats in each row:"))
    cl = []
    T_seat = r * c
    Ticket = Bookyourmovie()
    Ticket.seats()
    Audience_list = [[None for j in range(c)] for i in range(r)]
    Book_seats = 0
    Ticket_price = 0
    if T_seat<=60:
        T_income=T_seat * 10
    else:
        T_income=(T_seat * 10)-(r*c)
    r_no = 0
    c_no = 0

    d = 0
    while d == 0:
        Ticket.Option()
        x = int(input())
        if x == 1:
            Ticket.seat_structure()
            vacant_seats = T_seat - Book_seats
            if vacant_seats == T_seat:
                print()
                print(" ", "ALL SEATS VACANT")
                print()
            else:
                print(f"Row {r_no}'s seat no.{c_no} Booked")
            d = 0
        elif x == 2:
            seat_r = int(input("Enter the row number:"))
            if seat_r in range(1, r + 1):
                seat_c = int(input("Enter the column number:"))
                if seat_c in range(1, c + 1):
                    if cl[seat_r - 1][seat_c - 1] == "S":
                        r_no = seat_r
                        c_no = seat_c
                        if r * c <= 60:
                            Ticket_price = 10
                        elif seat_r <= int(r / 2):
                            Ticket_price = 10
                        else:
                            Ticket_price = 8
                        print("Your Ticket Price -", "$", Ticket_price)
                        confirmation =input("yes for Booking and no for exit:")
                        Person_dict = {}
                        if confirmation =="yes" or confirmation =="Yes" or confirmation =="YES":
                            Person_dict['Name'] = input("Name:")
                            Person_dict['Gender'] = input("Gender(M/F/O):")
                            Person_dict['Age'] = int(input("Age:"))
                            Person_dict['Phone_no'] = int(input("Phone No:"))
                            Person_dict["Ticket_Price"] = Ticket_price
                            cl[seat_r - 1][seat_c - 1] = "B"
                            Book_seats += 1
                        else:
                            continue
                        Audience_list[seat_r - 1][seat_c - 1] = Person_dict
                        print("Booked Successfully")
                        print()
                    else:
                        print("Seat is already Booked")
                        print()
                else:
                    print("Invalid Seat Column")
                    print("Max Column can be: ", c)
                    print("  Try again ")
                    print()
            else:
                print("Invalid Seat Row")
                print("Max Column can be:", r)
                print("  Try again")
                print()
            d = 0

        elif x == 3:
            Ticket.seat_structure()
            print()
            print("Number of Purchased Tickets: ", Book_seats)
            print("Percentage of Tickets Booked: ", Ticket.percentage())
            print("Current Income: ", "$", Ticket_price)
            print("Total Income: ", "$", T_income)
            print()
            d = 0

        elif x == 4:
            r = int(input("Enter Row: "))
            c = int(input("Enter Column: "))
            if r in range(1, r + 1) and c in range(1, c + 1):
                if cl[r - 1][c - 1] != "B":
                    print("Seat is available, You can Book it")
                    print()
                    d = 0
                else:
                    person: None = Audience_list[r - 1][c - 1]
                    print("Name: ", person["Name"])
                    print("Gender: ", person["Gender"])
                    print("Age: ", person["Age"])
                    print("Ticket Price: ", person["Ticket_Price"])
                    print("Phone No: ", person["Phone_no"])
                    print()
                    d = 0
            else:
                print("Invalid Entry, Enter valid Row And Column")
                print()
                d = 0
        elif x == 0:
            print("Thanks For Visiting Bookyourmovie.com")
            break