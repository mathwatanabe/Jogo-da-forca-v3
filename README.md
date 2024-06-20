<h1><b>Jogo-da-forca-v3</b></h1> 

## Objetivo
O objetivo do presente projeto foi o desenvolvimento de um jogo da forca simples com uma espécie de tabuleiro definido e o conceito de Classes Python. O intuito principal do trabalho foi o aprimoramento e aprofundamento na prática de conceitos e técnicas da linguagem Python. Um conceito importante foi a utilização do pacote random e o aprofundamento na construção de funções. Dessa forma, o foco do projeto não foi a construção de um código otimizado, com menor tempo de execução ou simplificação, mas sim para o aperfeiçoamento e desenvolvimento de habilidades e competências referentes à linguagem Python.

## Ferramentas
* Python 3.10.13

## Desenvolvimento
O primeiro passo foi importar a biblioteca <code>random</code> que foi utilizada para selecionar um item aleatório de uma lista que foi definida no decorrer do trabalho e criação de uma função resposável por limpar a tela do programa durante cada nova execução.
```neon
import random
from os import system, name
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
```
Foi definida uma variável para guardar cada um dos estágios do tabuleiro chamado de board no código.
```neon
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

...

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
```
Seguiu-se para a principal parte do projeto, a criação de uma <code>Class</code> capaz de guardar métodos e atributos relacionados ao jogo da forca. A primeira parte foi realizar o método construtor <code>init</code>, definindo alguns atributos da classe <code>Hangman()</code>.
```neon
class Hangman():
    #Método construtor da classe é inicializado
    def __init__(self,palavra):
        self.palavra = palavra
        self.gabarito = []
        self.letras_erradas = []
        #Definição do número fixo de tentativas
        self.tentativas = 7
        self.num = 0
```
Um método para a criação automática de um gabarito, no qual, as letras eram substituídas por '_'.
```neon
class Hangman():
    def gabarit(self):
        self.palavra
        for i in self.palavra:
            self.gabarito.append('_')
        return self.gabarito
```
Outro método foi definido na classe para que quando chamado ele fosse capaz de pedir uma letra ao usuário e verificar se ela se encontrava na palavra. Mais explicações podem ser encontradas em [Jogo-da-forca-v3-notebook.ipynb](https://github.com/mathwatanabe/Jogo-da-forca-v3/blob/main/Jogo-da-forca-v3-notebook.ipynb).
```neon
class Hangman():
    def adivinhar_letra(self):
        #Pedir a inserção de uma letra a ser testada
        letra = input('Insira uma letra: ')
        if letra in self.palavra:
            for i in range(0,len(self.palavra)):
                #Inserir a letra correta no gabarito
                if letra == self.palavra[i]:
                    self.gabarito[i] = letra
        elif letra in self.letras_erradas:
            return
        #Caso a letra estivesse incorreta
        else:
            self.tentativas -= 1
            #Alterando o estado do tabuleiro
            self.num += 1
            self.letras_erradas.append(letra)
            return
```
Para mostrar a situação do tabuleiro para o usuário, o método abaixo foi criado. Nele, a variável "num" define qual situação do tabuleiro.
```neon
class Hangman():    
    def board_print(self):
        print(board[self.num])
        print(' '.join(self.gabarito))
        print(f'Você ainda tem {self.tentativas} tentativas')
        print('Letras erradas:',' '.join(self.letras_erradas))
```
Com todos os métodos e atributos da classe Hangman() criados, foi criada uma função para selecionar aleatoriamente uma palavra de uma lista de frutas definidas.
```neon
def escolher_palavra():
    lista = ['banana','maça','abacaxi','maracuja','morango']
    palavra = random.choice(lista)
    return palavra
```
Com todos os blocos necessários finalizados, o próximo passo foi a construção da ordem que seria executado cada método e função.
```neon
def main():
    game = Hangman(escolher_palavra())
    game.gabarit()
    while not game.status():
        game.board_print()
        game.adivinhar_letra()
    game.won_lose()
    
if __name__ == '__main__':
    main()
```
