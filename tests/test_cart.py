import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


@pytest.mark.smoke
def test_add_single_item(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart(BACKPACK)
    assert inv.cart_badge.inner_text() == "1"


def test_add_multiple_items(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart(BACKPACK)
    inv.add_to_cart(BIKE_LIGHT)
    assert inv.cart_badge.inner_text() == "2"


def test_remove_item(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart(BACKPACK)
    inv.remove_from_cart(BACKPACK)
    assert inv.cart_badge.count() == 0


def test_items_visible_in_cart(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart(BACKPACK)
    inv.add_to_cart(BIKE_LIGHT)
    inv.open_cart()
    assert CartPage(logged_in_page).items.count() == 2
