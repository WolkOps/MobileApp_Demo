import os
from time import sleep

import unittest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['skipUnlock'] = True
        desired_caps['app'] = PATH(
            '/Users/itomaldonado/git/wolkops/MobileApp_Demo/platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        # end the session
        self.driver.quit()


    def test_home_tab(self):
        # pause a moment, so xml generation can occur
        sleep(5)

        el = self.driver.find_element_by_accessibility_id("Home")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("Welcome to Ionic!")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("This starter project comes with simple tabs-based layout for apps that are going to primarily use a Tabbed UI.")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("home Home")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("information circle About")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("contacts Contact")
        self.assertIsNotNone(el)


    def test_about_tab(self):
        # pause a moment, so xml generation can occur
        sleep(5)
        
        el = self.driver.find_element_by_accessibility_id("information circle About")
        el.click()
        sleep(1)
        
        el = self.driver.find_element_by_accessibility_id("About")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("home Home")
        el.click()
        sleep(1)

        el = self.driver.find_element_by_accessibility_id("Home")
        self.assertIsNotNone(el)


    def test_contact_tab(self):
        # pause a moment, so xml generation can occur
        sleep(5)
        
        el = self.driver.find_element_by_accessibility_id("contacts Contact")
        el.click()
        sleep(1)
        
        el = self.driver.find_element_by_accessibility_id("Contact")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("Follow us on Twitter")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("ionic")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("@ionicframework")
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_accessibility_id("home Home")
        el.click()
        sleep(1)

        el = self.driver.find_element_by_accessibility_id("Home")
        self.assertIsNotNone(el)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)