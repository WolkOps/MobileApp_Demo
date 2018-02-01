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
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['automationName'] = 'Appium'
        desired_caps['skipUnlock'] = True
        desired_caps['autoWebview'] = True
        desired_caps['app'] = PATH(
            '/Users/itomaldonado/git/wolkops/MobileApp_Demo/platforms/android/app/build/outputs/apk/debug/app-debug.apk'
        )

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    def tearDown(self):
        # end the session
        self.driver.quit()


    def test_home_tab(self):
        # pause a moment, so xml generation can occur
        sleep(5)

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-0"]/page-home/ion-header/ion-navbar/div[2]/ion-title/div')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, 'Home')
        
        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-0"]/page-home/ion-content/div[2]/h2')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, 'Welcome to Ionic!')

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-0"]/page-home/ion-content/div[2]/p[1]')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, 'This starter project comes with simple tabs-based layout for apps that are going to primarily use a Tabbed UI.')

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-0"]/page-home/ion-content/div[2]/p[3]')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, 'Hello, world!')

        el = self.driver.find_element_by_xpath('//*[@id="tab-t0-0"]')
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_xpath('//*[@id="tab-t0-1"]')
        self.assertIsNotNone(el)

        el = self.driver.find_element_by_xpath('//*[@id="tab-t0-2"]')
        self.assertIsNotNone(el)


    def test_about_tab(self):
        # pause a moment, so xml generation can occur
        sleep(5)

        el = self.driver.find_element_by_id('tab-t0-1') # About
        self.assertIsNotNone(el)
        el.click()
        sleep(1)
        
        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-1"]/page-about/ion-header/ion-navbar/div[2]/ion-title/div')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, 'About')
        
        el = self.driver.find_element_by_id('tab-t0-0') # Home
        el.click()
        sleep(1)
        
        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-0"]/page-home/ion-header/ion-navbar/div[2]/ion-title/div')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, 'Home')


    def test_contact_tab(self):
        # pause a moment, so xml generation can occur
        sleep(5)
        
        el = self.driver.find_element_by_id('tab-t0-2') # Contact
        self.assertIsNotNone(el)
        el.click()
        sleep(1)

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-2"]/page-contact/ion-header/ion-navbar/div[2]/ion-title/div')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, 'Contact')

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-2"]/page-contact/ion-content/div[2]/ion-list/ion-list-header/div[1]/div/ion-label')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, 'Follow us on Twitter')

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-2"]/page-contact/ion-content/div[2]/ion-list/ion-item/div[1]/div/ion-label')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, '@ionicframework')

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-2"]/page-contact/ion-content/div[2]/ion-list/ion-item/ion-icon')
        self.assertIsNotNone(el)
        self.assertEquals(el.get_attribute('name'), 'ionic')

        
        el = self.driver.find_element_by_id('tab-t0-0') # Home
        el.click()
        sleep(1)
        
        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-0"]/page-home/ion-header/ion-navbar/div[2]/ion-title/div')
        self.assertIsNotNone(el)
        self.assertEquals(el.text, 'Home')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
