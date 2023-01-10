from sueca_suits_ranks import *
class CardInvalid(Exception):
    def __init__(self, card):
        super().__init__(f"Card {card} is invalid.")
class Card:
    def  __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.Points = rank_points(rank)

       


    def points(self):
        return self.Points
 
    def higher_than(self, other,s,t):
        if self.suit == other.suit:
            return rank_higher_than(self.rank, other.rank)
        if self.suit == t:
            return True
        if other.suit == t:
            return False
        if self.suit == s:
            return True
        if other.suit == s:
            return False
             
        
        
    def show(self):
            return f"{self.rank}{self.suit}"

            

def parseCard(cs):
    if type(cs) != str:
        raise CardInvalid(cs)
    elif len(cs) != 2:
        raise CardInvalid(cs)
    elif not cs.isupper():
        raise CardInvalid(cs)
    rank = cs[0]
    if not valid_rank(rank):
        raise CardInvalid(cs)
    suit = cs[1]
    if not valid_suit(suit):
        raise CardInvalid(cs)
    return Card(rank, suit)
        
