from pygame import *

class Board:
	# General screen setup
	screen_width = 1200
	screen_height = 800
	margin_x = 2
	margin_y = 200
	# General board setup
	players_value_number = 4
	width_value_number = 400
	height_value_number = 100
	if(width_value_number > screen_width):
		width_value_number = screen_width
	if(height_value_number > (screen_height / 2)):
		height_value_number = (screen_height / 2)
	# Tmp game setup
	local_number_of_players = players_value_number
	local_width_value_number = width_value_number
	local_height_value_number = height_value_number
	# Pygame setup
	font.init()
	UI_font = font.SysFont('Arial', 15)
	my_font = font.SysFont('Arial', 15)
	screen = display.set_mode((screen_width, screen_height))
	animation_timer = time.Clock()
	# Card setup
	local_card_offset_dist = 5
	number_of_cards = 52
	card_background = image.load("Artwork/card_background.jpg")
	# Mini menu setup                               - On 1200x800 screen(default) setup values:
	menu_x_position = (screen_width / 2) - (200 / 2) 	#500
	menu_y_position = (screen_height - 130) 			#670
	menu_width = 200
	menu_height = 130
	# Mini menu buttons
	menu_button_big_confirm_width = 100
	menu_text_name_width = 70
	menu_text_name_x_position = menu_x_position + 22
	menu_text_name_x_position_2 = menu_x_position + 12
	menu_text_name_y_position_1 = menu_y_position + 10
	menu_text_name_y_position_2 = menu_y_position + 40
	menu_text_name_y_position_3 = menu_y_position + 70
	menu_button_width = 20
	menu_button_height = 20

	menu_button_x_position_1 = menu_x_position + 80  # 580
	menu_button_x_position_2 = menu_x_position + 110 # 610
	menu_button_x_position_3 = menu_x_position + 160 # 660

	menu_button_y_position_1 = menu_y_position + 10  # 680
	menu_button_y_position_2 = menu_y_position + 40  # 710
	menu_button_y_position_3 = menu_y_position + 70  # 740
	menu_button_y_position_4 = menu_y_position + 100 # 770

	def __init__(self, screen_width, screen_height):
		self.screen_width = screen_width
		self.screen_height = screen_height

	def gameMenu(self, screen):
		screen_width = self.screen_width
		screen_height = self.screen_height

		my_font = self.UI_font
		players_value_number = self.players_value_number
		width_value_number = self.width_value_number
		height_value_number = self.height_value_number

		# Mini menu location
		self.drawElementInMenu(screen, self.menu_x_position, self.menu_y_position, self.menu_width + 4, self.menu_height + 4, "", (255, 255, 255), (255, 255, 255), -1, -1)
		self.drawElementInMenu(screen, self.menu_x_position + 2, self.menu_y_position + 2, self.menu_width, self.menu_height, "", (0, 0, 0), (0, 0, 0), -1, -1)

		# Text in the Menu ("Players:", "Width:", "Height")
		self.drawElementInMenu(screen, self.menu_text_name_x_position, self.menu_text_name_y_position_1, self.menu_text_name_width, self.menu_button_height, "Players: ", (0, 0, 0), (0, 255, 0), self.menu_text_name_x_position_2, self.menu_text_name_y_position_1 + 2)
		self.drawElementInMenu(screen, self.menu_text_name_x_position, self.menu_text_name_y_position_2, self.menu_text_name_width, self.menu_button_height, "Rows: ", (0, 0, 0), (0, 255, 0), self.menu_text_name_x_position_2, self.menu_text_name_y_position_2 + 2)
		self.drawElementInMenu(screen, self.menu_text_name_x_position, self.menu_text_name_y_position_3, self.menu_text_name_width, self.menu_button_height, "Columns: ", (0, 0, 0), (0, 255, 0), self.menu_text_name_x_position_2, self.menu_text_name_y_position_3 + 2)

		# Minus blocks for every text
		self.drawElementInMenu(screen, self.menu_button_x_position_1, self.menu_button_y_position_1, self.menu_button_width, self.menu_button_height, "-", (255, 255, 255), (0, 0, 0), self.menu_button_x_position_1 + (self.menu_button_width / 4), self.menu_button_y_position_1 + 2)
		self.drawElementInMenu(screen, self.menu_button_x_position_1, self.menu_button_y_position_2, self.menu_button_width, self.menu_button_height, "-", (255, 255, 255), (0, 0, 0), self.menu_button_x_position_1 + (self.menu_button_width / 4), self.menu_button_y_position_2 + 2)
		self.drawElementInMenu(screen, self.menu_button_x_position_1, self.menu_button_y_position_3, self.menu_button_width, self.menu_button_height, "-", (255, 255, 255), (0, 0, 0), self.menu_button_x_position_1 + (self.menu_button_width / 4), self.menu_button_y_position_3 + 2)

		# Value blocks for every text
		self.drawElementInMenu(screen, self.menu_button_x_position_2, self.menu_button_y_position_1, (self.menu_button_width * 2), self.menu_button_height, str(players_value_number), (255, 255, 255), (0, 0, 0), self.menu_button_x_position_2 + (self.menu_button_width / 4), self.menu_button_y_position_1 + 2)
		self.drawElementInMenu(screen, self.menu_button_x_position_2, self.menu_button_y_position_2, (self.menu_button_width * 2), self.menu_button_height, str(width_value_number), (255, 255, 255), (0, 0, 0), self.menu_button_x_position_2 + (self.menu_button_width / 4), self.menu_button_y_position_2 + 2)
		self.drawElementInMenu(screen, self.menu_button_x_position_2, self.menu_button_y_position_3, (self.menu_button_width * 2), self.menu_button_height, str(height_value_number), (255, 255, 255), (0, 0, 0), self.menu_button_x_position_2 + (self.menu_button_width / 4), self.menu_button_y_position_3 + 2)

		# Plus blocks for every text
		self.drawElementInMenu(screen, self.menu_button_x_position_3, self.menu_button_y_position_1, self.menu_button_width, self.menu_button_height, "+", (255, 255, 255), (0, 0, 0), self.menu_button_x_position_3 + (self.menu_button_width / 4), self.menu_button_y_position_1 + 2)
		self.drawElementInMenu(screen, self.menu_button_x_position_3, self.menu_button_y_position_2, self.menu_button_width, self.menu_button_height, "+", (255, 255, 255), (0, 0, 0), self.menu_button_x_position_3 + (self.menu_button_width / 4), self.menu_button_y_position_2 + 2)
		self.drawElementInMenu(screen, self.menu_button_x_position_3, self.menu_button_y_position_3, self.menu_button_width, self.menu_button_height, "+", (255, 255, 255), (0, 0, 0), self.menu_button_x_position_3 + (self.menu_button_width / 4), self.menu_button_y_position_3 + 2)

		#Confirm button
		self.drawElementInMenu(screen, self.menu_button_x_position_1, self.menu_button_y_position_4, self.menu_button_big_confirm_width , self.menu_button_height, "Confirm", (255, 255, 255), (0, 0, 0), self.menu_button_x_position_1 + (self.menu_button_big_confirm_width / 4), self.menu_button_y_position_4 + 2)

	def drawElementInMenu(self, screen, x_position, y_position, width, height, text, rect_color, text_color, text_x_position, text_y_position):
		draw.rect(screen, rect_color, (x_position, y_position, width, height))
		text_display = self.my_font.render(text, True, text_color)
		screen.blit(text_display, (text_x_position, text_y_position))

	def gameUI(self, players_matrix, turn, on_screen_manager):
		my_font = self.my_font
		list_of_players_on_screen = []

		for iterator_through_players_on_screen in range(0, self.local_number_of_players + 1):
			self.drawElementInMenu(self.screen, iterator_through_players_on_screen * 110, 0, 122, 52, "", (255, 255, 255), (255, 255, 255), -1, -1) # white stripe around border of first line
			self.drawElementInMenu(self.screen, iterator_through_players_on_screen * 110, 0, 120, 50, "", (0, 0, 0), (0, 0, 0), -1, -1) # black box to hide the text
			#draw.rect(self.screen, (0, 0, 0), (iterator_through_players_on_screen * 110, 0, 120, 50))
		self.drawPlayerListOnScreen(list_of_players_on_screen, players_matrix)
		self.drawElementInMenu(self.screen, 0, 0, 0, 0, "List of players: ", (0, 0, 0), (111, 255, 111), 5, 20)

		#Current player : Player and the text under it about solving the board!
		self.drawElementInMenu(self.screen, 0, 98, 300, 70, "", (255, 255, 255), (255, 255, 255), -1, -1) # white stripe around border of first line
		self.drawElementInMenu(self.screen, 0, 100, 298, 66, "", (0, 0, 0), (0, 0, 0), -1, -1)

		self.drawElementInMenu(self.screen, 0, 0, 0, 0, "Current player: ", (0, 0, 0), (111, 255, 111), 5, 105)
		self.drawElementInMenu(self.screen, 0, 0, 0, 0, players_matrix[turn - 1].name, (0, 0, 0), (255, 255, 0), 120, 105)
		self.drawElementInMenu(self.screen, 0, 0, 0, 0, on_screen_manager, (0, 0, 0), (111, 255, 111), 5, 135)

	def drawPlayerListOnScreen(self, list_of_players_on_screen, players_matrix):
		for iterator_through_players_on_screen in range(0, self.local_number_of_players):
			list_of_players_on_screen.append(self.my_font.render(players_matrix[iterator_through_players_on_screen].name, True, (255, 255, 0)))
		if(self.local_number_of_players < 11):
			for iterator_through_players_on_screen in range(0, self.local_number_of_players):
				self.screen.blit(list_of_players_on_screen[iterator_through_players_on_screen], ((iterator_through_players_on_screen + 1) * 110, 20))
		else:
			iterator_through_players_on_screen = 0
			first_line = self.my_font.render("...", True, (255,255, 0))
			self.screen.blit(first_line, ((iterator_through_players_on_screen+1) * 140, 20))
			for iterator_through_players_on_screen in range(0, 9):
				self.screen.blit(list_of_players_on_screen[(self.local_number_of_players - 9) + iterator_through_players_on_screen], ((iterator_through_players_on_screen + 2) * 110, 20))

	def leaderboardDrawPosition(self, print_position, winner, points, more_winners):
		if(print_position < 11):
			if(more_winners):
				winner = self.my_font.render("1) " + str(winner) + " - " + str(points) + " points!", True, (255, 255, 0))
			elif not(more_winners):
				winner = self.my_font.render(str(print_position + 1) + ") " + str(winner) + " - " + str(points) + " points!", True, (111, 255, 111))
		elif(print_position == 11):
			winner = self.my_font.render("... and more", True, (255, 255, 0))
			self.screen.blit(winner, (((self.screen_width / 2) - 20), ((self.margin_y * 1.2) + print_position * 30)))
			return
		else:
			return
		self.screen.blit(winner, (((self.screen_width / 2) - 60), ((self.margin_y * 1.2) + print_position * 30)))

	def leaderboardDrawBackground(self, screen):
		my_font = font.SysFont('Arial', 25)
		draw.rect(self.screen, (255, 255, 255), (0, 98, 1200, 554))
		draw.rect(self.screen, (0, 0, 0), (2, 100, 1196, 550))
		# Don't want to call this function through the drawElementInMenu() function because I want my specified font for this.
		leaderboard_text = my_font.render("Leaderboard:", True, (111, 255, 111))
		self.screen.blit(leaderboard_text, (((self.screen_width / 2) - 65), ((self.margin_y))))

	def leaderboardThanksMessage(self, screen):
		text_to_display = "Thank you for playing! Feel free to play a new game through the menu at the bottom! =)"
		self.drawElementInMenu(screen, 0, 0, 0, 0, text_to_display, (0, 0, 0), (111, 255, 111), ((self.screen_width / 2) - 275), ((self.margin_y + 425)))

	def returnCardImage(self, image_number):
		card_image = image.load("Artwork/" + str(image_number) + ".png")
		return card_image


