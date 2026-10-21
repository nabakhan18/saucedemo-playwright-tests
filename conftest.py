import pytest
from pages.login_page import LoginPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def logged_in_page(page):
    """Login karke inventory page par pohanchata hai."""
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    page.wait_for_url("**/inventory.html")
    return page
