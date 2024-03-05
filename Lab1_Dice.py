print("Please roll the dice 5 times!")
print("We will then show you the statistics after.")

import random
r1 = random.randint(1, 6)
print("Your first roll is a " + str(r1))

r2 = random.randint(1, 6)
print("Your second roll is a " + str(r2))

r3 = random.randint(1, 6)
print("Your third roll is a " + str(r3))

r4 = random.randint(1, 6)
print("Your fourth roll is a " + str(r4))

r5 = random.randint(1, 6)
print("Your final roll is a " + str(r5))


dice_avg = ((r1+r2+r3+r4+r5) / 5)
dice_score = r1+r2+r3+r4+r5

print("Dice Statistics:")
print("Your dice average is: " + str(dice_avg))
print("Your dice score is: " +str(dice_score))

if dice_score > 18:
    print("High Score!")
elif dice_score > 12:
    print("Medium Score!")
else:
    print("Low Score!")