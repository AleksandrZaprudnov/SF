import sys

def set_symbol(simbol):
    # Возвращаем только англ. "Х"
    str_X = 'хХxX'

    return 'X' if simbol in str_X else '0'
# End: set_symbol()

def create_user(db_users, c):
    # Добавление пользователя и есть возможность - имена поумолчанию
    default_list_users = ['Krestikov', 'Nolikov']
    record = {}

    user_name = input(f'Введите имя {c}-го игрока: ')
    record['name'] = user_name if user_name else default_list_users[c - 1]

    if record['name'] in default_list_users:
        print(f'Будете - {record["name"]}')

    if db_users:
        user_simbol = db_users[str(c - 1)]['simbol']
        user_simbol = '0' if user_simbol == 'X' else 'X'
    else:
        user_simbol = set_symbol(input('Х или 0: '))

    record['simbol'] = user_simbol

    return record
# End: create_user()

def add_users(c):
    # Словарь пользователей. Можно расширить и хранить доп. статистику и др. данные
    dict_users = {}
    for i in range(c):
        dict_users[str(i + 1)] = create_user(dict_users, i + 1)

    return dict_users
# End: add_users()

def gen_playing_field():
    # Генератор поля
    tuple_playing_field = (
        {1: '-'}, {2: '-'}, {3: '-'},
        {4: '-'}, {5: '-'}, {6: '-'},
        {7: '-'}, {8: '-'}, {9: '-'}
    )

    return tuple_playing_field
# End: gen_playing_field()

def rend_field(tpf):
    # Вывод рабочего игрового поля
    # ║ ╗ ╝ ╚ ╔ ╦ ╩ ╠ ═ ╬

    str_tab = '\t' * 5 # Не получилось вставить строку сразу в print

    print(f'  Ход игры{str_tab}\tНомера клеток')
    print(f'╔═══╦═══╦═══╗{str_tab}╔═══╦═══╦═══╗')
    print(f'║ {tpf[0][1]} ║ {tpf[1][2]} ║ {tpf[2][3]} ║{str_tab}║ 1 ║ 2 ║ 3 ║')
    print(f'║═══╬═══╬═══║{str_tab}║═══╬═══╬═══║')
    print(f'║ {tpf[3][4]} ║ {tpf[4][5]} ║ {tpf[5][6]} ║{str_tab}║ 4 ║ 5 ║ 6 ║')
    print(f'║═══╬═══╬═══║{str_tab}║═══╬═══╬═══║')
    print(f'║ {tpf[6][7]} ║ {tpf[7][8]} ║ {tpf[8][9]} ║{str_tab}║ 7 ║ 8 ║ 9 ║')
    print(f'╚═══╩═══╩═══╝{str_tab}╚═══╩═══╩═══╝')
# End: rend_field()

def combinations():
    # Выигрышные комбинации
    list_combinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]

    return list_combinations
# End: combinations()

def check_winner(current_position, tpf):
    # Проверка выигрыша
    list_comb = combinations()

    for comb in list_comb:
        list_ = []
        if current_position in comb:
            for i in comb:
                list_.append(str(tpf[i - 1].values()))
            if len(list(set(list_))) == 1:
                return True

    return False
# End: check_winner()

def main_TicTacToe():
    # Основная функция
    print('Добро пожаловать в игру "Крестики-нолики"' + '\n' * 2 + 'Создание игроков')
    print('Можно пропускать ввод сведений об игроках, данные заполнятся автоматически (пропуск - Enter)')

    dict_users = add_users(2)
    list_completed_moves = []
    playing_field = gen_playing_field()

    index_user = 1
    i = 1
    not_repeat_move = True
    winning = False

    while True:
        if not_repeat_move and not winning and i < 10:
            print('\n' * 30)
            print(dict_users["1"]["name"] + " играет " + dict_users["1"]["simbol"] + "-м")
            print(dict_users["2"]["name"] + " играет " + dict_users["2"]["simbol"] + "-м")
            print('Для завершения нажмите любую букву или Enter')

            rend_field(playing_field)
        elif winning or i == 10:
            print('\n' * 30)

            rend_field(playing_field)

            print('Игра закончена' + ' в ничью.' if not winning else '.')
            break

        field_position = input(f'Ваш ход {dict_users[str(index_user)]["name"]}: ') # Если сразу приводить к int,
        # Учитываем нажатии еще и "Enter"
        field_position = 0 if not field_position or str(field_position) not in '123456789' else int(field_position)

        if field_position in list_completed_moves:
            print('Ход уже сделан, выполните новый')
            not_repeat_move = False
            continue
        else:
            if str(field_position) not in '123456789':
                break

            list_completed_moves.append(field_position)
            not_repeat_move = True

        playing_field[field_position - 1][field_position] = dict_users[str(index_user)]['simbol']

        if check_winner(field_position, playing_field):
            print('\n' * 30)
            print(f'Победа, {dict_users[str(index_user)]["name"]}!')
            winning = True

        if not winning:
            i += 1
            # Индекс игрока можно проверять как остаток от деления == 1,
            # но, все равно, получается пара строк.
            index_user += 1
            index_user = 1 if index_user > 2 else index_user
# End: main_TicTacToe()

# Идеи не реализованные, в виду занятости ;-)
# 1. Повторение игры, для начавших игру, при завершении партии
# 2. Проверка ввода имени (для исключения повторяющихся имен пользователей), при создании пользователей
# 3. Замер времени игры:
#     а) общее время игры;
#     б) каждого игрока (в кортеже tuple_playing_field его подсловарях можно хранить доп. информацию)
# 4. В конце игры можно показать выделение победных ячеек.
# Идеи продолжают генерироваться, думаю вернусь к открытым вопросам. Очень хочется привести ближе к идеалу.
# Главное - цель достигнута. Работает!

main_TicTacToe()
