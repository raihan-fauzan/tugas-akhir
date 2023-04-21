from Class import *
import GUI_sementara as GUI





# Change pref vector


def BanPhase1(urutan):
    '''
    INPUT:
    urutan: urutan drafting
    OUTPUT:
    sistem ban hero
    '''
    if urutan == 1:
        
        # 1 Radiant
        print("Radiant Ban #1")
        ban1 = InputHero()
        ban1.Banning(Radiant)
        GUI.gui_update()
        GUI.print_gui()

        
        # 2 Dire
        print("Dire Ban #1")
        ban2 = InputHero()
        ban2.Banning(Dire)
        GUI.gui_update()
        GUI.print_gui()

        # 3 Radiant
        print("Radiant Ban #2")
        ban3 = InputHero()
        ban3.Banning(Radiant)
        GUI.gui_update()
        GUI.print_gui()

        # 4 Dire
        print("Dire Ban #2")
        ban4 = InputHero()
        ban4.Banning(Dire)
        GUI.gui_update()
        GUI.print_gui()


    if urutan == 2:

        # 1 Dire
        print("Dire Ban #1")
        ban1 = InputHero()
        ban1.Banning(Dire)
        GUI.gui_update()
        GUI.print_gui()

        # 2 Radiant
        print("Radiant Ban #1")
        ban2 = InputHero()
        ban2.Banning(Radiant)
        GUI.gui_update()
        GUI.print_gui()
        
        # 3 Dire
        print("Dire Ban #2")
        ban3 = InputHero()
        ban3.Banning(Dire)
        GUI.gui_update()
        GUI.print_gui()

        # 4 Radiant
        print("Radiant Ban #2")
        ban4 = InputHero()
        ban4.Banning(Radiant)
        GUI.gui_update()
        GUI.print_gui()

def PickPhase1(urutan):
    if urutan == 1:
        print("Radiant Pick #1")
        pick1 = InputHero()
        pick1.Picking(Radiant)
        GUI.gui_update()
        GUI.print_gui()

        print("Dire Pick #1")
        pick2 = InputHero()
        pick2.Picking(Dire)
        GUI.gui_update()
        GUI.print_gui()

        print("Dire Pick #2")
        pick3 = InputHero()
        pick3.Picking(Dire)
        GUI.gui_update()
        GUI.print_gui()

        print("Radiant Pick #2")
        pick4 = InputHero()
        pick4.Picking(Radiant)
        GUI.gui_update()
        GUI.print_gui()
    
    if urutan == 2:
        print("Dire Pick #1")
        pick1 = InputHero()
        pick1.Picking(Dire)
        GUI.gui_update()
        GUI.print_gui()

        print("Radiant Pick #1")
        pick2 = InputHero()
        pick2.Picking(Radiant)
        GUI.gui_update()
        GUI.print_gui()

        print("Radiant Pick #2")
        pick3 = InputHero()
        pick3.Picking(Radiant)
        GUI.gui_update()
        GUI.print_gui()

        print("Dire Pick #2")
        pick4 = InputHero()
        pick4.Picking(Dire)
        GUI.gui_update()
        GUI.print_gui()

def AllPick(team):
    for i in range(5):
        print(f'{team.name} Pick {i + 1}')
        pick = InputHero()
        pick.Picking(team)
        team.UpdatePickVector()
        GUI.gui_update()
        GUI.print_gui()

def AllPickFromList(list,team):
    for hero in list:
        pick = FindHeroFromAll_name(hero)
        pick.Picking(team)
    team.UpdatePickVector()
    GUI.gui_update()
    GUI.print_gui()