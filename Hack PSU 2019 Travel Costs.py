# Hack PSU 2019
# Asks user for departing airport, number of days, and budget, returning a list of cities where they can travel to within the budget
# Team Members: Stephen Polacheck, Greg Westfall, TJ Schaeffer, Devarshi Gohil, Charles Alba

def main():
    # Airport Question
    Airport = input("Where are you flying from? Enter 1 for New York City, 2 for Philadelphia, 3 for Washington D.C.: ")
    while Airport != '1' and Airport != '2' and Airport != '3':
        Airport = input("You entered an invalid airport! Try again: Where are you flying from? Enter 1 for New York City, 2 for Philadelphia, 3 for Pittsburgh, 4 for Washington D.C.: ")

    # Days Question
    DaysError = 1
    Days = 0
    while DaysError == 1:
        try:
            Days = int(input("How many days will you be on the trip? "))
            while Days <= 0:
                Days = int(input("You entered an invalid number of days! Try again: How many days will you be on the trip? "))
            DaysError = 0
        except ValueError or TypeError:
            print("You entered an invalid number of days! Try again: ")
            DaysError = 1


    
    # Budget Question
    BudgetError = 1
    Budget = 0
    while BudgetError == 1:
        try:
            Budget = int(input("What is your budget for the trip? "))
            while Budget <= 0:
                Budget = int(input("You entered an invalid budget! Try again: What is your budget for the trip? "))
            BudgetError = 0
        except ValueError:
            print("You entered an invalid budget! Try again: ")
            BudgetError = 1

    while Budget <= 0:
        Budget = input("You entered an invalid budget! Try again: What is your budget for the trip? ")

    dest_file = "dest.txt"
    cost_file = "cost.txt"
    flight_file = Airport + ".txt"

    first = process_dest(dest_file)
    destinations_list = first

    second = process_cost(cost_file)
    cost_per_day_list = second

    third = process_flight(flight_file)
    flight_cost_list = third

    output = finalcitylist(Budget, Days, cost_per_day_list, destinations_list, flight_cost_list)

    count = 0
    print("\nThe cities you can go to are:")
    while count < len(output):
        print(output[count])
        count = count + 1


def process_dest(airport_filename):
    destinations_list = []
    myfile = open(airport_filename, 'r')
    for line in myfile:
        destinations_from_file = line
        destinations_in_string = destinations_from_file.rstrip('\n')
        destinations_list.append(destinations_in_string)
    myfile.close()
    return destinations_list

def process_flight(airport_filename):
    destinations_list = []
    myfile = open(airport_filename, 'r')
    for line in myfile:
        destinations_from_file = line
        destinations_in_string = destinations_from_file.rstrip('\n')
        destinations_list.append(int(destinations_in_string))
    myfile.close()
    return destinations_list

def process_cost(cost_filename):
    cost_per_day_list = []
    cost_file = open(cost_filename, 'r')
    for line1 in cost_file:
        cost_from_file = line1
        cost_in_int = int(cost_from_file.rstrip('\n'))
        cost_per_day_list.append(cost_in_int)
    cost_file.close()
    return cost_per_day_list

def finalcitylist(Budget, Days, cost_per_day_list, destinations_list, flight_cost_list):
    x = 0
    finallist = []
    while x < len(destinations_list):
        totalcost = cost_per_day_list[x] * Days + flight_cost_list[x]
        if totalcost <= Budget:
            finallist.append(destinations_list[x])
            x = x + 1
        else:
            x = x + 1
    return finallist

    
main()
