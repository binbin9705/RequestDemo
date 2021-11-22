
import requests
import unittest
class Runmain(unittest.TestCase):
    def get(self,url,data,headers):
        self.res=requests.get(url=url,params=data,headers=headers)
        return self.res
    def post(self,url,data,headers):
        self.res=requests.post(url=url,data=data,headers=headers)
        return self.res
    def run_main(self,method,url,data=None,headers=None):
        if method=='GET':
            res=self.get(url,data,headers)
            return res
        elif method=='POST':
            res=self.post(url,data,headers)
            return res

