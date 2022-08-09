from bs4 import BeautifulSoup
import requests

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

htmlText = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(htmlText, 'lxml')
ulTag = soup.find('ul', class_="new-joblist")
liTags = ulTag.find_all('li')
for liTag in liTags:
   titles = liTag.find_all('h2')
   companyName = liTag.find('h3')
   location = liTag.find('span')
   skills = liTag.find('span', class_="srp-skills")
   for title in titles:
      # print(title.text)
      propName = ignoreSpaces(companyName.text)
      propTitle = ignoreSpaces(title.text)
      propSkills = ignoreSpaces(skills.text)
      propLocation = ignoreSpaces(ignoreSpaces(location.text))
      print()
      print("Company Name: " + propName  + "\nJob Title: " + propTitle + "\nSkills Requirement: " + propSkills + "\nJob Location: " + propLocation);

