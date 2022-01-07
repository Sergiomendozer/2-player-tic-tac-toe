# did x win, need two functions
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
        print (player_x_name +" is the winner!")
    # 4 5 6 filled with X
    elif position_four == "X" and position_five == "X" and position_six == "X":
        print (player_x_name +" is the winner!")
    # 7 8 9 filled with X
    elif position_seven == "X" and position_eight == "X" and position_nine == "X":
        print (player_x_name +" is the winner!")
    elif position_one == "X" and position_four == "X" and position_seven == "X":
        print (player_x_name +" is the winner!")
    elif position_two == "X" and position_five == "X" and position_eight == "X":
        print (player_x_name +" is the winner!")
    elif position_three == "X" and position_six == "X" and position_nine == "X":
        print (player_x_name +" is the winner!")
    elif position_one == "X" and position_five == "X" and position_nine == "X":
        print (player_x_name +" is the winner!")
    elif position_three == "X" and position_five == "X" and position_seven == "X":
        print (player_x_name +" is the winner!")
    else:
        return tic_tac_toe_player_o (player_x_name, player_o_name,tic_tac_toe_chart)

#####################################
# tic_tac_toe_chart = "1 2 3 \n4 5 6\n7 8 9\n" 
tic_tac_toe_chart = "1 2 X \n4 X 6\nX 8 9\n" 
print (tic_tac_toe_chart)
player_x_name = 1 
player_o_name = 2
did_x_win(player_x_name, player_o_name,tic_tac_toe_chart)