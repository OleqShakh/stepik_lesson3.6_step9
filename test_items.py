import time

from selenium import webdriver




class TestItems:

    def test_is_element_present(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        assert browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket"), "Basket button is not found"
        time.sleep(3)
        browser.quit()


