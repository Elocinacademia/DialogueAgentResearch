import csv


file = open('test.csv')
reader = csv.reader(file)
header_row = next(reader)

new_file = []








header = ['UID','Datatype','Recipient','Condition','Class']

final_file = []
final_file.append(header)



for k, value in enumerate(new_file):
    if value[-1] == 'not shared with others':
        print(k)
        print(value)
        

# import pdb;pdb.set_trace()



datatype = {'1':'email', 
'2':'banking','3':'healthcare',
'4':'door locker','5':'camera','6':'call assistant',
'7':'video call',
'8':'location',
'9':'voice recording',
'10':'todo',
'11':'sleep hours',
'12':'playlists',
'13':'thermostat',
'14':'shopping',
'15':'weather'}



recipient = {'1':'your parents',
'2':'your partner',
'3':'your siblings',
'4':'your housemates',
'5':'your children',
'6': 'neighbours',
'7':'your friends',
'8':'close family',
'9':'house keeper/helper',
'10':'visitors in general',
'11':'assistant provider',
'12':'skills',
'13':'other skills',
'14':'advertising agencies',
'15':'law enforcement agencies'}

condition = {'no condition': '0',
'no conditions': '0',
'if the data is anonymous': '1',
'if the data is confidentia': '2',
'if the data is kept confidentia': '2',
'if the data is kept confidential': '2',
'if the data is confidential i.e. not shared with others': '2',
'if the data is kept confidential i.e. not shared with others.': '2',
'if the data is kept confidential i.e. not shared with others': '2',
'if the data is stored for as long as necessary for the purpose above':'3',
'if the data is stored for as long as reasonably for the purpose above': '3',
'if the data stored for as long as necessary for the purpose above': '3',
'if the data stored for as long as necessary for the purpose above.' : '3',
'if the data is stored for as long as necessary for the purpose': '3',
'if you are notified': '4',
'if you can review or delete the data': '5',
'if you review or delete the data': '5',
'if you can delete or review the data': '5'
}


def get_key (dict, value):
    for k, v in dict.items():
        if v == value:
            return k

    
label = {'Somewhat Acceptable' : '1',
'Somewhat acceptable' : '1',
'Completely Acceptable' : '1',
'Completely Acceptable ': '1',
'Neutral' : '1',
'Completely acceptable': '1',
'Somewhat unacceptable': '0',
'Completely unacceptable': '0',
'Completely Unacceptable': '0',
'Somewhat Unacceptable': '0'
}





outlier_key = []
for k,v in enumerate(reader):
    buffer =[]
    buffer.append(v[0])
    # import pdb;pdb.set_trace()
    num_data = get_key(datatype,v[1])
    buffer.append(num_data)

    
    #deal with recipient
    # print(v[7])
    num_recipient = get_key(recipient,v[2])
    buffer.append(num_recipient)

    #deal with condition
    # print(v[8])
    if v[3] in condition.keys():
        buffer.append(condition[v[3]])
    else:
        print(v[3])
        import pdb;pdb.set_trace()
    buffer.append(v[4])
    final_file.append(buffer)




   

save_file = './tree_incremental/test.csv'
with open(save_file,"w") as csv_file:
    writer=csv.writer(csv_file)
    for key,value in enumerate(final_file):
        # import pdb; pdb.set_trace() 
        writer.writerow(value)
import pdb;pdb.set_trace()








