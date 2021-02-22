#! /usr/bin/env python
import sys
import numpy as np
import pandas as pd
from Random import Random
import seaborn as sns
import matplotlib.pyplot as plt

 # read the user-provided seed from the command line (if there)
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed and trial from suspected dice
    seed = 7890
    trial_b = (350)

    prob = 1/6

    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]

    if '-trial_b' in sys.argv:
        p = sys.argv.index('-trial_b')
        trial_b = sys.argv[p+1]
        trial_b = int(sys.argv[p+1])

        #class instance for random class

random_number = Random(seed)
myx = []
#default trial


for x in range(1,trial_b):
    faces = random_number.Category6()
    myx.append(faces)


plt.figure()
plt.hist(myx ,6 , density=False, facecolor='green', histtype ="barstacked", alpha=0.75)

    # plot formating options
plt.xlabel('Dice faces')
plt.ylabel('Probability' , fontweight="bold" , fontsize="17")
plt.title('Categorical Distribution' , fontweight="bold" , fontsize="17")
plt.grid(True , color='r')


    # save and show figure
plt.savefig("Dice.png")
plt.show()
