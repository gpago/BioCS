import sys
import time
from termcolor import colored, cprint
from random import randint

class Exr15:

    sqn = ""
    length = 0
    queue = 0

    def readFiles(self):
        self.sqn = open("BioData\Alactalbumin", 'r').read()
        self.sqn = self.sqn.replace('\n', '').replace('\r', '')
        self.sqn = self.sqn.rstrip()
        self.sqn = self.sqn.lstrip()

    def countSQN(self):
        self.length = len(self.sqn)

    #-----------------------------------------------------------------

    def smartCalc(self):
        result = 0
        if(self.queue % 2 == 0):
            print()
        else:
            print()
        return result

    # -----------------------------------------------------------------

    def player1(self):
        #print("Winning code")
        move = self.smartCalc(self)
        cprint(move, "blue")

    def player2(self):
        #print("Random code")
        move = randint(1, 2)
        self.queue -= move
        cprint(move, "red")

    # -----------------------------------------------------------------

    def playBall(self):
        print("Play ball!")
        counter = 1
        while (self.queue > 0):
            print("Round: ", counter)

            self.player1(self)
            if(self.queue == 0):
                cprint("Player 1 wins!", "green")
                break
            #time.sleep(0.01)
            self.player2(self)
            if (self.queue == 0):
                cprint("Player 2 wins!", "green")
                break

            if(counter > self.length):
                cprint("Error! Overflow.", "black", "red")
                break
            counter += 1



    def main(self):
        print("Starting..")
        self.readFiles(self)
        self.countSQN(self)
        print("Get set.")
        print(self.sqn)
        self.queue = self.length
        self.playBall(self)
        cprint("--------------------", "green")
        cprint("Done!", "green")


Exr15.main(Exr15)