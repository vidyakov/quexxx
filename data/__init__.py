import json
import os


PATH_ANSWERS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'answers.json')
PATH_QUESTIONS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions.json')
PATH_USERS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.json')


with open(PATH_ANSWERS, 'r', encoding='utf-8') as file:
    ANSWERS = json.load(file)

with open(PATH_QUESTIONS, 'r', encoding='utf-8') as file:
    QUESTIONS = json.load(file)

with open(PATH_USERS, 'r', encoding='utf-8') as file:
    USERS = json.load(file)


def save_user(user_id: int, first_name: str,  username: str):
    USERS.update({
        str(user_id): {
            'name': first_name,
            'user': username,
            'stickers': []
        }
    })
    with open(PATH_USERS, 'w', encoding='utf-8') as users_file:
        json.dump(USERS, users_file, indent=4)


def add_sticker(user_id, sticker_id):
    USERS[str(user_id)]['stickers'].append(sticker_id)
    with open(PATH_USERS, 'w', encoding='utf-8') as users_file:
        json.dump(USERS, users_file, indent=4)


def is_sticker_at_user(user_id, sticker_id):
    return sticker_id in USERS[str(user_id)]['stickers']


def get_user_stickers(user_id):
    return USERS[str(user_id)]['stickers']


def get_all_users() -> []:
    return USERS.keys()


def count_users() -> int:
    return len(USERS)


if __name__ == '__main__':
    print(PATH_ANSWERS)
    print(PATH_QUESTIONS)
    print(PATH_USERS)
