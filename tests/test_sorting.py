from pages.inventory_page import InventoryPage


def test_six_products_displayed(logged_in_page):
    assert InventoryPage(logged_in_page).items.count() == 6


def test_sort_price_low_to_high(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.sort_by("lohi")
    prices = inv.get_prices()
    assert prices == sorted(prices)


def test_sort_price_high_to_low(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.sort_by("hilo")
    prices = inv.get_prices()
    assert prices == sorted(prices, reverse=True)


def test_sort_name_z_to_a(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.sort_by("za")
    names = inv.get_names()
    assert names == sorted(names, reverse=True)
