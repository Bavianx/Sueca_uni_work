class Cards:
   SUITS = {"C": "Clubs", "D": "Diamonds", "H": "Hearts", "S": "Spades"}

   ranks = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "Q": 2,
        "J": 3,
        "K": 4,
        "7": 10,
        "A": 11
    }


   def valid_suits(suit: str ) -> bool:
        try:
          if suit in Cards.SUITS:
            return True
        except KeyError:
           return False
     

   def valid_rank(rank: int ) -> bool:
        try:
          if rank in Cards.ranks:
            return True
        except KeyError:
           return False
   
   
   def suits_full_name(self, ranks: str, suit: str) -> str:
        try:
            if suit in Cards.ranks:
                return f"{ranks} of {Cards.SUITS[suit]}"
        except KeyError:
            raise KeyError("Invalid suit key provided.")
   def rank_points(self, rank: str):
     try:
            fmt_rank = Cards.ranks[rank]
     except KeyError:
            raise KeyError("Invalid rank key provided.")
     return fmt_rank

   def larger_ranks(self, rank_one: str, rank_two: str):
        fmt_rone = Cards.ranks[rank_one]
        fmt_rtwo = Cards.ranks[rank_two]
        return rank_one if fmt_rone > fmt_rtwo else rank_two




Cards.larger_ranks("3","2","2")