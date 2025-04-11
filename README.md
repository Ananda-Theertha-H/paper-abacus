The abacus consists of multiple beads arranged in columns and rows, each representing a digit. The user can click on the beads to manipulate their position, with the beads moving in response to clicks. The current number represented by the abacus is displayed on the screen, and a reset button allows the user to clear the abacus and start over.

Key Features:
Bead Movement Animation: Beads animate smoothly when moved by the user. The target position of each bead is calculated, and the bead moves towards the target with an animation speed controlled by ANIMATION_SPEED.

Interactive Click Handling: The abacus allows the user to click on beads to change their positions. The position of the beads changes based on which row is clicked. Clicking a bead toggles its state, either activating or deactivating it, depending on its current position.

Bead Calculation: The abacus calculates a number based on the state of the beads. Each column represents a digit, with the beads in the top row representing 5 and the beads in the other rows representing single units. The total number is displayed on the right panel of the screen.

Abacus Frame and Divider: The abacus frame has a wood-like color (WOOD_COLOR), with a dividing line placed between the top and bottom rows of beads to mimic a traditional abacus design. The divider is drawn as a simple line separating the two bead groups.

Reset Button: A reset button is placed on the right panel. When clicked, all beads are reset to their initial position, effectively clearing the abacus.

Hover Effect: When the mouse hovers over a bead, the bead changes color, indicating that it can be interacted with.

Code Overview:
Initialization: The script initializes the Pygame window, sets the necessary constants like the dimensions of the screen and beads, and defines color constants for rendering the abacus.

Drawing Functions:

draw_abacus(): Handles drawing the abacus frame, beads, rods, and divider, as well as animating the movement of beads towards their target positions.

draw_right_panel(): Draws the panel on the right side that displays the total number calculated from the abacus and the reset button.

Event Handling:

handle_click(): Detects clicks on beads and the reset button. It updates the bead states and their positions accordingly.

Target Updates: The update_targets() function recalculates the target positions for each bead based on user interaction, such as toggling beads on or off.

Main Loop: The game loop listens for events like quitting the game or mouse button clicks and continuously updates the screen at 60 frames per second (clock.tick(60)).

Purpose:
This code provides an interactive simulation of an abacus with animated bead movements, useful for educational purposes or as a simple visualization tool for learning basic arithmetic. The reset functionality and dynamic bead manipulation make it an engaging way to represent numbers.
