__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# function/function_01.py
# 业务功能脚本（用例脚本可调用此处的功能脚本）

from encapsulation.encapsulation import UIHandle
from constant.constant_1 import LOGIN_URL
import config.login_config
from config.config_01 import browser_config
from picture.picture1 import *
import time

def login():

    # 打开浏览器
    driver = browser_config['chrome']
    # print(driver)
    # driver = Case_01.driver
    # print(driver)
    driver.maximize_window()
    driver.implicitly_wait(30)
    # 脚本运行时，错误的信息将被打印到这个列表中
    driver.verificationErrors = []
    # #是否继续接受下一下警告
    driver.accept_next_alert = True
    # 传入driver对象
    uihandle = UIHandle(driver)
    # 输入url地址
    uihandle.get(LOGIN_URL)
    driver.find_element_by_link_text(u"登录").click()
    time.sleep(3)

    # 调用登录方法
    config.login_config.login(driver)

    res = driver.page_source
    title = driver.title
    img = get_screenshot(driver)

    a = [res, title, img]
    # uihandle.quit()
    # driver.close()
    # time.sleep(5)

    # driver.quit()
    return a


