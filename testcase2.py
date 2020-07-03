import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec

import page


class SpecifyBookingDate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Applications/chromedriver')
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.booking.com/")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

    def test_specify_booking_date(self):
        mainPage = page.MainPage(self.driver)
        mainPage.select_bui_item_city()
        mainPage.click_room_button()
        mainPage.set_date()
        mainPage.submit_search()





    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()