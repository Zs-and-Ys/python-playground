import random

debug = False

# Init
ranks = 'A 2 3 4 5 6 7 8 9 10 11 12 13'.split()
deck = []

for i in range(len(ranks)):
    deck.append(ranks[i] + 'r')
    deck.append(ranks[i] + 'r')
    deck.append(ranks[i] + 'b')
    deck.append(ranks[i] + 'b')
# end Init



# function returns True if card is an Ace
def isCardAce(card):
    cardValue = card[0]

    if cardValue == 'A':
        return True
    else:
        return False



# function returns True if card1 is playable on top of card2
def isCardPlayable(card1, card2):
    card1Value = int(card1[:-1])
    card1Color = card1[-1]
    card2Value = int(card2[:-1])
    card2Color = card2[-1]

    if card1Value + 1 == card2Value and card1Color != card2Color:
        return True
    else:
        return False



while True:
    print('Enter the number of rounds you wish to simulate:')
    userInput = input()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # Evaluate round number input
    if int(userInput) and int(userInput) > 0:
        rounds = int(userInput)
        deadGameCount = 0

        # begin all simulations
        for i in range(rounds):
            # Start of round
            random.shuffle(deck)
            field = deck[0:7]
            hand = deck[7:15]
            isGameDead = True

            if debug == True:
                print('~~Debug~~')
                print('Round #' + str(i + 1))
                # print(deck)
                print('Field: ' + str(field))
                print('Hand: ' + str(hand))

            # 1) check for Aces
            for j in range(len(field)):
                if isCardAce(field[j]):
                    if debug == True:
                        print('Ace found in Field, game is not dead')
                    isGameDead = False
                    break
            if isGameDead == True:
                for k in range(len(hand)):
                    if isCardAce(hand[k]):
                        if debug == True:
                            print('Ace found in Hand, game is not dead')
                        isGameDead = False
                        break

            # 2) check Field cards playable on Field cards
            if isGameDead == True:
                for x in range(len(field)):
                    if isGameDead == False:
                        break
                    else:
                        for y in range(len(field)):
                            if x != y and isCardPlayable(field[x], field[y]):
                                if debug == True:
                                    print('Card in Field: ' + field[x] + ' playable on card in Field: ' + field[y])
                                    print('Playable card found on Field, game is not dead')
                                isGameDead = False
                                break

            # 3) check Hand cards playable on Field cards
            if isGameDead == True:
                for x in range(len(hand)):
                    if isGameDead == False:
                        break
                    else:
                        for y in range(len(field)):
                            if isCardPlayable(hand[x], field[y]):
                                if debug == True:
                                    print('Card in Hand: ' + hand[x] + ' playable on card in Field: ' + field[y])
                                    print('Playable card found in Hand, game is not dead')
                                isGameDead = False
                                break

            if isGameDead == True:
                deadGameCount = deadGameCount + 1
                if debug == True:
                    print('Game is dead!')

        # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Total Rounds: ' + str(rounds))
        print('Dead Game Count: ' + str(deadGameCount))
        print('Odds of dealing a Dead game of Solitaire: ' + str(deadGameCount / rounds * 100) + '%')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    else:
        break