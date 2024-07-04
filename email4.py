import smtplib
import speech_recognition as sr
import pyttsx3
import easyimap as e 

unm="yashbachhe1@gmail.com"
pwd="lorb igly jycq velg"
from email.message import EmailMessage
listener= sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
    engine.say(text)
    print (text)
    engine.runAndWait()
def get_info():
    try:
        with sr.Microphone() as source:
            talk("speak now")
            print('Listening...')
            #talk("speak now")
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
        
    except:
      talk ("sorry could not recognize what you said")
def send_email(reciever,subject,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    #put your email address and password
    server.login("yashbachhe1@gmail.com","lorb igly jycq velg")
    email=EmailMessage()
    email['From']='Sender_Email'
    email['TO']=reciever
    email['Subject']=subject
    email.set_content(message)
    server.send_message(email)
email_list= {
    'chetan': 'surashechetan@gmail.com',
    'rahul':'waghmarerahul716@gmail.com'
}

def get_email_info():
    str="Who do you want to send this email too"
    talk(str)
    name=get_info()
    receiver=email_list [name]
    print(receiver)
    talk(receiver)
    talk('What is the subject of your email?')
    subject=get_info()
    talk('your subject is.')
    talk(subject)
    talk('Tell me the message you what to send in your email')
    message=get_info()
    talk('Your message is.')
    talk(message)
    send_email(receiver,subject,message)
    print ("sending email...")
    talk('Dear user your message send successfully!')
    talk('Do you want to send more emails?')
    send_more=get_info()
    if 'yes' in send_more:
        get_email_info()

    #talk('have good day')

#get_email_info()
def readmail():
  server = e.connect("imap.gmail.com",unm,pwd)
  server.listids()
  str="please say the serial number of the email you want to read starting from latest"
  talk(str)

  a=get_info()
  if(a=="Tu"):
      a="2"
  b=int(a)-1
  email=server.mail(server.listids()[a])

  str="The email is from: "
  talk(str)
  talk(email.from_addr)
  str="The subject of the email is : "
  talk(str)
  talk(email.body)

while(1):
    str="what do you want to do?"
    talk(str)

    str="speak SEND to send mail    speak READ to read Inbox    speak EXIT to exit"
    talk(str)
    ch=get_info()

    if(ch=='send'):
        str="you have chossen to send email"
        talk(str)
        get_email_info()
    
    elif(ch=='read'):
        str="you have chossen to read email"
        talk(str)
        readmail()

    elif(ch=='exit'):
        str="you have chossen to exit from email,bye bye , have a good day"
        talk(str)
        exit()
    
    