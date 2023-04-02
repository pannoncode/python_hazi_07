from utils.match_check import check_match_horizontal, check_match_vertical, check_match_diagonal
from utils.win import winner

table_draft = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]


def table(table_draft):
    for item in table_draft:
        print(item)


def chosed_pos(user, pos):
    for item in table_draft:
        for idx, value in enumerate(item):
            if pos in value:
                item[idx] = user.upper()
    table(table_draft)


def launch_game():
    counter = 0
    input_type = "X"
    table(table_draft)
    while counter < 9:
        user_pos = input(
            f"{input_type} játékos válaszd ki a pozicíót (!csak számot adhatsz meg!): ")

        try:
            int(user_pos)
            if int(user_pos) > 9 or int(user_pos) < 1:
                print("Nincs ilyen pozicíó")
            else:
                if input_type == "X":
                    chosed_pos(input_type, user_pos)

                    if check_match_horizontal(table_draft) is True:
                        winner(input_type)
                        break

                    if check_match_vertical(table_draft) is True:
                        winner(input_type)
                        break

                    if check_match_diagonal(table_draft) is True:
                        winner(input_type)
                        break

                    input_type = "O"
                else:
                    chosed_pos(input_type, user_pos)

                    if check_match_horizontal(table_draft) is True:
                        winner(input_type)
                        break

                    if check_match_vertical(table_draft) is True:
                        winner(input_type)
                        break

                    if check_match_diagonal(table_draft) is True:
                        winner(input_type)
                        break

                    input_type = "X"
            counter += 1
            print(counter)
        except:
            print("Nem számot adtál meg!")
            break

    print("VÉGE A JÁTÉKNAK")


launch_game()
