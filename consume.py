import datetime
import json
import time

sch = {}
with open('gti-1/control.json', 'r') as f:
  sch = json.loads(f.read())


print(sch)

old_key = ""
count = 0
while True:
    time.sleep(17)
    count += 1
    current_time = datetime.datetime.now()
    key = f'{current_time.hour:02d}:{current_time.minute:02d}'
    if sch.get(key,None) is not None:
        if old_key != key:
            print(old_key,key,sch.get(key,'off'))
            old_key = key
    if count > 9:
        count = 0
        with open('gti-1/control.json', 'r') as f:
            sch = json.loads(f.read())


