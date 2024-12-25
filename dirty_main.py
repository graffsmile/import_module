from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    personal = ['Иванов И.П.', 'Петров П.И.']
    salary_list = ['1000', '1500']
    get_employees(personal)
    calculate_salary(salary_list)