from constants import *
import random
    

def deposit():
    while True:
        amount = input("Type in the amount you want to deposit: $ ")
        if(amount.lstrip("-").isdigit()):
            amount = int(amount)
            if(amount > 0):
                break
            else:
                print("Please print a positive number!")
        else:
            print("Please enter a number !")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Type in number of lines you want to bet (1 - {MAX_LINES}): $ ")
        if(lines.lstrip("-").isdigit()):
            lines = int(lines)
            if(lines > 0 and lines <= 3):
                break
            else:
                print(f"Please print a number between 1 and {MAX_LINES} !")
        else:
            print("Please enter a number !")
    return lines
def get_bet():
    while True:
        bet_amount = input(f"What would you like to bet on each line? ({MIN_BET} - {MAX_BET}) $ ")
        if(bet_amount.lstrip("-").isdigit()):
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Please print a number between ${MIN_BET} and ${MAX_BET} !")
        else:
            print("Please enter a number !")
    return bet_amount

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, all_symbol_count in symbol_count.items():
        for _ in range(all_symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            column.append(value)
            current_symbol.remove(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    # transpose the columns
    length = len(columns[0])
    width = len(columns)
    for i in range(width):
        for j in range(length):
            if(j != length - 1):
                print(columns[i][j], end="|")
            else:
                print(columns[i][j])

def check_winnings(columns, lines, bet):
    winnings = 0
    winnning_lines = []
    for line in range(lines):
        symbol = columns[line][0]
        for j in range(len(columns[0])):
            if(columns[line][j] != symbol):
                break
        else:
            winnning_lines.append(line + 1)
            winnings += bet * symbol_val[symbol]
    return winnings, winnning_lines



def main():
    columns = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(columns)
    balance = deposit()
    while True:
        lines = get_number_of_lines()
        bet_amount = get_bet()
        if(lines*bet_amount > balance):
            print(f"Uh oh! current bet is over your balance of ${balance}. Please try again.")
        else:
            balance -= lines*bet_amount
            break
    print(f"Hello user ! You are currently betting ${bet_amount} on {lines} lines for a total of ${lines*bet_amount}. Your current balance is ${balance}")

    winnings, winning_lines = check_winnings(columns, lines, bet_amount)
    if(winnings > bet_amount*lines):
        print(f"Congrats You just won ${winnings} on lines ", end="")
        for i, line in enumerate(winning_lines):
            if(i != len(winning_lines) - 1):
                print(line, end=',')
            else:
                print(line)
    else:
        print(f"Oh no you just lost ${bet_amount*lines - winnings} !")
    


main()