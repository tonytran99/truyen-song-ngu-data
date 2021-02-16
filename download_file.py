import json
import requests
base_url = "https://tonytran99.github.io/truyen-song-ngu-data/"
with open('truyen-song-ngu.json') as json_file:
    dataJsonFile = json.load(json_file)
    for keyCat in dataJsonFile:
        dataCat = dataJsonFile[keyCat]
        if dataCat["photo"] is not None:
            r = requests.get(dataCat["photo"], allow_redirects=True)
            open("files/photo/categories/" + keyCat + ".jpg", 'wb').write(r.content)
            dataCat['photo'] = base_url + "files/photo/categories/" + keyCat + ".jpg"
        dataStories = dataCat['stories']
        for keySto in dataStories:
            dataSto = dataStories[keySto]
            if dataSto["photo"] is not None:
                r = requests.get(dataSto["photo"], allow_redirects=True)
                open("files/photo/stories/" + keySto + ".jpg", 'wb').write(r.content)
                dataSto['photo'] = base_url + "files/photo/stories/" + keySto + ".jpg"
            if dataSto['audio'] is not None:
                r = requests.get(dataSto["audio"], allow_redirects=True)
                open("files/audio/stories/" + keySto + ".mp3", 'wb').write(r.content)
                dataSto['audio'] = base_url + "files/audio/stories/" + keySto + ".mp3"
            dataStories[keySto] = dataSto
        dataCat['stories'] = dataStories
        dataJsonFile[keyCat] = dataCat
    with open('data.json', 'w', encoding='utf-8') as outfile:
        json.dump(dataJsonFile, outfile, ensure_ascii=False, indent=4)
