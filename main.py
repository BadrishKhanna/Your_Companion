def main():
    print("Your Companion")
    print("What do you want to do? (Typing test/Math/Expense Tracker/Tic-Tac-Toe/Art)")
    choice = input("Enter any one from the above choices: ").lower()

    if choice == "typing test":
        import Speed
        Speed.speed()
    elif choice == "math":
        import Math
        Math.math()
    elif choice == "expense tracker":
        import Expense
        Expense.expense()
    elif choice == "tic-tac-toe":
        import Game
        Game.game()
    elif choice == "art":
        import Art
        Art.art()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
  