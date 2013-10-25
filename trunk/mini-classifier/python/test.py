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
        print self.label,
        for i in range(0, len(self.feaIdx)):
            print self.feaIdx[i] + ":" + self.feaVal[i],
        print ''

class Data(object):
    """A Class that contains training or test set"""
    def __init__(self, fn):
        self.instances = []
        file = open(fn, 'r')
        while 1:
            line = file.readline()
            if not line:
                break
            self.instances.append(Instance(line.strip('\n')))
                
        file.close()
        for ins in self.instances:
            ins.description()


ins = Instance("1 1:1 2:1 3:1")
ins.description()

dat = Data('test')