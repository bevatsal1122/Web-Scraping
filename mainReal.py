from ast import keyword
from bs4 import BeautifulSoup
import requests

keywords = input("Enter Keywords: ")
keywords = keywords.replace(' ', '+');

requestPage = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=' + keywords + '&txtLocation='
def ignoreSpaces(text):
   word = ''
   i = False
   for letter in text:
      if (letter.isalpha() or (i and letter != '\n')):
         word += letter
         i = True
      else:
         i = False
   return word; 

htmlText = requests.get(requestPage).text
soup = BeautifulSoup(htmlText, 'lxml')
ulTag = soup.find('ul', class_="new-joblist")
liTags = ulTag.find_all('li', class_="clearfix job-bx wht-shd-bx")

for liTag in liTags:
   title = liTag.find('h2')
   companyName = liTag.find('h3')
   skills = liTag.find('span', class_="srp-skills")

   ulInner = liTag.find('ul', class_="top-jd-dtl clearfix")
   liInner = ulInner.find_all('li')
   # print(title.text)
   propName = ignoreSpaces(companyName.text)
   propTitle = ignoreSpaces(title.text)
   propSkills = ignoreSpaces(skills.text)

   print('\n')
   print(f"Company Name: {propName}\nJob Title: {propTitle}\nSkills Requirement: {propSkills}")

   location=""
   if (len(liInner) >= 3):
      propCTC = ignoreSpaces(liInner[1].text)
      location = liInner[2].find('span')
      print(f"Job CTC Range: {propCTC}")
   else:
      location = liInner[1].find('span')

   propLocation = ignoreSpaces(location.text)
   print(f"Job Location: {propLocation}")
