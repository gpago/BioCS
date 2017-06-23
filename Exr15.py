class Exr15:

    sqn = ""

    def readFiles(self):
        global sqn
        sqn = open("BioData\Alactalbumin", 'r').read()

    def main(self):
        print("Starting..")
        self.readFiles(self)
        print(sqn)

    def player1(self):
        print("player1 code")

    def player2(self):
        print("player2 code")





Exr15.main(Exr15)