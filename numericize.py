def numericize_gender(row):
        if row["gender_normalized"] == "Male":
            return 1
        elif row["gender_normalized"] == "Female":
            return 0
        else:
            return None
    
def numericize_difficulty(row, attribute):
    if row[attribute] == "Very difficult":
        return 1
    elif row[attribute] == "Somewhat difficult":
        return 2/3
    elif row[attribute] == "Somewhat easy":
        return 1/3
    elif row[attribute] == "Very easy":
        return 0
    else:
        return None
    
def numericize_yes_no(row, attribute):
    if row[attribute] == "Yes":
        return 1
    elif row[attribute] == "No":
        return 0
    elif row[attribute] == "Maybe":
        return 0.5
    elif row[attribute] == "Some of them":
        return 0.5
    else:
        return None

def numericize_no_employees(row, attribute):
    if row[attribute] == "1-5":
        return 0
    elif row[attribute] == "6-25":
        return 1/5
    elif row[attribute] == "26-100":
        return 2/5
    elif row[attribute] == "100-500":
        return 3/5
    elif row[attribute] == "500-1000":
        return 4/5
    elif row[attribute] == "More than 1000":
        return 1
    else:
        return None
    
def numericize_frequency(row, attribute):
    if row[attribute] == "Often":
        return 1
    elif row[attribute] == "Sometimes":
        return 2/3
    elif row[attribute] == "Rarely":
        return 1/3
    elif row[attribute] == "Never":
        return 0/3
    else:
        return None