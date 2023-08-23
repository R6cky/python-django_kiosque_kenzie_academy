from management.product_handler import get_product_by_id, get_products_by_type
from management.product_handler import add_product, menu_report
from management.tab_handler import calculate_tab
from menu import products
new_product = {
            "title": "Bolinho JS",
            "price": 1.0,
            "rating": 2,
            "description": "Bolinho de JS com cenoura",
            "type": "bakery",
        }
if __name__ == "__main__":
