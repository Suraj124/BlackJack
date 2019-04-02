import random

suits=('Hearts','Spades','Diamonds','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','jack','King','Queen','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'King':10,'Queen':10,'Ace':11}

class Card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
class Deck():

    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()

    def __len__(self):
        return len(self.deck)

class Hand():
    
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_cards(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]

        if card.rank=='Ace':
            self.aces+=1
    
    def adjust_for_aces(self):
        if self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1
d=Deck()
d.shuffle()
pulled_card=d.deal()
print(pulled_card)
p1=Hand()
p1.add_cards(pulled_card)
print(p1.value)