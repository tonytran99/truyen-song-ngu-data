import json
import requests

with open('truyen-song-ngu.json') as json_file:
    dataJsonFile = json.load(json_file)
    for keyCat in dataJsonFile:
        dataCat = dataJsonFile[keyCat]
        if dataCat["photo"] is not None:
            r = requests.get(dataCat["photo"], allow_redirects=True)
            open("files/photo/categories/" + keyCat + ".jpg", 'wb').write(r.content)
            # dataCat['photo'] =
        dataStories = dataCat['stories']
        for keySto in dataStories:
            dataSto = dataStories[keySto]
            if dataSto["photo"] is not None:
                r = requests.get(dataSto["photo"], allow_redirects=True)
                open("files/photo/stories/" + keySto + ".jpg", 'wb').write(r.content)
            if dataSto['audio'] is not None:
                r = requests.get(dataSto["audio"], allow_redirects=True)
                open("files/audio/stories/" + keySto + ".mp3", 'wb').write(r.content)


