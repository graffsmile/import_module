def calculate_salary(salary_list):
    salary_list = ', '.join(salary_list)
    salary = []
    for i in salary_list:
        salary.extend(i)
    return (''.join(salary))
