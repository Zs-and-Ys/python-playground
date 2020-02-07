# Mission statement:
# Input:
#   1. Number of players involved
#   2. Number of rounds (games) to be simulated
#   3. For each player involved, the strategy to be tested
#       -This could get complicated, especially as number of players increases
# Output:
#   1. Debug: line-by-line plays
#   2. Debug?: Result of each game
#   3. Results of all rounds

import random

debug = True

# Init
ranks = 'A 2 3 4 5 6 7 8 9 T J Q K'.split()
pond = []

for i in range(len(ranks)):
    pond.append(ranks[i])
    pond.append(ranks[i])
    pond.append(ranks[i])
    pond.append(ranks[i])
print('Welcome to the Go Fish Simulator!')
# end Init



# function that takes an array and searches for 4 of a kind.
def checkForBooks(cards, score):
    cards.sort()

    for i in range(len(cards) - 3):
        j = cards[i]
        # print('round ' + str(i + 1))
        # print(j)
        # print(cards.count(j))
        # print(cards.index(j))

        if cards.count(j) == 4:
            while cards.count(j) > 0:
                cards.remove(j)
            score = score + 1

            checkForBooks(cards, score)
            break

    if debug == True:
        print('Cards: ' + str(cards))
        print('Score: ' + str(score))






while True:
    inputPlayers = '2'

    # TODO: increase possible number of players
    # while int(inputPlayers) == False or int(inputPlayers) < 2 or int(inputPlayers) > 2:
    #     print('Enter the number of players [2]:')
    #     inputPlayers = input()

    print('Enter the number of rounds you wish to simulate:')
    inputRounds = input()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # Evaluate round number input
    if int(inputRounds) and int(inputRounds) > 0:
        rounds = int(inputRounds)


        # begin all simulations
        for i in range(rounds):
            # Start of round
            random.shuffle(pond)
            turn = 1
            playersTurn = 1
            p1score = 0
            p2score = 0

            if debug == True:
                print('Round #' + str(i + 1))

                # print('Deck:', end=' ')
                # for i in range(len(pond)):
                #     print(pond[i], end=' ')
                # print()

            hand1 = pond[0:7]
            hand2 = pond[7:14]
            pond = pond[14:52]


            print('testing function now:')
            print('(expecting [\'A\', \'J\', \'Q\'] and score: 0 to be returned)')
            checkForBooks(['Q', 'A', 'J'], p1score)
            print('(expecting [\'2\', \'2\', \'A\', \'J\', \'Q\'] and score: 1 to be returned)')
            checkForBooks(['2', '3', 'Q', '3', '3', 'J', 'A', '2', '3'], p1score)


            if debug == True:
                print('Turn #0')

                print('Hand1:', end=' ')
                for i in range(len(hand1)):
                    print(hand1[i], end=' ')
                print()

                print('Hand2:', end=' ')
                for i in range(len(hand2)):
                    print(hand2[i], end=' ')
                print()

                print('Pond:', end=' ')
                for i in range(len(pond)):
                    print(pond[i], end=' ')
                print()
            # end of start of round


            # While cards in pond and hands still exist...
            while len(pond) > 0 and len(hand1) > 0 and len(hand2) > 0:
                if debug == True:
                    print('Turn #' + str(turn) + ', Player ' + str(playersTurn) + '\'s turn')


                



                input() # placeholder, stops infinite loop for now

                # end of turn
                playersTurn = playersTurn + 1
                if playersTurn > int(inputPlayers):
                    playersTurn = 1
                turn = turn + 1
                # end of end of turn

                # Strategies:
                # 1. Random: reduce hand to unique ranks, then choose one at random
                # 2. Sequential: always guess first rank, then after guessing move it to the end
                # 3. Diabolical: tries to 'go fish' as much as possible in early game, remembers opponents' previous guesses, etc

    else:
        break