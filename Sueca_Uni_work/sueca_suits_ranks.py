
S = {"C": "Clubs", "D": "Diamonds", "H": "Hearts", "S": "Spades"}

R= {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0,"Q": 2, "J": 3, "K": 4, "7": 10, "A": 11}
class CardInvalid(Exception):
    def __init__(self, card):
        super().__init__(f"Card {card}  is invalid.")
def valid_suit(s):
       if s in S:
            return True
    
def valid_rank(r):
       if r in R:
           return True 
    

def suit_full_name(s):
        if s in S:
            return S[s]
        raise ValueError("Invalid suit symbol")
       
def rank_points(r):
       if r in R:
           R[r]
       else:
           raise ValueError("Invalid rank symbol")
       return R[r]
   
def rank_higher_than(r1, r2):
    if not valid_rank(r1):
            raise ValueError(f"invalid rank symbol {r1}")
    elif not valid_rank(r2):
        raise ValueError(f"invalid rank symbol {r2}")
    elif rank_points(r1) == 0 and rank_points(r2) == 0:
        return int(r1) > int(r2)
    else:
        return rank_points(r1) > rank_points(r2)