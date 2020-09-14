from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains



class BookingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Driver/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_BookigHomePage(self):
        self.driver.get("https://www.booking.com/")
        print("Page Opened")
        self.driver.find_element_by_xpath("//span[contains(text(),'Sign in')]").click()
        self.driver.find_element_by_xpath("//input[@id='username']").send_keys("hamzamajid18@gmail.com")
        self.driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("bsef13a528")
        self.driver.find_element_by_xpath(
            "//button[@class='bui-button bui-button--large bui-button--wide']//span[@class='bui-button__text'][contains(text(),'Sign in')]").click()
        print("Login Successfull")

    def test_Booking(self):
        print("After login")
        location = self.driver.find_element_by_xpath("//input[@id='ss']")
        location.clear()
        location.send_keys("Murree")
        selectfromdate = self.driver.find_element_by_xpath(
                "//div[contains(@class,'xp__dates-inner xp__dates__checkin')]")
        selectfromdate.click()
        selectfromdate.find_element_by_xpath(
            "//form[1]//div[1]//div[2]//div[2]//div[1]//div[1]//div[3]//div[1]//table[1]//tbody[1]//tr[3]//td[3]//span[1]//span[1]").click()
        self.driver.find_element_by_xpath(
            "//div[contains(@class,'bui-calendar__main b-a11y-calendar-contrasts')]//div[1]//table[1]//tbody[1]//tr[3]//td[7]").click()
        self.driver.find_element_by_xpath("//button[contains(@class,'sb-searchbox__button')]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Price (lowest first)')]").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[@id='hotellist_inner']//div[1]//div[2]//div[3]//div[1]//div[1]//div[1]//div[1]//div[2]//div[3]//div[1]//div[1]//div[1]//a[1]").click()
        self.driver.find_element_by_id("b_tt_holder_1").click()
        time.sleep(10)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
