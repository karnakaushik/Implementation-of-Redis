import datetime
import time
import bisect

class Structure:
    
    # CREATE DICTIONARY FOR MEMORY AND "TIME TO CHECK"
    def __init__(self):
        self.memoryDictionary = {}
        self.timeDictionary = {}
        self.setDictionary = {}

    # SET THE KEY-VALUE PAIR IN MEMORY DICTIONARY, THE TIME TO KEEP A PARTICULAR KEY
    def SET(self,key,value):    
        self.memoryDictionary[key] = value
        self.timeDictionary[key] = "UNL"


    # USING LAZY-DELETION HERE TO CHECK FOR THE TIME TILL A KEY WOULD BE PRESENT

    def EXPIRE(self,key,time):
        expirationTime = datetime.datetime.now() + datetime.timedelta(seconds=time)
        self.timeDictionary[key] = expirationTime
        
    # GET THE VALUE OF A KEY, NEED TO CHECK FOR THE TIME TILL VALUE WAS PRESENT
    def GET(self,key):
        value = self.memoryDictionary.get(key)
        if(value == None):
            return "Nil"
        if(self.timeDictionary.get(key) == 'UNL'):
            return value
        elif self.timeDictionary.get(key) < datetime.datetime.now():
            self.memoryDictionary.pop(key)              # POPING THE KEY-VALUE AS IT WILL NOT BE REQUIRED
            self.timeDictionary.pop(key)
            return 'Nil'
        else:
            return value
    
    # ADDING THE SETS WITH SCORES 
    def ZADD(self,zSet,score,key):
        if self.memoryDictionary.get(zSet) == None:
            self.memoryDictionary[zSet] = {}
            self.timeDictionary[zSet] = 'UNL'
            self.memoryDictionary[zSet][key] = score
            self.setDictionary[zSet] = {score:[key]}
        
        else:
            if self.setDictionary[zSet].get(score) == None:
                self.setDictionary[zSet][score] = []

            self.memoryDictionary[zSet][key] = score
            bisect.insort(self.setDictionary[zSet][score] , key)
        

        return 1

    # EXTRACTING RANK FROM TWO DIFFERENT DICTIONARIES ONE IS FOR MEMORY AND OTHER IS FOR SKIP-LIST

    def ZRANK(self,zSet,key):
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
            return 
            

    # GETTING DATA BASED ON SCORES
    def ZRANGE(self,zSet,start,end):
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



# STUB-CODE TO TEST THE FUNCTIONALITIES
def main():
    obj = Structure()
    obj.SET("abc",123)
    obj.SET("inf",45456)
    obj.ZADD("myset",1,'orange')
    obj.ZADD("myset",1,'apple')
    obj.ZADD("myset",2,"three")
    print(obj.ZRANK("myset","three"))
    print(obj.GET('myset'))
    print(obj.ZRANGE("myset",-2,-1))



if __name__ == "__main__":
    main()
    
