import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 500
ROWS = 5
COLS = 5
BEAD_RADIUS = 20
BEAD_GAP = 10
TOP_MARGIN = 60
LEFT_MARGIN = 60
ANIMATION_SPEED = 5  # pixels per frame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WOOD_COLOR = (240, 220, 180)
HOVER_COLOR = (255, 255, 255)

# Font
FONT = pygame.font.SysFont("Arial", 28)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Abacus with Divider")

# Bead state
beads = [[False for _ in range(ROWS)] for _ in range(COLS)]

# Bead actual and target positions
positions = [[0 for _ in range(ROWS)] for _ in range(COLS)]
targets = [[0 for _ in range(ROWS)] for _ in range(COLS)]

# Initialize positions and targets
for col in range(COLS):
    for row in range(ROWS):
        if row == 0:
            targets[col][row] = TOP_MARGIN
        else:
            targets[col][row] = TOP_MARGIN + 120 + row * (BEAD_RADIUS * 2 + BEAD_GAP)
        positions[col][row] = targets[col][row]


def calculate_abacus_number():
    number = 0
    for col in range(COLS):
        digit = 0
        if beads[col][0]:
            digit += 5
        digit += sum(beads[col][1:])
        number += digit * (10 ** (COLS - col - 1))
    return number


def draw_right_panel():
    total = calculate_abacus_number()

    # Draw number
    number_text = FONT.render("Number:", True, BLACK)
    value_text = FONT.render(f"{total}", True, BLACK)

    screen.blit(number_text, (WIDTH - 130, HEIGHT // 2 - 80))
    screen.blit(value_text, (WIDTH - 130, HEIGHT // 2 - 45))

    # Reset button
    rect = pygame.Rect(WIDTH - 130, HEIGHT // 2, 100, 40)
    pygame.draw.rect(screen, (230, 230, 230), rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, rect, 2, border_radius=10)
    text = FONT.render("Reset", True, BLACK)
    screen.blit(text, (rect.x + 10, rect.y + 5))
    return rect


def draw_abacus(mouse_pos):
    screen.fill(WHITE)

    # Frame calculations
    padding_x = 30
    padding_y = 50
    bead_width = BEAD_RADIUS * 2 + BEAD_GAP
    bead_area_width = COLS * bead_width
    bead_area_height = (ROWS - 1) * (BEAD_RADIUS * 2 + BEAD_GAP) + 120 + 60
    frame_x = LEFT_MARGIN - BEAD_RADIUS - padding_x
    frame_y = TOP_MARGIN - padding_y
    frame_width = bead_area_width + 2 * padding_x
    frame_height = bead_area_height + 2 * padding_y

    # Draw abacus frame
    frame_rect = pygame.Rect(frame_x, frame_y, frame_width, frame_height)
    pygame.draw.rect(screen, WOOD_COLOR, frame_rect, border_radius=20)
    pygame.draw.rect(screen, BLACK, frame_rect, 4, border_radius=20)

    # Draw divider line
    divider_y = TOP_MARGIN + 80  # Positioned between top and bottom beads
    pygame.draw.line(screen, BLACK, (frame_x + 5, divider_y), (frame_x + frame_width - 5, divider_y), 4)

    # Draw beads and rods
    for col in range(COLS):
        x = LEFT_MARGIN + col * (BEAD_RADIUS * 2 + BEAD_GAP)

        for row in range(ROWS):
            # Animate bead movement
            if positions[col][row] < targets[col][row]:
                positions[col][row] = min(positions[col][row] + ANIMATION_SPEED, targets[col][row])
            elif positions[col][row] > targets[col][row]:
                positions[col][row] = max(positions[col][row] - ANIMATION_SPEED, targets[col][row])

            draw_y = positions[col][row]
            dist = ((mouse_pos[0] - x) ** 2 + (mouse_pos[1] - draw_y) ** 2) ** 0.5
            hover = dist <= BEAD_RADIUS

            color = (0, 0, 0) if not hover else HOVER_COLOR  # Beads are black unless hovered

            pygame.draw.circle(screen, color, (x, int(draw_y)), BEAD_RADIUS)

        # Rod line
        pygame.draw.line(screen, BLACK, (x, TOP_MARGIN - 30), (x, HEIGHT - 60), 3)

    return draw_right_panel()


def update_targets():
    contact_gap = 4  # Smaller gap for close contact effect
    for col in range(COLS):
        for row in range(ROWS):
            if row == 0:
                y = TOP_MARGIN
                targets[col][row] = y + 30 - contact_gap if beads[col][row] else y
            else:
                y = TOP_MARGIN + 120 + row * (BEAD_RADIUS * 2 + BEAD_GAP)
                targets[col][row] = y - 30 + contact_gap if beads[col][row] else y


def handle_click(pos):
    if reset_button.collidepoint(pos):
        for col in range(COLS):
            for row in range(ROWS):
                beads[col][row] = False
        update_targets()
        return

    for col in range(COLS):
        x = LEFT_MARGIN + col * (BEAD_RADIUS * 2 + BEAD_GAP)
        for row in range(ROWS):
            y = positions[col][row]
            dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
            if dist <= BEAD_RADIUS:
                if row == 0:
                    beads[col][row] = not beads[col][row]
                else:
                    if beads[col][row]:
                        for r in range(row, ROWS):
                            beads[col][r] = False
                    else:
                        for r in range(1, ROWS):
                            beads[col][r] = (r <= row)
                update_targets()
                return


# Main loop
clock = pygame.time.Clock()
while True:
    mouse_pos = pygame.mouse.get_pos()
    reset_button = draw_abacus(mouse_pos)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(event.pos)

    clock.tick(60)
