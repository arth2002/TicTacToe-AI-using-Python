import random

# X is humanplayer
# O is computer player
x_player = "X"
o_player = "O"


mainboard = ['0', '1', '2', '3', '4', '5', '6', '7', '8']


def draw_mainboard():
    frow = "|" + "|".join(mainboard[0:3]) + "|"
    srow = "|" + "|".join(mainboard[3:6]) + "|"
    trow = "|" + "|".join(mainboard[6:10]) + "|"

    return frow + "\n" + srow + "\n" + trow

# mainboard = [" ", "X", "X", " ", "O", "X", " ", " ", " "]

# this function will return true if a specific position is empty


def free_spaces(pos):
    return mainboard[pos].isnumeric()

# this function will let you know how many square(posotion) are empty in whole mainboard


def all_empty_spaces(mainboard):
    all_empty_spaces_var = []
    for i in range(9):
        empty = free_spaces(i)
        if empty == True:
            all_empty_spaces_var.append(i)

    return all_empty_spaces_var

# this function will check winner


def check_winner(mainboard, currmark):
    this_condition = (mainboard[0] == currmark and mainboard[1] == currmark and mainboard[2] == currmark or mainboard[0] == currmark and mainboard[3] == currmark and mainboard[6] == currmark or mainboard[0] == currmark and mainboard[4] == currmark and mainboard[8] == currmark or mainboard[1] == currmark and mainboard[4] == currmark and mainboard[7]
                      == currmark or mainboard[2] == currmark and mainboard[5] == mainboard[8] == currmark or mainboard[2] == currmark and mainboard[4] == currmark and mainboard[6] == currmark or mainboard[3] == currmark and mainboard[4] == currmark and mainboard[5] == currmark or mainboard[6] == currmark and mainboard[7] == currmark and mainboard[8] == currmark)

    if this_condition:
        return True
    else:
        return False

# this function is for user to make move


def get_move_user(x_player):
    user_move = int(input("choose: "))
    mainboard[user_move] = "X"

# this funtion is for ai to make move


def get_move_ai(o_player):
    if len(all_empty_spaces(mainboard)) == 9:
        move = random.choice(o_player.all_empty_spaces())
    else:
        move = minimax(mainboard, o_player)
    return move


def minimax(curr_board, curr_player):
    # available_spaces is list of all_empty_spaces in mainboard
    available_spaces = all_empty_spaces(mainboard)

    # this is for termination stage
    if check_winner(mainboard, "O"):  # if computer won we will return 1
        return {"score": 1}
    elif check_winner(mainboard, "X"):  # if user win we will return -1
        return {"score": -1}
    elif len(all_empty_spaces(mainboard)) == 0:  # else return 0
        return {"score": 0}

    # game info is list in which we will return best move of computer
    game_info = []
    # here we will run loop in range of 0 to len(available_spaces)
    for i in range(0, len(available_spaces)):
        # this is dictionary it will store value of index which will be  available space and score which will decide next move for ai
        # after this for loop ends curr_game_info will have all posible moves and indexes
        curr_game_info = {}
        # here in curr_game_info  index available_spaces will be stored
        curr_game_info["index"] = available_spaces[i]
        # here curr_player's mark will put  to the mainboard
        mainboard[available_spaces[i]] = curr_player
        # if curr_player is o_player(ai)
        if curr_player == o_player:
            result = minimax(mainboard, x_player)
            curr_game_info["score"] = result["score"]
        # else then curr_player will be x_player(human)
        else:
            result = minimax(mainboard, o_player)
            curr_game_info["score"] = result["score"]

        mainboard[available_spaces[i]] = f"{available_spaces[i]}"
        # now curr_game_info have all posibilities of winning and losing for any next move
        game_info.append(curr_game_info)

    # curr_game_info have all posible move for ai to get best next move
    # now from here this minimax function will find best move for ai
    best = None

    if curr_player == o_player:
        # for ai we need to maximize it's winning posibilities so take best_score negative (i.e, -1000 , -infinity)
        best_score = -1000
        # this for loop will give us highest best_score posible move to win
        for i in range(0, len(game_info)):
            if game_info[i]["score"] > best_score:
                best_score = game_info[i]["score"]
                best = i

    else:
        best_score = 1000
        # for ai we need to minimize it's losing  posibilities so take best_score positive (i.e, 1000 , infinity)
        for i in range(0, len(game_info)):
            # this for loop will give us lowest best_score posible move to to minimize losing posibility
            if game_info[i]["score"] < best_score:
                best_score = game_info[i]["score"]
                best = i
    # best move will return by this minimax function
    return game_info[best]

    # print(availabel_spaces[3])


# minimax(mainboard, o_player)

def play_game():

    while len(all_empty_spaces(mainboard)) > 0:
        try:
            print(draw_mainboard())
            get_move_user("X")
            if check_winner(mainboard, x_player):
                print("user won")
                break
            if len(all_empty_spaces(mainboard)) == 0:
                print("Tie")
                break

            ai = get_move_ai("O")['index']
            mainboard[ai] = "O"
            if check_winner(mainboard, o_player):
                print("ai won")
                break
            if len(all_empty_spaces(mainboard)) == 0:
                print("Tie")
                break
            print(all_empty_spaces(mainboard))

        except Exception as e:
            print(e)


play_game()
