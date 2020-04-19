import datetime
import time
import bisect
from collections import OrderedDict

class Structure:
    
    def __init__(self):
        self.memoryDictionary = {}
        self.timeDictionary = {}
        self.setDictionary = {}

    def setKey(self,key,value):    
        self.memoryDictionary[key] = value
        self.timeDictionary[key] = "UNL"

    def expireKey(self,key,time):
        expirationTime = datetime.datetime.now() + datetime.timedelta(seconds=time)
        self.timeDictionary[key] = expirationTime
        
    
    def getKey(self,key):
        value = self.memoryDictionary.get(key)
        if(value == None):
            return "Nil"
        if(self.timeDictionary.get(key) == 'UNL'):
            return value
        elif self.timeDictionary.get(key) < datetime.datetime.now():
            self.memoryDictionary.pop(key)
            self.timeDictionary.pop(key)
            return 'Nil'
        else:
            return value

    def zaddSet(self,zSet,score,key):
        if self.memoryDictionary.get(zSet) == None:
            self.memoryDictionary[zSet] = {}
            self.timeDictionary[zSet] = 'UNL'
            self.memoryDictionary[zSet][key] = score
            self.setDictionary[zSet] = {score:[key]}
        
        else:
            # bisect.insort(self.memoryDictionary[zSet][key] , value)
            if self.setDictionary[zSet].get(score) == None:
                self.setDictionary[zSet][score] = []

            self.memoryDictionary[zSet][key] = score
            bisect.insort(self.setDictionary[zSet][score] , key)
        

        return 1

    def zRank(self,zSet,key):
        if self.memoryDictionary.get(zSet) == None:
            return 'Nil'
        else:
            score = self.memoryDictionary[zSet][key]
            tempDict = self.setDictionary[zSet]
            dict1 = dict(sorted(tempDict.items()))
            #print(dict1)
            i = 0
            for x in dict1:
                if(x == score):
                    break
                i+=1
            return i

    def zRange(self,zSet,start,end):
        if self.memoryDictionary.get(zSet) == None:
            return 'Nil'
        else:
            tempDict = self.setDictionary[zSet]
            dict1 = dict(sorted(tempDict.items()))
            list1 = list(dict1.values())
            if start > end:
                return []
            if(end == -1):
                return list1[start:]
            elif (end > 0):
                return list1[start:end+1]
            elif start < 0:
                return list1[start:end+1]

def main():
    obj = Structure()
    obj.setKey("abc",123)
    obj.setKey("inf",45456)
    obj.zaddSet("myset",1,'orange')
    obj.zaddSet("myset",1,'apple')
    obj.zaddSet("myset",2,"three")
    print(obj.zRank("myset","three"))
    print(obj.getKey('myset'))
    print(obj.zRange("myset",-2,-1))



if __name__ == "__main__":
    main()
    