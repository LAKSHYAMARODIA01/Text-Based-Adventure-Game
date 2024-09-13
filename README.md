# Text-Based Adventure Game

Welcome to the **Text-Based Adventure Game**! This is a simple Python-based interactive game where players navigate through different scenes based on their choices.

## How to Play

In this game, you start in a dark forest and make choices that determine your path. The game offers multiple branching paths, and your objective is to explore the forest and make decisions that lead you to the village to win.

### Game Flow
- The game presents a scene with a description.
- You will be given a set of choices for each scene, and you must type the corresponding number to make your choice.
- Based on your choices, you will navigate to different scenes until you either win or get lost!

### Scenes
- **Starting Scene**: You begin your journey in a dark forest with options to go North or East.
- **North Path**: If you go North, you encounter a narrow path. You can choose to go back or continue deeper into the forest.
- **East Path**: If you go East, you encounter a river and can either swim across or go back.
- **Deep Forest**: If you continue North, you get lost in the deep forest and the game ends.
- **River Crossing**: If you swim across the river, you reach a village and win the game.

## Installation and Running the Game

1. Make sure you have Python installed on your system. You can download it [here](https://www.python.org/downloads/).

2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/text-adventure-game.git
   ```

3. Navigate to the game folder:
   ```bash
   cd text-adventure-game
   ```

4. Run the Python script to start the game:
   ```bash
   python adventure_game.py
   ```

## Code Structure

- The game is defined using a dictionary called `story`. Each key represents a scene in the game, and each scene has:
  - `text`: The description of the scene.
  - `choices`: A dictionary of available choices, where each choice has a corresponding next scene.

- The `display_scene()` function displays the current scene's description and choices.
  
- The `get_player_choice()` function prompts the player to input a valid choice.

- The main game loop runs the game, starting from the "start" scene and continuing based on the player's choices.

## Example Gameplay

```
You find yourself in a dark forest. You can go North or East.
1. Go North
2. Go East
Enter your choice: 2

You walk east and reach a river. You can swim across or go back.
1. Swim across
2. Go back
Enter your choice: 1

You swim across the river and find a village. You win!
```

## Future Improvements

- Add more scenes and storylines for a richer gameplay experience.
- Introduce inventory management and decision consequences.
- Implement saving and loading game progress.

## Contributing

If you'd like to contribute to the project, feel free to submit a pull request. Please make sure to follow the coding standards and provide clear descriptions for your contributions.

##Screenshot  

<img width="956" alt="ss1" src="https://github.com/user-attachments/assets/7cf2b8da-10a6-437a-805e-da0a6d43b8b4">



