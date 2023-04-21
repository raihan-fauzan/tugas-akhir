from Class import *
import PicknBan as pnb
import Payoff as po

print(Hero.All)

coefficient = {'synergy':1/2,'counter':1/2,'preference':0}
radiant_hero_list = ['Crystal Maiden',
        'Bane',
        'Witch Doctor',
        'Vengeful Spirit',
        'Puck'
        ]
radiant_pref_vector = [
    ['Axe',0.2],
    ['Witch Doctor',0.1],
    ['Razor',0.3],
    ['Puck',0.2]
]
dire_hero_list = [
    'Anti-Mage',
    'Sven',
    'Juggernaut',
    'Bloodseeker',
    'Riki'
]
dire_pref_vector = [
    ['Bloodseeker',0.4],
    ['Tidehunter',0.1]
]
pnb.AllPickFromList(radiant_hero_list,Radiant)
pnb.AllPickFromList(dire_hero_list,Dire)


Radiant.ChangePrefVector(radiant_pref_vector)
Dire.ChangePrefVector(dire_pref_vector)
print(po.StaticPayoff(Radiant,Dire,coefficient)['counter_average_winrate'])
print(po.StaticPayoff(Dire,Radiant,coefficient)['counter_average_winrate'])
#print((po.StaticSynergyPayoff(Radiant)['average_winrate']+po.StaticSynergyPayoff(Radiant)['synergy_value']+po.StaticCounterPayoff(Radiant,Dire)['average_winrate']+po.StaticCounterPayoff(Radiant,Dire)['counter_value'])/2)
#print((po.StaticSynergyPayoff(Dire)['average_winrate']+po.StaticSynergyPayoff(Dire)['synergy_value']+po.StaticCounterPayoff(Dire,Radiant)['average_winrate']+po.StaticCounterPayoff(Dire,Radiant)['counter_value'])/2)
#pnb.BanPhase1(1)
#pnb.PickPhase1(1)
#for hero1 in Hero.All:
#    for hero2 in Hero.All:
#        print(f'winrate {hero1.name} vs {hero2.name} : {hero1.WinrateVersus(hero2.name)}')







