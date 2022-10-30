import json

sch = {}

sch['00:00'] = 'off'
sch['01:00'] = 'off'
sch['02:00'] = 'off'
sch['03:00'] = 'off'
sch['04:00'] = 'off'
sch['05:00'] = 'off'
sch['06:00'] = 'off'
sch['07:00'] = 'off'
sch['08:00'] = 'off'
sch['09:00'] = 'off'
sch['l0:00'] = 'off'
sch['l1:00'] = 'on'
sch['l2:00'] = 'on'
sch['13:00'] = 'on'
sch['14:00'] = 'on'
sch['16:00'] = 'on'
sch['17:00'] = 'on'
sch['18:00'] = 'on'
sch['19:00'] = 'on'
sch['19:15'] = 'on'
sch['19:30'] = 'on'
sch['19:45'] = 'off'
sch['20:00'] = 'on'
sch['20:15'] = 'off'
sch['20:30'] = 'on'
sch['20:45'] = 'off'
sch['21:00'] = 'on'
sch['22:00'] = 'off'
sch['23:00'] = 'off'


print(json.dumps(sch))
