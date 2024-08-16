def Happiness(total_score, people):
    return total_score/people


meet = {"Boss": "1",
        "Colleague_1": "5",
        "Colleague_2": "2",
        "Colleague_3": "8",
        "Colleague_4": "3",
        "Colleague_5": "6",
        "Colleague_6": "5"}

total_score = 0
people = 0
for position, score in meet.items():
    people += 1
    if position == "Boss":
        total_score += int(score)*2
    else:
        total_score += int(score)

if Happiness(total_score, people) <= 5:
    print("Get out now!")
else:
    print("Nice Work Champ!")
