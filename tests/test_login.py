import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_valid_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url


def test_invalid_password(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "wrong_pass")
    assert login.error.is_visible()
    assert "do not match" in login.error.inner_text()


def test_locked_out_user(page):
    login = LoginPage(page)
    login.open()
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.error.inner_text()


def test_empty_username(page):
    login = LoginPage(page)
    login.open()
    login.login("", "secret_sauce")
    assert "Username is required" in login.error.inner_text()


def test_logout(logged_in_page):
    InventoryPage(logged_in_page).logout()
    assert logged_in_page.url.rstrip("/") == "https://www.saucedemo.com"
