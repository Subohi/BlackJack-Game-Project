from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        self.dealer=Dealer()
        self.player_list=[]
        for i in player_names:
            playerobject=Player(i,self.dealer)
            self.player_list.append(playerobject)    

        

    def play_rounds(self, num_rounds=1):#15 POINTS 
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """
        string1=''
        for rounds in range(num_rounds):
            self.dealer.shuffle_deck()
            for i in range(0,2):# FIRST TWO ROUNDS
                for j in self.player_list:
                    self.dealer.signal_hit(j)
                self.dealer.signal_hit(self.dealer)


            if self.dealer.card_sum==21: #IF DEALER HAS 21 AS SUM AFTER FIRST TWO ROUNDS
                string1+='Round '+str(rounds+1)+'\n'
                string1+=str(self.dealer)+'\n' 
                for c in self.player_list:
                    if c.card_sum==21:
                        c.record_tie()
                    elif c.card_sum<21:
                        c.record_loss()
                    string1+=str(c)+'\n'
                    c.discard_hand() 

            elif self.dealer.card_sum!=21:# IF DEALER DOESNOT HAVE SUM AS 21 AFTER TWO ROUNDS                                    
                for x in self.player_list:
                    x.play_round()
                self.dealer.play_round()
                string1+='Round '+str(rounds+1)+'\n'   
                string1+=str(self.dealer)+'\n'
                
                for players in self.player_list:
                    if self.dealer.card_sum<=21:#IF DEALER HAS SUM LESS THAN OR EQUAL TO 21 AFTER PLAYING 
                        if players.card_sum>self.dealer.card_sum and players.card_sum<=21:
                            players.record_win()
                        elif players.card_sum==self.dealer.card_sum and players.card_sum<=21:
                            players.record_tie()
                        elif players.card_sum<self.dealer.card_sum or players.card_sum>21:
                            players.record_loss()
                    elif self.dealer.card_sum>21:#IF DEALER HAS SUM GREATER THAN 21 AFTER PLAYING 
                        if players.card_sum<=21:
                            players.record_win()
                        else:
                            players.record_loss()            
                    string1+=str(players)+'\n'
                    players.discard_hand()
                self.dealer.discard_hand()    
            

        string1=string1.rstrip()        
        return string1    

        

    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """
        for play in self.player_list:
            play.reset_stats()
        self.dealer.hand=[]    


if __name__ == "__main__":
    import doctest
    doctest.testmod()
