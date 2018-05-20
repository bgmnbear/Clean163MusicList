import json
from time import sleep

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


def get_map(tags, l, i):
    tag_list = []
    for tag in tags:
        tag_list.append(tag['name'])

    print('tag_list', tag_list)
    print('--------------------')

    if '华语' in tag_list or '内地' in tag_list or '台湾' in tag_list:
        l[i] = 1
    elif '欧美' in tag_list or '美国' in tag_list or '英国' in tag_list:
        l[i] = 2
    elif '日本' in tag_list:
        l[i] = 3


if __name__ == '__main__':
    songs = get_songs()
    print('songs length', len(songs))
    i = 0
    l = [0 for j in range(100)]
    for song in songs:
        print('song_name', song.split('(')[0])

        sleep(2)
        tags = get_song_tags(song.split('(')[0])
        get_map(tags, l, i)
        i += 1

        if i == 25:
            break

    with open('data.json', 'w') as f:
        json.dump(l, f)
