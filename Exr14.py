class Exr14:

    brain = ""
    muscle = ""

    def readFiles(self):
        global brain
        global muscle
        brain = open("BioData\BrainSqn", 'r').read()
        muscle = open("BioData\MuscleSqn", 'r').read()



    def player1(self):
        print("player1 code")

    def player2(self):
        print("player2 code")


    def main(self):
        print("Starting..")

        self.readFiles(self)
        print(brain)
        print("-----------------------------")
        print(muscle)






Exr14.main(Exr14)