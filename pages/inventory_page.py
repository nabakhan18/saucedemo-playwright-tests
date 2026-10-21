class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.items = page.locator(".inventory_item")
        self.prices = page.locator(".inventory_item_price")
        self.names = page.locator(".inventory_item_name")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")

    def add_to_cart(self, product_slug):
        self.page.locator(f"[data-test='add-to-cart-{product_slug}']").click()

    def remove_from_cart(self, product_slug):
        self.page.locator(f"[data-test='remove-{product_slug}']").click()

    def sort_by(self, value):
        # az, za, lohi, hilo
        self.sort_dropdown.select_option(value)

    def get_prices(self):
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]

    def get_names(self):
        return self.names.all_inner_texts()

    def open_cart(self):
        self.cart_link.click()

    def logout(self):
        self.page.locator("#react-burger-menu-btn").click()
        self.page.locator("#logout_sidebar_link").click()
