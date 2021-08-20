class GameField:

    def __init__(self, player_name):
        self.player_name = player_name if player_name else 'Петр Современный'
        self.show_ships = False
        self.q_deck = 0
        self.coordinats = [
            [[1], [2], [3], [4], [5], [6]],
            [[7], [8], [9], [10], [11], [12]],
            [[13], [14], [15], [16], [17], [18]],
            [[19], [20], [21], [22], [23], [24]],
            [[25], [26], [27], [28], [29], [30]],
            [[31], [32], [33], [34], [35], [36]]
        ]
        self.coordinats_i_j = [
            [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
            [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
            [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6],
            [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6],
            [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6],
            [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]
        ]
        self.field = (
            {1: 'O', 'deck': False}, {2: 'O', 'deck': False}, {3: 'O', 'deck': False},
            {4: 'O', 'deck': False}, {5: 'O', 'deck': False}, {6: 'O', 'deck': False},
            {7: 'O', 'deck': False}, {8: 'O', 'deck': False}, {9: 'O', 'deck': False},
            {10: 'O', 'deck': False}, {11: 'O', 'deck': False}, {12: 'O', 'deck': False},
            {13: 'O', 'deck': False}, {14: 'O', 'deck': False}, {15: 'O', 'deck': False},
            {16: 'O', 'deck': False}, {17: 'O', 'deck': False}, {18: 'O', 'deck': False},
            {19: 'O', 'deck': False}, {20: 'O', 'deck': False}, {21: 'O', 'deck': False},
            {22: 'O', 'deck': False}, {23: 'O', 'deck': False}, {24: 'O', 'deck': False},
            {25: 'O', 'deck': False}, {26: 'O', 'deck': False}, {27: 'O', 'deck': False},
            {28: 'O', 'deck': False}, {29: 'O', 'deck': False}, {30: 'O', 'deck': False},
            {31: 'O', 'deck': False}, {32: 'O', 'deck': False}, {33: 'O', 'deck': False},
            {34: 'O', 'deck': False}, {35: 'O', 'deck': False}, {36: 'O', 'deck': False},
        )
        self.occup_coordinates = []
        self.coordinats_shots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    def get_player_name(self):
        return self.player_name

    def get_show_ships(self):
        return self.show_ships

    def get_coordinats(self):
        return self.coordinats

    def get_field(self):
        return self.field

    def get_q_deck(self):
        return self.q_deck

    def get_coordinats_i_j(self):
        return self.coordinats_i_j

    def get_coordinats_shots(self):
        return self.coordinats_shots

    def get_occup_coordinates(self):
        return self.occup_coordinates

    def set_q_deck(self, q_deck_):
        self.q_deck += q_deck_

    def set_show_ships(self, show_ships_):
        self.show_ships = show_ships_

    def set_player_name(self, player_name_):
        self.player_name = player_name_ if player_name_ else 'Петр Современный'

    def set_coordinats_i_j_del(self, el_del=[]):
        if el_del in self.coordinats_i_j:
            self.coordinats_i_j.pop(self.coordinats_i_j.index(el_del))

    def set_coordinats_shots_del(self, el_del):
        if el_del in self.coordinats_shots:
            self.coordinats_shots.pop(self.coordinats_shots.index(el_del))

    def set_ship_field(self, object_ship):
        list_coordinats = object_ship.get_build_ship()
        for s, c in list_coordinats:
            str_ = self.coordinats[s - 1]
            col_ = str_[c - 1]
            self.field[col_[0] - 1]['deck'] = True

    def set_occup_coordinates(self, coord):
        self.occup_coordinates.append(coord)

    def set_shot_field(self, coord):
        if coord is None or coord == '-':
            return None

        if str(coord).isdigit():
            self.field[coord - 1][coord] = 'X' if self.field[coord - 1]['deck'] else '~'
            self.set_q_deck(-1 if self.field[coord - 1]['deck'] else 0)
            self.set_coordinats_shots_del(coord)
        else:
            i = None
            j = None
            list_col = ['A', 'B', 'C', 'D', 'E', 'F']
            str_coord = ''.join(coord)

            try:
                if str_coord[0].isdigit():
                    i = int(str_coord[0])
                else:
                    return None

                if str_coord[1].isdigit():
                    return None
                else:
                    j = list_col.index(str_coord[1].upper()) + 1
            except:
                return None

            str_ = self.coordinats[i - 1]
            col_ = str_[j - 1]

            try:
                id_ = self.coordinats_shots.index(col_[0])
            except ValueError as e:
                return None

            self.field[col_[0] - 1][col_[0]] = 'X' if self.field[col_[0] - 1]['deck'] else '~'
            self.coordinats_shots.pop(id_)
            return True
