"""
 编写一个函数，传入端口名称，返回这个端口运行情况中所描述
的address地址信息。
"""
import re
def get_address(port):
   """
   :param port: 端口名称
   :return: 端口对应的address
   """
   f = open('exc.txt')
   while True:
       data = ''
       for line in f:
           if line =='\n':






