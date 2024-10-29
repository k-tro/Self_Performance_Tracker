# gui/home_tab.py
import tkinter as tk
from tkinter import messagebox
from logic.data_manager import save_data, load_data

def create_home_tab(frame):
    # Load previously saved data
    brushing_value, bathing_value, coursework_value, morning_walk_value, breakfast_value, \
    guitar_value, gym_value, ml_value, avoid_porn_value, avoid_stagnation_value = load_data()
    
    def submit_input():
        # Get values from the sliders
        brushing_value = brushing_slider.get()
        bathing_value = bathing_slider.get()
        coursework_value = coursework_slider.get()
        morning_walk_value = morning_walk_slider.get()
        breakfast_value = breakfast_slider.get()
        guitar_value = guitar_slider.get()
        gym_value = gym_slider.get()
        ml_value = ml_slider.get()
        avoid_porn_value = avoid_porn_slider.get()
        avoid_stagnation_value = avoid_stagnation_slider.get()

        # Save the values
        save_data(
            brushing_value, bathing_value, coursework_value, morning_walk_value, breakfast_value, 
            guitar_value, gym_value, ml_value, avoid_porn_value, avoid_stagnation_value
        )

        message = (f"Brushing: {brushing_value}\nBathing: {bathing_value}\nCoursework: {coursework_value} hours\n"
                   f"Morning Walk: {morning_walk_value}\nBreakfast: {breakfast_value}\nGuitar: {guitar_value} hours\n"
                   f"Gym: {gym_value}\nML Study: {ml_value} hours\n"
                   f"Avoided Porn: {avoid_porn_value}\nAvoided Stagnation: {avoid_stagnation_value}")
        messagebox.showinfo("Daily Input", message)

    # Brushing
    tk.Label(frame, text="Brushing Daily").pack()
    brushing_slider = tk.Scale(frame, from_=0, to=1, orient="horizontal")
    brushing_slider.pack()

    # Bathing
    tk.Label(frame, text="Bathing Daily").pack()
    bathing_slider = tk.Scale(frame, from_=0, to=1, orient="horizontal")
    bathing_slider.pack()

    # Coursework
    tk.Label(frame, text="Coursework Hours").pack()
    coursework_slider = tk.Scale(frame, from_=0, to=15, orient="horizontal")
    coursework_slider.pack()

    # Morning Walk
    tk.Label(frame, text="Morning Walk").pack()
    morning_walk_slider = tk.Scale(frame, from_=0, to=1, orient="horizontal")
    morning_walk_slider.pack()

    # Breakfast
    tk.Label(frame, text="Had Breakfast").pack()
    breakfast_slider = tk.Scale(frame, from_=0, to=1, orient="horizontal")
    breakfast_slider.pack()

    # Guitar Practice
    tk.Label(frame, text="Guitar Practice Hours").pack()
    guitar_slider = tk.Scale(frame, from_=0, to=3, orient="horizontal")
    guitar_slider.pack()

    # Gym
    tk.Label(frame, text="Gym").pack()
    gym_slider = tk.Scale(frame, from_=0, to=1, orient="horizontal")
    gym_slider.pack()

    # Machine Learning Study Hours
    tk.Label(frame, text="Machine Learning Study Hours").pack()
    ml_slider = tk.Scale(frame, from_=0, to=10, orient="horizontal")
    ml_slider.pack()

    # Avoided Pornography
    tk.Label(frame, text="Avoided Pornography").pack()
    avoid_porn_slider = tk.Scale(frame, from_=-1, to=1, orient="horizontal")  # -1 for failure
    avoid_porn_slider.pack()

    # Avoided Stagnation
    tk.Label(frame, text="Avoided Stagnation").pack()
    avoid_stagnation_slider = tk.Scale(frame, from_=-1, to=1, orient="horizontal")  # -1 for failure
    avoid_stagnation_slider.pack()

    # Submit Button
    tk.Button(frame, text="Submit", command=submit_input).pack()
