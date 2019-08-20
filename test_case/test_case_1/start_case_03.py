__author__ = 'dingxinhui'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_case/test_case_1/start_case_01.py

import unittest
from function.function_03 import *
from picture.picture import *
from selenium import webdriver
import time,os
from  config.config_01 import  *
# 用例
class Case_03(unittest.TestCase):

    '''  医药馆  '''
    def setUp(self):
        self.imgs = []

    def test_medical(self):
        b = login()
        # print("这是page:" + b[0] + "这是结果啊啊啊啊啊")

        self.imgs.append(b[2])
        time.sleep(3)

        assert "日常用药" in b[0]


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()