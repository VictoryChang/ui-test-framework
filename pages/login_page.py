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
