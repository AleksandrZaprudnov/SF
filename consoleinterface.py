class ConsoleInterface:

    def __init__(self, object_):
        self.object_ = object_
        self.symbol_deck = '█'

    def __str__(self):
        # Вывод рабочего игрового поля
        # ║ ╗ ╝ ╚ ╔ ╦ ╩ ╠ ╣ ═ ╬ █
        str_field = ''

        str_field += f'{self.object_.get_player_name()}, Ваша карта дислокации'
        str_field += '\n    A   B   C   D   E   F'
        str_field += '\n  ╔═══╦═══╦═══╦═══╦═══╦═══╗'

        i = 0
        for id_el in range(1, 37):
            cell_ = self.object_.get_field()[id_el - 1]

            if id_el in [1, 7, 13, 19, 25, 31]:
                i += 1
                str_field += f'\n{i} ║'

            if cell_['deck'] and self.object_.get_show_ships():
                simbol = cell_[id_el] if cell_[id_el] == 'X' else self.symbol_deck
                str_field += f' {simbol} ║'
            else:
                str_field += f' {cell_[id_el]} ║'

            if id_el % 6 == 0 and id_el < 36:
                str_field += '\n  ╠═══╬═══╬═══╬═══╬═══╬═══╣'

        str_field += '\n  ╚═══╩═══╩═══╩═══╩═══╩═══╝'
        return str_field
    # End: __str__()
