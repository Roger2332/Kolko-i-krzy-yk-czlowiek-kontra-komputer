X= "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQARES = 9
def displey_instrukcion():
    """Wyswietl instrukcje gry"""
    print(
    """
    Witaj w najwiekszym intelektualnym wyzwaniu wszech czasow, jakim jest gra 'kolko i krzyzyk'
    Bedzie to ostateczna rozgrywka pomiedzy Twojim mozgiem a moim krzemowym procesorem.
    
    swoje posuniecia wskazesz poprzez wprowadzenie liczby 0-8. 
    liczby te odpowiadaja pozycji na planszy zgodnie z ponizszym schematem 
    
            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8
            
    Przygotuj sie czlowieku, ostateczny batalion juz niebawem.\n
    """)

def ask_yes_no(guestion):
    """Zadaj pytanie na ktore mozna odpowiedziec tak lub nie."""
    response = None
    while response not in ("n", "t"):
        response = input(guestion).lower()
    return response



def ask_number(question, low, hight):
    """Popros o podanie numeru z odpowiedniego zakresu"""
    response = None
    try:
        while response not in range(low, hight):
            response = int(input(question))
    except ValueError:
        print("podana bledna wartosc")
    return response


def pieces():
    """Ustal czy pierwszy ruch nalezy do gracza czy do komputera"""
    go_first = ask_yes_no("Czy chcesz miec prawo do 1 ruchu: (t/n): ")
    if go_first == "t":
        print("Wiec wykonujesz 1 ruch")
        human = O
        computer = X
    else:
        print("Twoja odwaga cie zgubi, ja wykonuje 1 ruch")
        human = X
        computer = O
    return human,  computer


def new_bord():
    """Utworz nowa plansze gry"""
    bord = []
    for i in range(NUM_SQARES):
        bord.append(EMPTY)
    return bord

def display(bord):
    """Wyswietl plansze gry na ekranie"""
    print(f"\n\t{bord[0]}|{bord[1]}|{bord[2]} ")
    print("\t---------")
    print(f"\t{bord[3]}|{bord[4]}|{bord[5]} ")
    print("\t---------")
    print(f"\t{bord[6]}|{bord[7]}|{bord[8]}\n ")

def legal_move(bord):
    """Utworz liste prawidlowych rochow"""
    move = []
    for i in range(NUM_SQARES):
        if bord[i] == EMPTY:
            move.append(i)
    return move

def winer(bord):
    """Ustal zwyciezce"""
    WAY_TO_WIN = ((0,1,2),
                  (3, 4, 5),
                  (6,7,8),
                  (0,3,6),
                  (1,4,7),
                  (2,5,8),
                  (2,4,8),
                  (2,4,6))
    for row in WAY_TO_WIN:
        if bord[row[0]] == bord[row[1]] == bord[row[2]] != EMPTY:
            winer = bord[row[0]]
            return winer
        if EMPTY not in bord:
            return TIE
    return None

def human_move(bord, human):
    legal = legal_move(bord)
    move = None
    while move not in legal:
        move = ask_number("Jaki bedzie twoj ruch? ", 0, NUM_SQARES)
        if move not in legal:
            print("to pole jest juz zajene niemondru czlowieku.")
    print("Znakomicie")
    return move

def computer_move(board, computer, human):
    """Spowoduje wykonanie ruchu przez komputer"""
    board = board[:]
    BEST_MOVE = (4,0,2,6,8,1,3,5,7)
    print("Wybieram pole nr", end=" ")
    for move in legal_move(board):
        board[move] = computer
        if winer(board) == computer:
            print(move)
            return move
        #Ten ruchh zostal sprawdzony, wycofaj go
        board[move] = EMPTY
        #Jesli czlowiek moze wygrac, wykonaj ten ruch
    for move in legal_move(board):
        board[move] =human
        if winer(board) == human:
            print(move)
            return move
            #Ten ruch zostal sprrawdzony, wycofaj go
        board[move] =EMPTY
            #Jesli nikt nie jest wstanie wygrac, wykonaj najlepszy ruch
        for move in BEST_MOVE:
            if move in legal_move(board):
                print(move)
                return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congret_winer(the_winner, computer, human):
    """Pogratuluj zwyciezcy"""
    if the_winner != TIE:
        print(f"{the_winner} jest zywciezca")
    else:
        print("remis")
    if the_winner == human:
        print("No, nie. To nie mozliwe, Jakos udalo ci sie mnie zwiec czlowieku.\n"
              "Ale  to sie nigdy wiecej nie powtorzy, ja komputer przyzekam ci to")
    elif the_winner == computer:
        print("Jak przewidywalem czlowieku, jeszcze raz zostalem trumfem, \n"
              "Dowod na to zre komputer przewyzszaja ludzi pok kazdym wzgledem")
    else:
        print("Miales mnostwo szczescia, Czlowieku, i jakos udalo ci sie ze mna zremisowac.\n"
              "Swietuj ten dzien,,, bo to najlepszy wynik jaki mozesz kiedykolwiek osiagnac")

def main():
    displey_instrukcion()
    computer, human =pieces()
    turn =  X
    board = new_bord()
    display(board)
    while not winer(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board,computer,human)
            board[move] = computer
        display(board)
        turn = next_turn(turn)
    the_winner = winer(board)
    congret_winer(the_winner, computer, human)

main()
