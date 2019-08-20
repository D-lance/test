__author__ = 'dingxinhui'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# function/function_01.py
# 业务功能脚本（用例脚本可调用此处的功能脚本）

from config.config_01 import browser_config
import time
from encapsulation.encapsulation import UIHandle
from constant.constant_1 import LOGIN_URL
from picture.picture1 import *
import config.login_config

#
def login(search):

    # # 打开浏览器
    driver = browser_config['chrome']
    # driver.maximize_window()
    # driver.implicitly_wait(30)
    # # #脚本运行时，错误的信息将被打印到这个列表中
    # driver.verificationErrors = []
    # # #是否继续接受下一下警告
    # driver.accept_next_alert = True

    # 传入driver对象
    uihandle = UIHandle(driver)
    # #输入url地址
    # uihandle.get(LOGIN_URL)
    # driver.find_element_by_link_text(u"登录").click()
    # time.sleep(3)
    #
    # #调用登录方法
    # config.login_config.login(driver)

    # 调用二次封装后的方法，此处可见操作了哪个页面，哪个元素，后面是要插入的值，插入值得操作在另外一个用例文件中传入
    handles = driver.window_handles
    driver.switch_to.window(handles[0])
    uihandle.Input('老白首页', '搜索输入框', search)
    time.sleep(3)
    uihandle.Click('老白首页', '搜索按钮',)
    time.sleep(3)
    handles = driver.window_handles
    print(handles)
    driver.switch_to_window(handles[1])
    uihandle.Click('老白首页', '第一个商品')
    time.sleep(3)
    handles1 = driver.window_handles
    print(handles1)
    driver.switch_to_window(handles1[2])
    uihandle.Click('老白首页', '加入购物车')
    time.sleep(3)
    uihandle.Click('老白首页', '去结算')
    time.sleep(3)
    js = "window.scrollTo(0,1000)"
    driver.execute_script(js)
    uihandle.Click('老白首页', '提交订单')

    time.sleep(5)

    # print(driver.page_source)

    res = driver.page_source

    title = driver.title

    img = get_screenshot(driver)

    a = [res, title, img]
    # uihandle.quit()
    driver.switch_to_window(handles1[2])
    driver.close()
    driver.switch_to_window(handles1[1])
    driver.close()
    return a