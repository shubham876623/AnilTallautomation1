
import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
import re
username = 'shubhamsaini8766@gmail.com'
password = 'nareshlal890'


def get_otp():
    otp = []
    
    # create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)
    
    status, messages = imap.select("Inbox")
    # number of top emails to fetch
    N = 1
    # total number of emails
    messages = int(messages[0])
    
    for i in range(messages, messages - N, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # print(str(msg))
                soup=BeautifulSoup(str(msg),'html.parser')
                str1=soup.find('span').text
                # print(int(filter(str.isdigit, str1)))
                print(re.findall("\d+", str1)[0])
                return re.findall("\d+", str1)[0]
                
                
        
    imap.close()
    imap.logout()