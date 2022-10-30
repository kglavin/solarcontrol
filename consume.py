import datetime
import json
import time



sch = {}
with open('gti-1/gti-1.json', 'r') as f:
  sch = json.loads(f.read())

print(sch)

old_key = ""
while True:
    time.sleep(1)
    current_time = datetime.datetime.now()
    key = f'{current_time.minute:02d}:00'

    if old_key != key:
        old_key = key
        print(key,sch.get(key,'off'))
