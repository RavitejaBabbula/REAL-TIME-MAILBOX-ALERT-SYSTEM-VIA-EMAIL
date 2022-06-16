import smtplib
from email.message import EmailMessage
from datetime import datetime
from dateutil.tz import gettz
from datetime import date
now = datetime.now(tz=gettz('Asia/Kolkata'))
current_time = now.strftime("%H:%M:%S")
today = date.today()
current_day = today.strftime("%d/%m/%y")
User_name ="chatbot021@gmail.com"
Password = "Abhinaypal@98"

def Request_news():
    import requests
    from bs4 import BeautifulSoup as BS
    page = requests.get("https://cms.iare.ac.in/")
    contents = BS(page.content.decode(),"html.parser")
    News = (contents.find_all(class_ = "container")[3]).find_all('a')
    data =[]
    for x in News:
        contents = x.contents
        link = x.get('href').strip()
        news = contents[-1].contents[0].strip()
        data.append((link,news))
    return data


contents ="<body><h1> IARE EXAMINATION NEWS </h1><br>"
data = Request_news()
for x,y in data:
    contents+=f'<br><h4>{y} <a href = "{x}">..(more)</a><br><h4>'
contents+="</body>"




email = EmailMessage()
email['Subject'] = f' IARE EXAMINATION NEWS - Date : {current_day}   Time : {current_time}'
email['From'] = User_name
email['To'] = ["braviteja2910@gmail.com","tallakarthik50@gmail.com"]
email.set_content(contents, subtype='html')
#print(email)

# Send the message via local SMTP server.
with smtplib.SMTP('smtp.gmail.com',587) as s:
    s.starttls()
    s.login(User_name,Password)
    s.send_message(email)
