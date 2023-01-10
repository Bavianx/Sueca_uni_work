from __future__ import annotations

from typing import Dict, List

from sueca_tricks import parseGameFile

from sueca_tricks import *
from sueca_tricks import Trick


class DealerDoesNotHoldTrumpCard(Exception):
    def __init__(self, card):
        super().__init__(
            f"The dealer has not got the trump card in his hand {card.show()}!"
        )
class AlreadyPlayed(Exception):
    def __init__(self, card: Card):
        super().__init__(f"Card {card.show()} has been played already!")
class IllegalMove(Exception):
    def __init__(self, card: Card):
        super().__init__(
            f"Illegal card ({card.show()}) played. Card isnt the same as the leading suit."
        )


class Game:
    def __init__(self, t_card):
        self.trump_card = t_card
        self.cards_played: Dict[str, List[Card]] = {"1": [], "2": [], "3": [], "4": []}
        lead = {"1": 0, "2": 0, "3": 0, "4": 0}
        self.lead = lead
        self.tricks = []

    def gameTrump(self):
        t_card = self.trump_card
        return t_card

    def score(self):
        p1 = self.lead["1"] + self.lead["3"]
        p2 = self.lead["2"] + self.lead["4"]
        return (p1, p2)

    def playTrick(self, t):
        w = t.trick_winner(self.trump_card.suit)
        p = t.points()
        self.cards_played["1"].append(t.cards[0])
        self.cards_played["2"].append(t.cards[1])
        self.cards_played["3"].append(t.cards[2])
        self.cards_played["4"].append(t.cards[3])
        self.tricks.append(t)
        self.leaderboard[str(w)] += p

    def cardsOf(self, p):
        numbers = [1,2,3,4]
        if p not in numbers:
            raise ValueError("Player number not foud must be between 1 and 4")
        return self.cards_played[str(p)]

    def gameTricks(self):
        trick = self.tricks
        return trick

