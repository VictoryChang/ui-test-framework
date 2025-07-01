from pages.orangehrm_homepage import OrangeHrmHomePage


def test_login_orange(page):
    homepage = OrangeHrmHomePage(page)
    homepage.navigate()
    homepage.login(username="Admin", password="admin123")
    page.wait_for_timeout(3000)
    assert (
        page.url
        == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )
