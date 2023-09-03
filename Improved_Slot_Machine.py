import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Define symbols and their counts/values
symbols = {
    "A": {"count": 2, "value": 4},
    "B": {"count": 4, "value": 4},
    "C": {"count": 6, "value": 3},
    "D": {"count": 8, "value": 2}
}

def check_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbols[symbol]["value"] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, data in symbols.items():
        count = data["count"]
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        random.shuffle(all_symbols)
        column = [all_symbols.pop() for _ in range(rows)]
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        try:
            amount = int(input("Enter the amount you want to deposit: $"))
            if amount > 0:
                return amount
            else:
                print("Please enter an amount greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def get_number_of_lines():
    while True:
        try:
            lines = int(input(f"Enter the number of lines to play (1-{MAX_LINES}): "))
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Please enter a valid number of lines.")
        except ValueError:
            print("Please enter a valid number.")

def get_bet():
    while True:
        try:
            bet = int(input(f"What would you like to bet on each line (${MIN_BET}-{MAX_BET}): $"))
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        except ValueError:
            print("Please enter a valid number.")

def spin(balance, lines, bet):
    print("\nSpinning the slot machine...")
    slots = get_slot_machine_spin(ROWS, COLS, symbols)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet)
    total_winnings = winnings - (lines * bet)
    balance += total_winnings

    print(f"\nYou won ${total_winnings}!")
    if winning_lines:
        print(f"You won on lines: {', '.join(map(str, winning_lines))}")
    else:
        print("No winning lines this time.")

    return balance

def main():
    print("Welcome to the Slot Machine Game!")
    balance = deposit()

    while True:
        print(f"\nCurrent balance: ${balance}")
        lines = get_number_of_lines()
        bet = get_bet()

        if lines * bet > balance:
            print(f"You do not have enough balance to bet ${lines * bet}.")
            continue

        balance = spin(balance, lines, bet)

        play_again = input("\nPress Enter to play again or 'q' to quit: ")
        if play_again.lower() == 'q':
            break

    print(f"Thank you for playing! You left with ${balance}.")

if __name__ == "__main__":
    main()
