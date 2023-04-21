from Class import *

def AverageWinrate(team):
    TotalWinrate = 0
    for hero in team.pick:
        TotalWinrate = TotalWinrate + hero.winrate
    return TotalWinrate/(len(team.pick))

def StaticSynergyValueHero(hero,team):
    ValueSum = 0
    MatchSum = 0
    for other_hero in team.pick:
        if other_hero != hero:
            ValueSum = ValueSum + hero.SynergyValue(other_hero.name)*hero.MatchWith(other_hero.name)
            MatchSum = MatchSum + hero.MatchWith(other_hero.name)
    Data = {'total_match':MatchSum,'total_value':ValueSum,'average_value':ValueSum/MatchSum}
    return Data

def StaticSynergyPayoff(team):
    TotalSynergy = 0
    TotalMatch = 0
    for hero in team.pick:
        data = StaticSynergyValueHero(hero,team)
        TotalSynergy = TotalSynergy + data['total_value']
        TotalMatch = TotalMatch + data['total_match']
    TotalAverageValue = TotalSynergy/TotalMatch
    Winrate = AverageWinrate(team)
    SynergyData = {'average_winrate':round(Winrate,3),'synergy_value':round(TotalAverageValue,3),
                   'synergy_payoff':round(Winrate,3)+round(TotalAverageValue,3)}
    return SynergyData

def StaticCounterValueHero(hero,enemy_team):
    ValueSum = 0
    MatchSum = 0
    for other_hero in enemy_team.pick:
        ValueSum = ValueSum + hero.CounterValue(other_hero.name)*hero.MatchVersus(other_hero.name)
        MatchSum = MatchSum + hero.MatchVersus(other_hero.name)
    Data = {'total_match':MatchSum,'total_value':ValueSum,'average_value':ValueSum/MatchSum}
    return Data

def StaticCounterPayoff(team,enemy_team):
    TotalCounter = 0
    TotalMatch = 0
    for hero in team.pick:
        data = StaticSynergyValueHero(hero,enemy_team)
        TotalCounter = TotalCounter + data['total_value']
        TotalMatch = TotalMatch + data['total_match']
    TotalAverageValue = TotalCounter/TotalMatch
    Winrate = AverageWinrate(team)
    SynergyData = {'average_winrate':round(Winrate,3),'counter_value':round(TotalAverageValue,3),
                   'counter_payoff':round(Winrate,3)+round(TotalAverageValue,3)}
    return SynergyData

def StaticPreferencePayoff(team):
    PrefVector = team.pref
    PickVector = team.PickVector
    PayoffValue = 0
    for i in range(len(PickVector)):
        PayoffValue = PayoffValue + PrefVector[i]*PickVector[i]
    return PayoffValue

def StaticPayoff(team,enemy_team,coefficient):
    Synergy = StaticSynergyPayoff(team)['synergy_payoff']
    SynergyWinrate = StaticSynergyPayoff(team)['average_winrate']
    Counter = StaticCounterPayoff(team,enemy_team)['counter_payoff']
    CounterWinrate = StaticCounterPayoff(team,enemy_team)['average_winrate']
    Preference = StaticPreferencePayoff(team)
    SynergyCoefficient = coefficient['synergy']
    CounterCoefficient = coefficient['counter']
    PreferenceCoefficient = coefficient['preference']
    SynergyValue = Synergy*SynergyCoefficient
    CounterValue = Counter*CounterCoefficient
    PreferenceValue = Preference*PreferenceCoefficient
    Data = {'synergy':SynergyValue/100,'counter':CounterValue/100,'preference':PreferenceValue,
            'total':(SynergyValue/100)+(CounterValue/100)+PreferenceValue,'synergy_average_winrate':SynergyWinrate,'counter_average_winrate':CounterWinrate}
    return Data
