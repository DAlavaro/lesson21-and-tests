# Попробуем реализовать собственный склад на примере класса
#
# В этом задании Вам необходимо:
# 1. Дописать два внутренних метода класса Storage:
# 1.1. `_get_total`, который возвращает общее число товара на складе (по аттрибуту класса)
# 1.2. `_set_total`, который принимает в качестве аргумента целое число и присваивает переменной
#                    класса `goods_quantity`новое значение.

#
# 2. После этого используйте внутренние методы класса 
# в конструкторе (__init__) класса Storage так, 
# чтобы реализовывалась следующая логика работы:
#
# 2.1. Если количество имеющихся товаров на складе больше, 
#      чем запрошено при инициализации класса, тогда
#      вычитаем из имеющихся на складе товаров (аттрибут `goods_quantity` - класса)
#      запрашиваемое количество и устанавливаем новое значение 
#      имеющихся на складе товаров с помощью метода `_set_total`.
#
#      - Далее, в методе __init__ присваиваем значение аттрибуту экземпляра класса используя self.
#      Для наглядности используйте, 
#      пожалуйста название `goods_quantity`
#
# 2.2. Если количество имеющихся товаров на складе меньше, 
#      чем запрошено при инициализации класса, тогда
#      вне зависимости от запрашиваемого количества товаров
#      присваиваем переменной определяющей число товаров 
#      на складе нулевое значение. А экземпляру класса передаём
#      значение всех имеющихся на складе товаров.
#
# Например, значение goods_quantity класса Storage = 5.
# Мы создаём экземпляр класса: goods = Storage(2)
#
# После этого аттрибут goods_quantity класса Storage
# должен измениться с 5 на 3
# Storage.goods_quantity=3
#
# А аналогичный аттрибут экземпляра класса должен иметь значение 2
# goods.goods_quantity=2


class Storage:
    goods_quantity = 10

    def __init__(self, qnt):
        if qnt < self._get_total():
            self._set_total(self._get_total() - qnt)
            self.i = qnt
        else:
            self.i = self._get_total()
            self._set_total(0)
    @classmethod
    def _get_total(cls):
        return cls.goods_quantity

    def get_total_2(self):
        return self.goods_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.goods_quantity = qnt


# Как закончите писать код, запустите его, 
# чтобы проверить работоспособность
# своего склада
if __name__ == '__main__':
    print("Всего на складе: ", Storage.goods_quantity)
    print("Создаём экземпляр класса Goods (пытаемся забрать 4 ед. со склада)")
    python = Storage(qnt=4)
    print(python.get_total_2())
    print("Осталось на складе: ", Storage.goods_quantity)
    print("Отгрузили со склада в экземпляр класса:", python.i)
    print("Создаём экземпляр класса Goods (пытаемся забрать 5 ед. со склада)")
    python = Storage(qnt=5)
    print("Осталось на складе: ", Storage.goods_quantity)
    print("Отгрузили со склада в экземпляр класса:", python.i)
    print("Создаём экземпляр класса Goods (пытаемся забрать 2 ед. со склада)")
    python = Storage(qnt=2)
    print("Осталось на складе: ", Storage.goods_quantity)
    print("Отгрузили со склада в экземпляр класса:", python.i)
    print('=' * 20)

