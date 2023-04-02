def check_match_horizontal(table_draft):
    if table_draft[0][0] == table_draft[0][1] == table_draft[0][2]:
        return True
    if table_draft[1][0] == table_draft[1][1] == table_draft[1][2]:
        return True
    if table_draft[2][0] == table_draft[2][1] == table_draft[2][2]:
        return True


def check_match_vertical(table_draft):
    if table_draft[0][0] == table_draft[1][0] == table_draft[2][0]:
        return True
    if table_draft[0][1] == table_draft[1][1] == table_draft[2][1]:
        return True
    if table_draft[0][2] == table_draft[1][2] == table_draft[2][1]:
        return True


def check_match_diagonal(table_draft):
    if table_draft[0][0] == table_draft[1][1] == table_draft[2][2]:
        return True
    if table_draft[0][2] == table_draft[1][1] == table_draft[2][0]:
        return True
