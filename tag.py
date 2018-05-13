import requests
from bs4 import BeautifulSoup


def get_songs():
    headers = {
        'Referer': 'http://music.163.com/',
        'Host': 'music.163.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0Iceweasel/38.3.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    list_url = 'http://music.163.com/playlist?id=502400338'

    s = requests.session()
    content = s.get(list_url, headers=headers).content

    bs = BeautifulSoup(content, "lxml")
    songs = bs.find('ul', {'class': 'f-hide'})
    songs = [i.text for i in songs.find_all('a')]

    return songs


def get_song_tags(name):
    headers = {"User_Agent": "Mozilla/5.0(compatible; MSIE 5.5; Windows 10)"}
    url = 'https://api.douban.com/v2/music/search?q={}'.format(name)

    r = requests.get(url, headers=headers).json()

    try:
        tags = r['musics'][0]['tags']
        print(r['musics'][0]['tags'])
    except IndexError:
        tags = []

    return tags


if __name__ == '__main__':
    songs = get_songs()
    for song in songs:
        print('song_name', song.split('(')[0])
        get_song_tags(song)
