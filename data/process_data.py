import csv
import numpy as np
import random
import pprint

file = open('smarthome.csv')
reader = csv.reader(file)
header_row = next(reader)

header = ['uid', 'datatype', 'recipient','condition']

final_file = []


random.seed(0)


print('============================================================================')
print('Data processing begins ...')
print('============================================================================')
# print("{:=^50s}".format("="))

print('1320 user detected.')
#1320
index = random.sample(range(0,1320),20)
#[788, 861, 82, 530, 1047, 995, 829, 621, 976, 733, 1194, 447, 1033, 285, 577, 286, 194, 1266, 513, 1090]

train_set = []
test_set = []


print('Splitting train, preliminary test set ... ...')
for k,v in enumerate(reader):
    if int(v[0]) not in index:
        train_set.append(v)
    elif int(v[0]) in index:
        test_set.append(v)
    else:
        print('index not found!')

print('Num in train set:', len(train_set))
print('Num in whole test set:', len(test_set))
print('============================================================================')

print('Splitting incremental, real test set ... ...')

dictionary = dict([(key,[]) for key in index])




for k,v in enumerate(test_set):
    dictionary[int(v[0])].append(v)

num = []
incremental_set = []
real_test = []
for order,i in enumerate(index):
    random.shuffle(dictionary[i])
    num.append(len(dictionary[i]))
    cut = int(np.round(0.3 * num[0]))
    for item in dictionary[i][:cut]:
        incremental_set.append(item)
    for item in dictionary[i][cut:]:
        real_test.append(item)



print('Num in incremental set:', len(incremental_set))
print('Num in final test (validation) set:', len(real_test))
print('Done, saving the files ...')

print('============================================================================')




with open('train.csv',"w") as csv_file:
    writer=csv.writer(csv_file)
    for key,value in enumerate(train_set):
        # import pdb; pdb.set_trace() 
        writer.writerow(value)


with open('incremental_set.csv',"w") as csv_file:
    writer=csv.writer(csv_file)
    for key,value in enumerate(incremental_set):
        # import pdb; pdb.set_trace() 
        writer.writerow(value)

with open('test.csv',"w") as csv_file:
    writer=csv.writer(csv_file)
    for key,value in enumerate(real_test):
        # import pdb; pdb.set_trace() 
        writer.writerow(value)

import pdb;pdb.set_trace()







import pdb; pdb.set_trace()




      



    





