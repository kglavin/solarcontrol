import datetime
import json
import time



sch = {}
with open('gti-1/gti-1.json', 'r') as f:
  sch = json.loads(f.read())

print(sch)

old_key = ""
count = 0
while True:
    time.sleep(1)
    count += 1
    current_time = datetime.datetime.now()
    key = f'{current_time.hour:02d}:{current_time.minute:02d}'
    if current_time.minute in [0,15,30,45]:
        if sch.get(key,None) is not None:
            if old_key != key:
                old_key = key
                print(key,sch.get(key,'off'))
    if count > 47:
        count = 0
        with open('gti-1/gti-1.json', 'r') as f:
            sch = json.loads(f.read())


