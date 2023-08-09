import pygame
import pyautogui
import os

# Allows input to be recieved when pygame window is not in focus
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

pygame.init()

pygame.joystick.init()
joysticks = []

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Controller OS Interaction')

isRunning = True
mouseMultiplier = 10

# Loop
while isRunning:

    # Event handler
    for event in pygame.event.get():
        # Handle new controller
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
        # Handle lost controller
        if event.type == pygame.JOYDEVICEREMOVED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.remove(joy)
        # Handle button press
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0: # A
                pyautogui.mouseDown()
            elif event.button == 1: # B
                pyautogui.press('f')
            elif event.button == 2: # X
                pyautogui.press('m')
            elif event.button == 3: # Y
                mouseMultiplier = 100
        # Handle button release
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0: # A
                pyautogui.mouseUp()
            elif event.button == 3: # Y
                mouseMultiplier = 10
        # Quit
        if event.type == pygame.QUIT:
            isRunning = False

    # Moving mouse
    mouse_x = round(pygame.joystick.Joystick(0).get_axis(0))
    mouse_y = round(pygame.joystick.Joystick(0).get_axis(1))
    pyautogui.moveRel(mouse_x * mouseMultiplier, mouse_y * mouseMultiplier, 0.1)

    window.fill('white')

    # Render minimize instruction text
    text_surface = my_font.render('Minimize This Window', True, (0,0,0), (255,255,255))
    window.blit(text_surface, (0,0))

    pygame.display.flip()