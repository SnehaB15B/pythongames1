

## Catch the Falling Objects - Pygame

### Overview
This is a simple game built using Pygame where the player controls a catcher to catch falling objects. The objective is to catch as many objects as possible while avoiding missing them.

### Requirements
- Python 3.x
- Pygame library

### Installation
To install Pygame, use the following command:
```sh
pip install pygame
```

### How to Run
1. Save the script as `catch_game.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using:
   ```sh
   python catch_game.py
   ```

### Controls
- **Left Arrow (←)**: Move the catcher left
- **Right Arrow (→)**: Move the catcher right
- **Q**: Quit the game

### Features
- Catcher moves left and right to catch falling objects.
- If an object is caught, the score increases.
- If an object is missed, the game restarts and the score resets.
- Displays the current score on the screen.

### Customization
- Modify `FALL_SPEED` in the script to adjust difficulty.
- Change `CATCHER_WIDTH`, `CATCHER_HEIGHT`, or colors to personalize the game.
- Add more objects for increased difficulty.
- Implement a "lives" system to prevent immediate game reset.

### Troubleshooting
- Ensure you have Pygame installed (`pip install pygame`).
- If the game window does not open, check for any errors in the terminal.

### License
This project is open-source and free to use or modify.

