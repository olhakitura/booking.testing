from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MainPageLocators(object):
    INCREASE_CHILDREN_NUMBER_BUTTON = (By.CSS_SELECTOR,
                                       "#xp__guests__inputs-container > div > div > div.sb-group__field.sb-group-children > div > div.bui-stepper__wrapper.sb-group__stepper-a11y > button.bui-button.bui-button--secondary.bui-stepper__add-button")
    SELECT_STRANGERS_MENU = (By.ID, "xp__guests__toggle")
    CHILDREN_LABEL = (By.CSS_SELECTOR, "#xp__guests__inputs-container > div > div > div.sb-group__children__field.clearfix > label")
    ROOM_BUTTON = (By.LINK_TEXT, "Показать цены")
    DATE_IN = (By.CSS_SELECTOR, "#frm > div:nth-child(9) > div > div.sb-dates__grid.u-clearfix > div.sb-dates__col.--checkin-field > div > div > div.c2-calendar > div.c2-calendar-body > div.c2-calendar-viewport > div > div > div:nth-child(1) > table > tbody > tr:nth-child(4) > td:nth-child(4)" )
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#frm > div.sb-searchbox__row.u-clearfix.-submit.sb-searchbox__footer.-last > div.sb-searchbox-submit-col.-submit-button > button")