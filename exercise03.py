from socket import *

class mylist:
    def __init__(self):
        self._elem = []

    def push(self,val):
        self._elem.append(val)

    def pop(self):
        return self._elem.pop()

    def empty(self):
        return self._elem == []

class Ver:
    def __init__(self):
        self.parens = "{}[]()"  #　需要验证的字符
        self.left_parens = "{[("
        #　验证配对是否正确
        self.opposite = {'}':'{',']':'[',')':'('}
        self.vessel = mylist()


    # 负责提供遍历到的括号
    def parent(self,text):
      """
      遍历字符串,提供括号字符和其位置
      """
      #　ｉ记录索引位置
      i,text_len = 0,len(text)
      while True:
        # 循环遍历字符串
        # 到结尾结束，遇到括号提供给ｖｅｒ
        while i < text_len and text[i] not in self.parens:
          i += 1

        if i >= text_len:
          return
        else:
          yield  text[i],i
          i += 1


    #　字符是否匹配的验证工作
    def ver(self,text):
      for pr, i in self.parent(text):
        if pr in self.left_parens:
          self.vessel.push((pr,i))  #　左括号入栈
        elif self.vessel.empty() or self.vessel.pop()[0] != self.opposite[pr]:
          print("Unmatching is found at %d for %s"%(i,pr))
          break
      #　ｆｏｒ循环正常结束
      else:
        if self.vessel.empty():
          print("All parentheses are matched")
        else:
          #　剩下左括号了
          p = self.vessel.pop()
          print("Unmatching is found at %d for %s" % (p[1], p[0]))


# 主程序只负责做括号的验证
if __name__ == '__main__':
    file = input(">>")
    v = Ver()
    with open(file) as f:
        v.ver(f.read())
