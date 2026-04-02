import customtkinter as ctk
import random

# Appearance Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class RPSGame(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rock Paper Scissors Pro")
        self.geometry("500x450")
        
        self.user_wins = 0
        self.comp_wins = 0
        self.options = ["rock", "paper", "scissor"]

        # --- UI Elements ---
        
        # Header
        self.label = ctk.CTkLabel(self, text="Choose Your Move", font=("Roboto", 24, "bold"))
        self.label.pack(pady=30)

        # Button Container
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        # Styled Buttons
        self.rock_btn = ctk.CTkButton(self.button_frame, text="🪨 Rock", command=lambda: self.play("rock"), width=120, height=40)
        self.rock_btn.grid(row=0, column=0, padx=10)

        self.paper_btn = ctk.CTkButton(self.button_frame, text="📄 Paper", command=lambda: self.play("paper"), width=120, height=40)
        self.paper_btn.grid(row=0, column=1, padx=10)

        self.scissor_btn = ctk.CTkButton(self.button_frame, text="✂️ Scissor", command=lambda: self.play("scissor"), width=120, height=40)
        self.scissor_btn.grid(row=0, column=2, padx=10)

        # Result Display
        self.result_text = ctk.CTkLabel(self, text="Waiting for your move...", font=("Roboto", 16), text_color="gray")
        self.result_text.pack(pady=40)

        # Scoreboard
        self.score_frame = ctk.CTkFrame(self, corner_radius=15)
        self.score_frame.pack(pady=10, fill="x", padx=50)

        self.score_label = ctk.CTkLabel(self.score_frame, text="You: 0  |  CPU: 0", font=("Roboto", 18, "bold"))
        self.score_label.pack(pady=10)

    def play(self, user_choice):
        comp_choice = random.choice(self.options)
        
        if user_choice == comp_choice:
            res = "It's a draw!"
            color = "#FFCC00" # Yellow
        elif (user_choice == "rock" and comp_choice == "scissor") or \
             (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "scissor" and comp_choice == "paper"):
            res = f"Victory! {user_choice.title()} beats {comp_choice}."
            self.user_wins += 1
            color = "#2ECC71" # Green
        else:
            res = f"Defeat! {comp_choice.title()} beats {user_choice}."
            self.comp_wins += 1
            color = "#E74C3C" # Red

        # Update UI
        self.result_text.configure(text=res, text_color=color)
        self.score_label.configure(text=f"You: {self.user_wins}  |  CPU: {self.comp_wins}")

if __name__ == "__main__":
    app = RPSGame()
    app.mainloop()