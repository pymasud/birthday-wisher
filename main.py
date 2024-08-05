from datetime import datetime
import pandas
import random
import smtplib

# 1. Update the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="yynodia@gmail.com", password="oumb dbhm bztc dlmu")
            connection.sendmail(from_addr="yynodia@gmail.com", to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")