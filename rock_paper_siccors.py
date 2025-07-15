import random

# Emojis for choices
emoji_map = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

# Score
user_score = 0
computer_score = 0

# Valid choices
choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

print("🎮 Welcome to Rock-Paper-Scissors Game!")

while True:
    print("\n👉 Choose rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("⚠️ Invalid choice. Try again!")
        continue

    computer_choice = random.choice(choices)

    print(f"\n🧍 You chose: {user_choice} {emoji_map[user_choice]}")
    print(f"💻 Computer chose: {computer_choice} {emoji_map[computer_choice]}")

    result = get_winner(user_choice, computer_choice)

    if result == "tie":
        print("😐 It's a tie!")
    elif result == "user":
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("😞 Computer wins this round!")
        computer_score += 1

    print(f"\n📊 Score: You {user_score} 🆚 Computer {computer_score}")

    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\n👋 Thanks for playing!")
        break

