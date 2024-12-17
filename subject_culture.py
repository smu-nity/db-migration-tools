import json
import os


def read_json(file):
    with open(file, 'r') as file:
        return json.load(file)


def save_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)


def culture(path, domain):
    sql, insert = '', 'INSERT INTO subject_culture (sub_domain, credit, name, number)\nVALUES '
    sub_domain = domain.split('.')[0]
    datas = read_json(os.path.join(path, domain))
    for data in datas:
        name, number, credit = data['name'], data['number'], data['credit']
        sql += f"{insert}('{sub_domain}', {credit}, '{name}', '{number}');\n"
    return sql


def main():
    sql = ''
    dataset_path, result_file = 'datasets/subject_culture', 'sql/subject_culture.sql'
    domains = os.listdir(dataset_path)
    for domain in domains:
        sql += culture(dataset_path, domain)
    save_file(sql, result_file)


if __name__ == "__main__":
    main()
