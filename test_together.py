# coding=utf-8

import unittest
from test_case.test_case_1.start_case_01 import Case_01
# from test_case.test_case_1.start_case_09 import Case_09
from test_case.test_case_1.start_case_11 import Case_11

# from laobai_shiyongzhongxin import shiyongzhongxin

#构造测试集
suite = unittest.TestSuite()
suite.addTest(Case_01("test_login"))
# suite.addTest(Case_09("test_order"))
suite.addTest(Case_11("test_laobaiergodic"))

#suite.addTest(shiyongzhongxin("test_syzx"))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
