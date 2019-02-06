
def average_grade(roster):
    sum = 0
    for i in range(10):
        sum = sum + roster[i].get_grade()
    average = sum/10
    return average
