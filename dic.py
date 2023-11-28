
employee_info = {
    "Name": "gokul",
    "Last Name": "N",
    "Address": "india",
    "Job": {"frontend", "Developer"},
    "Age": 34,
    "Hobbies": ("Reading", "Wacthing Movies", "Walking"),
    2002: "Date of Birth",
    "Married": False,
    "Favorite Songs": ["Un Dia", "Blinding Lights", "Shallow"],
    "Best Friend": {"Name": "rajesh"},
    "Special One": None
}

# ----->clear()
# employee_info.clear()
# print(employee_info)

# # -----copy()

# shan = employee_info.copy()
# shan["Best Friend"] = "gokul"
# print(shan)

# # -----fromkeys()
 
letter = {'a','e','i','o','u'}
number = [1,2]

vowles = dict.fromkeys(letter) 
print(vowles)

