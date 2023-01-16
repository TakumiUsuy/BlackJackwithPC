import random as rd
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

pc = rd.choices(cards, k=2)
player = rd.choices(cards, k=2)
player_new = []
pc_new = []


def game():
    player_new.clear()
    pc_new.clear()

    def con_que():
        print("Type 'y' to ""get another card, type 'n' to pass: ", end='')
        if str(input().lower()) == 'y':
            return True
        else:
            return False

    def ace():
        for obj in player:
            player_new.append(int(obj))
        for obj in pc:
            pc_new.append(int(obj))
        if 11 in pc_new or 11 in player_new:
            if sum(player_new) > 21:
                while 11 in player_new:
                    player_new.remove(11)
                    player_new.append(1)
            if sum(pc) > 21:
                while 11 in pc_new:
                    pc_new.remove(11)
                    pc_new.append(1)

    ace()

    def calc_score(someone):
        score_sm = 0
        for _ in someone:
            score_sm += _
        return score_sm

    score_player = calc_score(player_new)
    score_pc = calc_score(pc_new)

    def check_went_over():
        if score_player == 21 and len(player_new) == 2:
            return f"    Your cards: {player}, current score: {score_player}\n"f"    Computer's first card: {pc[0]}\n" \
                   "Win with a Blackjack 😎 "
        elif score_pc == 21 and len(pc_new) == 2:
            return "    Your cards: {player}, current score: {score_player}\n"f"    Computer's first card: {pc[0]}\n" \
                   "Lose, opponent has Blackjack 😱"
        elif score_player > 21:
            return "You went over. You lose 😭"
        elif score_pc > 21:
            return "Opponent went over. You win 😁"
        else:
            return False

    def end_game():
        if score_player == score_pc:
            return "Draw 🙃"
        elif score_pc > score_player:
            return "You lose 😤"
        elif score_player > score_pc:
            return "You win 😃"

    if not check_went_over():
        print(f"    Your cards: {player}, current score: {score_player}\n"f"    Computer's first card: {pc[0]}\n",
              end="")
        if con_que():
            pc.append(rd.choice(cards))
            player.append(rd.choice(cards))
            game()
        else:
            print(end_game())
            if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
                clear()
                print(logo)
                game()
    else:
        print(check_went_over())
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
            clear()
            print(logo)
            game()


if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print(logo)
    game()
