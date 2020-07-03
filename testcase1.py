import unittest
from selenium import webdriver
import time
import page
from unittest import TestCase
from unittest.suite import TestSuite
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from page import *


#first test case
class SpecifyChildNumber(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Applications/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.booking.com/")


    def test_specify_child_number(self):
        mainPage = page.MainPage(self.driver)
        mainPage.open_menu()
        mainPage.increase_children_number()
        if mainPage.children_label():
            assert True





    def tearDown(self):
            self.driver.close()


if __name__ == '__main__':
    unittest.main()