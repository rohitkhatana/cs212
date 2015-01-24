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
#find() return -1 when not found <---> index() raise valueError when not found
rank_map = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
def convert_char_to_num(char):
    return int(char)
def substitue_num_to_char(char):
    if char in rank_map:
        return rank_map[char]
    else:
        return char
def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    # ['--23456789TJQKA'.index(r) for r,s in ['6H', 'AH']] peter sir solution
    ranks = [r for r,s in cards]
    ranks = map(substitue_num_to_char, ranks)
    ranks = map(convert_char_to_num, ranks)
            
    ranks.sort(reverse=True)
    return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]

def kind(n, ranks):
    """Return the first rank that this hand has exactky n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    #peter solution
    #using set data structure
    return ranks == list(reversed(range(ranks[4], ranks[4]+5)))

def poker(hands):
    return max(hand, key=hand_rank)

def hand_rank(hand):
    pass

def test():
    "test case for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    
    assert poaer([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
