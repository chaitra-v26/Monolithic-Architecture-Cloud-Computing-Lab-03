from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    """
    Retrieves and returns a list of Product objects efficiently.
    """
    products = dao.list_products()
    return [Product.load(product) for product in products]


def get_product(product_id: int) -> Product:
    """
    Retrieves a single product by its ID and converts it to a Product object.
    """
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    """
    Adds a new product using the provided product dictionary.
    """
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Updates the quantity of a product, ensuring the quantity is non-negative.
    """
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)

