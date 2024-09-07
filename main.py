import pygame

from frame import Frame

pygame.init()
pygame.font.init()


class Puzzle:
    def __init__(self, screen) -> None:
        self.screen: pygame.Surface = screen
        self.running: bool = True
        self.FPS: int = pygame.time.Clock()
        self.is_arranged = False
        self.font = pygame.font.SysFont("freesansbold", 32)
        self.background_color = (255, 174, 66)
        self.message_color = (17, 53, 165)

    def draw(self, frame):
        frame.draw(self.screen)
        pygame.display.update()

    def instruction(self):
        instructions = self.font.render(
            "Use Arrow Keys to move the tiles", True, self.message_color
        )
        self.screen.blit(instructions, (5, 460))

    def main(self, frame_size):
        self.screen.fill("white")
        frame = Frame(frame_size)
        self.instruction()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.draw(frame)
                self.FPS.tick(30)

        pygame.quit()


if __name__ == "__main__":
    window_size = (500, 500)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Puzzle Game")
    game = Puzzle(screen)
    game.main(window_size[0])
