__author__ = 'dingxinhui'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_case/test_case_1/start_case_01.py

import unittest
from function.function_06 import *
from picture.picture import *
from selenium import webdriver
import time,os
from  config.config_01 import  *
# 用例
class Case_06(unittest.TestCase):

    '''  隐形眼镜  '''
    def setUp(self):
        self.imgs = []

    def test_Contactlenses(self):
        b = login()
        # print("这是page:" + b[0] + "这是结果啊啊啊啊啊")

        self.imgs.append(b[2])

        assert "日抛" in b[0]


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()