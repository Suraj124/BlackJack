import random

suits=('Hearts','Spades','Diamonds','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','King','Queen','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'King':10,'Queen':10,'Ace':11}
playing=True

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

class Chips():
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, a bet must be a integer')
        else:
            if chips.bet>chips.total:
                print(f'You don\'t have enough chips. Currently you have {chips.total}')
            else:
                break
def hit(deck,hand):

    hand.add_cards(deck.deal())
    hand.adjust_for_aces()



def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input("Do you wan to hit or stand ? h or s : ")

        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("Player stand and now dealer turn")
            playing=False
        else:
            print("I dont understand, Please enter h or s only!!!")
            continue
        break

def show_some(player,dealer):
    print("Dealer's card")
    print("<One card Hidden>")
    print(dealer.cards[1])
    print(" \n")
    print("Player Cards",*player.cards,sep="\n")
def show_all(player,dealer):
    print("\nDealer's card",*dealer.cards,sep='\n')
    print("\nDealer's value",dealer.value,sep='\n')
    print("\nPlayer's card",*player.cards,sep='\n')
    print("\nPlayer's value",player.value,sep='\n')
def player_busts(chips):
    print("Player BUSTS")
    chips.lose_bet()
def player_win(chips):
    print("Player WIN")
    chips.win_bet()
def dealer_busts(chips):
    print("Delear BUSTS")
    chips.win_bet()
def delear_win(chips):
    print("Player BUSTS")
    chips.lose_bet()
def push():
    print("Player and Delaer Tie")

#Game Start

while True:
    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())

    player_chips=Chips()
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value>21:
            player_busts(player_chips)
            break
    if player_hand.value<21:

        while dealer_hand.value<player_hand.value:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value>21:
            dealer_busts(player_chips)
        elif dealer_hand.value<player_hand.value:
            dealer_busts(player_chips)
        elif dealer_hand.value>player_hand.value:
            delear_win(player_chips)
        else:
            push()
    print(f"Player currently have {player_chips.total}")

    new_game=input("Do you want to play agaian? y/n ? : ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        break



