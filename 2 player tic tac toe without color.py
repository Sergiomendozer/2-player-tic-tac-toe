def tic_tac_toe (player_x_name, player_o_name,tic_tac_toe_chart):
    print(tic_tac_toe_chart) 
    position = input (player_x_name + ", select a position you would like to place X:")
    replace = tic_tac_toe_chart.find(position)
    replace = tic_tac_toe_chart.find(position)
    tic_tac_toe_chart = tic_tac_toe_chart[:replace] + 'X' + tic_tac_toe_chart[replace+1:]

    # return tic_tac_toe(player_x_name, player_o_name,tic_tac_toe_chart)
    print(tic_tac_toe_chart) 
    position = input (player_x_name + ", select a position you would like to place X:")
    replace = tic_tac_toe_chart.find(position)
    replace = tic_tac_toe_chart.find(position)
    tic_tac_toe_chart = tic_tac_toe_chart[:replace] + Red + 'O' + END+ tic_tac_toe_chart[replace+1:]
    return tic_tac_toe(player_x_name, player_o_name,tic_tac_toe_chart)

    # call after each if ########################
# def player_o_tic_tac_toe(player_x_name, player_o_name,tic_tac_toe_chart):
#     print ("called")
#     print (END + tic_tac_toe_chart)
#     position = input(Red + player_o_name + ", select a position you would like to place O:")
#     replace = tic_tac_toe_chart.find(position)
#     if position == '3': #add notes why this is needed, accounts for blue
#         replace = tic_tac_toe_chart.find(position)
#         spot_of_blue =tic_tac_toe_chart.find("4", replace)
#         spot_of_red = tic_tac_toe_chart.find("1", replace)
#         if spot_of_blue == replace +1:
#             print('blueo')#####D
#             not_blue=tic_tac_toe_chart.find('3', spot_of_blue) 
#             tic_tac_toe_chart = (tic_tac_toe_chart[:not_blue] +"\033[0;31mO\033[0m" +tic_tac_toe_chart[not_blue+1:])
#             return player_o_tic_tac_toe(player_x_name, player_o_name,tic_tac_toe_chart)
#         elif spot_of_red == replace +1:
#             print('redo')#####D
#             not_red=tic_tac_toe_chart.find('3', spot_of_red) 
#             tic_tac_toe_chart = (tic_tac_toe_chart[:not_red] +"\033[0;31mO\033[0m" +tic_tac_toe_chart[not_red+1:])
#             return player_o_tic_tac_toe(player_x_name, player_o_name,tic_tac_toe_chart)
#         else:
#             print("its okayo") #####D
#             tic_tac_toe_chart = (tic_tac_toe_chart[:replace]+ "\033[0;31mO\033[0m" + tic_tac_toe_chart[replace + 1:])
#             return player_o_tic_tac_toe(player_x_name, player_o_name,tic_tac_toe_chart)
#     else:
# #         print ("ELSEo") #####D
#         replace = tic_tac_toe_chart.find(position)
#         replace = tic_tac_toe_chart.find(position)
#         tic_tac_toe_chart = tic_tac_toe_chart[:replace] + Red + 'O' + END+ tic_tac_toe_chart[replace+1:]
#         return player_x_tic_tac_toe(player_x_name, player_o_name,tic_tac_toe_chart)
    # tic_tac_toe_chart = tic_tac_toe_chart[:replace] + Red +"O" + END + tic_tac_toe_chart[replace+1:]
    # return player_x_tic_tac_toe (player_x_name, player_o_name,tic_tac_toe_chart)


player_x_name = str(input("Enter player name that wil play X:"))
player_o_name = str(input("Enter player name that wil play O:"))
tic_tac_toe_chart = "1 2 3 \n4 5 6\n7 8 9\n"
tic_tac_toe (player_x_name, player_o_name,tic_tac_toe_chart)