def display_scene(scene):
    """Displays the scene's text and available choices."""
    print(scene["text"])  # Print the scene's description
    if "choices" in scene:  # Check if there are choices in this scene
        for choice_num, (choice_text, _) in scene["choices"].items():
            print(f"{choice_num}. {choice_text}")  # Print each choice with its number

def get_player_choice(scene):
    """Gets and validates the player's choice."""
    while True:  # Keep asking until a valid choice is made
        choice = input("Enter your choice: ")
        if choice in scene["choices"]:  # Check if the choice is valid
            return choice
        else:
            print("Invalid choice. Please try again.")

# Define the story structure (using a dictionary)
story = {
    # Each scene is a key in the dictionary
    "start": {
        "text": "You find yourself in a dark forest. You can go North or East.",
        "choices": {  # Dictionary of choices for this scene
            "1": ("Go North", "north_path"),  # Choice number: (Choice text, Next scene key)
            "2": ("Go East", "east_path")
        }
    },
    "north_path": {
        "text": "You are on a narrow path leading deeper into the forest. You can go back or continue north.",
        "choices": {
            "1": ("Go back", "start"),
            "2": ("Continue north", "deep_forest")
        }
    },
    "east_path": {
        "text": "You walk east and reach a river. You can swim across or go back.",
        "choices": {
            "1": ("Swim across", "river_crossing"),
            "2": ("Go back", "start")
        }
    },
    "deep_forest": {
        "text": "You are lost in the deep forest. There is no way out.",
        # No choices means the end of the game
    },
    "river_crossing": {
        "text": "You swim across the river and find a village. You win!",
        # No choices means the end of the game
    }
}

# Main game loop
current_scene = "start"  # Start at the 'start' scene
while True:
    display_scene(story[current_scene])  # Display the current scene
    if "choices" not in story[current_scene]:  # Check if it's an ending scene (no choices)
        break
    choice = get_player_choice(story[current_scene])  # Get the player's choice
    _, current_scene = story[current_scene]["choices"][choice]  # Update the current scene
