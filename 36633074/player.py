import random


class Player:

    def __init__(self, name, dealer):
        self.name=name
        self.dealer=dealer
        self.win=0
        self.loss=0
        self.tie=0
        self.hand=[]

    def decide_hit(self):
        # DO NOT MODIFY
        return random.choice([True, True, False])

    def deal_to(self,card_value):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.hand
        [11]
        >>> player.deal_to(10)
        >>> player.hand
        [11, 10]
        """
        self.hand.append(card_value)
        

    @property
    def card_sum(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(2)
        >>> player.card_sum
        2
        >>> player.deal_to(10)
        >>> player.card_sum
        12
        """
        sum1=0
        for i in self.hand:
            sum1+=i
        return sum1    


    def play_round(self):
        """
        >>> from dealer import Dealer
        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> player = Player(None, dealer)

        We see that after the first call the play_round, we have only hit once as dictated by decide_hit
        >>> player.play_round()
        >>> player.hand
        [10]

        After calling play_round again, decide_hit has decided to stand
        >>> player.play_round()
        >>> player.hand
        [10]

        After a third call to play_round, we've decided to hit, but busted!
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]

        After a final call to play_round, our hand shouldn't change since we've already busted
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]
        """
        count=self.decide_hit()
        while count!=False and self.card_sum<21:
            self.dealer.signal_hit(self)#ask the professor
            count=self.decide_hit()

    def discard_hand(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.deal_to(5)
        >>> player.discard_hand()
        >>> player.hand
        []
        """
        self.hand.clear()

    @property
    def wins(self):
        return self.win

    @property
    def ties(self):
        return self.tie

    @property
    def losses(self):
        return self.loss

    def record_win(self):
        """
        >>> player = Player(None, None)
        >>> player.record_win()
        >>> player.wins
        1
        """
        self.win+=1

    def record_loss(self):
        """
        >>> player = Player(None, None)
        >>> player.record_loss()
        >>> player.losses
        1
        """
        self.loss+=1

    def record_tie(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.ties
        1
        """
        self.tie+=1

    def reset_stats(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.record_loss()
        >>> player.record_win()
        >>> player.reset_stats()
        >>> player.ties
        0
        >>> player.wins
        0
        >>> player.losses
        0
        """
        self.tie=0
        self.win=0
        self.loss=0

    def __repr__(self):
        """
        Output should include the player name, their current hand, and their wins/ties/losses in that order
        >>> player = Player("Eric", None)
        >>> player.record_loss()
        >>> player.record_win()
        >>> player.record_win()
        >>> player
        Eric: [] 2/0/1
        """

        return "{}: {} {}/{}/{}".format(self.name,self.hand,self.wins,self.ties,self.losses)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
