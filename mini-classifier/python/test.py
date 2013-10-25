import os

class Instance(object):
    """A Class that contains one instance"""
    def __init__(self, line):
        tks = line.split()
        self.label = tks[0]
        self.feaIdx = []
        self.feaVal = []
        for i in range(1, len(tks)):
            tk = tks[i]
            a = tk.find(':')
            self.feaIdx.append(tk[0:a])
            self.feaVal.append(tk[a+1:])
        self.length = len(self.feaIdx)
    
    def description(self):
        for i in range(0, len(self.feaIdx)):
            print self.feaIdx[i] + ":" + self.feaVal[i],

ins = Instance("1 1:1 2:1 3:1")
ins.description()