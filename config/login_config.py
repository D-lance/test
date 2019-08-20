__author__ = 'dingxinhui'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
def login(driver):
    driver.find_element_by_css_selector("input[type=\"text\"]").clear()
    driver.find_element_by_css_selector("input[type=\"text\"]").send_keys("xxx")
    time.sleep(2)
    driver.find_element_by_css_selector("input[type=\"password\"]").clear()
    driver.find_element_by_css_selector("input[type=\"password\"]").send_keys("xxx")
    time.sleep(2)
    driver.find_element_by_css_selector("div.submit").click()
    time.sleep(3)
