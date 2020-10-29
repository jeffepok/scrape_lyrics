from bs4 import BeautifulSoup
import requests
import csv
def scrape():
    source = requests.get('http://lyrics.ghospel.com/akan-songs/').text
    soup = BeautifulSoup(source, 'lxml')
    with open('lyrics_scrape.csv', 'w', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', lineterminator = '+++')
        spamwriter.writerow(['song_title', 'lyrics'])
        links = soup.find('div', 'p', 'title', class_ = 'entry-content clearfix')
        for link in links.find_all('a'):
            lyrics_page = requests.get(link.get('href')).text
            lyrics_soup = BeautifulSoup(lyrics_page, 'lxml')
            lyrics = lyrics_soup.find('div', class_ = 'entry-content clearfix').text
            song_title = lyrics_soup.title.text
            spamwriter.writerow([song_title, lyrics])
if __name__ == '__main__':
    scrape()
