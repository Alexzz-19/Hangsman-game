import random
import tkinter as tk
from tkinter import messagebox

# ------------------------------------------------------------
# Word list (all uppercase)
# ------------------------------------------------------------
WORDS = [
    "PYTHON", "JAVA", "JAVASCRIPT", "HANGMAN", "PROGRAMMING",
    "COMPUTER", "ALGORITHM", "INTELLIGENCE", "DATA", "STRUCTURE",
    "VARIABLE", "FUNCTION", "LOOP", "CONDITIONAL", "LIST",
    "DICTIONARY", "CLASS", "OBJECT", "INHERITANCE", "CODEINPLACE"
]

MAX_MISTAKES = 6  

# ------------------------------------------------------------
# Main game class with Tkinter
# ------------------------------------------------------------
class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman - Code in Place")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")

        # Game variables
        self.secret_word = ""
        self.guessed_letters = set()
        self.mistakes = 0
        self.game_active = True

        # Dictionary of coordinates to draw the hangman
        self.drawings = {
            0: self.draw_structure,
            1: self.draw_head,
            2: self.draw_torso,
            3: self.draw_left_arm,
            4: self.draw_right_arm,
            5: self.draw_left_leg,
            6: self.draw_right_leg
        }

        # Create widgets
        self.create_widgets()

        # Start new game
        self.new_game()

    def create_widgets(self):
        # Top frame for the hangman drawing
        self.canvas_frame = tk.Frame(self.root, bg="#ECF0F1", bd=2, relief=tk.RIDGE)
        self.canvas_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, width=400, height=250, bg="white")
        self.canvas.pack(pady=10, padx=10)

        # Frame for the hidden word
        self.word_frame = tk.Frame(self.root, bg="#2C3E50")
        self.word_frame.pack(pady=15)

        self.word_label = tk.Label(
            self.word_frame, text="", font=("Courier", 28, "bold"),
            bg="#2C3E50", fg="#F1C40F"
        )
        self.word_label.pack()

        # Frame for used letters
        self.used_frame = tk.Frame(self.root, bg="#2C3E50")
        self.used_frame.pack(pady=5)

        self.used_label = tk.Label(
            self.used_frame, text="Used letters: ", font=("Arial", 12),
            bg="#2C3E50", fg="#BDC3C7"
        )
        self.used_label.pack()

        # Frame for keyboard buttons (A-Z)
        self.keyboard_frame = tk.Frame(self.root, bg="#34495E")
        self.keyboard_frame.pack(pady=15, padx=10, fill=tk.BOTH)

        # Create buttons for each letter
        self.letter_buttons = {}
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, letter in enumerate(letters):
            btn = tk.Button(
                self.keyboard_frame, text=letter, width=4, height=1,
                font=("Arial", 12, "bold"), bg="#3498DB", fg="white",
                command=lambda l=letter: self.try_letter(l)
            )
            row = i // 9
            column = i % 9
            btn.grid(row=row, column=column, padx=3, pady=3, sticky="nsew")
            self.letter_buttons[letter] = btn

        # Button to restart game
        self.restart_btn = tk.Button(
            self.root, text="🔄 New Word", font=("Arial", 12, "bold"),
            bg="#E67E22", fg="white", command=self.new_game
        )
        self.restart_btn.pack(pady=10)

        # Label to show status (messages)
        self.status_label = tk.Label(
            self.root, text="Guess the word!", font=("Arial", 11, "italic"),
            bg="#2C3E50", fg="#ECF0F1"
        )
        self.status_label.pack(pady=5)

    # ---------- Game methods ----------
    def new_game(self):
        """Reset all variables and interface."""
        self.secret_word = random.choice(WORDS)
        self.guessed_letters = set()
        self.mistakes = 0
        self.game_active = True

        # Reset colors and states of buttons
        for letter, btn in self.letter_buttons.items():
            btn.config(state=tk.NORMAL, bg="#3498DB", fg="white")

        # Clear canvas and draw initial structure
        self.canvas.delete("all")
        self.draw_structure()

        # Update interface all at once
        self.update_interface()
        self.update_used_letters()
        
        # Status messages with delay for the temporary message
        self.status_label.config(text="New word! Guess letter by letter.", fg="#2ECC71")
        self.root.after(2000, lambda: self.status_label.config(text="Guess the word!", fg="#ECF0F1"))

    def try_letter(self, letter):
        """Process a letter attempt."""
        if not self.game_active:
            return

        # If letter was already used
        if letter in self.guessed_letters:
            messagebox.showinfo("Repeated letter", f"You already tried the letter '{letter}'. Try another one.")
            return

        # Add to used and disable button immediately
        self.guessed_letters.add(letter)
        self.letter_buttons[letter].config(state=tk.DISABLED, bg="#95A5A6")

        # Check if letter is in the word
        if letter in self.secret_word:
            # Correct guess
            self.status_label.config(text=f"✅ Good! '{letter}' is in the word.", fg="#2ECC71")
            
            # Check if won BEFORE updating interface
            if self.check_victory():
                self.update_interface()
                self.update_used_letters()
                self.end_game(winner=True)
            else:
                self.update_interface()
                self.update_used_letters()
        else:
            # Wrong guess
            self.mistakes += 1
            self.status_label.config(text=f"❌ Wrong! '{letter}' is not in the word.", fg="#E74C3C")
            
            # Draw hangman and update interface
            self.draw_hangman()
            self.update_interface()
            self.update_used_letters()
            
            # Check if lost
            if self.mistakes >= MAX_MISTAKES:
                self.end_game(winner=False)

    def check_victory(self):
        """Returns True if all letters of the secret word have been guessed."""
        return all(letter in self.guessed_letters for letter in self.secret_word)

    def update_interface(self):
        """Update the display of the hidden word."""
        displayed_word = []
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                displayed_word.append(letter)
            else:
                displayed_word.append("_")
        self.word_label.config(text=" ".join(displayed_word))

    def update_used_letters(self):
        """Update the used letters label."""
        if self.guessed_letters:
            text = "Used letters: " + ", ".join(sorted(self.guessed_letters))
        else:
            text = "Used letters: none"
        self.used_label.config(text=text)

    def draw_hangman(self):
        """Draw the corresponding part based on the number of mistakes."""
        if self.mistakes in self.drawings:
            self.drawings[self.mistakes]()

    def draw_structure(self):
        """Base of the gallows."""
        self.canvas.create_line(50, 200, 150, 200, width=3, tags="structure")   # horizontal base
        self.canvas.create_line(100, 200, 100, 50, width=3, tags="structure")    # vertical pole
        self.canvas.create_line(100, 50, 200, 50, width=3, tags="structure")     # top crossbeam
        self.canvas.create_line(200, 50, 200, 80, width=3, tags="structure")      # rope

    def draw_head(self):
        self.canvas.create_oval(175, 80, 225, 130, width=2, tags="body")  # head circle

    def draw_torso(self):
        self.canvas.create_line(200, 130, 200, 180, width=2, tags="body")  # body line

    def draw_left_arm(self):
        self.canvas.create_line(200, 140, 170, 160, width=2, tags="body")  # left arm

    def draw_right_arm(self):
        self.canvas.create_line(200, 140, 230, 160, width=2, tags="body")  # right arm

    def draw_left_leg(self):
        self.canvas.create_line(200, 180, 170, 210, width=2, tags="body")  # left leg

    def draw_right_leg(self):
        self.canvas.create_line(200, 180, 230, 210, width=2, tags="body")  # right leg

    def end_game(self, winner):
        """End the game and show final message."""
        self.game_active = False
        
        # Disable all letter buttons immediately
        for btn in self.letter_buttons.values():
            btn.config(state=tk.DISABLED)
        
        if winner:
            self.status_label.config(text="YOU WON! You're awesome!", fg="#F1C40F")
            # Use after to prevent blocking
            self.root.after(100, lambda: messagebox.showinfo(
                "Congratulations!",
                f"🎉✨ Congratulations for passing the game, Code in Place participant! ✨🎉\n\n"
                f"You guessed the word: {self.secret_word}\n"
                f"Mistakes: {self.mistakes}/{MAX_MISTAKES}"
            ))
        else:
            # Show the complete word
            self.word_label.config(text=" ".join(self.secret_word))
            self.status_label.config(text="You lost... Press 'New Word' to continue.", fg="#E74C3C")
            # Use after to prevent blocking
            self.root.after(100, lambda: messagebox.showinfo(
                "Hanged!",
                f"💀 You lost! 💀\nThe word was: {self.secret_word}\n"
                f"Mistakes: {self.mistakes}/{MAX_MISTAKES}\n\nTry again."
            ))

# ------------------------------------------------------------
# Main execution
# ------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()