import smtplib
from email.message import EmailMessage

i= 0

while i < 5:

	email = EmailMessage()
	email['from'] = 'Meraj Sayed'
	email['to'] = 'mrj.ahmed22@gmail.com'
	email['subject'] = 'Do you know you are awesome ?'

	email.set_content('you are good programmer buddy')

	with smtplib.SMTP(host ='smtp.gmail.com' , port= 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login('syit026@rizvicollege.edu.in' , 'rizvicollege')
		smtp.send_message(email)
		print ('all done pal')

		i+=1
