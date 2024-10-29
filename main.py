# main.py
import tkinter as tk
from gui.home_tab import create_home_tab
from gui.analytics_tab import create_analytics_tab

def run_app():
    root = tk.Tk()
    root.title("Performance Tracker")

    notebook = tk.ttk.Notebook(root)
    
    home_tab = tk.Frame(notebook)
    create_home_tab(home_tab)
    notebook.add(home_tab, text="Home")
    
    analytics_tab = tk.Frame(notebook)
    create_analytics_tab(analytics_tab)
    notebook.add(analytics_tab, text="Analytics")

    notebook.pack(expand=1, fill="both")
    root.mainloop()

if __name__ == "__main__":
    run_app()
