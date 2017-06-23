class Exr16:

    sqn = ""
    countA = 0
    countG = 0
    countT = 0
    countC = 0

    def readFiles(self):
        global sqn
        sqn = open("BioData\Alactalbumin", 'r').read()

    def main(self):
        print("Starting..")
        self.readFiles(self)
        print(sqn)
        self.getCounts(self)
        print("A:" , countA)
        print("T:" , countT)
        print("C:" , countC)
        print("G:" , countG)

    def getCounts(self):
        global countC, countA, countT, countG
        countA = sqn.count('A')
        countG = sqn.count('G')
        countC = sqn.count('C')
        countT = sqn.count('T')

    def player1(self):
        print("player1 code")

    def player2(self):
        print("player2 code")





Exr16.main(Exr16)