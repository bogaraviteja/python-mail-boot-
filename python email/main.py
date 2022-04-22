# Python code to send email to a list of
# emails from a spreadsheet

# import the required libraries
import pandas as pd
import smtplib

# change these as per use
your_email = "ravitejaboga1998@gmail.com"
your_password = "XAKDJJKdsfgh"

# establishing connection with gmail
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)

# reading the spreadsheet
email_list = pd.read_excel('C:/Users/DELL/OneDrive/Desktop/python email/emails.xlsx')

# getting the names and the emails
names = email_list['NAME']
emails = email_list['EMAIL']

# iterate through the records
for i in range(len(emails)):

	# for every record get the name and the email addresses
	name = names[i]
	email = emails[i]

	# the message to be emailed
	message = "Hello " + name
	'''this is automated mail from a mail boot!'''

	# sending the email
	server.sendmail(your_email, [email], message)

# close the smtp server
server.close()
