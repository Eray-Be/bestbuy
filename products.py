class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price must be zero or positive")
        if quantity < 0:
            raise ValueError("Quantity must be zero or positive")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if self.quantity == 0:
            self.deactivate()

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Stock cannot be negative")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("You must buy at least one item")
        if not self.is_active():
            raise ValueError("Product is not available")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")

        total_cost = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return total_cost