from moves import *


def legal_move(board, mov):
    return (mov[0] in board and
            mov[1] in board and
            mov[2] not in board)


def legal_move_interface(board_str, mov):
    temp = set()
    for i in range(len(board_str)):
        if board_str[i] != '0':
            temp.add(i)
    return legal_move(temp, mov)


# board_str = "110001100101011"
# mov = (14, 13, 12)
# print(legal_move_interface(board_str, mov))
# mov = (10, 11, 12)
# print(legal_move_interface(board_str, mov))


def sum(n):
    if n is 0:
        return 0
    return n+sum(n-1)


def all_legal_moves(size, board):
    llist = set()
    for move in all_moves(size):
        if legal_move(board, move):
            llist.add(move)
    return llist


def all_legal_moves_interface(size, board_str):
    if(sum(size) is not len(board_str)):
        return "String is not "+str(sum(size))+" char long"
    temp = set()
    for i in range(len(board_str)):
        if board_str[i] != '0':
            temp.add(i)

    return all_legal_moves(size, temp)


# board_str = "110001100101011"
# n = 5
# print(all_legal_moves_interface(n, board_str))

# board_str = "0110011011"
# n = 4
# print(all_legal_moves_interface(n, board_str))


def update_board(board, mov):
    board.remove(mov[0])
    board.remove(mov[1])
    board.add(mov[2])
    return board


def update_board_interface(board_str, mov):
    temp = set()
    for i in range(len(board_str)):
        if board_str[i] != '0':
            temp.add(i)

    temp = update_board(temp, mov)
    string = ""
    for i in range(len(board_str)):
        if i in temp:
            string += '1'
        else:
            string += '0'
    return string


# board_str = "110001100101011"
# mov = (14, 13, 12)
# print(update_board_interface(board_str, mov))
# mov = (0, 1, 3)
# print(update_board_interface(board_str, mov))
# board_str = "0110011011"
# mov = (5, 2, 0)
# print(update_board_interface(board_str, mov))
