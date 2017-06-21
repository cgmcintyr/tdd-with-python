#!/usr/bin/env python3
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def get_firefox_driver():
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = False
    binary = FirefoxBinary('/usr/bin/firefox')
    return webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = get_firefox_driver()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new to-do app. She goes to check out its
        # homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # She is invited to enter her to-do item straight away

        # She types "Buy peacock feathers" into a text box

        # When she hits enter, the page updates, and now the pages lists
        # "1: Buy peacock feathers as an itme in a to-do list"

        # There is still a text box inviting her to add another item. She enters
        # "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees that
        # the site has generated a unique URL for her -- there is some explanatory
        # text to that effect

        # She visits that URL - her to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
