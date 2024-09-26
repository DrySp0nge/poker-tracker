from pyfiglet import Figlet
import sys

pot = 0
bankroll = 0
player_list = []
active_player_list = []
small_blind = 0
big_blind = 0
person_won = False
current_round = 0
continuous_round = 0


class Player:
    def __init__(self, name, start_money):
        global bankroll
        self.name = str(name).strip().title()
        self.balance = start_money
        self.active = True

    def bet(self, money):
        global pot
        pot += int(money)


def main():
    f = Figlet(font="big")
    print(f.renderText("     Welcome  to"))
    f = Figlet(font="coinstak")
    print(f.renderText("           Po ker\n  Trac ker"))
    print("What would you like to do?")
    while True:
        choice = input(
            "====================\n1.Use PokerTracker(use)\n2.Learn about PokerTracker(learn)\n3.Command Help(help)\n4.Exit\n====================\n"
        )
        choice = choice.strip().lower()
        match choice:
            case "1" | "use pokertracker" | "use":
                poker()
            case "2" | "learn about pokertracker" | "learn":
                learn_pokertracker()
            case "3" | "help" | "command help":
                print(
                    "=========================================================\nTo enter an action, you can enter the number that represents the command, you can enter the first word of the given option(except checking balance, you cannot enter 'check' to check balance.), or you can enter the word given in the brackets\n=========================================================\n"
                )
            case "4" | "exit":
                sys.exit("Goodbye!")
            case _:
                print("Please enter one of the given options")


def learn_pokertracker(n=0):
    if n == 0:
        print(
            "=========================================================\nHow to use this program: "
        )
        print(
            "This program will help you play poker. It will keep track of each player's bankroll.\nEnter how many players are playing, the small blind, each player's name and balance.\nYou will have to manually enter 'small blind' or 'big blind'. This program assumes that you know how to play poker and just have no way to keep count of cash, since it allows to immediately check after someone calls/raises or bets.\nAll you have to do is, each turn, enter what you did.\nIf you checked, you put in 'check'. If you fold, you put in 'fold'. You can also check other people's balance as well as who else is left. You can check commands in the 'Commands' option in the main menu\n========================================================="
        )
        return True
    # elif n == 1:
    #     return False


def poker():
    global bankroll
    global active_player_list
    global person_won
    global current_round
    # Makes sure the number of players given is a number.
    while True:
        try:
            players = int(input("Number of players: "))
            blind_bets()
            break
        except ValueError:
            print("Please enter a number")
            pass
    player_setup(players)
    person_won = False
    while True:
        if person_won == True:
            active_player_list.clear()
            for human in player_list[current_round:]:
                if human.balance >= big_blind:
                    active_player_list.append(human)
                    human.active = True
                else:
                    print(
                        f"{human.name} was not added to the round due to insufficient balance\nBalance: ${human.balance}"
                    )
                    while True:
                        add_balance_choice = input(
                            f"Would you like to add balance {human.name} to the amount of ${human.balance}? (yes/no)"
                        )
                        match add_balance_choice:
                            case "yes" | "y":
                                add_balance_amount = input(
                                    "How much money would you like to add? (input number only)"
                                )
                                if add_balance_amount.isnumeric() == False:
                                    print(
                                        "Please enter only a number without any other signs/letters."
                                    )
                                    pass
                                elif add_balance_amount.isnumeric() == True:
                                    final_amount = int(human.balance) + int(
                                        add_balance_amount
                                    )
                                    if final_amount >= big_blind:
                                        human.balance = int(human.balance) + int(
                                            add_balance_amount
                                        )
                                        print(
                                            f"${add_balance_amount} were successfully added to {human.name}'s balance. New balance: ${human.balance}"
                                        )
                                        break
                                    else:
                                        print("Inputted money not sufficient")
                                        pass
                            case "no" | "n":
                                break
            for being in player_list[0:(current_round)]:
                if being.balance >= big_blind:
                    active_player_list.append(being)
                    being.active = True
                else:
                    print(
                        f"{being.name} was not added to the round due to insufficient balance"
                    )
                    while True:
                        add_balance_choice = input(
                            f"Would you like to add balance {being.name} to the amount of ${being.balance}? (yes/no)"
                        )
                        match add_balance_choice:
                            case "yes" | "y":
                                add_balance_amount = input(
                                    "How much money would you like to add? (input number only)"
                                )
                                if add_balance_amount.isnumeric() == False:
                                    print(
                                        "Please enter only a number without any other signs/letters."
                                    )
                                    pass
                                elif add_balance_amount.isnumeric() == True:
                                    final_amount = int(being.balance) + int(
                                        add_balance_amount
                                    )
                                    if final_amount >= big_blind:
                                        being.balance = int(being.balance) + int(
                                            add_balance_amount
                                        )
                                        print(
                                            f"${add_balance_amount} were successfully added to {being.name}'s balance. New balance: ${being.balance}"
                                        )
                                        break
                                    else:
                                        print("Inputted money not sufficient")
                                        pass
                            case "no" | "n":
                                break
            winning_list = []
            for man in active_player_list:
                if man.active == True:
                    winning_list.append(man)
            if len(winning_list) == 1:
                print(f"{winning_list[0].name} won the game!")
                sys.exit()
            else:
                pass
        bet_before = False
        person_won = False
        print(
            f"======================\nRound {continuous_round + 1}\n======================"
        )
        for player in active_player_list:
            if player.active == True:
                # take an action as input, make sure its a valid action(if not, while loop), and call the required class method for it
                while True:
                    global pot
                    print("============\nCurrent Pot: " + "$" + str(pot))
                    action = str(
                        input(
                            f"Choose your action {player.name}:\n1.Bet/Raise/Call 2.Check 3.Fold 4.Somebody Won(won) 5.Check Balance(Balance) 6.Who is Left(Left)\n"
                        )
                    )
                    action = action.strip().lower()
                    match action:
                        case "bet" | "raise" | "1" | "call":
                            bet_before = True
                            bet_money(player)
                            break
                        case "check" | "2":
                            if bet_before == False:
                                print("You checked")
                                break
                            elif bet_before == True:
                                print(
                                    "You cannot check, someone in this round has bet before"
                                )
                                pass
                        case "fold" | "3":
                            print("You folded")
                            fold_check(player)
                            break
                        case "won" | "4" | "somebody won":
                            player_found = False
                            while True:
                                won_player = input("Player who won: ")
                                for thing in active_player_list:
                                    if won_player.strip().lower().title() == thing.name:
                                        player_found = True
                                        pot_win(won_player)
                                        break
                                if player_found == True:
                                    break
                                elif player_found == False:
                                    print("Please enter a valid name")
                                    pass
                            if player_found == True:
                                break

                        case "check balance" | "balance" | "5":
                            bal_found = False
                            while bal_found == False:
                                player_bal = input(
                                    "Name of player whose balance is to be checked: "
                                )
                                player_bal = player_bal.strip().lower().title()
                                for user in player_list:
                                    if user.name == player_bal:
                                        print(f"{user.name} has ${user.balance} left")
                                        bal_found = True
                                    else:
                                        pass
                                pass
                        case "who is left" | "left" | "6" | "who":
                            for person in active_player_list:
                                if person.active == True:
                                    print(f"{person.name}, ", end="", sep="")
                            print("are left")
                        case _:
                            print("Please choose one of the options given")
                            pass
                if person_won == True:
                    break
                else:
                    pass
            else:
                pass


def fold_check(player):
    global person_won
    fold_list = []
    player.active = False
    for person in player_list:
        if person.active == False:
            fold_list.append(person)
        else:
            pass
    if len(fold_list) == (len(player_list) - 1):
        final_list = set(player_list) - set(fold_list)
        for thing in final_list:
            pot_win(thing.name)
    else:
        pass


def bet_money(player):
    global pot
    while True:
        print(
            "You can enter a number that is bigger or equal to the big blind, or type 'small blind' or 'big blind' to bet those respective amounts"
        )
        money = input("Enter bet value: ")
        if str(money).strip().lower() == "big blind":
            pot += int(big_blind)
            player.balance -= int(big_blind)
            break
        elif str(money).strip().lower() == "small blind":
            pot += int(small_blind)
            player.balance -= int(small_blind)
            break
        else:
            try:
                if player.balance >= int(money) >= big_blind:
                    # add bet money to pot and subtract bet money from player balance
                    pot = int(pot) + int(money)
                    print(f"You bet ${money}")
                    pot = int(pot)
                    player.balance = int(player.balance) - int(money)
                    break
                else:
                    raise ValueError
            except ValueError:
                print(
                    "Please enter a valid bet number, or 'small blind' or 'big blind' "
                )
                pass


def player_setup(n):
    global player_list
    global active_player_list
    # give each player a name and a starting balance, and add to the player_list
    # give error if only one player is selected
    for i in range(n):
        while True:
            try:
                name = input("Name of player " + str(int(i) + 1) + ": ")
                start_money = int(input(f"Starting money for {name}: "))
                break
            except ValueError:
                print("Please enter number for starting money")
                pass
        player = Player(name, start_money)
        player_list.append(player)
        active_player_list.append(player)


def pot_win(n):
    global pot
    global current_round
    global person_won
    global continuous_round
    continuous_round += 1
    current_round += 1
    if current_round == len(player_list):
        current_round = 0
    found = False
    person_won = True
    while found == False:
        n = str(n).strip().lower().title()
        found = False
        for player in active_player_list:
            if player.name == n:
                player.balance = int(player.balance)
                player.balance += int(pot)
                pot = 0
                found = True
                print(f"{player.name} won the pot")
            else:
                pass
        if found == False:
            print("Please enter correct name")
            return False
    return True


def blind_bets(n=0):
    global small_blind
    global big_blind
    if n == 0:
        small_blind = int(
            input("Small blind(Big blind is twice the amount of small blind): ")
        )
        big_blind = 2 * small_blind
    else:
        return True


if __name__ == "__main__":
    main()
