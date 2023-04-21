import json
import requests

hero_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 119, 120, 121, 123, 126, 128, 129, 135, 136, 137, 138]

class Hero:
    '''
    HERO ATTRIBUTE
    hero_name: Nama Hero
    hero_id: Penomoran Hero
    hero_winrate: Nilai Winrate Hero tersebut (dalam desimal)
    pick: Menyatakan keadaan apakah Hero tersebut sudah di-pick atau belum (0 = unpicked, 1 = Radiant, 2 = Dire)
    ban: Menyatakan keadaan apakah Hero tersebut sudah di-pick atau belum (0 = unbanned, 1 = ban by Radiant, 2 = ban by Dire)

    HERO CLASS VARIABLE
    All: List semua Hero
    Unpickban: List Hero yang tidak di-pick dan di-ban

    HERO ACTION
    Picking:
        INPUT: self, team
        OUTPUT: Hero tersebut di-pick oleh team
    Banning:
        INPUT: self, team
        OUTPUT: Hero tersebut di-ban oleh team
    '''
  # CLASS VARIABLE
    All = []
    Unpickban = []

    def __init__(self,hero_name: str, hero_id: int, hero_winrate = 0.5,pick = "none", ban = "none"):
    
    # Assign Self
        self.name = hero_name
        self.id = hero_id
        self.winrate = hero_winrate
        self.data_counter = []
        self.data_synergy = []
        self.winrate_list = []
        self.pick = pick
        self.ban = ban
        if self not in Hero.All:
            Hero.All.append(self)
        if self not in Hero.Unpickban:
            Hero.Unpickban.append(self)

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def read_from_json(cls):
        with open('data_all_heroes.json', 'r') as f:
            data_json = json.load(f)
        for hero in data_json:
            Hero(
                hero_name = hero['hero_name'],
                hero_id = hero['hero_id'],
                hero_winrate = hero['avg_winrate'],
                )
        for hero in Hero.All:
            for data in data_json:
                if hero.id == data['hero_id']:
                    hero.data_counter = data['data_counter']
                    hero.data_synergy = data['data_synergy']

    # ACTION
    ## Pick
    def Picking(self,team):
        if self.ban == "none":

            self.pick = team.name
            team.pick.append(self)
            Hero.Unpickban.remove(self)

        else:
            print(f'{self.name} cant be picked!')

    ## Ban
    def Banning(self,team):
        if self.pick == "none":
            self.ban = team.name
            team.ban.append(self)
            Hero.Unpickban.remove(self)
            
        else:
            print(f'{self.name} cant be banned!')
    
    def CounterValue(self,hero_name):
        id = GetIDFromHeroName(hero_name)
        for data in self.data_counter:
            if data['id'] == id:
                return data['counter_value']
        return 0
            
    def SynergyValue(self,hero_name):
        id = GetIDFromHeroName(hero_name)
        for data in self.data_synergy:
            if data['id'] == id:
                return data['synergy_value']
        return 0
            
    def WinrateVersus(self,hero_name):
        id = GetIDFromHeroName(hero_name)
        for data in self.data_counter:
            if data['id'] == id:
                return data['winrate_versus']
        return 0
    
    def WinrateWith(self,hero_name):
        id = GetIDFromHeroName(hero_name)
        for data in self.data_synergy:
            if data['id'] == id:
                return data['winrate_with']
        return 0
    
    def MatchVersus(self,hero_name):
        id = GetIDFromHeroName(hero_name)
        for data in self.data_counter:
            if data['id'] == id:
                return data['total_versus']
        return 0
            
    def MatchWith(self,hero_name):
        id = GetIDFromHeroName(hero_name)
        for data in self.data_synergy:
            if data['id'] == id:
                return data['total_with']
        return 0
        

            

Hero.read_from_json()

#def GetAllWinrate():
#    for hero in Hero.All:
#        hero.GetWinrate()

#GetAllWinrate()

def InputHero():
    '''
    INPUT:
        hero_name: nama Hero
    OUTPUT: Hero
    DESC: mencari objek hero dari list hero yang tidak dipick dan diban berdasarkan nama
    '''
    check = False
    while check == False:
        hero_name = input("Hero: ")
        for hero in Hero.Unpickban:
            if hero.name == hero_name:
                check == True
                return hero
        print("Hero can't be found, try again!")

def FindHero(hero_name):
    '''
    INPUT: 
        hero_name: nama Hero
    OUTPUT: Hero
    DESC: 
    '''
    for hero in Hero.Unpickban:
        if hero.name == hero_name:
            return hero
        
def FindHeroFromAll_name(hero_name):
    '''
    INPUT: 
        hero_name: nama Hero
    OUTPUT: Hero
    DESC: 
    '''
    for hero in Hero.All:
        if hero.name == hero_name:
            return hero

def GetIDFromHeroName(hero_name):
    for hero in Hero.All:
        if hero.name == hero_name:
            return hero.id

class Team:
    '''
    INPUT:
    team_name: nama tim (Radiant/Dire)
    '''
    def __init__(self,team_name: str) :
        self.name = team_name
        self.pref = [1/138]*138
        self.pick = []
        self.ban = []
        self.PickVector = [0 for i in range(138)]
    
    # update pick vector after a pick
    def UpdatePickVector(self):
        for hero in self.pick:
            self.PickVector[hero.id-1] = 1
    
    # print pick vector
    def ShowPickVector(self):
        print("[", end="")
        for value in self.PickVector:
            print(value, end="")
        print("]")

    def AssignPrefVector(self, num_heroes):
        self.pref = [0 for i in range(len(Hero.All))]
        for i in range(num_heroes):
            print("Assign Pref Value to")
            hero = InputHero()
            value = float(input("Value: "))
            self.pref[hero.id-1] = value

    def ChangePrefVector(self, pref_list): #[[hero_name, pref_value], ... ]
        self.pref = [0 for i in range(138)]
        for vector in pref_list:
            id = GetIDFromHeroName(vector[0])
            self.pref[id-1] = vector[1]
    
    # print pref vector
    def ShowPrefVector(self):
        print("[", end="")
        for value in self.pref:
            print(value,"", end="")
        print("]")

        
    
            

Radiant = Team("Radiant")
Dire = Team("Dire")