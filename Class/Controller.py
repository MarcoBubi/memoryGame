import Card
import Player
import Board
import pygame
from pygame.locals import *
import operator
import sys
import os
import random as rand
from collections import Counter

class Controller:

############################## Start of: Main game setup starts! ##########################

	# --Sound setup
	s_dir = os.path.dirname(__file__)
	file_path = os.path.join(s_dir, "../Sound/")
	pygame.mixer.init()
	background_sound = pygame.mixer.Sound(file_path + "sound_background.wav")
	click_sound = pygame.mixer.Sound(file_path + "sound_click.wav")
	correct_sound = pygame.mixer.Sound(file_path + "sound_correct.wav")
	incorrect_sound = pygame.mixer.Sound(file_path + "sound_incorrect.wav")

	pygame.mixer.Sound.set_volume(background_sound, 0.05)
	pygame.mixer.Sound.set_volume(correct_sound, 0.05)
	pygame.mixer.Sound.set_volume(incorrect_sound, 0.05)
	pygame.mixer.Sound.set_volume(click_sound, 0.4)
	pygame.mixer.Sound.play(background_sound, -1)

	# --Board initialization
	board_object = Board.Board(1200, 800)
	pygame.init()
	screen_width = board_object.screen_width
	screen_height = board_object.screen_height
	screen = pygame.display.set_mode((screen_width, screen_height))
	board_object.gameMenu(screen)

############################## End of: Main game setup starts! ############################

	def __init__(self):
	######################################################## Start of: Game initialize!  #########################################################

		self.initializeGamePygame(self.board_object.players_value_number, self.board_object.width_value_number, self.board_object.height_value_number)

	######################################################## End of: Game initialize!  ###########################################################

	def initializeGamePygame(self, number_of_players, board_width, board_height):
		self.board_object.local_number_of_players = self.board_object.players_value_number
		self.screen.fill((0,0,0))

		players_matrix = self.getInputNumberOfPlayers(number_of_players) #Create a number_of_players objects of Players
		board_matrix = self.getCardGameValues(board_width, board_height) #Create a board of cards of (board_width * board_height) size

		players_value_number = self.board_object.players_value_number
		width_value_number = self.board_object.width_value_number
		height_value_number = self.board_object.height_value_number

		self.drawGameBoard(self.screen, board_width, board_height, board_matrix) #Draw the cards on the board.


	############################## Start of: Last parameters before the game starts! ############################

		mouse_x = 0
		mouse_y = 0
		turn = 1
		click_manager = [0, 0, 0] #click_manager = [stage to get number of clicks, first click value, second click value]
		pygame.display.set_caption('Cateia Memory Game')
		on_screen_manager = "It's " + players_matrix[turn - 1].name + "'s turn!"

	############################## End of: Last parameters before the game starts! ##############################


	############################## Start of: Event handling loop! ###############################################

		game_over = False
		while not(game_over):
			for e in pygame.event.get():
				if e.type == QUIT:
					game_over = True
					pygame.quit()
					sys.exit()
				# elif e.type == MOUSEMOTION: --REAL TIME COORDINATE PRINT(CONSOLE)!
				# 	mouse_x, mouse_y = e.pos
				# 	print(mouse_x, mouse_y)
				elif e.type == MOUSEBUTTONUP:
					mouse_x, mouse_y = e.pos
					pygame.mixer.Sound.play(self.click_sound, 0)
					pygame.display.set_caption(('Cateia Memory Game ' + str(mouse_x) + 'x' + str(mouse_y))) # --IN TITLE COORDINATE PRINT

				################ Start of: Menu coordinates mouse registering! ###############################
				
				#Confirm button
				if(mouse_x > self.board_object.menu_button_x_position_1 and mouse_x < (self.board_object.menu_button_x_position_1 + self.board_object.menu_button_big_confirm_width) and mouse_y > self.board_object.menu_button_y_position_4 and mouse_y < (self.board_object.menu_button_y_position_4 + self.board_object.menu_button_height)):
					if(self.board_object.width_value_number > self.board_object.screen_width):
						self.board_object.width_value_number = self.board_object.screen_width
					if(self.board_object.height_value_number > (self.board_object.screen_height / 2)):
						self.board_object.height_value_number = (self.board_object.screen_height / 2)
					self.initializeGamePygame(self.board_object.players_value_number, self.board_object.width_value_number, self.board_object.height_value_number)
				#players_value_number buttons
				#Minus sign logic
				if(mouse_x > self.board_object.menu_button_x_position_1 and mouse_x < (self.board_object.menu_button_x_position_1 + self.board_object.menu_button_width) and mouse_y > self.board_object.menu_button_y_position_1 and mouse_y < (self.board_object.menu_button_y_position_1 + self.board_object.menu_button_height)):
					if(self.board_object.players_value_number == 1):
						self.board_object.players_value_number = 1
					else:
						self.board_object.players_value_number -= 1
				# -- Plus sign logic
				elif(mouse_x > self.board_object.menu_button_x_position_3 and mouse_x < (self.board_object.menu_button_x_position_3 + self.board_object.menu_button_width) and mouse_y > self.board_object.menu_button_y_position_1  and mouse_y < (self.board_object.menu_button_y_position_1 + self.board_object.menu_button_height)):
					self.board_object.players_value_number += 1
				#width_value_number buttons
				# -- Minus sign logic
				if(mouse_x > self.board_object.menu_button_x_position_1 and mouse_x < (self.board_object.menu_button_x_position_1 + self.board_object.menu_button_width) and mouse_y > self.board_object.menu_button_y_position_2 and mouse_y < (self.board_object.menu_button_y_position_2 + self.board_object.menu_button_height)):
					if(self.board_object.width_value_number < 3):
						if(self.board_object.height_value_number == 1):
							self.board_object.height_value_number = 2
						self.board_object.width_value_number = 1
					else:
						self.board_object.width_value_number -= 1
				# -- Plus sign logic
				elif(mouse_x > self.board_object.menu_button_x_position_3 and mouse_x < (self.board_object.menu_button_x_position_3 + self.board_object.menu_button_width) and mouse_y > self.board_object.menu_button_y_position_2 and mouse_y < (self.board_object.menu_button_y_position_2 + self.board_object.menu_button_height)):
					self.board_object.width_value_number += 1
				#height_value_number buttons
				#Minus sign logic
				if(mouse_x > self.board_object.menu_button_x_position_1 and mouse_x < (self.board_object.menu_button_x_position_1 + self.board_object.menu_button_width) and mouse_y > self.board_object.menu_button_y_position_3 and mouse_y < (self.board_object.menu_button_y_position_3 + self.board_object.menu_button_height)):
					if(self.board_object.height_value_number < 3):
						if(self.board_object.width_value_number == 1):
							self.board_object.width_value_number = 2
						self.board_object.height_value_number = 1
					else:
						self.board_object.height_value_number -= 1
				# -- Plus sign logic
				elif(mouse_x > self.board_object.menu_button_x_position_3 and mouse_x < (self.board_object.menu_button_x_position_3 + self.board_object.menu_button_width) and mouse_y > self.board_object.menu_button_y_position_3 and mouse_y < (self.board_object.menu_button_y_position_3 + self.board_object.menu_button_height)):
					self.board_object.height_value_number += 1

			################ End of: Menu coordinates mouse registering! #################################


			################ Start of: Board coordinates mouse registering! ##############################

				if(click_manager[0] == 0): 	# -- FIRST CLICK:
					pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
					first_coordinate_x, first_coordinate_y = self.calculateCoordinateOfCard(mouse_x, mouse_y, width_value_number, height_value_number,
					board_matrix, self.screen_width, self.screen_height)
					click_manager[1] = board_matrix[first_coordinate_x][first_coordinate_y]
					if(first_coordinate_x < 0 or first_coordinate_y < 0):
						click_manager[0] = 0
					elif click_manager[1].is_complete:
						click_manager[0] = 0
					else:
						click_manager[1].startAnimation(first_coordinate_x, first_coordinate_y, board_width, board_height, True)
						click_manager[0] += 1
					mouse_x = 0
					mouse_y = 0
					pygame.event.set_allowed(pygame.MOUSEBUTTONUP)

				elif(click_manager[0] == 1): # -- SECOND CLICK:
					pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
					second_coordinate_x, second_coordinate_y = self.calculateCoordinateOfCard(mouse_x, mouse_y, width_value_number, height_value_number,
					board_matrix, self.screen_width, self.screen_height)
					click_manager[2] = board_matrix[second_coordinate_x][second_coordinate_y]
					if(second_coordinate_x < 0 or second_coordinate_y < 0):
						click_manager[0] = 1
					elif click_manager[1] == click_manager[2]:
						click_manager[0] = 1
					elif click_manager[2].is_complete:
						click_manager[0] = 1
					else:
						click_manager[2].startAnimation(second_coordinate_x, second_coordinate_y, board_width, board_height, True)
						click_manager[0] += 1
					mouse_x = 0
					mouse_y = 0
					pygame.event.set_allowed(pygame.MOUSEBUTTONUP)

				elif(click_manager[0] == 2): # -- THIRD CLICK:
					pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
					if(click_manager[1].value != click_manager[2].value): # -- DIFFERENT CARDS
						pygame.mixer.Sound.play(self.incorrect_sound, 0)
						click_manager[1].startAnimation(first_coordinate_x, first_coordinate_y, board_width, board_height, False)
						click_manager[2].startAnimation(second_coordinate_x, second_coordinate_y, board_width, board_height, False)
						click_manager[1].display = False
						click_manager[2].display = False
						turn +=1
						if(turn == self.board_object.players_value_number + 1):
							turn = 1
						on_screen_manager = "Better luck next time! It's " + players_matrix[turn - 1].name + "'s turn!"
					else: # -- IDENTICAL CARDS
						pygame.mixer.Sound.play(self.correct_sound, 0)
						click_manager[1].is_complete = True
						click_manager[2].is_complete = True
						on_screen_manager = "Good job! It's still " + players_matrix[turn - 1].name + "'s turn!"
						players_matrix[turn - 1].increasePlayerPoints()
					pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
					mouse_x = 0
					mouse_y = 0
					click_manager = [0, 0, 0]

				################ End of: Board coordinates mouse registering! ################################


		#################### Start of: Game UI and mini menu mouse registering! ##############################

			self.board_object.gameUI(players_matrix, turn, on_screen_manager)
			self.board_object.gameMenu(self.screen)

		#################### End of: Game UI and mini menu mouse registering! ################################


		#################### Start of: Win condition and leaderboard display #################################

			if(self.winCondition(board_matrix, height_value_number, width_value_number)): # -- WIN CONDITION
				self.board_object.leaderboardDrawBackground(self.screen)
				self.leaderBoards(players_matrix)
				self.board_object.leaderboardThanksMessage(self.screen)

		#################### Start of: Win condition and leaderboard display #################################

			pygame.display.update()

	############################## End of: Event handling loop! #############################################
	def drawGameBoard(self, screen, h, w, matrix):
		for height in range (0, w):
			for width in range (0, h):
				matrix[height][width].cardDrawOnBoard(screen, width, height, h, w, False)
		if((h * w) % 2 != 0):
			matrix[w - 1][h - 1].cardDrawOnBoard(screen, width, height, h, w, True)
			matrix[w - 1][h - 1].is_complete = True

	def getInputNumberOfPlayers(self, number_of_players):
		player_objects = [Player.Player("Player_" + str(i + 1)) for i in range(int(number_of_players))]
		return player_objects

	def getCardGameValues(self, board_width, board_height):
		max_number_of_cards = board_height * board_width
		singlemax_number_of_cards = []
		max_number_of_cards_was_even = False

		if(max_number_of_cards % 2 != 0):
			max_number_of_cards -= 1
			max_number_of_cards_was_even = True
		for x in range(0, max_number_of_cards):
			singlemax_number_of_cards.append(int((max_number_of_cards - x) % (((board_height * board_width)) / 2)))
		for value in range(0, max_number_of_cards):
			if(singlemax_number_of_cards[value] > self.board_object.number_of_cards):
				singlemax_number_of_cards[value] = singlemax_number_of_cards[value] % self.board_object.number_of_cards
		rand.shuffle(singlemax_number_of_cards)
		if(max_number_of_cards_was_even):
			singlemax_number_of_cards.append(-1)
		board_matrix = self.setValueToEachCard(singlemax_number_of_cards, board_width, board_height)
		return board_matrix

	def setValueToEachCard(self, all_possible_card_values, board_width, board_height):
		board_matrix = [[0 for x in range(board_width)] for y in range(board_height)]
		iterator = 0

		for h in range(0, board_height):
			for w in range(0, board_width):
				board_matrix[h][w] = Card.Card(all_possible_card_values[iterator])
				iterator += 1
		return board_matrix

	def calculateCoordinateOfCard(self, mouse_x, mouse_y, board_width, board_height, board_matrix, screen_width, screen_height):
		coordinate_in_range = 1
		x_coordinate = int((mouse_x / (screen_width / board_width)))
		y_coordinate = int((mouse_y - 199) / ((screen_height - 400) / board_height))

		if(x_coordinate > board_width or x_coordinate == board_width or y_coordinate > board_height or y_coordinate == board_height):
			coordinate_in_range = -1
		elif(x_coordinate < 0 or y_coordinate < 0):
			coordinate_in_range = -1
		if(coordinate_in_range != -1):
			if(board_matrix[y_coordinate][x_coordinate].is_complete == False):
				board_matrix[y_coordinate][x_coordinate].display = True
			return y_coordinate, x_coordinate
		return -1, -1

	def winCondition(self, board_matrix, board_width, board_height):
		condition = [[False for x in range(board_height)] for y in range(board_width)]

		for h in range(0, board_width):
			for w in range(0, board_height):
				condition[h][w] = board_matrix[h][w].is_complete
				if not(condition[h][w]):
					return False
		return True

	def leaderBoards(self, players_matrix):
		players_dict = dict([(player.name, player.returnPlayerPoints()) for player in players_matrix])
		players_dict_sorted = sorted(players_dict.items(), key = operator.itemgetter(1), reverse = True)
		winners = 0
		iterator = 0

		for x in range (1, len(players_dict_sorted)):
			if(players_dict_sorted[0][1] == players_dict_sorted[x][1]):
				winners += 1
		for key, value in players_dict_sorted:
			if(iterator < winners + 1):
				more_winners = True
			else:
				more_winners = False
			self.board_object.leaderboardDrawPosition(iterator, key, value, more_winners)
			iterator += 1


