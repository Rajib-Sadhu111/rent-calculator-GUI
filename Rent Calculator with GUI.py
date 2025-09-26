## Inputs from the user.
# Total rent
# Total food ordered for snacking
#  Electricity units spend
# Charge per unit
# persons living in room or flat

## Output 
# Total amount you have to pay is

import tkinter as tk

root = tk.Tk()
root.title("Rent Calculator")
root.geometry("400x400")
root.configure(background="light yellow")

    # rent = int(input("enter your hostel or flat rent: "))
    # food_odr = int(input("enter the amount of food ordered: "))
    # electricity_units = int(input("enter how much electricity units spend: "))
    # charge_per_unit = int(input("enter amount of charge per unit: "))
    # persons = int(input("how many people living in  room or flat: "))

header = tk.Label(root, text="Welcome to Rent Calculator", font=("Georgia", 25), foreground="dark blue")
header.pack()

rent = tk.Label(root,text="Enter your hostel or flat rent", font=("Aerial", 15))
rent.pack(pady=20)
rent = tk.Entry(root, font=("Aerial",10))
rent.pack()

food_odr = tk.Label(root, text="Enter the amount of food ordered", font=("Aerial", 15))
food_odr.pack(pady=10)
food_odr = tk.Entry(root, font=("Aerial",10))
food_odr.pack()

electricity_units = tk.Label(root, text="Enter how much electricity units spend", font=("Aerial", 15))
electricity_units.pack(pady=10)
electricity_units = tk.Entry(root, font=("Aerial",10))
electricity_units.pack()

charge_per_unit = tk.Label(root, text="Enter the amount of charge per unit", font=("Aerial", 15))
charge_per_unit.pack(pady=10)
charge_per_unit = tk.Entry(root, font=("Aerial",10))
charge_per_unit.pack()

persons = tk.Label(root, text="How many people living in room or flat", font=("Aerial", 15))
persons.pack(pady=10)
persons = tk.Entry(root, font=("Aerial",10))
persons.pack()

result_label = tk.Label(root, text="Result will show here", font=("Aerial", 20))
result_label.pack(pady=20)


def rent_calc():
  try:
    total_amount = int(rent.get()) + int(food_odr.get()) + (int(electricity_units.get()) * int(charge_per_unit.get()))//int(persons.get())
    
    result_label.config(text=f"Each person has to pay: {total_amount}")

  except ValueError:
    print("you have to only enter numerical values.")

  except ZeroDivisionError:
    print("please enter correct value that how many persons living.")
  

btn = tk.Button(root, text="Calculate", font=("Aerial",15), command=rent_calc)
btn.pack(pady=15)


root.mainloop()
