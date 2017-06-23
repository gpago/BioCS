# import module

class Exr22:
    sqn = ""
    lyz = ""

    def readFiles(self):
        global sqn
        global lyz
        sqn = open("BioData\Alactalbumin", 'r').read()
        lyz = open("BioData\LYZC", 'r').read()


    def main(self):
        print("Starting..")
        self.readFiles(self)
        print(sqn)
        print("-----------------")
        print(lyz)




Exr22.main(Exr22)