#!python3
class ShoppingCart(object):
    """Cоздает корзину для покупок
    для нашего сайта."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Добавляет продукт в корзину."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " добавлен.")
        else:
            print(product + " уже в корзине.")

    def remove_item(self, product):
        """Удаляет продукт из корзины."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " убран.")
        else:
            print(product + " нет в корзине.")