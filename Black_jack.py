import random
import os
import time       
def menu():
     print("                ♠   ♣️   BLACKJAK  ♥️  ♦️ ")
     
     print(r"""
_______________________¶¶¶¶___¶¶¶¶¶
_____________________¶¶____¶¶¶____¶¶__¶¶¶
___________________¶¶___¶¶¶____¶¶¶¶¶¶¶___¶¶
_________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
______________¶¶¶¶¶__¶__________________________¶¶
___________¶¶¶¶__¶¶__¶___________________________¶
_________¶¶¶_¶¶__¶__¶¶¶__________________________¶
______¶¶¶_¶¶_¶¶¶_¶_¶¶_¶¶_________¶_______________¶
_____¶_¶¶__¶_¶_¶¶¶¶_¶¶¶__________¶¶______________¶
___¶¶¶_¶¶¶¶¶_¶¶¶¶¶¶_¶¶¶_________¶¶¶______________¶
_¶¶__¶¶¶¶¶¶¶¶_¶¶_¶¶____________¶¶¶¶¶_____________¶
¶_¶¶__¶__¶¶¶¶____¶¶___________¶¶¶¶¶¶¶____________¶
¶__¶¶¶¶¶¶¶¶¶¶____¶¶__________¶¶¶¶¶¶¶¶¶¶__________¶
_¶¶¶_¶_¶¶___¶¶___¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶
__¶¶_¶¶_¶___¶¶___¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶
___¶¶____¶___¶___¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶
____¶¶___¶¶__¶¶__¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶
_____¶¶___¶__¶¶__¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶
______¶¶___¶__¶__¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶
_______¶¶__¶¶_¶__¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶
________¶¶__¶_¶¶_¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶
_________¶¶__¶_¶_¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶
__________¶¶_¶¶¶_¶¶___¶¶¶¶¶¶¶¶¶__¶¶__¶¶¶¶¶¶¶¶¶___¶
____________¶_¶¶_¶¶_____¶¶¶¶¶____¶¶____¶¶¶¶¶_____¶
_____________¶_¶¶¶¶___________¶¶¶¶¶¶¶¶___________¶
______________¶¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶______¶¶__¶
_______________¶¶¶____________¶¶¶¶¶¶¶¶_______¶¶¶_¶
________________¶¶__________________________¶¶_¶_¶
_________________¶¶__________________________¶¶__¶
_________________¶¶__________________________¶¶¶_¶
__________________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__________________¶¶¶¶¶¶¶¶¶¶¶¶
_____________________¶¶¶¶¶¶
           """)
CARDS ={"A":''' 
 -------
|A      |
|       |
|       |
|       |
|      A|
 ------- ''',"2": '''
 -------
|2      |
|       |
|       |
|       |
|      2|
 ------- ''',"3":
 '''
 -------
|3      |
|       |
|       |
|       |
|      3|
 ------- ''', "4":'''
 -------
|4      |
|       |
|       |
|       |
|      4|
 ------- ''',"5":'''
 -------
|5      |
|       |
|       |
|       |
|      5|
 ------- ''',"6":  '''
 -------
|6      |
|       |
|       |
|       |
|      6|
 ------- ''',"7":'''
 -------
|7      |
|       |
|       |
|       |
|      7|
 ------- ''', "8":'''
 -------
|8      |
|       |
|       |
|       |
|      8|
 ------- ''', "9": '''
 -------
|9      |
|       |
|       |
|       |
|      9|
 ------- ''', "10": '''
 -------
|10     |
|       |
|       |
|       |
|     10|
 ------- ''',"J": ''' 
 -------
|J      |
|       |
|       |
|       |
|      J|
 ------- ''',"Q":'''
 -------
|Q      |
|       |
|       |
|       |
|      Q|
 ------- ''',"K":'''
 -------
|K      |
|       |
|       |
|       |
|      K|
 ------- ''',"BLANKCARD": '''
 -------
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
 ------- '''
}

card_values = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}
cards = ["2", "3", "4", "5","6", "7", "8", "9", "10", "J", "Q", "K","A"]
def cls():
    os.system("cls"if os.name=="nt" else"clear")
def add_card(player):
    onecard=cards.pop()
    player.append(card_values[onecard])
    return onecard
def print_card(hand,player):
 print(f'{player}')
 card_line=[]
 for line in hand:
                lines=CARDS[line].split("\n")
                card_line.append(lines)
 for line_indx in range(len(card_line[0])):
         for i in card_line:
            print(i[line_indx],end="     ")
         print()
def shuffle():
     random.shuffle(cards)
     for _ in range(2):
      player_hand.append(cards.pop())
      dealer_hand.append(cards.pop())   
     for i in player_hand:
       total_palyer.append(card_values[i])
     for i in dealer_hand:
       total_dealer.append(card_values[i]) 
def adjust_ace(hand):
    while 11 in hand and sum(hand) > 21:
        index = hand.index(11)
        hand[index] = 1
resullt=False
player_hand=[]
dealer_hand=[]
total_palyer=[]
total_dealer=[]
blind_card=["BLANKCARD"]
resullt=False
def check_direct_win():
    global resullt
    if sum(total_dealer)==21 and sum(total_palyer)==21:
     cls()
     print_card(player_hand,"your cards")         
     print_card(dealer_hand,"deler cards")
     print("Push")
     resullt=True
    elif sum(total_palyer)==21:
     cls()
     print("you win....")
     print_card(player_hand,"your cards")         
     print_card(dealer_hand,"deler cards")
     resullt=True
    elif sum (total_palyer)>21:
     cls()
     print("You busted! Dealer wins.")
     print_card(player_hand,"your cards")         
     print_card(dealer_hand,"deler cards")
     resullt=True
def player_turn():
    global resullt
    ask=input('Hit OR Stand y/n: ').strip()
    if ask.strip()=="y":
               resullt=False
    while ask=="y" and sum(total_palyer)<21:
                time.sleep(1.3)
                cls()            
                player_hand.append(add_card(total_palyer)) 
                print(player_hand)
                print_card(player_hand,"your cards")
                print_card(blind_card,"deler cards")
                adjust_ace(total_palyer)
                if sum(total_palyer)==21:
                    break
                elif  sum(total_palyer)>21:
                    cls()
                    print_card(player_hand,"your cards")         
                    print_card(dealer_hand,"deler cards")
                    print("You busted! Dealer wins.")
                    resullt=True
                    break
                else:
                    ask=input('Hit OR Stand y/n: ').strip()
def dealer_turn():
    global resullt
    print("dealar turn.....")
    time.sleep(1)        
    while sum(total_dealer)<17:
                    dealer_hand.append(add_card(total_dealer)) 
                    adjust_ace(total_dealer)
                    time.sleep(1) 
                    cls()
                    print_card(player_hand,"your cards")         
                    print_card(dealer_hand,"deler cards")
                    print(total_dealer)
                    if sum(total_dealer)>21:
                        time.sleep(1)
                        cls()
                        print_card(player_hand,"your cards")         
                        print_card(dealer_hand,"deler cards")
                        print("you win....")
                        resullt=True
                        break
def final_result():
    if sum (total_dealer)==sum (total_palyer):
        time.sleep(1)
        cls()
        print_card(player_hand,"your cards")         
        print_card(dealer_hand,"deler cards")
        print("Push")
    elif sum (total_palyer)>sum(total_dealer):
        time.sleep(1)
        cls()
        print_card(player_hand,"your cards")         
        print_card(dealer_hand,"deler cards")
        print("you win....")
    else:
        time.sleep(1)
        cls()
        print_card(player_hand,"your cards")         
        print_card(dealer_hand,"deler cards")
        print('You busted! Dealer wins.')
def main():
    menu()
    shuffle()
    blind_card=[dealer_hand[0], "BLANKCARD"]
    time.sleep(1)
    cls()
    print_card(player_hand,"your cards")
    print_card(blind_card,"deler cards")
    check_direct_win()
    if resullt:
        return
    player_turn()
    if resullt:
        return
    dealer_turn()
    if resullt:
        return
    final_result()
while True:
    player_hand.clear()
    dealer_hand.clear()
    total_palyer.clear()
    total_dealer.clear()
    resullt = False
    cards = ["2", "3", "4", "5","6", "7", "8", "9", "10", "J", "Q", "K","A"]
    
    time.sleep(1)
    main()
    if (input ("play again? y/n : "))!="y":
     break
    
