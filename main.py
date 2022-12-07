import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        top = self.top - self.cell_size
        for i in range(self.height):
            top += self.cell_size
            left = self.left
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (left, top, self.cell_size, self.cell_size), 1)
                left += self.cell_size

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        top = self.top - self.cell_size
        for i in range(self.height):
            top += self.cell_size
            left = self.left
            right = left + self.cell_size
            bottom = top + self.cell_size
            for j in range(self.width):
                if left <= x <= right and top <= y <= bottom:
                    return i, j
                left += self.cell_size
                right += self.cell_size
        return None

    def on_click(self, screen, cell_coords=None):
        if cell_coords:
            c = cell_coords
            if self.board[c[0]][c[1]] == 0:
                self.board[c[0]][c[1]] = 1
            else:
                self.board[c[0]][c[1]] = 0
        for i, row in enumerate(self.board):
            for j, el in enumerate(row):
                left = self.left + self.cell_size * j
                top = self.top + self.cell_size * i
                if el == 1:
                    pygame.draw.rect(screen, 'green', (left, top, self.cell_size, self.cell_size), 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (left, top, self.cell_size, self.cell_size), 0)

    def get_click(self, mouse_pos, screen):
        cell = self.get_cell(mouse_pos)
        if cell is None:
            return None
        self.on_click(screen, cell)
