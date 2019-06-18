# Dependencies
from bs4 import BeautifulSoup,NavigableString, Tag
from lxml import html
import requests
import pymongo
import os
from splinter import Browser
from selenium import webdriver
import types
import re

str1=''

url = 'https://www.gallaudet.edu/research-support-and-international-affairs/international-affairs/world-deaf-information-resource/deaf-orgs/local-orgs/canada'
# Retrieve page with the requests module
response = requests.get(url)
print(response)

# Create BeautifulSoup object; parse with 'html.parser'
# soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(response.text, 'html.parser')

for br in soup.select('br'):
    br.replace_with('\n')
# print(soup.text.strip())



main = soup.div.find(id='main-content')
# print(main)
AddrList = []
# emailList=[]

# email = soup.select('a[href^="mailto"]')

for email in main.select('a[href^="mailto"]'):
    email.replace_with('mail ' + email.text)
    print('email',email.text)
    
for web in main.select('a[href^="http://"]'):
    web.replace_with('web' + web.text)
    print('web ',web.text)


# if (email):
#     for maillink in email:
#         print('mail',maillink.text)
#         email = 'mail ' + maillink.text + '\n'
#         emailList.append(maillink.text)
org = main.find_all('p')


i = 0
for o in org:

    

    if not ('Disclaimer' in o.text) and not ('Submit' in o.text):
        strings = o  
        i = 0
        for s in strings:
            
            # print(i,s)
            if i == 0:
                if (not 'Phone' in str1 and
                    not 'Fax' in str1 and
                    not 'TTY' in str1 and
                    not '+' in str1 and
                    not 'mail' in str1 and
                    not 'web' in str1):
                    organization = s
                    o = s
                    print('Organization:',organization)
    #                 print(strings)
            else:
#                 for move in s:
                # if s.nextSibling:
                #     # if not 'strong' in s.nextSibling :
                #     s = s.nextSibling
                    str1 = ''.join(str(e) for e in s)
                    if not (str1.isspace()):
                        # if not 'strong' in s:    
                            # print('Address:',s)
                            if (not 'Phone' in str1 and
                                not 'Fax' in str1 and
                                not 'TTY' in str1 and
                                not '+' in str1 and
                                not 'mail' in str1 and
                                not 'web' in str1 and
                                not 'http://' in str1 ):
                                print('AddrString',str1)   
                            elif ('http://' in str1 and
                                  'web' in str1 ):
                                  print('Web 2',str1)
                            else:
                                print('Contact',str1)
                                # if s.prevSibling:
                                #     print('Contact Prev',s.prev_Sibling)
            emailList=[]
            email = o.select('mail')
            if (email):
                for maillink in email:
                    print('mail',maillink.text)
                    # email = 'mail ' + maillink.text + '\n'
                    emailList.append(maillink.text)
            
            webLink=[]         
            web = o.select('a[href^="http://"]')
            for link in web:
                print('web',link.text)
                webLink.append(link.text.strip())
            
            description = None
            if not (o.select('em') is None):
                desc = o.select('em') 
                for orgDesc in desc:
                    description = orgDesc.text.strip()
                    print('Description2',description)                 
                
                
  
            i = i + 1
    
    

