def get_employees(personal):
    personal = ', '.join(personal)
    all_list = []
    for i in personal:
        all_list.extend(i)
    return (''.join(all_list))



