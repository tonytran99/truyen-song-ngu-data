import json
from datetime import datetime
now = datetime.now()
dataJsonFile = {
    "lastUpdatedAt": str(datetime.timestamp(now))
}
with open('check-update.json', 'w', encoding='utf-8') as outfile:
    json.dump(dataJsonFile, outfile, ensure_ascii=False, indent=4)
