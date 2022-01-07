# did x win, need two functions
#use find of each and label
# 1= 0
# 2 =2
# 3 =4
# 4= 7
# 5= 9
# 6= 11
# 7= 13
# 8= 15
# 9= 17
# print (tic_tac_toe_chart[17])

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
    if position_one == "X":
        print ("yellow")
    else:
        print ('NO one one')

#####################################
tic_tac_toe_chart = "1 2 3 \n4 5 6\n7 8 9\n" 
tic_tac_toe_chart = "X 2 3 \n4 5 6\n7 8 9\n" 
print (tic_tac_toe_chart)
player_x_name = 1 
player_o_name = 2
did_x_win(player_x_name, player_o_name,tic_tac_toe_chart)