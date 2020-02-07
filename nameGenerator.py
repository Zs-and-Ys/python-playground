# The purpose of this program is to generate a list of random names by combining smaller bits of strings.

import random

##################################################
# input section
##################################################

# BFLMNR
partA = 'B F L M N R'.split()
partB = 'a e i o ai ee'.split()
partC = 'ba bee boo fa fee foo la lee loo ma mee moo na nee noo ra ree roo'.split()

# FQuLT
# partA = 'F Qu L T'.split()


##################################################
# output section
##################################################
while True:
    print('Enter the number of names you wish to simulate:')
    inputRounds = input()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # Evaluate round number input
    if int(inputRounds) and int(inputRounds) > 0:
        rounds = int(inputRounds)

        # begin all simulations
        for i in range(rounds):
            # Start of round
            name = ''

            name = name + random.choice(partA)
            name = name + random.choice(partB)
            name = name + random.choice(partC)

            if random.randint(0, 1) == 1:
                name = name + random.choice(partC)

            print('Round ' + str(i) + ': ' + name)
    else:
        break