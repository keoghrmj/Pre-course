def boredom(staff):
    total_score = 0
    for departments in staff.values():
        for department, score in department_score.items():
            if departments == department:
                total_score += score
    if total_score <= 80:
        return "kill me now"
    elif total_score < 100 and total_score > 80:
        return 'i can handle this'
    else:
        return 'party time'


staff = {"tim": "IS", "jim": "finance",
         "randy": "pissing about", "sandy": "cleaning", "andy": "cleaning",
         "katie": "cleaning", "laura": "pissing about", "saajid": "regulation",
         "alex": "regulation", "john": "accounts", "mr": "canteen"}

department_score = {"accounts": 1, "finance": 2, "canteen": 10,
                    "regulation": 3, "trading": 6, "change": 6, "IS": 8,
                    "retail": 5, "cleaning": 4, "pissing about": 25}
print(boredom(staff))
