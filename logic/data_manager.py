# logic/data_manager.py
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/daily_input.json')

# Update the save_data function to store all goals
def save_data(brushing, bathing, coursework, morning_walk, breakfast, guitar, gym, ml, avoid_porn, avoid_stagnation):
    data = {
        'brushing': brushing,
        'bathing': bathing,
        'coursework': coursework,
        'morning_walk': morning_walk,
        'breakfast': breakfast,
        'guitar': guitar,
        'gym': gym,
        'ml': ml,
        'avoid_porn': avoid_porn,
        'avoid_stagnation': avoid_stagnation
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

# Update the load_data function to retrieve all goals
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            return (
                data.get('brushing', 0), data.get('bathing', 0), data.get('coursework', 0),
                data.get('morning_walk', 0), data.get('breakfast', 0), data.get('guitar', 0),
                data.get('gym', 0), data.get('ml', 0), data.get('avoid_porn', 1), data.get('avoid_stagnation', 1)
            )
    return 0, 0, 0, 0, 0, 0, 0, 0, 1, 1  # Default values
