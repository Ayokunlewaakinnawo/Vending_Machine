#  This program is designed to be used by a vending machine to dispense change.
def main():
    print("WELCOME TO THE HU REFRESHING VENDING MACHINE :)")
    print("Kindly make a number selection of the choice of drinks you want to purchase.\n\n"
          " 1.  Coca-cola: $1.50\n", "2.  Snapples: $2.67\n",
          "3.  Sprite: $2.00\n", "4.  Pepsi: $1.50\n", "5.  Mountain-dew: $1.65\n")
#  Input of the item selection by the user
    try:
        try:

            it_select = int(input("Enter the specified item number (example; 1 for coca-cola) : "))

            #  The look-up item list and the item Dictionary (which includes the item prices)
            items = ["Coca-cola", "Snapples", "Sprite", "Pepsi", "Mountain-dew"]

            item_dict = {"Coca-cola": 1.50,
                         "Snapples": 2.67,
                         "Sprite": 2.00,
                         "Pepsi": 1.50,
                         "Mountain-dew": 1.65}

            #  Process; of getting the item from indexing
            it_select = items[int(it_select) - 1]

            #  Another input provided for the user to make payment
            pay_amount = float(input("You've selected " + it_select + "\nEnter/insert money amount: "))
            #  The loop is to make sure the right amount is paid for the item selected
            for item in item_dict:
                while pay_amount < item_dict[item]:
                    pay_amount = pay_amount + float(input("\n\nInsert more Money: "))

            #  PROCESS;
            #  Using conditional statement
            if it_select == "Coca-cola":
                it_cost = 1.50
            elif it_select == "Snapples":
                it_cost = 2.67
            elif it_select == "Sprite":
                it_cost = 2.00
            elif it_select == "Pepsi":
                it_cost = 1.50
            elif it_select == "Mountain-dew":
                it_cost = 1.65
            else:
                print("You've made an invalid selection!")
                return it_cost

            #  evaluating the total change dispensed by machine
            total_change = pay_amount - it_cost

            #  change dispensed in their respective denomination from  the highest
            dollar_bill = int(total_change // 1)
            new_total = total_change % 1

            quater_coins = int(new_total // 0.25)
            new_total = new_total % 0.25

            dime_coins = int(new_total // 0.10)
            new_total = new_total % 0.10

            nickel_coins = int(new_total // 0.05)
            new_total = new_total % 0.05

            pennies_coins = int(new_total // 0.01)
            new_total = new_total % 0.01

            print("\n\nPayment made Successfully,\nTOTAL CHANGE DISPENSED IS; ${0:0.2f}".format(total_change))
            print("", dollar_bill, "dollar bill\n", quater_coins, "quater coins\n", dime_coins, "dime coins\n",
                  nickel_coins,
                  "nickel coins\n", pennies_coins, "pennies")

        except ValueError:
            print("You've made an invalid selection")

    except IndexError:
            print("You've made an invalid selection")


main()