from cb_utils import *
import ast


def cb_one(size, config):
    if config.count("1") == 1:
        moves_made = "[]"
        return moves_made

    temp = all_legal_moves_interface(size, config)
    # print(temp)
    for mov in temp:
        updated = update_board_interface(config, mov)
        # print(updated)
        keep = cb_one(size, updated)
        if isinstance(keep, str):
            res = ast.literal_eval(keep)
            res.insert(0, mov)
            return str(res)
    return None


def cb_all(size, config):
    if config.count("1") == 1:
        return True

    temp = all_legal_moves_interface(n, config)
    # print(temp)
    llist = set()
    for mov in temp:
        updated = update_board_interface(config, mov)
        keep = cb_all(size, updated)
        if keep is True:
            ll = []
            ll.append(mov)
            llist.add(str(ll))

        if isinstance(keep, set):
            for ele in keep:
                res = ast.literal_eval(ele)
                res.insert(0, mov)
                llist.add(str(res))

    if len(llist) == 0:
        return None
    return llist


board_str = "0010100010"
n = 4
print(cb_one(n, board_str))
print(cb_all(n, board_str))
