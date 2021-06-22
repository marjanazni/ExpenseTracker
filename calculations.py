import csv


def calculate():
    total_income = []

    with open("expenses.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            if row[3] == "income":
                total_income.append(float(row[2]))

    return sum(total_income)


def calc_tot_exp():
    total_expenses = []

    with open("expenses.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            if row[3] != "income":
                total_expenses.append(float(row[2]))

    return sum(total_expenses)


def tot_rent_exp():
    tot_rent_expenses = []

    with open("expenses.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            if row[3] == "rent & bills":
                tot_rent_expenses.append(float(row[2]))

    return sum(tot_rent_expenses)


def tot_food_exp():
    tot_food_expenses = []

    with open("expenses.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            if row[3] == "food expense":
                tot_food_expenses.append(float(row[2]))

    return sum(tot_food_expenses)


def tot_drinks_exp():
    total_drinks_expenses = []

    with open("expenses.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            if row[3] == "drinks expense":
                total_drinks_expenses.append(float(row[2]))

    return sum(total_drinks_expenses)


def tot_travel_exp():
    total_travel_expenses = []

    with open("expenses.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            if row[3] == "travel expense":
                total_travel_expenses.append(float(row[2]))

    return sum(total_travel_expenses)


def tot_personal_exp():
    total_personal_care_expenses = []

    with open("expenses.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            if row[3] == "personal care expense":
                total_personal_care_expenses.append(float(row[2]))

    return sum(total_personal_care_expenses)


def tot_other_exp():
    total_other_expenses = []

    with open("expenses.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            if row[3] == "other expense":
                total_other_expenses.append(float(row[2]))

    return sum(total_other_expenses)
