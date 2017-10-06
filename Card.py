import random

class Card(object):
    def __init__(self, suit, cFace, value):
        self.suit = suit
        self.cFace = cFace
        self.value = value


    def getCardValue(self): #returns a numerical value based on cardFace value (mostly for the royalty)
        if isinstance(self.cFace, str):
            if(self.cFace == "Jack"):
                return 11
            elif(self.cFace == "Queen"):
                return 12
            elif(self.cFace == "King"):
                return 13
            elif(self.cFace == "Ace"):
                return 14
        else:
            return self.cFace

    def display(self):
        print "{} of {}".format(self.cFace, self.suit)
        return self

    

class Deck(object):
    def __init__(self):
        self.thisDeck = {}

    def newDeck(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        cFaces = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

        value = 0
        for suit in suits:
            for number in cFaces:
                if(number == "Jack"):
                    value = 11
                elif(number == "Queen"):
                    value = 12
                elif(number == "King"):
                    value = 13
                elif(number == "Ace"):
                    value = 14
                else:
                    value = number

                newCard = Card(suit, number, value)
        return self

    def display(self):
        string = ""
        for key in self.thisDeck:
            string += key + ": "
            for card in self.thisDeck[key]:
                string += str(card) + ", "
            string += "\n"
        print string
        return self

    def removeCard(self, card):
        self.thisDeck[card.suit].remove(card.cFace)
        return self

# class Hand(object):
#     def __init__(self):
#         self.thisHand = []

#     def drawCard(self):
#         pass

card1 = Card("Hearts", 3)
card2 = Card("Spades", "Ace")
deck1 = Deck().newDeck()
card1.display()
card2.display()
deck1.removeCard(card1).removeCard(card2).display()