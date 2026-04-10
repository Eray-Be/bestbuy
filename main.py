# from products import Product

# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)

# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())

# bose.show()
# mac.show()

# bose.set_quantity(1000)
# bose.show()

import products
from store import Store


product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)
products_list = best_buy.get_all_products()

print(best_buy.get_total_quantity())
print(best_buy.order([(products_list[0], 1), (products_list[1], 2)]))