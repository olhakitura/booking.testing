import time
import unittest

from selenium import webdriver

import page


class SpecifyBookingDate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Applications/chromedriver')
        self.driver.get("https://www.booking.com/")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_specify_booking_date(self):
        mainPage = page.MainPage(self.driver)
        mainPage.select_bui_item_city()
        mainPage.click_room_button()
        mainPage.set_date()
        mainPage.submit_search()
        time.sleep(30)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()