import json
from sqlalchemy.orm import Session
from database.models import Challenge
from database.db_connection import SessionLocal, get_mariadb_cursor
from collections import defaultdict

# ✅ Read Challenges from JSON & Insert into DB
def read_and_insert_challenges():
    files = ["challenges.json", "challenges2.json", "challenges3.json", "challenges4.json"]
    session = SessionLocal()
    added_count = 0

    for file_name in files:
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                
                for i in data['results']:
                    # ✅ Check if Challenge Exists
                    if session.query(Challenge).filter_by(name=i.get('name', 'Unknown')).first():
                        print(f"🔄 Challenge '{i.get('name', 'Unknown')}' already exists. Skipping...")
                        continue
                    
                    # ✅ Create & Insert Challenge
                    challenge = Challenge(
                        name=i.get('name', 'Unknown'),
                        author=i.get('author', 'Unknown'),
                        difficulty=i.get('difficulty', 'Unknown'),
                        event=(i.get('event') or {}).get('name', 'Unknown'),
                        category=(i.get('category') or {}).get('name', 'Unknown'),
                        solved_by_user=bool(i.get('solved_by_user', False)),
                        video_published=False,
                        post_published_medium=False
                    )

                    session.add(challenge)
                    added_count += 1

        except Exception as e:
            print(f"❌ Error processing {file_name}: {e}")

    session.commit()
    print(f"✅ {added_count} new challenges added (Duplicates skipped).")

# ✅ Get Total Challenges Count
def get_total_challenges():
    cur, _ = get_mariadb_cursor()
    cur.execute("SELECT COUNT(*) FROM challenges")
    return cur.fetchone()[0]

# ✅ Get Total Count Unsolved Challenges
def get_total_unsolved_challenges():
    cur, _ = get_mariadb_cursor()
    cur.execute("SELECT COUNT(*) FROM challenges WHERE solved_by_user = 0")
    return cur.fetchone()[0]

# ✅ Get Total List of Unsolved Challenges
def get_total_list_unsolved_challenges():
    cur, _ = get_mariadb_cursor()
    cur.execute("SELECT name, category, difficulty FROM challenges WHERE solved_by_user = 0")
    challenges = cur.fetchall()
    print_challenges(challenges)

# ✅ Get Total List of Unpublished Video Challenges
def get_total_list_unpublished_video_challenges():
    cur, _ = get_mariadb_cursor()
    cur.execute("SELECT name, category, difficulty FROM challenges WHERE video_published = 0")
    challenges = cur.fetchall()
    print_challenges(challenges)

# ✅ Calculate Percentage of Solved Challenges
def percentage_solved():
    total = get_total_challenges()
    not_solved = get_total_unsolved_challenges()
    solved_percentage = (1 - (not_solved / total)) * 100 if total else 0
    return f"{solved_percentage:.2f}% solved"

def add_challenge_video():
    name = input("Enter challenge name: ")
    session = SessionLocal()
    challenge = session.query(Challenge).filter_by(name=name).first()
    if challenge:
        challenge.video_published = True
        session.commit()
        print(f"Video for '{name}' marked as published!")
    else:
        print(f"Challenge '{name}' not found.")
    session.close()

def add_challenge_medium():
    name = input("Enter challenge name: ")
    session = SessionLocal()
    challenge = session.query(Challenge).filter_by(name=name).first()
    if challenge:
        challenge.post_published_medium = True
        session.commit()
        print(f"Medium post for '{name}' marked as published!")
    else:
        print(f"Challenge '{name}' not found.")
    session.close()

def print_challenges(challenges):
    categorized_challenges = defaultdict(lambda: defaultdict(list))
    
    # Organize challenges by category and difficulty
    for name, category, difficulty in challenges:
        categorized_challenges[category][difficulty].append(name)
    
    # Print formatted challenges
    for category, difficulties in sorted(categorized_challenges.items()):
        print(f"\n=== {category} ===")
        for difficulty in sorted(difficulties.keys(), key=int):
            print(f"\n  Difficulty {difficulty}:")
            for challenge in sorted(difficulties[difficulty]):
                print(f"    - {challenge}")