import smtplib
from email.message import EmailMessage


	email = EmailMessage()
	email['from'] = 'Yourname'
	email['to'] = 'abc@abc.com'
	email['subject'] = 'Do you know you are awesome ?'

	email.set_content('you are good programmer buddy')

	with smtplib.SMTP(host ='smtp.gmail.com' , port= 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login('xxx@abc.com' , 'YourPassword')
		smtp.send_message(email)
		print ('all done pal')


