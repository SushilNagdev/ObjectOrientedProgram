class TreasureChest:

    #PRIVATE question : STRING
    #PRIVATE answer : INTEGER
    #PRIVATE points : INTEGER

    def __init__(self, qs, ans, pts) :
        
        self.__question = qs 
        self.__answer = ans
        self.__points = pts
    
    def getQuestion(self):
        return self.__question

    def checkAnswer(self , answer):
        if answer == self.__answer:
            return True
        else:
            return False
    
    def getPoints(self , attempts):

        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return int(self.__points/2)
        elif attempts == 3 or attempts == 4:
            return int(self.__points/4)
        else:
            return 0
            
        




arrayTreasure = [""] * 5

def readData(): 
    global arrayTreasure
    i = 0
    myfile = open("TresureChestData.txt","r" )

    line1 = myfile.readline()
    while line1 != "" :
        line2 = myfile.readline()
        line3 = myfile.readline()
        arrayTreasure[i] = TreasureChest(line1 , line2 , line3)
        i = i + 1
        line1 = myfile.readline()
    myfile.close()

