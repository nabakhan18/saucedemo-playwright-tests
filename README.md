# SauceDemo Playwright Tests

UI automation testing project using **Python, Pytest and Playwright** with the **Page Object Model** pattern.
Target site: https://www.saucedemo.com (a public practice website).

## What is tested
- Login: valid, invalid password, locked-out user, empty fields, logout
- Cart: add, remove, multiple items, cart contents
- Sorting: price low-high, high-low, name Z-A
- Checkout: full flow, validation errors

## Project structure
```
pages/       Page Objects (locators + actions)
tests/       Test cases
conftest.py  Shared fixtures (logged_in_page)
pytest.ini   Pytest config
.github/     CI workflow (GitHub Actions)
```

## Setup
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
playwright install
```

## Run tests
```bash
pytest                       # headless
pytest --headed              # browser visible
pytest --headed --slowmo 500 # slow motion
pytest -m smoke              # only smoke tests
pytest --browser firefox     # other browser
```
Screenshots of failed tests are saved in `test-results/`.

## CI
Tests run automatically on every push through GitHub Actions.
