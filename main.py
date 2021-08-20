from ship import Ship
from gamefield import GameField
from consoleinterface import ConsoleInterface

import random

def start_game():

    print('\n' * 30)
    print('\t\t\t Пока Вы подписывали мировое соглашение,\n \
        вражеские корабли "БитБайта" заняли позиции...\n \
        Не теряйте время и отправьте свой флот на задание!\n \
        Ваш флот состоит из 4-х боевых катеров, 2-х ракетоносцев\n \
        и одного - Крейсер "Аврора"\n')

    while True:

        exit_play = False

        print('Если хотите дезертировать, вместо имени введите тире (-, минус)')

        # Поле реального игрока
        new_field_game1 = GameField(input('Небольшая формальность, Ваша подпись (ФИО): '))
        new_field_game1.set_show_ships(True)

        if new_field_game1.get_player_name() == '-':
            break

        # Создаем и предварительно показываем поле с координатами
        console_interface = ConsoleInterface(new_field_game1)
        print(f'\n{console_interface}')

        # Приступаем к размещению кораблей
        # Описание: приказ, подсказка, количество кораблей, количество палуб
        list_type_ship = [
            ['\nОтправьте катера по координатам', 'Введите позицию поля (%id%-й), например, 1F: ', 4, 1],
            ['\nРакетоносцы заряжены, отправляйте', 'Введите позицию поля (%id%-й) и расположение (V или H), например, 1FV: ', 2, 2],
            ['\nВперед Крейсер ""Аврора""', 'Введите позицию поля (%id%-н) и расположение (V или H), например, 1FV: ', 1, 3]
        ]

        print('\t\t\t\t\tВводите координату 1-й палубы (сверху-вниз или слева-направо, строка, потом столбец)\n\
              и расположение корабля: V - вертикаль, H - горизонталь. Все без пробелов!\n\
              Для отмены ввода координат нажмите Enter.\n')

        # Расстановка кораблей компьютера (ИИ)
        new_field_ai = GameField('БитБайт')
        new_field_ai.set_show_ships(False)
        console_interface_ai = ConsoleInterface(new_field_ai)

        iter_list = list_type_ship[::-1]
        for i_type in iter_list:
            for s in range(i_type[2]):
                try:
                    prm = ''.join(map(str, random.choice(new_field_ai.get_coordinats_i_j())))
                except ValueError and IndexError as e:
                    break

                if i_type[3] > 1:
                    curr_v_h = str(random.choice(['V', 'H']))
                    prm += curr_v_h

                new_ship_ai = Ship()
                iter_ = 1
                while True:
                    if iter_ > 3:
                        iter_ = 1
                        prm = ''.join(map(str, random.choice(new_field_ai.get_coordinats_i_j())))

                    new_ship_ai.set_build_ship(prm, i_type[3], new_field_ai)
                    if len(new_ship_ai.ship) > 0:
                        new_field_ai.set_ship_field(new_ship_ai)
                        break
                    else:
                        if iter_ == 1:
                            curr_v_h = 'V' if curr_v_h == 'H' else 'H'
                            iter_ = 2

                        if iter_ == 1:
                            prm = ''.join(map(str, random.choice(new_field_ai.get_coordinats_i_j())))
                        elif len(prm) > 2:
                            prm = prm[:2]

                        if i_type[3] > 1 and iter_ == 1:
                            prm += str(random.choice(['V', 'H']))
                        else:
                            prm += curr_v_h
                            iter_ += 1

            # print(f'\n{console_interface_ai}')

        # Расстановка кораблей пользователя
        for i_type in list_type_ship:
            print(i_type[0])

            for s in range(i_type[2]):
                comment = i_type[1].replace('%id%', str(s + 1))
                prm = input(f'{comment}')

                if prm == '':
                    exit_play = True
                    break

                new_ship = Ship()
                while True:
                    try:
                        new_ship.set_build_ship(prm, i_type[3], new_field_game1)
                        if len(new_ship.ship) > 0:
                            new_field_game1.set_ship_field(new_ship)
                        else:
                            prm = input('Повторите ввод:')
                            continue
                        break
                    except:
                        prm = input('Повторите ввод:')

            if exit_play:
                break

            print(f'\n{console_interface}')

        while True:
            print(f'{new_field_ai.get_player_name()} атаковал!')

            shot = random.choice(new_field_game1.get_coordinats_shots())
            new_field_game1.set_shot_field(shot)

            print(f'{console_interface}')

            if new_field_game1.get_q_deck() == 0:
                print(f'\n\n\n{new_field_ai.get_player_name()} - победил...')
                break

            print('Если сдаешься, жми минус')
            shot = None
            while new_field_ai.set_shot_field(shot) is None and shot != '-':
                shot = input(f'Огонь {new_field_game1.get_player_name()}: ')

            print(f'{console_interface_ai}')

            if new_field_ai.get_q_deck() == 0:
                print(f'\n\n\n{new_field_game1.get_player_name()} - УРА-А-А!!! Разгромили!')
                break

            if shot == '-':
                break

        print('\n' * 30)

    print('Exit')
# End: start_game()

start_game()
