from locator import *
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec




class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)


class MainPage(BasePage):

    def open_menu(self, *locator):
        strangers_menu = self.driver.find_element(*MainPageLocators.SELECT_STRANGERS_MENU)
        strangers_menu.click()

    def increase_children_number(self, *locator):
        increase_children = self.driver.find_element(*MainPageLocators.INCREASE_CHILDREN_NUMBER_BUTTON)
        increase_children.click()

    def children_label(self, *locator):
        children_label = self.driver.find_element(*MainPageLocators.CHILDREN_LABEL)
        print(children_label.is_displayed())

    def select_bui_item_city(self, *locator):
       bui_city = self.driver.find_element_by_class_name("unified-postcard__overlay")
       actions = ActionChains(self.driver)
       actions.move_to_element(bui_city).click(bui_city).perform()

    def click_room_button(self, *locator):
        room_button = self.driver.find_element(*MainPageLocators.ROOM_BUTTON)
        room_button.click()

    def set_date(self, *locator):
        date_in = self.driver.find_element(*MainPageLocators.DATE_IN).click()

    def submit_search(self, *locator):
        submit_search = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON).click()





