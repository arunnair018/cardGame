
import random
from collections import Counter
import operator
import time

# card game class


class cardGame:
    # constructor to initialize
    # no. of player
    # card faces
    # deck players
    def __init__(self, members=4):
        self.member = members
        self.cards = [
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
        ]
        self.deck = {
            "K": 4, "Q": 4, "J": 4, "10": 4, "9": 4, "8": 4, "7": 4, "6": 4, "5": 4, "4": 4, "3": 4, "2": 4, "A": 4,
        }
        self.players = {}

    # to set player in begining
    def setPlayers(self):
        for i in range(1, self.member+1):
            self.players[i] = []

    # if tie between player settle by extra card
    def tieBreaker(self, player):
        newCard = []
        for players in player:
            card = self.getfromDeck()
            newCard.append(self.cards.index(card))
            self.players[players].append(card)
        print("\ndraw between players {} \n".format(player))
        for i in player:
            self.showHand(i)
        maxCard = max(newCard)
        if newCard.count(maxCard) == 1:
            return str(player[newCard.index(maxCard)])
        else:
            players = [x for i, x in enumerate(
                player) if newCard[i] == maxCard]
            return str(self.tieBreaker(players))

    # if a hand contain all same cards -- first highest combination
    def Rule1(self, hand):
        for i in hand:
            if not i.isdigit():
                return False
        if hand[0] == hand[1] and hand[0] == hand[2]:
            return True
        return False

    # if a hand contain sequence of cards -- second highest combination
    def Rule2(self, hand):
        for i in hand:
            if i == "A":
                continue
            if not i.isdigit():
                return False
        a = [self.cards.index(i) for i in hand]
        a.sort()
        if (a[1]-a[0] == 1) and (a[2]-a[1] == 1):
            return True
        else:
            return False

    # if a hand contain pair of cards -- third highest combination
    def Rule3(self, hand):
        if (hand[0] == hand[1] or hand[1] == hand[2] or hand[0] == hand[2]):
            return True
        return False

    # if all combination fails
    # check for highest card
    def Rule4(self, players):
        # get highest cars of all players
        highest_player = self.getHighest(players)
        high_face = max(highest_player)
        # if 1 player got highest card
        if highest_player.count(high_face) == 1:
            return str(highest_player.index(high_face)+1)

        # if more than 1 player got highest card
        if highest_player.count(high_face) > 1:
            players = [i+1 for i, x in enumerate(
                highest_player) if x == high_face]
            return self.tieBreaker(players)

    # check for all highest combinations
    def applyRules(self, hand):
        if (self.Rule1(hand)):
            return 3
        if (self.Rule2(hand)):
            return 2
        if (self.Rule3(hand)):
            return 1
        return 0

    # get the highest card for all players hand
    def getHighest(self, players):
        h = []
        for player in players:
            hand = players[player]
            faces = [self.cards.index(i) for i in hand]
            h.append(max(faces))
        return h

    # gets random card from deck
    def getfromDeck(self):
        randomCard = random.randrange(13)
        card = self.cards[randomCard]
        if (self.deck[card] > 0):
            self.deck[card] -= 1
            return card
        else:
            return self.getfromDeck()

    # calculates the result of game
    def decision(self, players):
        # to store combination for each player index wise
        combinations = []

        # apply first 3 combination rules
        for player in players:
            combinations.append(self.applyRules(players[player]))

        # if all combinations fail
        if sum(combinations) == 0:
            return self.Rule4(self.players)

        high_combination = max(combinations)

        # if 1 player got highest combination
        if combinations.count(high_combination) == 1:
            return str(combinations.index(high_combination)+1)

        # if more than 1 player get highest combination
        # it means a tie
        if combinations.count(high_combination) > 1:
            tie_players = [i+1 for i, x in enumerate(
                combinations) if x == high_combination]
            return str(self.tieBreaker(tie_players))

    # draws initial cards and call result function
    def start(self):
        self.setPlayers()
        for _ in range(3):
            for player in self.players:
                self.players[player].append(self.getfromDeck())
        print('Cards drawn...\n')
        for player in self.players:
            self.showHand(player)
        result = self.decision(self.players)
        print("\nplayer " + result + " wins!")

    # show players hand
    def showHand(self, player):
        time.sleep(1)
        print(player, ' : ', self.players[player])


# main function
for _ in range(1):
    print("#################################################################\n")
    g = cardGame()
    g.start()
    print("\n-----------------------------------------------------------------")
