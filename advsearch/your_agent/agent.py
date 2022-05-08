import random
import sys

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

MAX_NUMBER = 10000000000
MIN_NUMBER = -10000000000


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta
    return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])

def decisao_minimax(the_board, color):
    v = valor_max(the_board, color, MIN_NUMBER, MAX_NUMBER)
    return 0

def valor_max(the_board, color, alpha, beta):
    if(teste_corte(the_board)):
        return heuristic_value(1,1)
    
    v = MIN_NUMBER

    for s in sucessores(the_board):
        v = max(v, valor_min(s, alpha, beta))
        alpha = max(alpha, v)
        if(alpha >= beta):
            break
    
    return v

def valor_min(the_board, alpha, beta):
    if(teste_corte(the_board)):
        return heuristic_value(1,1)
    
    v = MAX_NUMBER

    for s in sucessores(the_board):
        v = min(v, valor_max(s, alpha, beta))
        beta = min(beta, v)
        if(beta <= alpha):
            break
    
    return v

def teste_corte():
    return 0

def sucessores(the_board):
    return []

#Coin Parity Heuristic Value =
#	100 * (Max Player Coins - Min Player Coins ) / (Max Player Coins + Min Player Coins)
def coin_parity_value(max_player_coins, min_player_coins):
    return 100 * (max_player_coins - min_player_coins) / (max_player_coins + min_player_coins)


def heuristic_value(max_player_data, min_player_data):
    if(max_player_data + min_player_data != 0):
        return coin_parity_value(max_player_data, min_player_data)
    else:
        return 0


