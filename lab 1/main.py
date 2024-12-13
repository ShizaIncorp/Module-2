from task import Cheese, Lamp, MysteriousTangerine

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    cheese = Cheese(10, 10, 10)
    lamp = Lamp(1, 20)
    mysterious_tangerine = MysteriousTangerine(20, "синий")

    try:
     cheese.init_change_heigth("a")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     lamp.init_change_switch("a")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     mysterious_tangerine.init_repaint(12)
    except TypeError:
        print('Ошибка: неправильные данные')
