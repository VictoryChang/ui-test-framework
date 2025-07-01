from playwright.sync_api import Page


class OrangeHrmHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('//input[@name="username"]')
        self.password = page.locator('//input[@name="password"]')
        self.submit = page.locator('//button[@type="submit"]')

    def navigate(self):
        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

    def login(self, username: str, password: str):
        self.username.type(username)
        self.password.type(password)
        self.submit.click()
