# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
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


# Classe
class Hangman:

	index = 0 #variável para percorrer laços varrendo a palavra alvo
	word_aux = []#variável auxiliar para ser exibida na tela
	index_board = 0 #variável para controlar board
	wrong_attemps = [] #variável para armazenar letras digitadas erradas
	correct_attemps = [] #variável para armazenar letras digitadas corretamente

	# Método Construtor
	def __init__(self, word):
		self.word = word

		#inicializa variável auxiliar para imprimir os _ _ _ _ na tela
		while (self.index < len(word)):
			self.word_aux.append('_')
			self.index = self.index + 1
		
	# Método para adivinhar a letra
	def guess(self, letter):

		#verifica se a letra digitada aparece na palavra alvo
		if(letter in self.word):
			self.index=0
			#preenche a estrutura auxiliar nas posições corretas com a letra digitada corretamente
			while(self.index < len(self.word)):
				if(letter == self.word[self.index]):
					self.word_aux[self.index] = letter
				self.index = self.index + 1
			print("aqui")
			return True
		else:
			return False

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if(''.join(self.word_aux)==self.word or self.index_board == len(board)-1):
			return True
		else:
			return False
		return
		
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if (str(''.join(self.word_aux)) == self.word):
			return True
		elif(self.index_board < len(board)):
			return False
		return
		

	# Método para não mostrar a letra no board
	def hide_word(self, letter, status):
		#Se a letra é um acerto, insere a mesma na estrutura de acertos
		if(status==True):
			self.correct_attemps.append(letter)
		# Se a letra é um erro, insere a mesma na estrutura de erros e incrementa uma posição do board para impressão
		else:
			self.wrong_attemps.append(letter)
			self.index_board = self.index_board + 1
		return
		
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[self.index_board]+"\n")
		print("Palavra: " + ' '.join(self.word_aux) + "\n")
		print("Letras erradas:")
		print(str(self.wrong_attemps).strip('[]')+'\n')
		print("Letras corretas:")
		print(str(self.correct_attemps).strip('[]')+'\n')
		return



# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():
	# Objeto
	game = Hangman(rand_word())
	game.print_game_status()

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	finish = False #variável para verificar final do jogo
	while(finish!=True):
		#leitura da letra fornecida pelo usuário
		letter=''
		#Tratamento para não capturar vazios e nulos
		while(letter == ''):
			letter = str(input("Digite uma letra:\n")).strip()

		# verifica se a letra já foi digitada antes
		if (letter in game.wrong_attemps or letter in game.correct_attemps):
			print("Letra já digitada, tente outra")
		else:
			#inserção da letra na lista correta (acertos ou erros)
			game.hide_word(letter, game.guess(letter))

			#imprime status do jogo
			game.print_game_status()

			#verifica se o jogo acabou
			finish = game.hangman_over()

	# Verifica o status do jogo
	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == '__main__':
	main()
