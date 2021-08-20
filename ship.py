class Ship:

    # prm - строка и столбец, вертикальное или горизонтальное
    #       расположение корабля (V или H), например, 3FV
    # deck - количество палуб корабля, число
    def __init__(self):
        self.ship = []

    def set_build_ship(self, prm, decks, object_field):

        i_inc = 0
        j_inc = 0
        tmp_list_coord = []
        tmp_list_coord_del = []
        list_col = ['A', 'B', 'C', 'D', 'E', 'F']
        str_coord = ''.join(prm)
        i = int(str_coord[0])
        # Для подбора случайной координаты используем числа
        if str_coord[1].isdigit():
            # try:
            j = int(str_coord[1])
        else:
            # except TypeError as e:
            j = list_col.index(str_coord[1].upper()) + 1

        # Проверка, если указано направление корабля
        if len(str_coord) > 2:
            v_h = str_coord[2]
        else:
            v_h = None

        for id_deck in range(decks):
            if v_h is None or v_h in 'Hh':
                j_inc = id_deck
                if decks > 1 and j + decks - 1 > 6:
                    j -= 6 - decks - 1
                    # break
            elif v_h in 'Vv':
                i_inc = id_deck
                if decks > 1 and i + decks - 1 > 6:
                    i = 6 - decks - 1
                    # break

            if not [i + i_inc, j + j_inc] in object_field.get_coordinats_i_j():
                tmp_list_coord.clear()
                break

            tmp_list_coord_del.append([i + i_inc, j + j_inc])
            tmp_list_coord_del.append([i + i_inc, j + j_inc - 1])
            tmp_list_coord_del.append([i + i_inc, j + j_inc + 1])
            tmp_list_coord_del.append([i + i_inc - 1, j + j_inc - 1])
            tmp_list_coord_del.append([i + i_inc - 1, j + j_inc])
            tmp_list_coord_del.append([i + i_inc - 1, j + j_inc + 1])
            tmp_list_coord_del.append([i + i_inc + 1, j + j_inc - 1])
            tmp_list_coord_del.append([i + i_inc + 1, j + j_inc])
            tmp_list_coord_del.append([i + i_inc + 1, j + j_inc + 1])

            tmp_list_coord.append([i + i_inc, j + j_inc])

        if len(tmp_list_coord) > 0:
            self.ship = tmp_list_coord
            object_field.set_q_deck(len(tmp_list_coord))

            for el_ in tmp_list_coord_del:
                object_field.set_coordinats_i_j_del(el_)


    def get_build_ship(self):
        return self.ship
