from selenium import webdriver
import time
import os
import unittest
import requests
from method import Runmain
class testcase1(unittest.TestCase):
    @classmethod#必须声明的修饰123
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test01(self):
        url='http://www.baidu.com/s'
        data={
            'wd':'嘿嘿嘿'
        }
        res=Runmain.Runmain().get(url,data,None)
        self.assertEqual(res['code'],200,'状态码不对')
    @unittest.skip('强行跳过')
    def test02(self):
        pass
if __name__ == '__main__':
    unittest.main(verbosity=2)
