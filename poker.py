'''
auther - Rohit Khatana
card Number
1-9, T =10
Suits
C = Clubs
D = Diamonds
H = Hearts
S = Spades

The Rule of poker
0 - Nothing 
1 - Pair(1 pair)
2 - Two Pair(pair of two card)
3 - Three of a Kind(3 cards of same rank(no))
4 - Straight(5 card in sequtional order, suit does not matter)
5 - Flush(5 cards of same suit, rank dont matter)
6 - Full House(3 card of same number, 2 card also of same number)(2C, 2H, 2D,3D, 2D)
7 - Four of a Kind(5H,5C,5J,5S,7H)
8 - Straight Flush(9H,TH,JH,QH,KH)
'''
#max(iteratble_object, key=func)==>good to know

def poker(hands)
    return max(hand, key=hand_rank)

def hand_rank(hand):
    pass

def test():
    "test case for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
