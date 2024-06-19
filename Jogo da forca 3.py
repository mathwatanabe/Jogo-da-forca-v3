import random
from os import system, name

def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman():
    def __init__(self,palavra):
        self.palavra = palavra
        self.gabarito = []
        self.letras_erradas = []
        self.tentativas = 7
        self.num = 0

    def gabarit(self):
        self.palavra
        for i in self.palavra:
            self.gabarito.append('_')
        return self.gabarito

    def adivinhar_letra(self):
        letra = input('Insira uma letra: ')
        if letra in self.palavra:
            for i in range(0,len(self.palavra)):
                if letra == self.palavra[i]:
                    self.gabarito[i] = letra
        elif letra in self.letras_erradas:
            return
        else:
            self.tentativas -= 1
            self.num += 1
            self.letras_erradas.append(letra)
            return
    
    def status(self):
        n_jogando = False
        if self.gabarito.count('_') != 0 and self.tentativas != 0:
            pass
        else:
            n_jogando = True
        return n_jogando
    
    def won_lose(self):
        if self.gabarito.count('_') == 0:
            print(f'---------\nVocê ganhou! A resposta era {self.palavra}')
        elif self.tentativas == 0:
            print(f'---------\nVocê perdeu! A resposta era {self.palavra}')
        return
    
    def board_print(self):
        print(board[self.num])
        print(' '.join(self.gabarito))
        print(f'Você ainda tem {self.tentativas} tentativas')
        print('Letras erradas:',' '.join(self.letras_erradas))

def escolher_palavra():
    lista = ['banana','maça','abacaxi','maracuja','morango']
    palavra = random.choice(lista)
    return palavra

def main():
    game = Hangman(escolher_palavra())
    game.gabarit()
    while not game.status():
        game.board_print()
        game.adivinhar_letra()
    game.won_lose()

if __name__ == '__main__':
    main()