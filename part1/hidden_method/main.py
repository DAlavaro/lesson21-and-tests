# - В классе Item:
#   * Добавляем аттрибут discount_value который может содержать число (float) или значение None
#     Например, если скидку необходимо установить 10%  - передаём в discount_value значение 0.1.
#   * Добавляем метод _calculate_discount, который
#     будет возвращать цену с учётом скидки
#   * Рефакторим метод total_price и добавляем в него следующую логику:
#         Если свойство discount класса Item не равно None тогда:
#             вызываем внутренний метод _calculate_discount и пересчитываем цену
#         Если же свойство discount = None тогда возвращаем полную стоимость товара
# - В классе Cheque
#     Внесите соответсвующие изменения в метод add_item чтобы метод работал корректно
# Стартовый код
class Item:
    def __init__(self, title: str, price: int, unit: str, quantity: float):
        self.title = title
        self.price = price
        self.unit = unit
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Cheque:
    def __init__(self):
        self.company = None
        self.items = []

    def add_item(self, title: str, price: int, unit: str, quantity: int):
        item = Item(title=title, price=price, unit=unit, quantity=quantity)
        self.items.append(item)

    def purchases(self):
        return "\n".join(
            [f"{item.title}, {item.quantity} {item.unit} - {item.total_price()}" for item in self.items])
    
    def get_sum(self):
        cheque_sum = sum([item.total_price() for item in self.items])
        return f"Сумма: {cheque_sum}"
    
# Это проверочный код, запустите файл, чтобы увидеть логику работы классов
if __name__ == '__main__':
    # Создаём скидку
    # Создаём чек
    cheque = Cheque()
    # Добавляем товары в чек
    cheque.add_item(title='Сушеные питоны', price=1000, unit='шт', quantity=5, discount_value=0.2)
    cheque.add_item(title='Книги про PHP', price=700, unit='шт', quantity=3, discount_value=0.1)
    cheque.add_item(title='Кофе плохорастворенный', price=200, unit='л', quantity=0.2)
    # Печатаем чек
    print(cheque.purchases())
    print(cheque.get_sum())
