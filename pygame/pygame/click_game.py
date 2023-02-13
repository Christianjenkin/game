WIDTH = 300
HEIGHT = 300


def draw():
    screen.fill((128, 0, 0))


character = Actor("character")
character.pos = 0, 45

WIDTH = 500
HEIGHT = character.height + 20


def draw():
    screen.clear()
    character.draw()


def update():
    character.left += 2
    if character.left > WIDTH:
        character.right = 0

