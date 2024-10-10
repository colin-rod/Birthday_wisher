import pandas as pd
import datetime as dt
import os
import smtplib
import random

my_email = "testyt439@gmail.com"
password = "tvywvibqttdrqajr"


#Load csv file
df = pd.read_csv("birthdays.csv")

#Get current date
today_day = dt.datetime.now().day
today_month = dt.datetime.now().month

# Get rows where day and month match today
todays_bday_list = df[(df['day']==today_day) & (df['month']==today_month)]

#Get letter template
all_letters=os.listdir("letter_templates")

#create random personalised letter
def get_letter(name):
    random_letter = random.choice(all_letters)
    with open (os.path.join("letter_templates",random_letter),'r') as file:
        letter_content = file.read()
    personal_letter = letter_content.replace("[NAME]",name)
    return personal_letter

#Send email
def send_email(content,email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{content}"
                            )

for index, row in todays_bday_list.iterrows():
    name = row['name']
    email = row['email']
    new_letter = get_letter(name)
    send_email(new_letter,email)





