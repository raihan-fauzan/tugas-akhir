from Class import *


gui_radiant_ban_list = ["---","---","---","---","---","---","---"]
gui_dire_ban_list = ["---","---","---","---","---","---","---"]
gui_radiant_pick_list = ["---","---","---","---","---"]
gui_dire_pick_list = ["---","---","---","---","---"]

def gui_update():
    if len(Radiant.ban)>0:
        for i in range(len(Radiant.ban)):
            hero = Radiant.ban[i]
            gui_radiant_ban_list[i] = hero.name
        
    if len(Dire.ban)>0:
        for i in range(len(Dire.ban)):
            hero = Dire.ban[i]
            gui_dire_ban_list[i] = hero.name
    
    if len(Radiant.pick)>0:
        for i in range(len(Radiant.pick)):
            hero = Radiant.pick[i]
            gui_radiant_pick_list[i] = hero.name

    if len(Dire.pick)>0:
        for i in range(len(Dire.pick)):
            hero = Dire.pick[i]
            gui_dire_pick_list[i] = hero.name


def print_gui():
    print("=========================================")
    print("Radiant")
    print("Pick:")
    for i in range(len(gui_radiant_pick_list)-1):
        print("[",gui_radiant_pick_list[i],"]",end="")
    print("[",gui_radiant_pick_list[-1],"]")
    print("Ban:")
    for i in range(len(gui_radiant_ban_list)-1):
        print("[",gui_radiant_ban_list[i],"]",end="")
    print("[",gui_radiant_ban_list[-1],"]")
    print("")
    print("Dire")
    print("Pick:")
    for i in range(len(gui_dire_pick_list)-1):
        print("[",gui_dire_pick_list[i],"]",end="")
    print("[",gui_dire_pick_list[-1],"]")
    print("Dire Ban:")
    for i in range(len(gui_dire_ban_list)-1):
        print("[",gui_dire_ban_list[i],"]",end="")
    print("[",gui_dire_ban_list[-1],"]")
    print("=========================================")

    

