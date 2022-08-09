from bs4 import BeautifulSoup
import requests

keywords = ''
while keywords == '': 
   keywords = input("Enter Keywords: ")
   keywords = keywords.replace(' ', '+')

blacklist = input("Enter Skills to blacklist: ")
blacklist = blacklist.split(' ')

requestPage = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=' + keywords + '&txtLocation='

htmlText = requests.get(requestPage).text
soup = BeautifulSoup(htmlText, 'lxml')
ulTag = soup.find('ul', class_="new-joblist")
liTags = ulTag.find_all('li', class_="clearfix job-bx wht-shd-bx")

for index, liTag in enumerate(liTags):
   title = liTag.find('h2')
   detailsLink = liTag.header.h2.a['href']
   companyName = liTag.find('h3')
   skills = liTag.find('span', class_="srp-skills")

   ulInner = liTag.find('ul', class_="top-jd-dtl clearfix")
   liInner = ulInner.find_all('li')

   # print(title.text)

   dontshow = True
   propName = companyName.text.strip()
   propTitle = title.text.strip()
   propSkills = skills.text.strip()
   propDetailsLink = detailsLink.strip()

   for blackSKill in blacklist:
      if blackSKill == '' or blackSKill == ' ':
         break
      if (blackSKill in propSkills):
         dontshow = False
         break

   if dontshow:
      with open("posts/jobFile.txt", 'a') as file:
         file.write(f"Company Name: {propName}\nJob Title: {propTitle}\nSkills Requirement: {propSkills}")

         location=""
         if (len(liInner) >= 3):
            propCTC = liInner[1].text.strip().replace('₹', '')
            location = liInner[2].find('span')
            file.write(f"Job CTC Range: {propCTC}")
         else:
            location = liInner[1].find('span')

         propLocation = location.text.strip()
         file.write(f"Job Location: {propLocation}\nMore Job Details: {propDetailsLink}\n\n")

print("Job Information Saved in jobFile.text")
