from bs4 import BeautifulSoup
import json

with open('data_hero_id.json','r') as g:
    hero_id = json.load(g)
id_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
files = []
for id in id_list:
    files.append('stratz data\\'+str(id)+'.html')
docs = []
for file in files:
    with open(file, "r", encoding="utf8") as f:
        doc = BeautifulSoup(f, "html.parser")
        docs.append(doc)

data_all_heroes = []
# sort function
def SortFunc(data):
    return data['id']

# find ID list
def GenerateData(file,data_id):
    a_tags = file.find_all('a')
    id_list=[]
    for a in a_tags:
        txt = str(a['href'])
        txt_split = txt.split('/')
        id_list.append(int(txt_split[2]))

    data_heroes = {'hero_name':data_id['hero_name'],'hero_id':data_id['hero_id'],'avg_winrate':0,'data_counter':[],'data_synergy':[]}
    # find div
    counter_id = 0
    for a in a_tags:
        div_list = a.find_all('div')
        total_versus = int(div_list[3].text.replace(',',''))
        versus_winrate = float(div_list[8].text.replace('%','').replace('~',''))
        #versus_winrate.replace('%','')
        
        data_counter = {'id':id_list[counter_id],'total_versus':total_versus, 'winrate_versus':versus_winrate, 'counter_value':0}

        total_with = int(div_list[23].text.replace(',',''))
        with_winrate = float(div_list[28].text.replace('%','').replace('~',''))

        data_synergy = {'id':id_list[counter_id],'total_with': total_with, 'winrate_with': with_winrate, 'synergy_value':0}
        
        data_heroes['data_counter'].append(data_counter)
        data_heroes['data_synergy'].append(data_synergy)
        counter_id = counter_id + 1
    
    data_heroes['data_counter'].sort(key=SortFunc)
    data_heroes['data_synergy'].sort(key=SortFunc)

    winrate_sum = 0
    match_sum = 0
    for data in data_heroes['data_counter']:
        winrate_sum = winrate_sum + data['winrate_versus']*data['total_versus']
        match_sum = match_sum + data['total_versus']
    for data in data_heroes['data_synergy']:
        winrate_sum = winrate_sum + data['winrate_with']*data['total_with']
        match_sum = match_sum + data['total_with']
    avg_winrate = winrate_sum/match_sum
    data_heroes['avg_winrate'] = round(avg_winrate,3)

    for data in data_heroes['data_counter']:
        data['counter_value'] = round(data['winrate_versus']-data_heroes['avg_winrate'],3)
    for data in data_heroes['data_synergy']:
        data['synergy_value'] = round(data['winrate_with']-data_heroes['avg_winrate'],3)
    return data_heroes

for i in range(len(docs)):
    data_all_heroes.append(GenerateData(docs[i],hero_id[i]))

json_data = json.dumps(data_all_heroes, indent=1)
json_file = open('data_all_heroes.json','w')
json_file.write(json_data)
json_file.close()










