#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def get_firefox_driver():
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = False
    binary = FirefoxBinary('/usr/bin/firefox')
    return webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)

if __name__ == '__main__':
    browser = get_firefox_driver()
    browser.get('http://localhost:8080')
    assert 'Django' in browser.title
