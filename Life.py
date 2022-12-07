import pygame
from main import Board


class Life(Board):
    def next_move(self):
        leave_cells = []
        dead_cells = []
        for ind_row, row in enumerate(self.board):
            for ind_el, el in enumerate(row):
                neighborhood = []
                if ind_el != len(row) - 1 and ind_row != len(self.board) - 1 and ind_el != 0 and ind_row != 0:
                    neighborhood.append(self.board[ind_row - 1][ind_el])
                    neighborhood.append(self.board[ind_row - 1][ind_el + 1])
                    neighborhood.append(self.board[ind_row - 1][ind_el - 1])
                    neighborhood.append(self.board[ind_row + 1][ind_el - 1])
                    neighborhood.append(self.board[ind_row + 1][ind_el + 1])
                    neighborhood.append(self.board[ind_row + 1][ind_el])
                    neighborhood.append(row[ind_el + 1])
                    neighborhood.append(row[ind_el - 1])
                else:
                    if ind_el == 0 and ind_row != 0 and ind_row != len(self.board) - 1:
                        neighborhood.append(self.board[ind_row - 1][ind_el])
                        neighborhood.append(self.board[ind_row - 1][ind_el + 1])
                        neighborhood.append(self.board[ind_row + 1][ind_el + 1])
                        neighborhood.append(self.board[ind_row + 1][ind_el])
                        neighborhood.append(row[ind_el + 1])
                    elif ind_el == 0 and ind_row == 0:
                        neighborhood.append(self.board[ind_row + 1][ind_el + 1])
                        neighborhood.append(self.board[ind_row + 1][ind_el])
                        neighborhood.append(row[ind_el + 1])
                    elif ind_row == 0 and ind_el != len(row) - 1 and ind_el != 0:
                        neighborhood.append(self.board[ind_row + 1][ind_el - 1])
                        neighborhood.append(self.board[ind_row + 1][ind_el + 1])
                        neighborhood.append(self.board[ind_row + 1][ind_el])
                        neighborhood.append(row[ind_el + 1])
                        neighborhood.append(row[ind_el - 1])
                    elif ind_el == len(row) - 1 and ind_row == 0:
                        neighborhood.append(self.board[ind_row + 1][ind_el - 1])
                        neighborhood.append(self.board[ind_row + 1][ind_el])
                        neighborhood.append(row[ind_el - 1])
                    elif ind_el == len(row) - 1 and ind_row != 0 and ind_row != len(self.board) - 1:
                        neighborhood.append(self.board[ind_row - 1][ind_el])
                        neighborhood.append(self.board[ind_row - 1][ind_el - 1])
                        neighborhood.append(self.board[ind_row + 1][ind_el - 1])
                        neighborhood.append(self.board[ind_row + 1][ind_el])
                        neighborhood.append(row[ind_el - 1])
                    elif ind_el == 0 and ind_row == len(self.board) - 1:
                        neighborhood.append(self.board[ind_row - 1][ind_el])
                        neighborhood.append(self.board[ind_row - 1][ind_el + 1])
                        neighborhood.append(row[ind_el + 1])
                    elif ind_el == len(row) - 1 and ind_row == len(self.board) - 1:
                        neighborhood.append(self.board[ind_row - 1][ind_el])
                        neighborhood.append(self.board[ind_row - 1][ind_el - 1])
                        neighborhood.append(row[ind_el - 1])
                    else:
                        neighborhood.append(self.board[ind_row - 1][ind_el])
                        neighborhood.append(self.board[ind_row - 1][ind_el + 1])
                        neighborhood.append(self.board[ind_row - 1][ind_el - 1])
                        neighborhood.append(row[ind_el + 1])
                        neighborhood.append(row[ind_el - 1])
                if neighborhood.count(1) == 3 and self.board[ind_row][ind_el] == 0:
                    leave_cells.append((ind_row, ind_el))
                if neighborhood.count(1) > 3 or neighborhood.count(1) < 2 and self.board[ind_row][ind_el] == 1:
                    dead_cells.append((ind_row, ind_el))
        for row_ind, ind_el in dead_cells:
            self.board[row_ind][ind_el] = 0
        for row_ind, ind_el in leave_cells:
            self.board[row_ind][ind_el] = 1


def what_with_flag(flag):
    if flag:
        return False
    else:
        return True


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жизнь')
    size = width, height = 590, 590
    screen = pygame.display.set_mode(size)
    life = Life(29, 29)
    life.set_view(5, 5, 20)
    clock = pygame.time.Clock()
    fps = 15
    running = True
    life_run = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    life.get_click(event.pos, screen)
                elif event.button == 4:
                    fps += 1
                elif event.button == 5:
                    fps -= 1
                elif event.button == 3:
                    life_run = what_with_flag(life_run)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    life_run = what_with_flag(life_run)
        if life_run:
            life.next_move()
            life.on_click(screen)
        life.render(screen)
        clock.tick(fps)
        pygame.display.flip()
