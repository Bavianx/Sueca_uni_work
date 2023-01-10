from __future__ import annotations

from typing import List, Optional, Union

from sueca_cards import Card, CardInvalid, parseCard
from sueca_suits_ranks import R, valid_rank, valid_suit


class Trick:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    def points(self):
        return self.cards[0].points()+ self.cards[1].points()+ self.cards[2].points()+ self.cards[3].points()
    

    def trick_winner(self, t):
        p_cards: List[Card] = []
        ls = self.cards[0].suit
        for c in self.cards:
            if c.suit in [ls, t]:
                p_cards.append(c)
        if len(p_cards) == 1:
            return 1
        high_scorer = {"card": None, "position": 0, "score": 0}  
        for x in range(len(p_cards)):
            card = p_cards[x]
            o_cards = p_cards.copy()
            o_cards.remove(card)
            s_value = 0
            for oc in o_cards:
                if card.higher_than(oc, ls, t):
                    s_value += 1
            print(f"{card} + {s_value}")
            if s_value > high_scorer["score"]:
                high_scorer = {"card": card, "position": x + 1, "score": s_value}
        return self.cards.index(high_scorer["card"]) + 1

    def show(self):
        return " ".join([c.show() for c in self.cards])


def parseTrick(ts):
    ts = ts.replace("\n", "")
    c = ts.split()

    if len(c) != 4:
        raise ValueError(ts)
    for card in c:
        if not valid_rank(card[0]):
            raise CardInvalid(ts)
        elif not valid_suit(card[1]):
            raise CardInvalid(ts)
    c = [parseCard(card) for card in c]
    return Trick(c)


def parseGameFile(fname):
    t = None
    trick = []
    with open(fname, "r") as file:
        l = file.readlines()
        t = list(l[0].replace("\n", ""))
        if len(t) != 2:
            raise CardInvalid("".join(t))
        trump_rank, trump_suit = t
        if not valid_rank(trump_rank) :
            raise CardInvalid("".join([trump_rank, trump_suit]))
        elif not valid_suit(trump_suit):
            raise CardInvalid("".join([trump_rank, trump_suit]))
        t = parseCard(f"{trump_rank}{trump_suit}")
        del l[0]
        for tr in l:
            trick.append(parseTrick(tr))
    return [t, trick] 
 