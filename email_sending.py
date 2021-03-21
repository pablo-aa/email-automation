'''
	Author: Pablo Arruda Araujo
	Code :  Python code to send emails automatically using SMTP email Protocol
'''

# Creating Message Body
def create_message(name, message, personal_info):
	return f'''
		<p>Olá {name}, </p>
		<p>{message}</p>
		<p>{personal_info}<p>
	'''

# Sending Email
def envia_email(corpo_email, dest):

	msg = email.message.Message()
	msg['Subject'] = 'Sending email with Python'
	  
	msg['From'] = 'email@gmail.com'
	msg['To'] = dest
	password = "****" # Enter your password here
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(corpo_email)
	  
	# It's important to configure email to accept this kind of operation.
	# Gmail example: manage your account - security - access to low security apps

	s = smtplib.SMTP('smtp.gmail.com: 587') 
	s.starttls()
	# Login Credentials for sending the mail
	s.login(msg['From'], password)
	s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


import pandas as pd
import smtplib
import email.message

df_names = pd.read_excel('example.xlsx')

for idx, row in df_names.iterrows():
	corpo_email = create_message(row['Name'], row['Message'], row['Personal_info'])
	try:
		envia_email(str(corpo_email), str(row['Email'].strip()))
		print('Success ✨: '+ row['Name'] + ', '+row['Email'])
	except:
		print('Error in email ❗️'+row['Email'])
