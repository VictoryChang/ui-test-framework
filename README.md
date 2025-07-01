# UI Test Framework

## Motivation
Create a Python UI Test Framework, built with playwright and pytest, that is simple to read, run, and extend.

## Design Pattern
Encapsulating an Browser Page in a Web Application into a "Page" helps make the page be more extensible and the tests more readable.

Example Page:
```python
from playwright.sync_api import Page


class OrangeHrmHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('//input[@name="username"]')
        self.password = page.locator('//input[@name="password"]')
        self.submit = page.locator('//button[@type="submit"]')

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username: str, password: str):
        self.username.type(username)
        self.password.type(password)
        self.submit.click()
```

Example Test Case:
```python
from pages.orangehrm_homepage import OrangeHrmHomePage


def test_login_orange(page):
    homepage = OrangeHrmHomePage(page)
    homepage.navigate()
    homepage.login(username="Admin", password="admin123")
    page.wait_for_timeout(3000)
    assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
```

## Running Test Cases
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. ./run_tests.sh
