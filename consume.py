import datetime
import json
import time

min_conversions = {
59: 0,
0: 0, 
1: 0,
14: 15,
15: 15, 
16: 15,
29: 30,
30: 30,
31: 30,
44: 45, 
45: 45,
46: 45
} 

sch = {}
with open('gti-1/control.json', 'r') as f:
  sch = json.loads(f.read())


print(sch)

old_key = ""
count = 0
while True:
    time.sleep(31)
    count += 1
    current_time = datetime.datetime.now()
    if current_time.minute in min_conversions:
        minute = min_conversions[current_time.minute]
        key = f'{current_time.hour:02d}:{minute:02d}'
        if sch.get(key,None) is not None:
            if old_key != key:
                old_key = key
                print('minute ',minute, current_time.minute,old_key,key,sch.get(key,'off'))
    if count > 9:
        count = 0
        with open('gti-1/control.json', 'r') as f:
            sch = json.loads(f.read())


