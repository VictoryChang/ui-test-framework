# UI Test Framework

## Motivation
Create a Python UI Test Framework, built with playwright and pytest, that is simple to read, run, and extend.

## Design Pattern
Encapsulating a Browser Page in a Web Application into a "Page" helps make the page be more extensible and the tests more readable.

Example Login Page:
```python
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('//input[@id="user-name"]')
        self.password = page.locator('//input[@id="password"]')
        self.submit = page.locator('//input[@id="login-button"]')
    
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")
    
    def login(self, username: str, password: str):
        self.username.type(username)
        self.password.type(password)
        self.submit.click()
```

Example Inventory Page (upon the success login on the home page):
```python
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
    
    def isat(self):
        assert self.page.url == "https://www.saucedemo.com/inventory.html"

```


Example Test Case:
```python
from playwright.sync_api import Page

from pages import InventoryPage, LoginPage


def test_login_swaglabs(page: Page):
    homepage = LoginPage(page)
    homepage.navigate()
    homepage.login(username="standard_user", password="secret_sauce")
    inventory = InventoryPage(page)
    inventory.isat()
```

## Running Test Cases
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. ./run_tests.sh
