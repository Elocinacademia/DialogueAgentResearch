import sys, os
import json
import random

with open('smarthome_plaintext.csv') as fin:
    lines = fin.readlines()

usr_attr = []
usr_data = {}
datatypes = []
reciptypes = []
condtypes = []
for line in lines[1:]:
    elems = line.strip().split(',')
    attr = ','.join(elems[:-4])
    if attr not in usr_attr:
        usr_data[attr] = []
        usr_attr.append(attr)
    if elems[-1] == 'Permit':
        elems[-1] = '0'
    elif elems[-1] == 'Prohibit':
        elems[-1] = '1'
    if elems[-4] not in datatypes:
        datatypes.append(elems[-4])
    if elems[-3] not in reciptypes:
        reciptypes.append(elems[-3])
    if elems[-2] not in condtypes:
        condtypes.append(elems[-2])
    usr_data[attr].append(elems[-4:])

with open('reciptypes.txt', 'w') as fout:
    for recip in reciptypes:
        fout.write(recip + '\n')
with open('datatypes.txt', 'w') as fout:
    for data in datatypes:
        fout.write(data + '\n')
with open('conditions.txt', 'w') as fout:
    for cond in condtypes:
        fout.write(cond + '\n')

with open('usr_spec_data.json', 'w') as fout:
    json.dump(usr_data, fout, indent=4)

usr_ids = {}
for i, user in enumerate(usr_attr):
    usr_ids[user] = i
with open('userID.json', 'w') as fout:
    json.dump(usr_ids, fout, indent=4)

train = []
valid = []
test = []
for user in usr_attr:
    choice = random.random()
    if choice < 0.6:
        for datapiece in usr_data[user]:
            train.append(','.join([str(usr_ids[user])] + datapiece) + '\n')
    else:
        for datapiece in usr_data[user]:
            choice2 = random.random()
            if choice2 < 0.2:
                train.append(','.join([str(usr_ids[user])] + datapiece) + '\n')
            elif choice2 < 0.6:
                valid.append(','.join([str(usr_ids[user])] + datapiece) + '\n')
            else:
                test.append(','.join([str(usr_ids[user])] + datapiece) + '\n')

with open('train.csv', 'w') as fout:
    fout.writelines(train)
with open('valid.csv', 'w') as fout:
    fout.writelines(valid)
with open('test.csv', 'w') as fout:
    fout.writelines(test)
