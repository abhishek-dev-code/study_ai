import json
import os

FILE = "user_profile/history.json"

def save_user_history(user_id, question, answer):
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump({}, f)

    with open(FILE, "r") as f:
        data = json.load(f)

    if user_id not in data:
        data[user_id] = []

    data[user_id].append({"question": question, "answer": answer})

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_user_history(user_id):
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        data = json.load(f)

    return data.get(user_id, [])
