from bs4 import BeautifulSoup

with open('index.html', 'r') as htmlReading:
    content = htmlReading.read()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # aTags = soup.find_all('a')
    # print(aTags)
    # for tag in aTags:
    #     if (tag.text[:5] == 'Start'):
    #         print(tag.text[10:])
    cards = soup.find_all('div', class_='card')
    # print(cards);
    for card in cards:
        cardName = card.h5.text
        cardText = card.p.text
        cardRef = card.find_all('a')[-1].text
        cardPrice = cardRef.split(' ')[-1]
        print()
        # print(cardName)
        # print(cardPrice)
        print(f"{cardName} costs {cardPrice}")
