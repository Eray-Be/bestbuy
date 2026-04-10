# # from products import Product

# # bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# # mac = Product("MacBook Air M2", price=1450, quantity=100)

# # print(bose.buy(50))
# # print(mac.buy(100))
# # print(mac.is_active())

# # bose.show()
# # mac.show()

# # bose.set_quantity(1000)
# # bose.show()

# import products
# from store import Store


# product_list = [
#     products.Product("MacBook Air M2", price=1450, quantity=100),
#     products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#     products.Product("Google Pixel 7", price=500, quantity=250),
# ]

# best_buy = Store(product_list)
# products_list = best_buy.get_all_products()

# print(best_buy.get_total_quantity())
# print(best_buy.order([(products_list[0], 1), (products_list[1], 2)]))

import products
import store


def start(best_buy):
    while True:
        print("\nStore Menu")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            product_list = best_buy.get_all_products()
            for i, product in enumerate(product_list):
                print(f"{i + 1}. ", end="")
                product.show()

        elif choice == "2":
            total = best_buy.get_total_quantity()
            print(f"Total items in store: {total}")

        elif choice == "3":
            product_list = best_buy.get_all_products()
            shopping_list = []

            for i, product in enumerate(product_list):
                print(f"{i + 1}. ", end="")
                product.show()

            while True:
                product_index = input("Enter product number (or 'done'): ")

                if product_index.lower() == "done":
                    break

                try:
                    product_index = int(product_index) - 1
                    quantity = int(input("Enter quantity: "))

                    product = product_list[product_index]
                    shopping_list.append((product, quantity))

                except (ValueError, IndexError):
                    print("Invalid input, try again")

            try:
                total_price = best_buy.order(shopping_list)
                print(f"Order completed! Total price: {total_price}")
            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again")


# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)


if __name__ == "__main__":
    start(best_buy)