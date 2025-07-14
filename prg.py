import tkinter as tk
import random
choices = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}
user_score = 0
computer_score = 0
def play(choice_key):
    global user_score, computer_score

    you = choices[choice_key]
    computer = random.choice([-1, 0, 1])

    you_choice = reverseDict[you]
    comp_choice = reverseDict[computer]

    result = ""

    if computer == you:
        result = "It's a Draw! 😐"
    elif (computer == -1 and you == 1) or \
         (computer == 1 and you == 0) or \
         (computer == 0 and you == -1):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "You Lose! 😢"
        computer_score += 1

    user_choice_label.config(text=f"You: {you_choice}")
    computer_choice_label.config(text=f"Computer: {comp_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Snake Water Gun - Battle Game")
root.geometry("400x400")
root.configure(bg="#e0f7fa")

tk.Label(root, text="🐍💧🔫 Snake-Water-Gun", font=("Arial", 18, "bold"), bg="#e0f7fa").pack(pady=10)

button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(pady=20)

tk.Button(button_frame, text="🐍 Snake", font=("Arial", 12), width=10, command=lambda: play("s")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="💧 Water", font=("Arial", 12), width=10, command=lambda: play("w")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="🔫 Gun", font=("Arial", 12), width=10, command=lambda: play("g")).grid(row=0, column=2, padx=10)

user_choice_label = tk.Label(root, text="You: ", font=("Arial", 14), bg="#e0f7fa")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer: ", font=("Arial", 14), bg="#e0f7fa")
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="#00796b", bg="#e0f7fa")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 13), fg="#004d40", bg="#e0f7fa")
score_label.pack(pady=10)

tk.Button(root, text="Exit Game", font=("Arial", 12), bg="red", fg="white", command=root.destroy).pack(pady=10)

root.mainloop()
