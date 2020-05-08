import smtplib

# ['Spider-Man','Captain America','Thor','Iron Man']
 name1= ['Spider-Man','Captain America','Thor','Iron Man']
 name2= ['The Hulk','Black Panther','Doctor Strange']
# ['The Hulk','Black Panther','Doctor Strange']
 name3=name1+name2
# create 2 list
# name1 , name2 , name3

# concatenate all the iteams in name3

# add your name (append it)
name3.append('Mitanshi Rajput')
# now we need non magical super hero's so you will remove  'Doctor Strange'
name3.remove('Doctor Strange')
# 9 super hero's

#Power_points = {'Spider-Man': 70 , 'Captain America': 70 ,
#               'The Thor': 85,'Iron Man': 50,
#               'The Hulk':70,'Black Panther': 66,'your super hero name here eg the coder ': 90}
Power_points = {'Spider-Man': 70 , 'Captain America': 70 , 'The Thor': 85,'Iron Man': 50, 'The Hulk':70,'Black Panther': 66,
                'Mitanshi Rajput': 90}
Most_powerful_hero = max(Power_points,key = Power_points.get)
# find max Power points
# Most_powerful_hero = max(Power_points,key = Power_points.get)
# split first and last
f=Most_powerful_hero.split(' ')
# first name
first_name=f[0]
# last name
last_name=f[1]
# full = last name + " " +first name
full_name=last_name+ " " +first_name
# hero_name = full name.upper
hero_name = full_name.upper
# coder the real name
# email
# email password
# code is below use as it is 

gmail_user = "cu.18bcs1020@gmail.com"
gmail_pwd = "18BCS10204&"
TO = ['shantam1230@gmail.com']
SUBJECT = "Bonus task by your name "
TEXT = "Testing...... sending mail using Gmail with the help of python..." + hero_name + " Link to your branch file here"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
for i in range(len(TO)):
    BODY = '\r\n'.join(['To: %s' % TO[i],
                        'From: %s' % gmail_user,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    server.sendmail(gmail_user, [TO[i]], BODY)
    print('email sent to '+ str(TO[i]))

server.close()

