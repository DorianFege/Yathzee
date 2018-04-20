import random
import math
from collections import Counter
ptsinf = 0
ptssup = 0
ptstotal = 0
print ("Bienvenue dans le Yathzee")

Dés = []
for i in range (1,6) :
    Dés.append(random.randint(1,6))
print(Dés)
print("Quels dés voulez vous garder?")


def déid1 :
    id1 = Dés.count("1")
    ptsinf = ptsinf + id1
    


