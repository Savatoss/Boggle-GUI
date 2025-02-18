import tkinter as tk
import ex12_utils as helper
import boggle_board_randomizer as board
import tkinter.messagebox
from typing import Dict

START_DISPLAY = 'Enter letters'
START_SCORE = 0
WORD_DICT = 'boggle_dict.txt'
SEC = 60
INITIAL_TIME = '00:00'


class Boggle:
    _buttons: Dict[tuple, tk.Button] = {}

    def __init__(self, board):
        self.root = tk.Tk()
        self.root.title("Boggle Game")
        self.root.configure(bg="#2C3E50")
        self.root.geometry("800x600")  # Increased window size

        self.sec = SEC
        self.board = board
        self.score = START_SCORE
        self.selected_cells = []
        self.found_words = []
        self.words = helper.load_words_dict(WORD_DICT)

        # Main frame with grid layout (two columns: game and found words)
        self.main_frame = tk.Frame(self.root, bg="#2C3E50")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left frame for game controls and board
        self.left_frame = tk.Frame(self.main_frame, bg="#34495E")
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Right frame for found words list
        self.right_frame = tk.Frame(self.main_frame, bg="#2C3E50")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Configure column weights so left frame gets more space
        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=1)

        # Top controls in left frame (display, timer, score, start, check)
        self.top_controls = tk.Frame(self.left_frame, bg="#34495E")
        self.top_controls.pack(pady=10)

        self._display_label = tk.Label(self.top_controls, text=START_DISPLAY,
                                       font=("Helvetica", 20, "bold"), width=16,
                                       relief="ridge", bg="white")
        self._display_label.grid(row=0, column=0, columnspan=4, pady=5)

        self.time = tk.Label(self.top_controls, text=INITIAL_TIME, bg="black",
                             fg="red", font=("Helvetica", 15), width=5, relief="sunken")
        self.time.grid(row=1, column=0, padx=5, pady=5)

        self._score_board = tk.Label(self.top_controls, text=self.score, bg="black",
                                     fg="yellow", font=("Helvetica", 15), width=5, relief="sunken")
        self._score_board.grid(row=1, column=1, padx=5, pady=5)

        self._start_button = tk.Button(self.top_controls, text="Start", command=self.start_action,
                                       font=("Helvetica", 12), bg="#1ABC9C", fg="white", width=7)
        self._start_button.grid(row=1, column=2, padx=5, pady=5)

        self._check_button = tk.Button(self.top_controls, text="Check", font=("Helvetica", 12),
                                       command=self.check_word, state=tk.DISABLED,
                                       bg="#27AE60", fg="white", width=7)
        self._check_button.grid(row=1, column=3, padx=5, pady=5)

        # Board frame inside left frame
        self.board_frame = tk.Frame(self.left_frame, bg="#34495E")
        self.board_frame.pack(pady=10)
        self._make_buttons()

        # Bottom controls in left frame (Quit and Remove)
        self.bottom_controls = tk.Frame(self.left_frame, bg="#34495E")
        self.bottom_controls.pack(pady=10)

        self._quit_button = tk.Button(self.bottom_controls, text="QUIT", font=("Helvetica", 12),
                                      bg="red", fg="white", command=self.root.quit, width=10)
        self._quit_button.grid(row=0, column=0, padx=10, pady=5)

        self._remove_button = tk.Button(self.bottom_controls, text="Remove", font=("Helvetica", 12),
                                        bg="orange", fg="black", state=tk.DISABLED,
                                        command=self.remove_action, width=10)
        self._remove_button.grid(row=0, column=1, padx=10, pady=5)

        # Found words Listbox in right frame with scrollbar
        self.correct_words_listbox = tk.Listbox(self.right_frame, width=30, height=20, font=("Helvetica", 12))
        self.correct_words_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.scrollbar = tk.Scrollbar(self.right_frame, orient="vertical", command=self.correct_words_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.correct_words_listbox.config(yscrollcommand=self.scrollbar.set)

        # Set icon (if available)
        try:
            photo = tk.PhotoImage(file="Boggle-icon.png")
            self.root.iconphoto(False, photo)
        except Exception as e:
            print(f"Icon not loaded: {e}")

    def run(self):
        self.root.mainloop()

    def _make_buttons(self):
        """Create board buttons."""
        self._buttons = {}
        rows = len(self.board)
        cols = len(self.board[0])
        for i in range(rows):
            for j in range(cols):
                btn = tk.Button(self.board_frame,
                                text=self.board[i][j],
                                font=("Arial", 14, "bold"),
                                bg="#3498DB", fg="white",
                                height=2, width=4,
                                command=self._buttons_action(i, j),
                                state=tk.DISABLED)
                btn.grid(row=i, column=j, padx=5, pady=5)
                self._buttons[(i, j)] = btn

    def _buttons_action(self, i, j):
        def command_for_specific_cell():
            if self._display_label["text"] == START_DISPLAY:
                self._display_label.config(text=self.board[i][j])
                self.selected_cells = [(i, j)]
            else:
                self._display_label.config(text=self._display_label["text"] + self.board[i][j])
                self.selected_cells.append((i, j))

        return command_for_specific_cell

    def start_action(self):
        def tick():
            if self.sec > 0:
                self.sec -= 1
                minutes, seconds = divmod(self.sec, 60)
                self.time.config(text=f"{minutes:02}:{seconds:02}")
                self.time.after(1000, tick)
                self._remove_button.config(state=tk.NORMAL)
                self._check_button.config(state=tk.NORMAL)
                self._start_button.config(state=tk.DISABLED)
                for btn in self._buttons.values():
                    btn.config(state=tk.NORMAL)
            else:
                decision = tkinter.messagebox.askyesno(title="Boggle", message="Do you want to play again?")
                self.root.destroy()
                if decision:
                    Boggle(board.randomize_board()).run()

        tick()

    def check_word(self):
        if self.selected_cells:
            valid = helper.is_valid_path(self.board, self.selected_cells, self.words)
            if valid and valid not in self.found_words:
                self.found_words.append(valid)
                self.correct_words_listbox.insert(0, valid)
                self.score += len(valid) ** 2
                self._score_board.config(text=self.score)
            self._display_label.config(text=START_DISPLAY)
            self.selected_cells = []

    def remove_action(self):
        if len(self.selected_cells) > 1:
            self.selected_cells.pop()
            new_text = "".join(self.board[i][j] for i, j in self.selected_cells)
            self._display_label.config(text=new_text)
        else:
            self._display_label.config(text=START_DISPLAY)
            self.selected_cells = []


if __name__ == "__main__":
    boggle = Boggle(board.randomize_board())
    boggle.run()
