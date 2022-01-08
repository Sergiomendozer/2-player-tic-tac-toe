RED="\033[0;31m"          
BLUE="\033[0;34m" 
GREEN="\033[0;32m"
END = '\033[0m'

#Prompts user to select position and whatever user selects it will change number to X
def tic_tac_toe_player_x (player_x_name, player_o_name,tic_tac_toe_chart):
    print(tic_tac_toe_chart) 
    position = input (player_x_name + ", select a position you would like to place X:")
    replace = tic_tac_toe_chart.find(position)
    replace = tic_tac_toe_chart.find(position)
    tic_tac_toe_chart = tic_tac_toe_chart[:replace] + 'X' + tic_tac_toe_chart[replace+1:]
    #call is there a winner function
    did_x_win(player_x_name, player_o_name,tic_tac_toe_chart)

#Prompts user to select position and whatever user selects it will change number to O
def tic_tac_toe_player_o (player_x_name, player_o_name,tic_tac_toe_chart):
    print(tic_tac_toe_chart) 
    position = input (player_o_name + ", select a position you would like to place O:")
    replace = tic_tac_toe_chart.find(position)
    replace = tic_tac_toe_chart.find(position)
    tic_tac_toe_chart = tic_tac_toe_chart[:replace] +'O' + tic_tac_toe_chart[replace+1:]
    #call
    did_o_win(player_x_name, player_o_name,tic_tac_toe_chart)
    # return tic_tac_toe_player_x(player_x_name, player_o_name,tic_tac_toe_chart)

# checks to see if player X won if not then keeps game keeps playing
def did_x_win(player_x_name, player_o_name,tic_tac_toe_chart):
    position_one = tic_tac_toe_chart[0]
    position_two = tic_tac_toe_chart[2]
    position_three = tic_tac_toe_chart[4]
    position_four = tic_tac_toe_chart[7]
    position_five = tic_tac_toe_chart[9]
    position_six = tic_tac_toe_chart[11]
    position_seven= tic_tac_toe_chart[13]
    position_eight = tic_tac_toe_chart[15]
    position_nine = tic_tac_toe_chart[17]
    # 1 2 3 is filled with X
    if position_one == "X" and position_two == "X" and position_three == "X":
        print (BLUE + player_x_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    # 4 5 6 filled with X
    elif position_four == "X" and position_five == "X" and position_six == "X":
        print (BLUE + player_x_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    # 7 8 9 filled with X
    elif position_seven == "X" and position_eight == "X" and position_nine == "X":
        print (BLUE + player_x_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    elif position_one == "X" and position_four == "X" and position_seven == "X":
        print (BLUE + player_x_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    elif position_two == "X" and position_five == "X" and position_eight == "X":
        print (BLUE + player_x_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    elif position_three == "X" and position_six == "X" and position_nine == "X":
        print (BLUE + player_x_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    elif position_one == "X" and position_five == "X" and position_nine == "X":
        print (BLUE + player_x_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    elif position_three == "X" and position_five == "X" and position_seven == "X":
        print (BLUE + player_x_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    else:
        return tic_tac_toe_player_o (player_x_name, player_o_name,tic_tac_toe_chart)

# checks to see if player O won if not then keeps game keeps playing
def did_o_win(player_x_name, player_o_name,tic_tac_toe_chart):
    position_one = tic_tac_toe_chart[0]
    position_two = tic_tac_toe_chart[2]
    position_three = tic_tac_toe_chart[4]
    position_four = tic_tac_toe_chart[7]
    position_five = tic_tac_toe_chart[9]
    position_six = tic_tac_toe_chart[11]
    position_seven= tic_tac_toe_chart[13]
    position_eight = tic_tac_toe_chart[15]
    position_nine = tic_tac_toe_chart[17]
    # 1 2 3 is filled with X
    if position_one == "O" and position_two == "O" and position_three == "O":
        print (RED + player_o_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    # 4 5 6 filled with X
    elif position_four == "O" and position_five == "O" and position_six == "O":
        print (RED + player_o_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    # 7 8 9 filled with X
    elif position_seven == "O" and position_eight == "O" and position_nine == "O":
        print (RED + player_o_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    elif position_one == "O" and position_four == "O" and position_seven == "O":
        print (RED + player_o_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    elif position_two == "O" and position_five == "O" and position_eight == "O":
        print (RED + player_o_name +" is the winner!" + END)
    elif position_three == "O" and position_six == "O" and position_nine == "O":
        print (RED + player_o_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    elif position_one == "O" and position_five == "O" and position_nine == "O":
        print (RED + player_o_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    elif position_three == "O" and position_five == "O" and position_seven == "O":
        print (RED + player_o_name +" is the winner!" + END)
        return play_again(player_x_name, player_o_name,tic_tac_toe_chart)
    else:
        return tic_tac_toe_player_x (player_x_name, player_o_name,tic_tac_toe_chart)

# lets player play again and again
def play_again(player_x_name, player_o_name,tic_tac_toe_chart):
    print ("This is a new game")
    tic_tac_toe_chart = "1 2 3 \n4 5 6\n7 8 9\n"
    tic_tac_toe_player_x (player_x_name, player_o_name,tic_tac_toe_chart)

# prompts users to enter name and start playing game
player_x_name = str(input("Enter player name that wil play X:"))
player_o_name = str(input("Enter player name that wil play O:"))
tic_tac_toe_chart = "1 2 3 \n4 5 6\n7 8 9\n"
tic_tac_toe_player_x (player_x_name, player_o_name,tic_tac_toe_chart)