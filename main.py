
import random

#Constant to store number of Lines 
MAX_LINES = 3

#Constant to store number of bets
MAX_BET = 100
MIN_BET = 1

#Constant to store number of Rows and Columns
ROWS = 3
COLS = 3

# Dictionary used for Symbols to be put slot machine. The 'value'gives the number of the Particular value
symbol_count = {

    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8

}
# Dictionary used to assigin a (financial)value to each symbol
symbol_value = {

    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2

}



#Spin the Slot machine
def get_slot_machine_spin(rows, cols, symbols):

    #Creating a List to include all of our symbols(8+6+4+2)
    all_symbols = []

    #converting the instances 0f 'key' in Dictionary to a List(instances of A,B,C,D)
    # 'symbol' refers to the 'key'. 'symbol_count' refers to the 'values'.
    #  This is not good Terminology as we have alredy used 'symbol_ccount' to refer to a Dictionary
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            #The instances of 'symbol' or instances of the dictionary key are added to the List.(the values are not added)
            all_symbols.append(symbol)
    
    #Creating a List for our three Columns
    columns = []

    #The number of Columns(col) will be the value of 'cols' passed in as a parameter argument
    for col in range (cols):
        #Creates a column everytime it iterated and addes the column to a new List 'column'
        column = []
        #creating a copy of 'all_symbols'
        current_symbols = all_symbols[:]
        #iterating as many times as there 'rows'
        for row in range(rows):
            #Using the 'random' Function to pick a symbol from 'current_symbols'
            value = random.choice(current_symbols)
            #Removing an instance of the chosen 'symbol'
            current_symbols.remove(value)
            #Adding the 'symbol' to the List 'column'
            column.append(value)
        #Adding the 'column' instant  to the 'columns' List
        columns.append(column)

    #All of the symbols in the List 'columns' will be returned
    return columns


#We print out the 'columns' in the slot maching
#We use 'Transposing' to change from horizontal to vertical(change from row to column)
def print_slot_machine(columns):

    #We find the number of rows in one column(the length of the column will give us this)
        for row in range(len(columns[0])):
            #
            for i, column in enumerate(columns):

                #If 'i' is not the last row we print a '|' (we only want two'|')
                if i != len(columns) -1:
                 print(column[row],"|",end="")
            else:
              print(column[row], )




    

#Ask the user to deposite an amount as their 'balance'
def deposite():
    while True:
        amount = input("Please Enter an amount to Deposit")
        #checking if the input was a number
        if amount.isdigit():
            #storing the input as an 'int'
            amount = int(amount)
            #if amount is a positive number , we can break out of loop
            if(amount > 0):
                break
            else:
                #Amount must be a positive number
                print("amount must be greater than 0")
        else:
            print("Please enter a number")
    #The positive number will be returned        
    return amount


def get_number_of_lines():

    #We run a Loop until we get satisfactory input
    while True:
        #Storing the input in variable 'lines'
        lines = input("Please Enter the number of Lines to bet on(1 -" + str(MAX_LINES)+")?")
        #checking if input was a  positive number
        if lines.isdigit():
            #Converting 'lines' to type 'int'
            lines = int(lines)
            if  1<= lines  <= MAX_LINES :
                
                #If number entered is between MIN_LINES and MAX_LINES
                break
            else:
                #If number entered is not between MIN_LINES and MAX_LINES
                print("Enter a valid number of Lines")
        else:
            print("Please enter a number")
    #returns the number of lines bet on        
    return lines

# Method to invite user to place bet
def get_bet():

     while True:
        amount = input("What would you like to bet on each Line")
        if amount.isdigit():
            amount = int(amount)
            #if the amount(input) is in the allowed range, we break out of loop
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                #if a bet outside range was attempted
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            #if something other than a number was entered
            print("Please enter a number")
    
    #The bet(input) or 'amount' is returned
     return amount

#Method to check if three rows are the same(if the user has won)
def check_winnings(columns, lines, bet, value):

    #variable to store 'winnings'
    winnings = 0
    #List to store any lines that have won
    winning_lines = []


    for line in range(lines):
        symbol = columns[0][line]
        for colum in columns:
            symbol_to_check = colum[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol]* bet
            winning_lines.append(line +1)

    # returns both amount won and also the winning line(s)
    return winnings, winning_lines


#Method to be used in alternative Program
def check_all_same_elements(lst):
    
    #checks for lines that have the same symbol
    return all(x == lst[0] for x in lst)



    





def main():
    
     balance =deposite()
     lines = get_number_of_lines()

     while True:


        bet = get_bet()

        total_bet = lines*bet

        if total_bet > balance:
            print(f"You do not have enough in your balance to bet that amount, Your current balance is ${balance}")

        else:
            break

     print(f"You are betting ${bet} on 10{lines}. Your Total Bet is ${total_bet}")

     slots = get_slot_machine_spin(ROWS,COLS,symbol_count)

     print_slot_machine(slots)

     winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

     print(f"You won ${winnings}.")
     print(f"You won on lines :", *winning_lines )

    



main()

#Code to be used in alternative Program
"""
alpha = []

test_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

for key, value in test_count.items():
    for _ in range(value):
        alpha.append(key)

random.shuffle(alpha)  # Shuffle the elements in alpha

a = random.sample(alpha, 3)  # Select 3 random elements from alpha without replacement

print("Elements in a:", a)


check_all_same_elements(a)

"""



