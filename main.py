from dataclasses import dataclass
import random
import pygame
import pygame.draw as draw

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
rand = random.Random()


@dataclass
class Vector:
    x: float = 0
    y: float = 0


@dataclass
class Shape:
    size: int
    pos: Vector = (0, 0)
    dir: Vector = (0, 0)
    kind: str = 'circle'


@dataclass
class State:
    screen: pygame.Surface
    w: int
    h: int
    shapes = []


def main():
    pygame.init()
    pygame.display.set_caption("minimal program")
    dinfo = pygame.display.Info()

    screen = pygame.display.set_mode((dinfo.current_w, dinfo.current_h), pygame.FULLSCREEN)
    gamestate = State(screen, dinfo.current_w, dinfo.current_h)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    spawn(gamestate)

        update(gamestate)
        pygame.display.update()


def spawn(state: State):
    if len(state.shapes) > 3:
        state.shapes.pop(0)
    x = rand.randint(0, state.w)
    y = rand.randint(0, state.h)
    r = rand.randint(5, 100)
    s = Shape(r, Vector(x, y), Vector(rand.random() - 0.5, rand.random() - 0.5))
    state.shapes.append(s)
    pass


def update_position(shape: Shape):
    newy = shape.pos.y + 10 * shape.dir.y
    newx = shape.pos.x + 10 * shape.dir.x
    shape.pos = Vector(newx, newy)
    pass


def wrap_screen(shape: Shape, w: int, h: int):
    if shape.pos.x < 0:
        shape.pos.x = w
    elif shape.pos.x > w:
        shape.pos.x = 0
    if shape.pos.y < 0:
        shape.pos.y = h
    elif shape.pos.y > h:
        shape.pos.y = 0

    pass


def update(state: State):
    state.screen.fill(black)

    for s in state.shapes:
        shape: Shape = s
        update_position(shape)
        wrap_screen(shape, state.w, state.h)
        draw.circle(state.screen, white, (shape.pos.x, shape.pos.y), shape.size, 1)


if __name__ == "__main__":
    # call the main function
    main()
