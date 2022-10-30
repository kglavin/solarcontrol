import datetime
import json
import time


sch = {}
with open('gti-1/control.json', 'r') as f:
  sch = json.loads(f.read())

cthour = 0
ctminute = 0

print(sch)

old_key = ""
count = 0
while count < 24*60:
    ctminute +=1
    if ctminute == 60:
        ctminute = 0
        cthour += 1
        if cthour == 24:
            cthour = 0
    count += 1
    key = f'{cthour:02d}:{ctminute:02d}'
    if sch.get(key,None) is not None:
        if old_key != key:
            old_key = key
            print('minute ',ctminute,old_key,key,sch.get(key,'off'))


