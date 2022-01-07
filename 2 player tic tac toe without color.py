def tic_tac_toe (player_x_name, player_o_name,tic_tac_toe_chart):
    print(tic_tac_toe_chart) 
    position = input (player_x_name + ", select a position you would like to place X:")
    replace = tic_tac_toe_chart.find(position)
    replace = tic_tac_toe_chart.find(position)
    tic_tac_toe_chart = tic_tac_toe_chart[:replace] + 'X' + tic_tac_toe_chart[replace+1:]
    #call is there a winner function

    print(tic_tac_toe_chart) 
    position = input (player_o_name + ", select a position you would like to place O:")
    replace = tic_tac_toe_chart.find(position)
    replace = tic_tac_toe_chart.find(position)
    tic_tac_toe_chart = tic_tac_toe_chart[:replace] +'O' + tic_tac_toe_chart[replace+1:]
    return tic_tac_toe(player_x_name, player_o_name,tic_tac_toe_chart)


player_x_name = str(input("Enter player name that wil play X:"))
player_o_name = str(input("Enter player name that wil play O:"))
tic_tac_toe_chart = "1 2 3 \n4 5 6\n7 8 9\n"
tic_tac_toe (player_x_name, player_o_name,tic_tac_toe_chart)