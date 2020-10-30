from bs4 import BeautifulSoup
import requests
import pandas as pd
def scrape():
    source = requests.get('http://lyrics.ghospel.com/akan-songs/').text
    soup = BeautifulSoup(source, 'lxml')
    links = soup.find('div', 'p', 'title', class_ = 'entry-content clearfix')
    song_title_list = []
    lyrics_list = []
    for link in links.find_all('a'):
        lyrics_page = requests.get(link.get('href')).text
        lyrics_soup = BeautifulSoup(lyrics_page, 'lxml')
        lyrics = lyrics_soup.find('div', class_ = 'entry-content clearfix').text
        song_title_list.append(lyrics_soup.title.text)
        lyrics_list.append(lyrics)
    all_lyrics = {
    'title': song_title_list,
    'lyrics': lyrics_list
    }
    df = pd.DataFrame(all_lyrics)
    df.to_csv('scrape.csv')
if __name__ == '__main__':
    scrape()
