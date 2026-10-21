class CartPage:
    def __init__(self, page):
        self.page = page
        self.items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")

    def checkout(self):
        self.checkout_button.click()
