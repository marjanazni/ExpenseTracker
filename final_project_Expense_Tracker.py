import csv
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from calculations import calculate, calc_tot_exp, tot_rent_exp, tot_food_exp, tot_drinks_exp, tot_travel_exp, \
    tot_personal_exp, tot_other_exp
import matplotlib
matplotlib.use("TkAgg")


layout = [
    [sg.Text("Enter your income / expense:\n")],
    [sg.CalendarButton("Calendar", size=(14, 1)), sg.Input(do_not_clear=False)],
    [sg.Text("Item", size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text("Amount", size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text("Category", size=(15, 1)), sg.InputCombo(("income", "rent & bills expense", "food expense",
                                                       "drinks expense", "travel expense", "personal care expense",
                                                       "other expense"), size=(20, 1))],
    [sg.Text("")],
    [sg.Submit("Submit"), sg.Cancel()],
]

window = sg.Window("Welcome to EXPENSE TRACKER", layout)


def saving_to_csv():
    with open("expenses.csv", mode="a", newline="") as csv_file:
        fieldnames = ["Date", "Item", "Amount", "Category"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({"Date": values[0], "Item": values[1], "Amount": values[2], "Category": values[3]})
    print(values[0], values[1], values[2], values[3])


tot_income = calculate()
tot_expenses = calc_tot_exp()

print(f"Total income in EURO: {tot_income:.2f}")
print(f"Total expenses in EURO: {tot_expenses:.2f}")
percent_of_tot_expenses = (tot_expenses/tot_income) * 100
print(f"Percent of total expenses by income: {percent_of_tot_expenses:.2f}")

tot_expenses = calc_tot_exp()
total_rent_expenses = tot_rent_exp()

print(f"Total rent & bills expenses in EURO: {total_rent_expenses:.2f}")
percent_of_rent_expenses = (total_rent_expenses/tot_expenses) * 100
print(f"Percent of total rent & bills expenses of all expenses: {percent_of_rent_expenses:.2f}")

tot_expenses = calc_tot_exp()
total_food_expenses = tot_food_exp()

print(f"Total food expense in EURO: {total_food_expenses:.2f}")
percent_of_food_expenses = (total_food_expenses/tot_expenses) * 100
print(f"Percent of total food expenses of all expenses: {percent_of_food_expenses:.2f}")

tot_expenses = calc_tot_exp()
tot_drinks_expenses = tot_drinks_exp()

print(f"Total drinks expense in EURO: {tot_drinks_expenses:.2f}")
percent_of_drinks_expenses = (tot_drinks_expenses / tot_expenses) * 100
print(f"Percent of total drinks expenses of all expenses: {percent_of_drinks_expenses:.2f}")

tot_expenses = calc_tot_exp()
tot_travel_expenses = tot_travel_exp()

print(f"Total travel expenses in EURO: {tot_travel_expenses:.2f}")
percent_of_travel_expenses = (tot_travel_expenses / tot_expenses) * 100
print(f"Percent of total travel expenses of all expenses: {percent_of_travel_expenses:.2f}")

tot_expenses = calc_tot_exp()
tot_personal_care_expenses = tot_personal_exp()

print(f"Total personal care expense in EURO: {tot_personal_care_expenses:.2f}")
percent_of_personal_care_expenses = (tot_personal_care_expenses / tot_expenses) * 100
print(f"Percent of total personal care expenses of all expenses: {percent_of_personal_care_expenses:.2f}")

tot_expenses = calc_tot_exp()
tot_other_expenses = tot_other_exp()

print(f"Total other expense in EURO: {tot_other_expenses:.2f}")
percent_of_other_expenses = (tot_other_expenses / tot_expenses) * 100
print(f"Percent of total other expenses of all expenses: {percent_of_other_expenses:.2f}")


while True:
    event, values = window.read()
    if event == "Submit" or event == sg.Submit():
        saving_to_csv()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        calculate()
        break

window.close()

layout = [
    [sg.Text("ANALYSIS OF EXPENSES BY CATEGORY IN PERCENT\n")],
    [sg.Text("Total income in EURO:", size=(30, 1)), sg.Text(calculate())],
    [sg.Text("Total expenses in EURO:", size=(30, 1)), sg.Text(calc_tot_exp())],
    [sg.Text("Total expenses %:", size=(30, 1)), sg.Text(percent_of_tot_expenses)],
    [sg.Text("")],
    [sg.Text("Rent & bills expenses %:", size=(30, 1)), sg.Text(percent_of_rent_expenses)],
    [sg.Text("Food expenses %:", size=(30, 1)), sg.Text(percent_of_food_expenses)],
    [sg.Text("Drinks expenses %:", size=(30, 1)), sg.Text(percent_of_drinks_expenses)],
    [sg.Text("Travel expenses %:", size=(30, 1)), sg.Text(percent_of_travel_expenses)],
    [sg.Text("Personal care expenses %:", size=(30, 1)), sg.Text(percent_of_personal_care_expenses)],
    [sg.Text("Other expenses %:", size=(30, 1)), sg.Text(percent_of_other_expenses)],
    [sg.Text("")],
    [sg.Cancel("Continue")],
]

window = sg.Window("Analysis", layout)

while True:
    event, values = window.read()
    if event == "Continue" or event == sg.WIN_CLOSED:
        break

window.close()

data = {"Rent & bills": percent_of_rent_expenses, "Food": percent_of_food_expenses,
        "Drinks": percent_of_drinks_expenses, "Travel": percent_of_travel_expenses,
        "Personal care": percent_of_personal_care_expenses, "other": percent_of_other_expenses}

category = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))
plt.bar(category, values, color=("red", "orange", "yellow", "green", "blue", "gray"), width=0.5)
plt.xlabel("CATEGORY OF EXPENSE")
plt.ylabel("EXPENSE IN % OF ALL EXPENSES")
plt.title("ANALYSIS OF EXPENSES BY CATEGORY IN PERCENTAGE")
plt.show()
