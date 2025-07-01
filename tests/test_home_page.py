from playwright.sync_api import Page

from pages import InventoryPage, LoginPage


def test_login_swaglabs(page: Page):
    homepage = LoginPage(page)
    homepage.navigate()
    homepage.login(username="standard_user", password="secret_sauce")
    inventory = InventoryPage(page)
    inventory.isat()


