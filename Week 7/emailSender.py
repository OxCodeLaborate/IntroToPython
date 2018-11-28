import smtplib
import pandas as pd

"""
This program opens a .csv file called "starterQuiz.csv" and writes an email to each person with their contact information in the csv.


Necessary Columns in csv:
    Description
    Email Address
"""


df = pd.read_csv("starterQuiz.csv")
sender_email = # enter an email here
password = # Sorry, not giving you my password
email_column = "Email Address"

# Set Main Message
subject = "You Debugging Partners"
template = """
Dear {Name},
Thank you for joining us at CodeSoc today! Glad to hear you're interested in learning to program. Your partners have described themselves as:

    {desc2}
    {desc1}
    and {desc0}

Good luck finding your debugging partners. Programming -- despite the sterotypes -- is done best in a group :)

Regards,
William's Partner-Matcher

P.S. You should have 3 partners. If you do not have a full set of partners, then please find a group to join!
"""

# Write Columns

columns = []
for column in df:
    columns.append(column)
columns

# Group the data

data = []
for i in range(df.shape[0]):
    data.append(i//4)

df.insert(value = data, column = 'Group', loc = df.shape[1])

# Log in

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)    # If it returns an error, try 465
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(sender_email, password)

for i in range(df.shape[0]):
    recipient_email = df[email_column][i]
    insertions = {}
    for column in columns:
        insertions[column] = df[column][i]
    otherMembers = (df['Group'] == df['Group'][i]) & (df.index != df.index[i])
    for j in range(3):
        insertions['desc{}'.format(j)] = ''
    for j in range(sum(otherMembers)):
        member = df.loc[otherMembers]
        insertions['desc{}'.format(j)] = member['Description'].values[j]
    try:
        body = template.format(**insertions)
        sent_status = smtpObj.sendmail(sender_email, recipient_email, """Subject: {} \n {}""".format(subject, body))
        if sent_status == {}:
            print("{}. Email to {} was successfully sent".format(str(i), recipient_email))
        else:
            print("{}. An error occurred and an email was not sent to {}".format(str(i), recipient_email))
    except Exception as e:
        print("Exception: {}".format(e))

smtpObj.quit()



