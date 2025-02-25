import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("300x400")

        self.choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        self.results = []

        # GUI Components
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
        self.label.pack(pady=20)

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("R"))
        self.rock_button.pack(pady=10)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("P"))
        self.paper_button.pack(pady=10)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("S"))
        self.scissors_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

        self.results_button = tk.Button(root, text="Show Results", command=self.show_results)
        self.results_button.pack(pady=10)

    def play(self, user_choice):
        dic = {"R": 1, "S": 0, "P": -1}
        rev_dic = {1: "Rock", 0: "Scissors", -1: "Paper"}

        gamer_input = dic[user_choice]
        computer_input = random.choice([-1, 0, 1])

        computer_choice = rev_dic[computer_input]
        user_choice_str = self.choices[user_choice]

        if computer_input == gamer_input:
            result = "draw"
            messagebox.showinfo("Result", f"Computer chose {computer_choice}\nYou chose {user_choice_str}\nIt's a draw!")
        elif (gamer_input - computer_input) % 3 == 1:
            result = "win"
            messagebox.showinfo("Result", f"Computer chose {computer_choice}\nYou chose {user_choice_str}\nYou win!")
        else:
            result = "lose"
            messagebox.showinfo("Result", f"Computer chose {computer_choice}\nYou chose {user_choice_str}\nYou lose!")

        # Store the result
        self.results.append({
            "user_choice": user_choice_str,
            "computer_choice": computer_choice,
            "result": result
        })

    def show_results(self):
        results_window = tk.Toplevel(self.root)
        results_window.title("Game Results")
        results_window.geometry("300x400")

        results_label = tk.Label(results_window, text="Game Results", font=("Arial", 14))
        results_label.pack(pady=10)

        for index, game_result in enumerate(self.results, start=1):
            result_text = f"Game {index}: You chose {game_result['user_choice']}, Computer chose {game_result['computer_choice']}. Result: You {game_result['result']}."
            result_label = tk.Label(results_window, text=result_text, wraplength=280)
            result_label.pack(pady=2)

        save_button = tk.Button(results_window, text="Save to File", command=self.save_results)
        save_button.pack(pady=10)

    def save_results(self):
        with open("game_results.txt", "w") as file:
            for game_result in self.results:
                file.write(f"You chose {game_result['user_choice']}, Computer chose {game_result['computer_choice']}. Result: You {game_result['result']}.\n")
        messagebox.showinfo("Saved", "Results saved to game_results.txt")

# Main part of the program
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
