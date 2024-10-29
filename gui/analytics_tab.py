# gui/analytics_tab.py

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from logic.performance import calculate_performance_score
from logic.data_manager import load_weekly_data

def create_analytics_tab(frame):
    weekly_data = load_weekly_data()

    performance, score = calculate_performance_score(weekly_data)
    
    performance_text = (
        f"Weekly Performance:\n"
        f"Brushing: {performance['brushing']} days\n"
        f"Bathing: {performance['bathing']} days\n"
        f"Coursework: {performance['coursework']} hours\n"
        f"Morning Walk: {performance['morning_walk']} days\n"
        f"Breakfast: {performance['breakfast']} days\n"
        f"Guitar: {performance['guitar']} hours\n"
        f"Gym: {performance['gym']} days\n"
        f"Machine Learning: {performance['ml']} hours\n"
        f"Avoided Pornography: {performance['avoid_porn']} times failed\n"
        f"Avoided Stagnation: {performance['avoid_stagnation']} times failed\n"
        f"Performance Score (Norm): {score:.2f}"
    )

    tk.Label(frame, text=performance_text, justify="left").pack()

    def plot_performance():
        activities = [
            'Brushing', 'Bathing', 'Coursework', 'Morning Walk', 'Breakfast',
            'Guitar', 'Gym', 'Machine Learning', 'Avoid Porn', 'Avoid Stagnation'
        ]
        hours = [
            performance['brushing'], performance['bathing'], performance['coursework'], 
            performance['morning_walk'], performance['breakfast'], performance['guitar'],
            performance['gym'], performance['ml'], -performance['avoid_porn'], -performance['avoid_stagnation']
        ]

        fig, ax = plt.subplots()
        ax.bar(activities, hours, color=['blue', 'green', 'red', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'gray', 'brown'])
        ax.set_ylabel('Performance')
        ax.set_title('Weekly Performance')

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    plot_button = tk.Button(frame, text="Show Performance Graph", command=plot_performance)
    plot_button.pack()
