import json


def read_json(file):
    with open(file, 'r') as file:
        return json.load(file)


def list2dict(profs):
    res = dict()
    for prof in profs:
        if prof['user_id']:
            res[prof['user_id']] = prof
    return res


def save_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)


def get_year(year_id):
    year = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 9: 1, 10: 1, 11: 1, 12: 9}
    return year[year_id]


def main():
    sql = 'INSERT INTO COMMON_MEMBER (username, password, name, email, department_id, year_id, role, created_at, updated_at)\nVALUES '
    user_file, profile_file, result_file = '../datasets/common_member/auth_user.json', '../datasets/common_member/accounts_profile.json', '../sql/common_member.sql'
    users, profiles = read_json(user_file), read_json(profile_file)
    profiles = list2dict(profiles)
    for user in users:
        pk = user['id']
        if pk in profiles:
            profile = profiles[pk]
            username, password, email = user['username'], user['password'], user['email']
            name, department_id, year_id = profile['name'], profile['department_id'], get_year(profile['year_id'])
            sql += f"('{username}', '{password}', '{name}', '{email}', {department_id}, {year_id}, 'ROLE_USER', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),\n\t   "
    sql = sql[:-6]
    sql += ';\n\nCOMMIT;\n'
    save_file(sql, result_file)


if __name__ == "__main__":
    main()
