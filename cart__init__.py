import json
from cart import dao
from products import Product, get_product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list[Product]:
    """
    Retrieves the user's cart and converts product IDs into Product objects.
    """
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Optimized to avoid unnecessary loops and redundant operations
    items = [item for cart_detail in cart_details for item in json.loads(cart_detail['contents'])]
    product_map = {item_id: get_product(item_id) for item_id in set(items)}
    return [product_map[item_id] for item_id in items]


def add_to_cart(username: str, product_id: int):
    """
    Adds a product to the user's cart.
    """
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    """
    Removes a specific product from the user's cart.
    """
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    """
    Deletes the user's entire cart.
    """
    dao.delete_cart(username)

