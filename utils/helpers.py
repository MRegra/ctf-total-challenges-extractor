from database.db_connection import engine
from database.models import create_tables
from services.challenge_service import read_and_insert_challenges, percentage_solved, get_total_list_unsolved_challenges, get_total_list_unpublished_video_challenges

def menu():
    while True:
        print("\n=== Challenge Tracker Menu ===")
        print("1. Create Database & Tables")
        print("2. Read & Write challenges from files")
        print("3. Add Challenge Video Published")
        print("4. Add Challenge Medium Published")
        print("5. Print Solved Challenges Percentage")
        print("6. Print Unsolved Challenges")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # ✅ Create Tables if Needed
            create_tables(engine)
        elif choice == "2":
            # ✅ Insert Challenges from JSON
            read_and_insert_challenges()
        elif choice == "3":
            # add_challenge_video()
            print(3)
        elif choice == "4":
            # add_challenge_medium()
            print(4)
        elif choice == "5":
            # ✅ Show Solved Percentage
            print(percentage_solved())
        elif choice == "6":
            get_total_list_unsolved_challenges()
        elif choice == "7":
            get_total_list_unpublished_video_challenges()
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")

