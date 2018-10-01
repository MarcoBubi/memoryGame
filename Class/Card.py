import pygame
import Board

class Card:
	value = 0
	display = False
	is_complete = False
	object_board = Board.Board(1200, 800)
	local_screen_width = object_board.screen_width
	local_screen_height = object_board.screen_height
	local_font = object_board.UI_font
	margin_x = object_board.margin_x
	margin_y = object_board.margin_y
	card_background = object_board.card_background
	local_card_offset_dist = object_board.local_card_offset_dist

	def __init__(self, value):
		self.value = value
		return

	def settingsOfCard(self, h_iterator, w_iterator):
		w_size = ((self.local_screen_width - 0) / h_iterator)
		h_size = ((self.local_screen_height - (2 * self.margin_y)) / w_iterator)
		return w_size, h_size

	def cardDrawOnBoard(self, screen, w, h, h_iterator, w_iterator, even_card):
		w_size, h_size =  self.settingsOfCard(h_iterator, w_iterator)
		if(w_size < self.local_card_offset_dist + 1 or h_size < self.local_card_offset_dist + 1):
			if(self.local_card_offset_dist == 0):
				self.local_card_offset_dist = 0
				return
			if(h_size > w_size):
				self.local_card_offset_dist = w_size - 1
			else:
				self.local_card_offset_dist = h_size - 1
		if(even_card):
			pygame.draw.rect(screen, (0, 0, 0), ((w * w_size) + self.margin_x, (h * h_size) + self.margin_y, w_size - self.local_card_offset_dist, h_size - self.local_card_offset_dist))
		else:
			transformed_card_background = pygame.transform.scale(self.card_background, (w_size - self.local_card_offset_dist, h_size - self.local_card_offset_dist))
			screen.blit(transformed_card_background, (((w * w_size) + self.margin_x, (h * h_size) + self.margin_y)))

	def startAnimation(self, x_, y_, h_iterator, w_iterator, display_value_on_card):
		w_size, h_size =  self.settingsOfCard(h_iterator, w_iterator)
		font_size = int((h_size + w_size) * 0.1)
		my_font = pygame.font.SysFont('Arial', font_size)
		animation_timer = pygame.time.Clock()
		x = self.margin_x + y_ * w_size
 		y = self.margin_y + x_ * h_size
		x_start = x
		x_width = w_size - self.local_card_offset_dist
		y_width = h_size - self.local_card_offset_dist
		x_width_start = x_width
		card_background = self.object_board.card_background
		card_background_transformed = pygame.transform.scale(card_background, (x_width_start, y_width))
		card_image_transformed_inverted = pygame.transform.scale(card_background, (1, y_width))
		card_image = self.object_board.returnCardImage(self.value)
		card_image_transformed = pygame.transform.scale(card_image, (1, y_width))
		# I don't want to use any draw function in this segment because every element is somehow affected by the environment, beside the 3 draw functions that set the color.
		pygame.draw.rect(self.object_board.screen, (255, 255, 255), (x, y, x_width, y_width))
		for z in range(0, 100):
			pygame.draw.rect(self.object_board.screen, (0, 0, 0), (x_start - int(self.local_card_offset_dist / 2), y - int(self.local_card_offset_dist / 2), x_width_start + int(self.local_card_offset_dist), y_width + int(self.local_card_offset_dist)))
			if(x > ((x_start + x_width_start + x_start) / 2) or x == ((x_start + x_width_start + x_start) / 2)):
				if(display_value_on_card):
					pygame.draw.rect(self.object_board.screen, (255, 255, 255), (x, y, x_width, y_width))
					self.object_board.screen.blit(card_image_transformed, (int(x + x_width), y))
					card_image_transformed = pygame.transform.scale(card_image, (int(abs(x_width)), y_width))
				else:
					self.object_board.screen.blit(card_image_transformed_inverted, (int(x + x_width), y))
					card_image_transformed_inverted = pygame.transform.scale(card_background, (int(abs(x_width)), y_width))
			else:
				if(display_value_on_card):
					self.object_board.screen.blit(card_background_transformed, (int(x), y))
					card_background_transformed = pygame.transform.scale(card_background, (int(abs(x_width)), y_width))
				else:
					pygame.draw.rect(self.object_board.screen, (255, 255, 255), (x, y, x_width, y_width))
					self.object_board.screen.blit(card_image_transformed, (int(x), y))
					card_image_transformed = pygame.transform.scale(card_image, (int(abs(x_width)), y_width))
			x += (x_width_start * 0.01)
			x_width -= (x_width_start * 0.02)
			animation_timer.tick(150)
			pygame.display.update()
		pygame.draw.rect(self.object_board.screen, (0, 0, 0), (x_start - int(self.local_card_offset_dist / 2), y - int(self.local_card_offset_dist / 2), x_width_start + int(self.local_card_offset_dist), y_width + int(self.local_card_offset_dist)))
		if(display_value_on_card):
			pygame.draw.rect(self.object_board.screen, (255, 255, 255), (x_start, y, x_width_start, y_width))
			self.object_board.screen.blit(card_image_transformed, (x_start, y))
		else:
			self.object_board.screen.blit(card_background_transformed, (x_start, y))


