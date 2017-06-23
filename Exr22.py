# import module

class Exr22:
    sqn = ""

    def readFiles(self):
        global sqn
        sqn = open("BioData\Alactalbumin", 'r').read()


    def main(self):
        print("Starting..")
        self.readFiles(self)
        print(sqn)




Exr22.main(Exr22)