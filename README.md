🪨 Rock Paper Scissors – Python Game

A simple **Rock, Paper, Scissors** game built using **Python**, where you play against the computer in the terminal.  
This project is beginner-friendly and focuses on **conditionals, user input, randomness, and ASCII art**.

---

## 🎮 How the Game Works

1. The user selects one option:
   - `rock`
   - `paper`
   - `scissors`
2. The computer randomly chooses one option.
3. The program compares both choices.
4. The result is displayed:
   - You Win 🎉
   - Computer Wins 🤖
   - It's a Tie 🤝
5. Both choices are shown using **ASCII art** for better visualization.

---

## 🧠 Concepts Used

- `input()` for user interaction
- `random.choice()` for computer selection
- Lists
- Conditional statements (`if`, `elif`, `else`)
- String formatting
- ASCII art printing

---

## 🗂️ Project Structure

rock-paper-scissors/
│
├── rock_paper_scissors.py
└── README.md

yaml
Copy code

---

## ▶️ How to Run the Game

1. Make sure **Python 3** is installed.
2. Clone the repository or download the file.
3. Run the script:

```bash
python rock_paper_scissors.py
🕹️ Sample Input
java
Copy code
Enter your choice (rock, paper, scissors): rock
🖥️ Sample Output
yaml
Copy code
Welcome to Rock, Paper, Scissors!
Computer chose: scissors
You win!

your choice: rock
[rock ASCII art]

computer choice: scissors
[scissors ASCII art]
🚫 Invalid Input Handling
If the user enters anything other than:

rock

paper

scissors

The program will show:

python
Copy code
Invalid choice! Please choose rock, paper, or scissors.
✨ Future Improvements (Optional)
Add a score system

Allow multiple rounds

Add play again option

Convert to a GUI version

👨‍💻 Author
Mohit


