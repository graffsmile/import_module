from datetime import datetime
from application.db.people import get_employees
from pprint import pprint
from application.salary import calculate_salary
from dotenv import load_dotenv
import os.path

dotenv_path = 'salary_info.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
salary_info = os.getenv('salary_info')

def statement(personal, salary_list):
    salary_all = []
    for p, s in zip(personal, salary_list):
        salary_dict = {'name':p, 'salary':s}
        salary_all.append(salary_dict)
    return salary_all


if __name__ == '__main__':
    personal = ['Иванов И.П.', 'Петров П.И.']
    salary_list = ['1000', '1500']
    date_now = datetime.now()
    print(get_employees(personal))
    print(calculate_salary(salary_list))
    print(datetime.date(date_now))
    pprint(f'{salary_info}: {statement(personal, salary_list)}')


