import customtkinter
import tkinter as tk
from tkinter import scrolledtext

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Define the list of dictionaries
BridesmaidsBouquets = [
    {"name": "Roses", "quantity": 3, "color": "Red"},
    {"name": "Carnations", "quantity": 3, "color": "Red"},
    {"name": "Lilys", "quantity": 3, "color": "Red"},
    {"name": "Daiseys", "quantity": 3, "color": "Red"}
]

CenterPieces = [
    {"name": "Roses", "quantity": 6, "color": "Red"},
    {"name": "Carnations", "quantity": 9, "color": "Red"},
    {"name": "Lilys", "quantity": 2, "color": "Red"},
    {"name": "Daiseys", "quantity": 3, "color": "Red"}
]

Boutonnieres = [
    {"name": "Roses", "quantity": 1, "color": "Red"},
    {"name": "Carnations", "quantity": 7, "color": "Red"},
    {"name": "Lilys", "quantity": 12, "color": "Red"},
    {"name": "Daiseys", "quantity": 3, "color": "Red"}
]

Corsages = [
    {"name": "Roses", "quantity": 14, "color": "Red"},
    {"name": "Carnations", "quantity": 2, "color": "Red"},
    {"name": "Lilys", "quantity": 8, "color": "Red"},
    {"name": "Daiseys", "quantity": 3, "color": "Red"}
]

# Create a function to clear the frame and display results dynamically
def display_results():
    # Get user input as integers
    bridesmaids_quantity = int(entry1.get())
    centerpieces_quantity = int(entry2.get())
    boutonnieres_quantity = int(entry3.get())
    corsages_quantity = int(entry4.get())
    
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a new canvas on the frame with a background color
    background_canvas = tk.Canvas(master=frame, width=500, height=850, bg=customtkinter.get_default_color_theme())
    background_canvas.pack(fill="both", expand=True)

    # Create a scrolled text widget for displaying results with the same theme colors
    result_text = "Results:\n\n"

    def calculate_category(category, quantity, category_name):
        nonlocal result_text
        result_text += f"{category_name}:\n"
        for flower in category:
            flower_quantity = flower["quantity"] * quantity
            result_text += f"{flower['name']}: {flower_quantity}\n"
        result_text += "\n"  # Add space after each category

    calculate_category(BridesmaidsBouquets, bridesmaids_quantity, "Bridesmaids Bouquets")
    calculate_category(CenterPieces, centerpieces_quantity, "Center Pieces")
    calculate_category(Boutonnieres, boutonnieres_quantity, "Boutonnieres")
    calculate_category(Corsages, corsages_quantity, "Corsages")

   # Calculate the total quantity of each flower separately for each category
    total = {flower['name']: 0 for flower in BridesmaidsBouquets}

    def calculate_total_quantity(category, quantity):
        for flower in category:
            total[flower['name']] += flower['quantity'] * quantity

    calculate_total_quantity(BridesmaidsBouquets, bridesmaids_quantity)
    calculate_total_quantity(CenterPieces, centerpieces_quantity)
    calculate_total_quantity(Boutonnieres, boutonnieres_quantity)
    calculate_total_quantity(Corsages, corsages_quantity)

    # Add space before the "Total" category
    result_text += "\nTotal:\n"
    for flower, quantity in total.items():
        result_text += f"{flower}: {quantity}\n"

    # Create a scrolled text widget for displaying results on the result_frame
    result_display = scrolledtext.ScrolledText(master=background_canvas, wrap=tk.NONE, bg=customtkinter.get_theme_color("background"), fg=customtkinter.get_theme_color("text"))
    result_display.insert("1.0", result_text)
    result_display.config(state="disabled")
    result_display.pack(fill="both", expand=True)

    # Back button
    back_button = tk.Button(master=background_canvas, text="Back", command=reset_program, bg=customtkinter.get_theme_color("background"), fg=customtkinter.get_theme_color("text"))
    back_button.pack(pady=10)

def reset_program():
    for widget in frame.winfo_children():
        widget.destroy()
    create_input_form()

def create_input_form():
    # Title
    label = customtkinter.CTkLabel(master=frame, text="Wedding Calculator", font=("bold", 30), width=20, height=2)
    label.pack(pady=12, padx=10)

    # Entry Bars
    global entry1, entry2, entry3, entry4
    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="How many Bridesmaid's bouquets do you need?", width=300)
    entry1.pack(pady=30, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="How many Center Piece's do you need?", width=300)
    entry2.pack(pady=30, padx=10)

    entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="How many Boutonnier's do you need?", width=300)
    entry3.pack(pady=30, padx=10)

    entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="How many Corsage's do you need?", width=300)
    entry4.pack(pady=30, padx=10)

    # Calculate button
    calculate_button = customtkinter.CTkButton(master=frame, text="Calculate", command=display_results)
    calculate_button.pack(pady=12, padx=10)

# Create the main window
root = customtkinter.CTk()
root.geometry("500x850")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=15, fill="both", expand=True)

create_input_form()

root.mainloop()
