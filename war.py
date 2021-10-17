from random import shuffle

print('Welcome To A Simulation Of The Game Of War')

# ------------------------------------------------------------------------------------------------------------------------ #

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11,
          'Queen': 12, 'King': 13, 'Ace': 14}

# ------------------------------------------------------------------------------------------------------------------------ #

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    def shuffle_deck(self):
        shuffle(self.all_cards)
    
    def deal_one_card(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} card(s)'
    
    def remove_one_card(self):
        return self.hand.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.hand += new_cards
        else:
            self.hand.append(new_cards)

# ------------------------------------------------------------------------------------------------------------------------ #

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle_deck()

for card_object in range(26):
    player_one.add_cards(new_deck.deal_one_card())
    player_two.add_cards(new_deck.deal_one_card())

# ------------------------------------------------------------------------------------------------------------------------ #

game_on = True

round_count = 0

while game_on:
    round_count += 1
    print(f'Round {round_count}: Fight!')
    
    if len(player_one.hand) == 0:
        print(f'Player {player_one.name}, you are out of cards! You lose!')
        print(f'Player {player_two.name}, you are the winner! Congratulations!')
        game_on = False
        break
    
    if len(player_two.hand) == 0:
        print(f'Player {player_two.name}, you are out of cards! You lose!\n')
        print(f'Player {player_one.name}, you are the winner! Congratulations!')
        game_on= False
        break
    
    player_one_in_game_cards = []
    player_one_in_game_cards.append(player_one.remove_one_card())
    
    player_two_in_game_cards = []
    player_two_in_game_cards.append(player_two.remove_one_card())
    
    at_war = True
    
    while at_war:
        if player_one_in_game_cards[-1].value > player_two_in_game_cards[-1].value:
            player_one.add_cards(player_two_in_game_cards)
            player_one.add_cards(player_one_in_game_cards)
            at_war = False
        elif player_one_in_game_cards[-1].value < player_two_in_game_cards[-1].value:
            player_two.add_cards(player_two_in_game_cards)
            player_two.add_cards(player_one_in_game_cards)
            at_war = False
        else:
            print('War mode activated! Fight to the death!')
            if len(player_one.hand) < 5:
                print(f'Monstrosity! How and/or why do you not have enough cards in your arsenal to go to war player {player_one.name}?!')
                print(f'Player {player_one.name}, you ... lose. Congratulations Player {player_two.name}')
                game_on = False
                break
            elif len(player_two.hand) < 5:
                print(f'Monstrosity! How and/or why do you not have enough cards in your arsenal to go to war player {player_two.name}?!')
                print(f'Player {player_two.name}, you ... lose. Congratulations Player {player_one.name}')
                game_on = False
                break
            else:
                for card_going_war in range(5):
                    player_one_in_game_cards.append(player_one.remove_one_card())
                    player_two_in_game_cards.append(player_two.remove_one_card())