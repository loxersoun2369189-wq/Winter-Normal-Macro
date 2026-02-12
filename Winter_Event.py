
from Tools import botTools as bt
from Tools import winTools as wt
from Tools import avMethods as avM
import webhook
import keyboard
import time
import pyautogui
import sys
import os
from datetime import datetime
from threading import Thread
import pydirectinput
import ctypes
import subprocess
import json
import pygetwindow as gw

VERSION_N = '1.499999'

class Cur_Settings: pass

global Settings
Settings = Cur_Settings()

USE_KAGUYA = False

USE_BUU = False # Thanks to Doomgus for getting images for this strat to work :steamhappy:
USE_FREIZA = True

PRIVATE_SERVER_CODE = "" # Not in settings so u dont accidently share ur ps lol

TAK_FINDER = True # turn off if it runs into a wall while trying to find tak

ROUND_RESTART = 0 # 0 will make it so this doesnt happen, change it to what round u want it to restart

Settings_Path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Settings")
WE_Json = os.path.join(Settings_Path,"Winter_Event.json")

AINZ_SPELLS = False

def load_json_data():
    JSON_DATA = None
    if os.path.isfile(WE_Json):
        with open(WE_Json, 'r') as f:
            JSON_DATA = json.load(f)
    return JSON_DATA
if os.path.exists(Settings_Path):
    if os.path.exists(WE_Json):
        data = load_json_data()
        for variable in data:
            value = data.get(variable)
            try:
                if variable == "Unit_Positions" or variable == "Unit_Placements_Left":
                    if type(value[0]) == dict:
                        setattr(Settings, variable, value[0])
                else:
                    setattr(Settings, variable, value)
            except Exception as e:
                print(e)
else:
    print("Failed to find settings file. Closing in 10 seconds")
    time.sleep(10)
    sys.exit()
    
    
    
print("Loaded settings")
Settings.Units_Placeable.append("Doom")

if not USE_KAGUYA:
    Settings.Units_Placeable.remove("Kag")
# Failsafe key
global g_toggle
g_toggle = False
def toggle():
    global g_toggle
    g_toggle = not g_toggle
    if g_toggle == False:
        args = list(sys.argv)
        try:
            if "--restart" in args:
                args.remove("--restart")
            if "--stopped" in args:
                args.remove("--stopped")
        except Exception as e:
            print(e)
        sys.stdout.flush()
        subprocess.Popen([sys.executable, *args, "--stopped"])
        os._exit(0)
        
def kill():
    os._exit(0)
    
keyboard.add_hotkey(Settings.STOP_START_HOTKEY, toggle) 
keyboard.add_hotkey("k",kill)

# Actions
def click(x,y, delay: int | None=None, right_click: bool | None = None, dont_move: bool | None = None) -> None:
    if delay is not None:
        delay=delay
    else:
        delay = 0.65
    if dont_move is None:
        pyautogui.moveTo(x,y)
    ctypes.windll.user32.mouse_event(0x0001, 0, 1, 0, 0)
    time.sleep(delay)
    ctypes.windll.user32.mouse_event(0x0001, 0, -1, 0, 0)
    if right_click:
        pyautogui.rightClick()
    else:
        pyautogui.click()


# Wait for start screen
def wait_start(delay: int | None = None):
    i = 0
    if delay is None:
        delay = 1
    else:
        delay = delay
    found = False
    while found == False and i<90: # 1 and a half minute
        try: 
            i+=1
            if Settings.START_BUTTON_ID:
                if bt.does_exist("Winter\\VoteStartButton.png",confidence=0.8,grayscale=True):
                    found = True
            else:
                if pyautogui.pixel(874, 226) == (8,148,8): #green pixel
                    found = True
        except Exception as e:
            print(f"e {e}")
        time.sleep(delay)


def quick_rts(): # Returns to spawn
    locations =[(232, 873), (1146, 498), (1217, 267)]
    for loc in locations:
        click(loc[0], loc[1], delay=0.1)
        time.sleep(0.2)
        
def directions(area: str, unit: str | None=None): # This is for all the pathing
    '''
    This is the pathing for all the areas: 1 [rabbit, nami, hero (trash gamer)], 2 [speed, tak], 3: Mystery box, 4: Upgrader, 5: Monarch upgrader
    '''
    # All this does is set up camera whenever it's the first time running, disable if needed
        
    #Contains rabbit, nami, and hero
    if Settings.USE_NIMBUS:
        if area == '1':  
            #DIR_PATHING
            # Pathing
            if not Settings.CTM_P1_P2:
                keyboard.press('a')
                time.sleep(0.4)
                keyboard.release('a')
                time.sleep(1)
                keyboard.press_and_release('v')
                time.sleep(1.5)
                keyboard.press('w')
                time.sleep(1.5)
                keyboard.release('w')
                keyboard.press('a')
                time.sleep(1.1)
                keyboard.release('a')
            else:
                keyboard.press_and_release('v')
                time.sleep(1)
                for p in Settings.CTM_AREA_1:
                    click(p[0],p[1],delay=0.2,right_click=True)
                    time.sleep(1.9)
                time.sleep(1.5)
            if unit == 'rabbit':
                #[(558, 334)
                click(Settings.CTM_AREA_1_UNITS[0][0], Settings.CTM_AREA_1_UNITS[0][1], delay=0.2,right_click=True) # Click to move
                time.sleep(1)
            if unit == "nami":
                click(Settings.CTM_AREA_1_UNITS[1][0], Settings.CTM_AREA_1_UNITS[1][1], delay=0.2,right_click=True)
                time.sleep(1)
            if unit == "hero":
                click(Settings.CTM_AREA_1_UNITS[2][0], Settings.CTM_AREA_1_UNITS[2][1], delay=0.2,right_click=True)
                time.sleep(1)
            keyboard.press_and_release('v') 
            time.sleep(2)
        # Speed wagon + Tak
        if area == '2':
            if not Settings.CTM_P1_P2:
                keyboard.press('a')
                time.sleep(0.4)
                keyboard.release('a')
                time.sleep(1)
                keyboard.press_and_release('v')
                time.sleep(1.5)
                keyboard.press('w')
                time.sleep(1.5)
                keyboard.release('w')
            else:
                keyboard.press_and_release('v')
                time.sleep(1.3)
                for p in Settings.CTM_AREA_2:
                    click(p[0],p[1],delay=0.2,right_click=True)
                    time.sleep(1.5)
                time.sleep(1.5)
            #(534, 706), (535, 546)
            if unit == 'speed':
                click(Settings.CTM_AREA_2_UNITS[0][0], Settings.CTM_AREA_2_UNITS[0][1], delay=0.2,right_click=True)
                time.sleep(1)
            if unit == 'tak':
                click(Settings.CTM_AREA_2_UNITS[1][0], Settings.CTM_AREA_2_UNITS[1][1], delay=0.2,right_click=True)
                time.sleep(1)
            keyboard.press_and_release('v')
            time.sleep(2)
        # Gambling time
        if area == '3': 
            keyboard.press_and_release('v')
            time.sleep(1)
            keyboard.press('a')
            time.sleep(Settings.AREA_3_DELAYS[0])
            keyboard.release('a')

            keyboard.press('s')
            time.sleep(Settings.AREA_3_DELAYS[1])
            keyboard.release('s')

            keyboard.press('d')
            time.sleep(Settings.AREA_3_DELAYS[2])
            keyboard.release('d')

            keyboard.press('s')
            time.sleep(Settings.AREA_3_DELAYS[3])
            keyboard.release('s')
            keyboard.press_and_release('v')
            time.sleep(2)
            e_delay = 0.7
            timeout = 2.5/e_delay
            at_location = False
            while not at_location:
                keyboard.press_and_release('e')
                time.sleep(e_delay)
                if bt.does_exist("Winter\\LootBox.png",confidence=0.7,grayscale=True, region=(493, 543, 1024, 785)):
                    at_location = True
                if  bt.does_exist("Winter\\Full_Bar.png",confidence=0.7,grayscale=True, region=(493, 543, 1024, 785)):
                    at_location = True
                if  bt.does_exist("Winter\\NO_YEN.png",confidence=0.7,grayscale=True,  region=(493, 543, 1024, 785)):
                    at_location = True
                if timeout < 0:
                    quick_rts()
                    keyboard.press_and_release('v')
                    time.sleep(1)
                    keyboard.press('a')
                    time.sleep(Settings.AREA_3_DELAYS[0])
                    keyboard.release('a')

                    keyboard.press('s')
                    time.sleep(Settings.AREA_3_DELAYS[1])
                    keyboard.release('s')

                    keyboard.press('d')
                    time.sleep(Settings.AREA_3_DELAYS[2])
                    keyboard.release('d')

                    keyboard.press('s')
                    time.sleep(Settings.AREA_3_DELAYS[3])
                    keyboard.release('s')
                    keyboard.press_and_release('v')
                    time.sleep(2)
                    timeout = 3/e_delay
                timeout-=1
            print("At lootbox")

        if area == '4': #  Upgrader location
            keyboard.press_and_release('v')
            time.sleep(1)
            keyboard.press('a')
            time.sleep(Settings.AREA_4_DELAYS[0])
            keyboard.release('a')

            keyboard.press('s')
            time.sleep(Settings.AREA_4_DELAYS[1])
            keyboard.release('s')
            keyboard.press_and_release('v')
            time.sleep(2)
            
        if area == '5': # This is where it buys monarch
            keyboard.press_and_release('v')
            time.sleep(1)
            keyboard.press('a')
            time.sleep(Settings.AREA_5_DELAYS[0])
            keyboard.release('a')

            keyboard.press('w')
            time.sleep(Settings.AREA_5_DELAYS[1])
            keyboard.release('w')
            keyboard.press_and_release('v')
            time.sleep(2)
        
def upgrader(upgrade: str):
    '''
    Buys the upgrades for the winter event: fortune, range, damage, speed, armor
    '''
    e_delay = 0.2
    timeout = 3/e_delay
    keyboard.press_and_release('e')
    while not pyautogui.pixel(1111,310) == (255,255,255):
        if timeout < 0:
            quick_rts()
            directions('4')
            timeout = 3/e_delay
        timeout-=1
        keyboard.press_and_release('e')
        time.sleep(e_delay)
    click(607, 381, delay=0.2)
    time.sleep(0.5)
    if not Settings.USE_UI_NAV:
        if upgrade == 'fortune':
            click(966, 471, delay=0.2)
            time.sleep(0.5)
            while not pyautogui.pixelMatchesColor(966, 471,expectedRGBColor=(24, 24, 24),tolerance=40):
                if not g_toggle:
                    break
                click(966, 471, delay=0.2)
                time.sleep(0.8)
            print(pyautogui.pixel(966, 471))
            click(1112, 309, delay=0.2)
        if upgrade == 'range':
            click(962, 621, delay=0.2)
            time.sleep(0.5)
            while not pyautogui.pixelMatchesColor(962, 621,expectedRGBColor=(24, 24, 24),tolerance=40):
                if not g_toggle:
                    break
                click(962, 621, delay=0.2)
                time.sleep(0.8)
            click(1112, 309, delay=0.2)
        if upgrade == "damage":
            click(765, 497, delay=0.1)
            pos = (959, 399)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, -450, 0)
            time.sleep(0.2)
            click(pos[0], pos[1], delay=0.2)
            time.sleep(0.5)
            while not pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=40):
                if not g_toggle:
                    break
                click(pos[0], pos[1], delay=0.2)
                time.sleep(0.8)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, 1000, 0)
            click(1112, 309, delay=0.2)
        if upgrade == "speed":
            click(765, 497, delay=0.1)
            pos = (957, 424)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, -600, 0)
            time.sleep(0.2)
            click(pos[0], pos[1], delay=0.2)
            time.sleep(0.5)
            while not pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=40):  
                if not g_toggle:
                    break
                click(pos[0], pos[1], delay=0.2)
                time.sleep(0.8)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, 1000, 0)
            click(1112, 309, delay=0.2)
        if upgrade == "armor":
            click(765, 497, delay=0.1)
            pos = (955, 577)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, -600, 0)
            time.sleep(0.2)
            click(pos[0], pos[1], delay=0.2)
            time.sleep(0.5)
            while not  pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=40):
                if not g_toggle:
                    break
                click(pos[0], pos[1], delay=0.2)
                time.sleep(0.8)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, 1000, 0)
            click(1112, 309, delay=0.2)
    else:
        if upgrade == 'fortune':
            pos = (960, 406)
            print("hi")
            click(765, 497, delay=0.1)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, -1000, 0)
            time.sleep(0.2)
            pydirectinput.press('\\')
            pydirectinput.press('\\')
            while not pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=40):
                if not g_toggle:
                    break
                click(pos[0], pos[1], delay=0.2)
                time.sleep(0.8)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, 1000, 0)
            click(1112, 309, delay=0.2)
        if upgrade == 'range':
            pos = (955, 562)
            print("hi")
            click(765, 497, delay=0.1)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, -1000, 0)
            time.sleep(0.2)
            pydirectinput.press('\\')
            pydirectinput.press('\\')
            while not pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=40):
                if not g_toggle:
                    break
                click(pos[0], pos[1], delay=0.2)
                time.sleep(0.8)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, 1000, 0)
            click(1112, 309, delay=0.2)
        if upgrade == "damage":
            pos = (954, 415)
            print("hi")
            click(765, 497, delay=0.1)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, -1000, 0)
            time.sleep(0.2)
            pydirectinput.press('\\')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('\\')
            while not pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=40):
                if not g_toggle:
                    break
                click(pos[0], pos[1], delay=0.2)
                time.sleep(0.8)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, 1000, 0)
            click(1112, 309, delay=0.2)
        if upgrade == "speed":
            pos = (956, 566)
            print("hi")
            click(765, 497, delay=0.1)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, -1000, 0)
            time.sleep(0.2)
            pydirectinput.press('\\')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('\\')
            while not pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=40):
                if not g_toggle:
                    break
                click(pos[0], pos[1], delay=0.2)
                time.sleep(0.8)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, 1000, 0)
            click(1112, 309, delay=0.2)
        if upgrade == "armor":
            pos = (954, 561)
            print("hi")
            click(765, 497, delay=0.1)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, -1000, 0)
            time.sleep(0.2)
            pydirectinput.press('\\')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('\\')
            while not pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=40):
                if not g_toggle:
                    break
                click(pos[0], pos[1], delay=0.2)
                time.sleep(0.8)
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, 1000, 0)
            click(1112, 309, delay=0.2)
    
    
    print(f"Purchased {upgrade}")


def secure_select(pos: tuple[int,int]):
    click(pos[0],pos[1],delay=0.2)
    time.sleep(0.5)
    while not pyautogui.pixel(607,381) == (255,255,255):
        if bt.does_exist('Winter\\Erza_Armor.png',confidence=0.8,grayscale=True):
            click(752, 548,delay=0.2)
            time.sleep(0.6)
        click(pos[0],pos[1],delay=0.2)
        time.sleep(0.8)
    print(f"Selected unit at {pos}")


def place_unit(unit: str, pos : tuple[int,int], close: bool | None=None, region: tuple | None=None):
    '''
    Places a unit found in Winter\\UNIT_hb.png, at location given in pos. 
    '''
    time_out = 20
    time_out_2 = 50
    # Click on the unit
    if region is None:
        while not bt.does_exist(f"Winter\\{unit}_hb.png", confidence=0.8, grayscale=False):
            if time_out_2 <= 0:
                break
            time_out_2-=1
            time.sleep(0.3)
        bt.click_image(f'Winter\\{unit}_hb.png', confidence=0.8,grayscale=False,offset=(0,0))
    else:
        while not bt.does_exist(f"Winter\\{unit}_hb.png", confidence=0.8, grayscale=False,region=region):
            if time_out_2 <= 0:
                break
            time_out_2-=1
            time.sleep(0.3)
        bt.click_image(f'Winter\\{unit}_hb.png', confidence=0.8,grayscale=False,offset=(0,0),region=region)
        
    time.sleep(0.2)
    click(pos[0], pos[1], delay=0.67)
    time.sleep(0.5)
    while not pyautogui.pixel(607, 381) == (255,255,255):
        time_out-=1
        if time_out<=0:
            print("timed out")
            break
        if g_toggle == False:
            break
        click(pos[0], pos[1], delay=0.67)
        print(f"Target Color: (255,255,255), got: {pyautogui.pixel(607, 381)}")
        time.sleep(0.1)
        keyboard.press_and_release('q')
        time.sleep(0.5)
        click(pos[0], pos[1], delay=0.1)
        time.sleep(1)
        if bt.does_exist("Winter\\UnitExists.png",confidence=0.9,grayscale=True):
            break
        if pyautogui.pixel(607, 381) == (255,255,255):
            break
        if True: # if u want it to re-click
            print("Retrying placement...")
            try:
                # Click on the unit
                if region is None:
                    bt.click_image(f'Winter\\{unit}_hb.png', confidence=0.8,grayscale=False,offset=(0,0))
                else:
                    bt.click_image(f'Winter\\{unit}_hb.png', confidence=0.8,grayscale=False,offset=(0,0),region=region)
                time.sleep(0.2)
            except Exception as e:
                print(F"Error {e}")
        time.sleep(0.2)
    if close:
        click(607, 381, delay=0.2)
    print(f"Placed {unit} at {pos}")
        
def buy_monarch(): # this just presses e untill it buys monarch, use after direction('5')
    monarch_region = (686, 606, 818, 646)
    e_delay = 0.4
    timeout = 3/e_delay
    keyboard.press_and_release('e')
    while not bt.does_exist('Winter\\DetectArea.png',confidence=0.7,grayscale=True):
        if bt.does_exist('Winter\\Monarch.png',confidence=0.7,grayscale=False,region=monarch_region):
            break
        if timeout < 0:
            quick_rts()
            directions('5')
            timeout = 3/e_delay
        timeout-=1
        keyboard.press_and_release('e')
        time.sleep(e_delay)
    print("Found area")
    while not bt.does_exist('Winter\\Monarch.png',confidence=0.7,grayscale=False,region=monarch_region):
        if not g_toggle:
            break
        keyboard.press_and_release('e')
        time.sleep(0.8)
    print("got monarch")

def place_hotbar_units():
    # Scans and places all units in your hotbar, tracking them too
    placing = True
    while placing:
        is_unit = False
        for unit in Settings.Units_Placeable:
            if bt.does_exist(f"Winter\\{unit}_hb.png", confidence=0.8, grayscale=False):
                if unit != "Doom":
                    is_unit = True
                    unit_pos = Settings.Unit_Positions.get(unit)
                    index = Settings.Unit_Placements_Left.get(unit)-1
                    if index <0:
                        is_unit = False
                    print(f"Placing unit {unit} {index+1} at {unit_pos}")
                    place_unit(unit, unit_pos[index])
                    if unit == 'Kag':
                        if USE_KAGUYA:
                            kag_ability = [(645, 444), (743, 817), (1091, 244)]
                            for cl in kag_ability:
                                if cl == (743, 817):
                                    bt.click_image("Winter\\Kaguya_Auto.png", confidence=0.8, grayscale=False, offset=[0,0]) 
                                else:
                                    click(cl[0],cl[1],delay=0.2)
                                    time.sleep(1)
                else:
                    doom = (572, 560)
                    place_unit(unit,doom)
                    time.sleep(2)
                    set_boss()
                    keyboard.press_and_release('z')
                    click(607, 381, delay=0.2)
                    directions('5')
                    buy_monarch()
                    quick_rts()
                    click(doom[0],doom[1],delay=0.2)
                if unit != "Doom":
                    Settings.Unit_Placements_Left[unit]-=1
                    print(f"Placed {unit} | {unit} has {Settings.Unit_Placements_Left.get(unit)} placements left.")
                else:
                    print("Placed doom slayer.")
        if is_unit == False:
            placing = False
            
def ainz_setup(unit:str): 
    '''
    Set's up ainz's abilities and places the unit given.
    '''
    pos  = [(646, 513), (526, 622), (779, 439), (779, 511), (503, 400), (524, 541), (781, 491), (506, 398), (681, 458), (778, 506), (959, 645), (750, 559), (649, 587), (690, 677), (503, 377), (495, 456), (618, 521)]
    for v,i in enumerate(pos):
        if AINZ_SPELLS and v<12:
            continue
        if v == 12: # the click to open world items
            print("Selected Spells")
            click(Settings.Unit_Positions['Ainz'][0][0], Settings.Unit_Positions['Ainz'][0][1], delay=0.2)
            print("Waiting for world item logo")
            while not bt.does_exist("Winter\\CaloricThing.png",confidence=0.8,grayscale=False):
                time.sleep(0.5)
            print(f"Placing unit {unit}")
        click(i[0],i[1],delay=0.2)
    
        time.sleep(1)
        
        if v == 14:
            keyboard.write(unit)
        time.sleep(0.5)

def repair_barricades(): # Repair barricades 
    #DIR_BARRICADE
    keyboard.press_and_release('v')
    time.sleep(1)
    keyboard.press('a')
    time.sleep(0.7)
    keyboard.release('a')
    keyboard.press_and_release('e')
    keyboard.press_and_release('e')
    keyboard.press('w')
    time.sleep(0.2)
    keyboard.release('w')
    keyboard.press_and_release('e')
    keyboard.press_and_release('e')
    keyboard.press('s')
    time.sleep(0.4)
    keyboard.release('s')
    keyboard.press_and_release('e')
    keyboard.press_and_release('e')
    time.sleep(1)
    keyboard.press_and_release('v')
    time.sleep(2)
    
def set_boss(): # Sets unit priority to boss
    keyboard.press_and_release('r')
    keyboard.press_and_release('r')
    keyboard.press_and_release('r')
    keyboard.press_and_release('r')
    keyboard.press_and_release('r')
    
def on_failure():
    print("ran")
    time_out = 60/0.4
    click(Settings.REPLAY_BUTTON_POS[0],Settings.REPLAY_BUTTON_POS[1],delay=0.2)
    time.sleep(1)
    while bt.does_exist("Winter\\DetectLoss.png",confidence=0.7,grayscale=True,region=(311, 295, 825, 428)):
        if time_out<0:
            on_disconnect()
        click(Settings.REPLAY_BUTTON_POS[0],Settings.REPLAY_BUTTON_POS[1],delay=0.2)
        print("Retrying...")
        time_out-=1
        time.sleep(0.4)
    click(Settings.REPLAY_BUTTON_POS[0],Settings.REPLAY_BUTTON_POS[1],delay=0.2)
    

def sell_kaguya(): # Sells kaguya (cant reset while domain is active)
    sold = False
    tick = 0
    click(1119, 450,delay=0.2)
    time.sleep(1)
    while not sold:
        sell = bt.click_image('Winter\\Kaguya.png',confidence=0.8,grayscale=False,offset=[0,0])
        if g_toggle == False:
            break
        if sell == True:
            time.sleep(1)
            keyboard.press_and_release('x')
            sold = True
        ctypes.windll.user32.mouse_event(0x0800, 0, 0, -100, 0)
        tick+=1
        if tick>=40:
            sold = True
        time.sleep(0.4)

def detect_loss():
    time.sleep(10)
    print("Starting loss detection")
    while True:
        if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=10) or pyautogui.pixelMatchesColor(690,270,(199, 45, 40),tolerance=5):
            print("found loss")
            try:
                args = list(sys.argv)
                if "--stopped" in args:
                    args.remove("--stopped")
                if "--restart" in args:
                    args.remove("--restart")    
                sys.stdout.flush()
                subprocess.Popen([sys.executable, *args])
                os._exit(0)
            except Exception as e:
                print("Error")
        time.sleep(1)
def main():
    print("Starting Winter Event Macro")
    rabbit_pos = Settings.Unit_Positions.get("mirko")
    speed_pos =  Settings.Unit_Positions.get("speedwagon")
    start_of_run = datetime.now()
    num_runs = 0  
    while True:
        if ROUND_RESTART > 0:
            print("restart")
            if num_runs >= ROUND_RESTART:
                try:
                    print("recconect")
                    args = list(sys.argv)
                    if "--stopped" in args:
                        args.remove("--stopped")
                    sys.stdout.flush()
                    subprocess.Popen([sys.executable, *args, "--restart"])
                    os._exit(0)
                except Exception as e:
                    print(e)
        global g_toggle
        if g_toggle:
            # Reset all placement counts:
            Reset_Placements = {
                "Ainz": 1,
                'Beni': 3,
                'Rukia': 3,
                'Mage': 3,
                'Escanor': 1,
                'Hero': 3,
                'Kuzan':4,
                'Kag':1
            }   
            if not USE_KAGUYA:
                Reset_Placements['Kag'] = 0
                
            Settings.Unit_Placements_Left = Reset_Placements.copy()
            
            print("Starting new match")
            wait_start()
            quick_rts()
            time.sleep(2)
            # Set up first 2 rabbits
            got_mirko = False
            while not got_mirko:
                directions('1', 'rabbit')
                keyboard.press_and_release('e')
                keyboard.press_and_release('e')
                quick_rts()
                time.sleep(1.5)
                if bt.does_exist("Winter\\Bunny_hb.png",confidence=0.7,grayscale=False, region=(517, 761, 671, 885)):
                    print("Got mirko")
                    got_mirko = True
                else:
                    print("Didnt detect mirko, retrying purchase")
            click(835, 226, delay=0.2) # Start Match
            
             
            place_unit('Bunny', rabbit_pos[0], close=True)
            place_unit('Bunny', rabbit_pos[1], close=True)
            
            # get third
            got_mirko_two = False
            while not got_mirko_two:
                directions('1', 'rabbit')
                keyboard.press_and_release('e')
                quick_rts()
                time.sleep(1.5)
                if bt.does_exist("Winter\\Bunny_hb.png",confidence=0.7,grayscale=False, region=(517, 761, 671, 885)):
                    print("Got mirko")
                    got_mirko_two = True
                else:
                    print("Didnt detect mirko, retrying purchase")
            place_unit('Bunny', rabbit_pos[2], close=True)
            
            #Start farms - speedwagon
            directions('2', 'speed')
            keyboard.press_and_release('e')
            keyboard.press_and_release('e')
            keyboard.press_and_release('e')
            place_unit('Speed', speed_pos[0], close=True)
            place_unit('Speed', speed_pos[1], close=True)
            place_unit('Speed', speed_pos[2], close=True)
            for pos in speed_pos:
                click(pos[0], pos[1], delay=0.2)
                keyboard.press_and_release('z')
                time.sleep(0.5)
            click(607, 381, delay=0.2)
             
            # Tak's placement + max
            
        
            if bt.does_exist("Winter\\Tak_Detect.png",confidence=0.8,grayscale=True):
                bt.click_image("Winter\\Tak_Detect.png",confidence=0.8,grayscale=True,offset=(0,-20))   
                click(50,50,delay=0.1,right_click=True,dont_move=True)
            else:
                keyboard.press('w')
                time.sleep(Settings.TAK_W_DELAY)
                keyboard.release('w')
            if TAK_FINDER:
                path_tak = False
                while not path_tak:
                    keyboard.press('w')
                    time.sleep(0.1)
                    keyboard.release('w')
                    keyboard.press_and_release('e')
                    time.sleep(0.4)
                    if bt.does_exist('Winter\\TakDetect.png', confidence=0.7, grayscale=True,region=(581, 676, 958, 752)) or  bt.does_exist('Winter\\Tak_hb.png', confidence=0.7, grayscale=False):
                        path_tak = True
                    time.sleep(0.5)
            # Press e untill tak is bought
            while not bt.does_exist('Winter\\Tak_hb.png', confidence=0.7, grayscale=False):
                keyboard.press_and_release('e')
                time.sleep(0.2)
            
            place_unit("Tak", Settings.Unit_Positions.get("tak"))
            keyboard.press_and_release('z')
            time.sleep(0.5)
            click(607, 381, delay=0.2)
            
            #DIR_NAMICARD
            if bt.does_exist("Winter\\Nami_detect.png",confidence=0.8,grayscale=True):
                bt.click_image("Winter\\Nami_detect.png",confidence=0.8,grayscale=True,offset=(0,0))   
                click(50,50,delay=0.1,right_click=True,dont_move=True)
            else:
                click(Settings.CTM_NAMI_CARD[0], Settings.CTM_NAMI_CARD[1], delay=0.2, right_click=True) # Goes to nami's card
            time.sleep(2)
            #Nami
            while not bt.does_exist('Winter\\Nami_hb.png', confidence=0.7, grayscale=False, region=(528, 788, 749, 860)): # Buys nami's card
                keyboard.press_and_release('e')
                time.sleep(0.2)
            quick_rts()
            place_unit('Nami',(755, 524), region=(528, 788, 749, 860)) # Nami placement
            keyboard.press_and_release('z')
            # Go to upgrader for fortune
            directions('4')
            upgrader('fortune')
            quick_rts()
            
            # Start auto upgrading first rabbit
            secure_select(rabbit_pos[0])
            time.sleep(0.5)
            keyboard.press_and_release('z')
            click(607, 381, delay=0.2)
            
            # get +100% dmg upgrade
            directions('4')
            upgrader('damage')
            quick_rts()
            
            # Start auto upgrading rabbit 1 & 2
            secure_select(rabbit_pos[1])
            time.sleep(0.5)
            keyboard.press_and_release('z')
            click(607, 381, delay=0.2)
            time.sleep(1)
            secure_select(rabbit_pos[2])
            time.sleep(0.5)
            keyboard.press_and_release('z')
            click(607, 381, delay=0.2)
            time.sleep(1)
            
            # Get first monarch
            directions('5')
            buy_monarch()
            quick_rts()
            time.sleep(1)
            secure_select(rabbit_pos[0])
            
            # Wave 19 lane unlocks for 20% boost
            wave_19 = False
            while not wave_19:
                if avM.get_wave()>=19:
                    #DIR_BUYMAINLANES
                    keyboard.press('d')
                    time.sleep(Settings.BUY_MAIN_LANE_DELAYS[0])
                    keyboard.release('d')
                    keyboard.press_and_release('e')
                    keyboard.press_and_release('e')
                    keyboard.press('w')
                    time.sleep(Settings.BUY_MAIN_LANE_DELAYS[1])
                    keyboard.release('w')
                    keyboard.press_and_release('e')
                    keyboard.press_and_release('e')
                    wave_19=True
                if not g_toggle:
                    break
                time.sleep(0.5)
    
            # Get 2nd and 3rd bunny monarch'd
            quick_rts()
            directions('5')
            buy_monarch()
            quick_rts()
            time.sleep(1)
            secure_select(rabbit_pos[1])
            time.sleep(1)
            directions('5')
            buy_monarch()
            quick_rts()
            time.sleep(1)
            secure_select(rabbit_pos[2])
            
            # Get all upgrades
            directions('4')
            upgrader('range')
            upgrader('speed')
            upgrader('armor')
            quick_rts()
            directions('3')
            
            Ben_Upgraded = False
            Erza_Upgraded = False
            
            
            # Lucky box
            gamble_done = False
            g_toggle= True
            ainzplaced=False
            while not gamble_done:
                keyboard.press_and_release('e')
                 
                if bt.does_exist("Winter\\Full_Bar.png",confidence=0.7,grayscale=True, region=(493, 543, 1024, 785)) or bt.does_exist("Winter\\NO_YEN.png",confidence=0.7,grayscale=True,  region=(493, 543, 1024, 785)):
                    quick_rts()
                    time.sleep(3)
                    place_hotbar_units()
                    directions('3')
                if not Erza_Upgraded:
                    erza_buffer = Settings.Unit_Positions['Mage']
                    if Settings.Unit_Placements_Left['Mage'] == 0:
                        quick_rts()
                        time.sleep(1)
                        # BUffer
                        secure_select(erza_buffer[0])
                        time.sleep(8)
                        click(356,655)
                        time.sleep(0.8)
                        click(647, 449,delay=0.2)
                        while not bt.does_exist('Winter\\Erza_Armor.png',confidence=0.8,grayscale=True):
                            click(1015,690,delay=0.2)
                            time.sleep(0.5)
                        click(752, 548,delay=0.2)
                        time.sleep(0.5)
                        click(1140, 290,delay=0.2)
                        time.sleep(0.5)
                        click(607, 381, delay=0.2)
                            
                        #Duelist 1
                        secure_select(erza_buffer[1])
                        time.sleep(0.8)
                        keyboard.press_and_release('z')
                        click(647, 449,delay=0.2)
                        while not bt.does_exist('Winter\\Erza_Armor.png',confidence=0.8,grayscale=True):
                            click(747, 690,delay=0.2)
                            time.sleep(0.5)
                        click(752, 548,delay=0.2)
                        time.sleep(0.5)
                        click(1140, 290,delay=0.2)
                        set_boss()
                        time.sleep(0.5)
                        
                        #Duelist 2
                        secure_select(erza_buffer[2])
                        time.sleep(0.8)
                        click(647, 449,delay=0.2)
                        keyboard.press_and_release('z')
                        while not bt.does_exist('Winter\\Erza_Armor.png',confidence=0.8,grayscale=True):
                            click(747, 690,delay=0.2)
                            time.sleep(0.5)
                        click(752, 548,delay=0.2)
                        time.sleep(0.5)
                        click(1140, 290,delay=0.2)
                        set_boss()
                        time.sleep(0.5)
                        click(607, 381, delay=0.2)
                        
                        directions('5')
                        buy_monarch()
                        quick_rts()
                        click(erza_buffer[1][0],erza_buffer[1][1],delay=0.2)
                        time.sleep(0.5)
                        
                        directions('5')
                        buy_monarch()
                        quick_rts()
                        click(erza_buffer[2][0],erza_buffer[2][1],delay=0.2)
                        time.sleep(0.5)
                        Erza_Upgraded = True
                        # more gamble
                        directions('3')
                if not Ben_Upgraded:
                    if Settings.Unit_Placements_Left['Beni'] == 0:
                        quick_rts()
                        time.sleep(1)
                        for ben in Settings.Unit_Positions['Beni']:
                            click(ben[0],ben[1],delay=0.2)
                            secure_select((ben[0],ben[1]))
                            time.sleep(0.5)
                            keyboard.press_and_release('z')
                            set_boss()
                            time.sleep(0.5)
                            click(607, 381, delay=0.2)
                            directions('5')
                            buy_monarch()
                            quick_rts()
                            time.sleep(0.5)
                            secure_select((ben[0],ben[1]))
                            time.sleep(0.5)
                            click(607, 381, delay=0.2)
                        Ben_Upgraded = True
                        # more gamble
                        directions('3')
                if not ainzplaced:
                    if Settings.Unit_Placements_Left['Ainz'] == 0: # Ainz thingy
                        ainzplaced = True
                        quick_rts()
                        time.sleep(1)
                        ainz_pos = Settings.Unit_Positions['Ainz']
                        pos = Settings.Unit_Positions.get("Caloric_Unit")
                        secure_select((ainz_pos[0]))
                        time.sleep(0.5)
                        if Settings.USE_WD == True:
                            ainz_setup(unit="world des")
                        elif Settings.USE_DIO == True:
                            ainz_setup(unit="god")
                        elif USE_BUU:
                            ainz_setup(unit="boo")
                        elif USE_FREIZA:
                            ainz_setup(unit="Lord Fr")
                        else:
                            ainz_setup(unit=Settings.USE_AINZ_UNIT)
                        global AINZ_SPELLS
                        if not AINZ_SPELLS:
                            AINZ_SPELLS = True
                        click(pos[0], pos[1], delay=0.67) # Place world destroyer + auto upgrade
                        time.sleep(0.5)
                        while not pyautogui.pixel(607, 381) == (255,255,255):
                            if g_toggle == False:
                                break
                            click(pos[0], pos[1], delay=0.67)
                            time.sleep(0.5)
                        time.sleep(1)
                        if Settings.USE_DIO:
                            ability_clicks = [(648, 448), (1010, 563), (1099, 309)]
                            for p in ability_clicks:
                                click(p[0], p[1], delay=0.2)
                                time.sleep(1.2)
                        if Settings.MAX_UPG_AINZ_PLACEMENT:
                            keyboard.press_and_release('z')
                        if Settings.MONARCH_AINZ_PLACEMENT:
                            directions('5')
                            buy_monarch()
                            quick_rts()
                            time.sleep(1)
                            click(pos[0], pos[1], delay=0.67) 
                        if USE_FREIZA:
                            freiza_aliens = 0
                            alien_pos = [(825, 692), (883, 693), (931, 692)]
                            while freiza_aliens < 3:
                                secure_select(Settings.Unit_Positions.get("Caloric_Unit"))
                                while not bt.does_exist("Winter\\FreizaAbility.png",confidence=0.7,grayscale=True):
                                    time.sleep(0.5)
                                bt.click_image("Winter\\FreizaAbility.png",confidence=0.7,grayscale=True,offset=(0,0))
                                time.sleep(2)
                                click(466, 681,0.2)
                                time.sleep(0.5)
                                pos = alien_pos[p]
                                while not pyautogui.pixel(607, 381) == (255,255,255):
                                    click(pos[0], pos[1], delay=0.67)
                                    time.sleep(1)
                                time.sleep(1)
                                keyboard.press_and_release('z')
                                freiza_aliens+=1
                            click(607, 381, delay=0.2)
                        time.sleep(1)
                        print("Placed ainz's unit")
                        click(607, 381, delay=0.2)
                        
                        # Ainz auto upgrade + monarch
                        secure_select((ainz_pos[0]))
                        time.sleep(0.5)
                        keyboard.press_and_release('z')
                        time.sleep(0.5)
                        click(607, 381, delay=0.2)
                        directions('5')
                        buy_monarch()
                        quick_rts()
                        time.sleep(1)
                        click(ainz_pos[0][0],ainz_pos[0][1],delay=0.2)
                        time.sleep(1)
                        # go gamble more son
                        directions('3')
                print("===============================")
                is_done = True
                for unit in Settings.Units_Placeable:
                    if unit != "Doom":
                        if Settings.Unit_Placements_Left[unit] > 0:
                            is_done = False
                            print(f"{unit} has {Settings.Unit_Placements_Left[unit]} placements left.")
                print("===============================")
                if is_done:
                    gamble_done = True
                time.sleep(0.1)
            print("Gambling done")
             
               

            # Auto upgrade + Monarch everything else
            
            # set up buffer erza
            
            quick_rts()
            time.sleep(1)
    
            # World destroyer
            if Settings.USE_WD:
                secure_select(Settings.Unit_Positions.get("Caloric_Unit"))
                time.sleep(1)
                while True:
                    if bt.does_exist("Winter\\StopWD.png",confidence=0.8,grayscale=False,region=(433, 477, 603, 555)):
                        print("Stop")
                        break
                    if bt.does_exist("Unit_Maxed.png",confidence=0.8,grayscale=False):
                        print("Stop, maxed on accident")
                        break
                    keyboard.press_and_release('t')
                    time.sleep(0.5)
                time.sleep(0.5)
                click(607, 381, delay=0.2)
            elif Settings.USE_DIO:
                secure_select(Settings.Unit_Positions.get("Caloric_Unit"))
                time.sleep(1)
                while True:
                    if bt.does_exist("Winter\\DIO_MOVE.png",confidence=0.8,grayscale=False,region=(433, 477, 603, 555)):
                        print("Stop")
                        break
                    if bt.does_exist("Unit_Maxed.png",confidence=0.8,grayscale=False):
                        print("Stop, maxed on accident")
                        break
                    keyboard.press_and_release('t')
                    time.sleep(0.5)
                time.sleep(0.5)
                click(607, 381, delay=0.2)
            elif USE_BUU:
                secure_select(Settings.Unit_Positions.get("Caloric_Unit"))
                time.sleep(1)
                while True:
                    if bt.does_exist("Winter\\Buu_Ability.png",confidence=0.5,grayscale=False):
                        print("Found Ability")
                        bt.click_image("Winter\\Buu_Ability.png",confidence=0.5,grayscale=False,offset=(0,0))
                        time.sleep(1)
                        click(441,151,0.2)
                        time.sleep(1)
                    if bt.does_exist("Winter\\BuuSellDetect.png",confidence=0.8,grayscale=False, ):
                        print("SellBuu")
                        keyboard.press_and_release('x')
                        break
                    if not bt.does_exist("Winter\\Unit_Maxed.png",confidence=0.8,grayscale=False):
                        print("Upgrade")
                        keyboard.press_and_release('t')
                        time.sleep(.1)           
            elif Settings.MAX_UPG_AINZ_PLACEMENT == False:
                secure_select(Settings.Unit_Positions.get("Caloric_Unit"))
                time.sleep(1)
                while True:
                    if bt.does_exist("Winter\\YOUR_MOVE.png",confidence=0.8,grayscale=False,region=(433, 477, 603, 555)):
                        print("Stop")
                        break
                    if bt.does_exist("Unit_Maxed.png",confidence=0.8,grayscale=False):
                        print("Stop, maxed on accident")
                        break
                    keyboard.press_and_release('t')
                    time.sleep(0.5)
                time.sleep(0.5)
                click(607, 381, delay=0.2)
            
            # ice queen
            for ice in Settings.Unit_Positions['Rukia']:
                 
                secure_select((ice[0],ice[1]))
                time.sleep(0.5)
                set_boss()
                time.sleep(0.5)
                click(607, 381, delay=0.2)
                directions('5')
                buy_monarch()
                quick_rts()
                time.sleep(0.5)
                secure_select((ice[0],ice[1]))
                time.sleep(0.5)
                while True:
                    if bt.does_exist("Winter\\StopUpgradeRukia.png",confidence=0.8,grayscale=False,region=(433, 477, 603, 555)):
                        print("Stop")
                        break
                    if bt.does_exist("Unit_Maxed.png",confidence=0.8,grayscale=False):
                        print("Stop, maxed on accident")
                        break
                    keyboard.press_and_release('t')
                    time.sleep(0.5)
                time.sleep(0.5)
                click(607, 381, delay=0.2)
             
               

                
            for gamer in Settings.Unit_Positions['Hero']:
                 

                click(gamer[0],gamer[1],delay=0.2)
                time.sleep(0.5)
                keyboard.press_and_release('z')
                set_boss()
                time.sleep(0.5)
                click(607, 381, delay=0.2)
                directions('5')
                buy_monarch()
                quick_rts()
                time.sleep(0.5)
                click(gamer[0],gamer[1],delay=0.2)
                time.sleep(0.5)
                click(607, 381, delay=0.2)
             
            
            for kuzan in Settings.Unit_Positions['Kuzan']:
                click(kuzan[0],kuzan[1],delay=0.2)
                time.sleep(0.5)
                keyboard.press_and_release('z')
                set_boss()
                time.sleep(0.5)
                click(607, 381, delay=0.2)
                directions('5')
                buy_monarch()
                quick_rts()
                time.sleep(0.5)
                click(kuzan[0],kuzan[1],delay=0.2)
                time.sleep(0.5)
                click(607, 381, delay=0.2)

             
               
            for esc in Settings.Unit_Positions['Escanor']:
                click(esc[0],esc[1],delay=0.2)
                time.sleep(0.5)
                keyboard.press_and_release('z')
                set_boss()
                time.sleep(0.5)
                click(607, 381, delay=0.2)
                directions('5')
                buy_monarch()
                quick_rts()
                time.sleep(0.5)
                click(esc[0],esc[1],delay=0.2)
                time.sleep(0.5)
                click(607, 381, delay=0.2)
            if Settings.WAVE_RESTART_150:
                wave_150 = False
                done_path = False   
                while not wave_150:
                    if avM.get_wave() == 149 and not done_path:       
                        def spam_e():
                            while not done_path:
                                keyboard.press_and_release('e')
                                time.sleep(0.2)
                            print("Done buying lanes")
                        quick_rts()
                        #DIR_BUYRESTLANES
                        keyboard.press_and_release('f')
                        time.sleep(0.7)
                        bt.click_image("Winter\\LookDownFinder.png",confidence=0.8,grayscale=False,offset=[0,-50])
                        keyboard.press_and_release('f')
                        clicks_look_down =  [(404, 400), (649, 772), (745, 858)]
                        for i in clicks_look_down:
                            click(i[0],i[1],delay=0.1)
                            if i != (649, 772):
                                time.sleep(0.3)
                            else:
                                time.sleep(1)
                        keyboard.press('o')
                        time.sleep(1)
                        keyboard.release('o')
                        keyboard.press('s')
                        time.sleep(Settings.BUY_FINAL_LANE_DELAYS[0])
                        keyboard.release('s')
                        keyboard.press_and_release('v')
                        time.sleep(1)
                        Thread(target=spam_e).start()
                        keyboard.press('a')
                        time.sleep(Settings.BUY_FINAL_LANE_DELAYS[1])
                        keyboard.release("a")
                        keyboard.press('d')
                        time.sleep(Settings.BUY_FINAL_LANE_DELAYS[2])
                        keyboard.release('d')
                        keyboard.press_and_release('v')
                        quick_rts()
                        time.sleep(2)
                        done_path = True
                    if avM.get_wave()==150:
                        wave_150 = True
                    else:
                        if avM.get_wave()%2==0 or avM.get_wave() == 139:
                            repair_barricades()
                            quick_rts()
                    time.sleep(2)
            else:
                wave_140 = False
                done_path = False   
                while not wave_140:
                    if avM.get_wave() == 139 and not done_path:       
                        def spam_e():
                            while not done_path:
                                keyboard.press_and_release('e')
                                time.sleep(0.2)
                            print("Done buying lanes")
                        quick_rts()
                        #DIR_BUYRESTLANES
                        keyboard.press_and_release('f')
                        time.sleep(0.7)
                        bt.click_image("Winter\\LookDownFinder.png",confidence=0.8,grayscale=False,offset=[0,-50])
                        keyboard.press_and_release('f')
                        clicks_look_down =  [(404, 400), (649, 772), (745, 858)]
                        for i in clicks_look_down:
                            click(i[0],i[1],delay=0.1)
                            if i != (649, 772):
                                time.sleep(0.3)
                            else:
                                time.sleep(1)
                        keyboard.press('o')
                        time.sleep(1)
                        keyboard.release('o')
                        keyboard.press('s')
                        time.sleep(Settings.BUY_FINAL_LANE_DELAYS[0])
                        keyboard.release('s')
                        keyboard.press_and_release('v')
                        time.sleep(1)
                        Thread(target=spam_e).start()
                        keyboard.press('a')
                        time.sleep(Settings.BUY_FINAL_LANE_DELAYS[1])
                        keyboard.release("a")
                        keyboard.press('d')
                        time.sleep(Settings.BUY_FINAL_LANE_DELAYS[2])
                        keyboard.release('d')
                        keyboard.press_and_release('v')
                        quick_rts()
                        time.sleep(2)
                        done_path = True
                    if avM.get_wave()==140:
                        wave_140 = True
                    else:
                        if avM.get_wave()%2==0 or avM.get_wave() == 139 and done_path:
                            repair_barricades()
                            quick_rts()
                    time.sleep(2)
            num_runs+=1
            print(f"Run over, runs: {num_runs}")
            try:
                    victory = wt.screen_shot_memory()
                    runtime = f"{datetime.now()-start_of_run}"
                
                    g = Thread(target=webhook.send_webhook,
                        kwargs={

                                "run_time": f"{str(runtime).split('.')[0]}",
                                "num_runs": num_runs,
                                "task_name": "Winter Event",
                                "img": victory,
                            },
                        )            
                    g.start()
            except Exception as e:
                print(f" error {e}")
                
            if USE_KAGUYA:    
                ainz_pos = Settings.Unit_Positions['Ainz']
                click(ainz_pos[0][0],ainz_pos[0][1],delay=0.2)
                time.sleep(0.5)
                keyboard.press_and_release('x')
                time.sleep(0.5)
                keyboard.press_and_release('f')
                time.sleep(1)
                sell_kaguya()
                keyboard.press_and_release('f')
                
            match_restarted = False
            while not match_restarted:
                avM.restart_match() 
                time.sleep(0.5)
                if avM.get_wave() == 0:
                    match_restarted = True
                time.sleep(5)

def disconnect_checker():
    time.sleep(60) # intial detect delay
    while True:
       if bt.does_exist("Winter\\Disconnected.png",confidence=0.9,grayscale=True,region=(525,353,972,646)) or bt.does_exist("Winter\\Disconnect_Two.png",confidence=0.9,grayscale=True,region=(525,353,972,646)):
        print("found disconnected")
        try:
            args = list(sys.argv)
            if "--stopped" in args:
                args.remove("--stopped")
            if "--restart" in args:
                args.remove("--restart")    
            sys.stdout.flush()
            subprocess.Popen([sys.executable, *args])
            os._exit(0)
        except Exception as e:
            print("Error")
        time.sleep(6)
def on_disconnect():
    #win32 bindings using ctypes
    # FUCK CTYPS THIS HSIT IS CANCER RWHAT THE FUCK IS IT DOING 
    psapi = ctypes.WinDLL("Psapi.dll")
    kernel32 = ctypes.WinDLL("kernel32.dll")
    EnumProcesses = psapi.EnumProcesses
    EnumProcesses.argtypes = [ctypes.POINTER(ctypes.wintypes.DWORD), ctypes.wintypes.DWORD, ctypes.POINTER(ctypes.wintypes.DWORD)]
    EnumProcesses.restype = ctypes.wintypes.BOOL
    OpenProcess = kernel32.OpenProcess
    OpenProcess.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.BOOL, ctypes.wintypes.DWORD]
    OpenProcess.restype = ctypes.wintypes.HANDLE
    QueryFullProcessImageNameW = kernel32.QueryFullProcessImageNameW
    QueryFullProcessImageNameW.argtypes = [ctypes.wintypes.HANDLE, ctypes.wintypes.DWORD, ctypes.wintypes.LPWSTR, ctypes.POINTER(ctypes.wintypes.DWORD)]
    QueryFullProcessImageNameW.restype = ctypes.wintypes.BOOL
    CloseHandle = kernel32.CloseHandle
    PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
    def get_exe_path(pid):
        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        buf = ctypes.create_unicode_buffer(260)
        size = ctypes.wintypes.DWORD(len(buf))
        path = ctypes.windll.kernel32.QueryFullProcessImageNameW(handle,0,buf,ctypes.byref(size))
        CloseHandle(handle)
        return buf.value if path else None
    def find_roblox_pid():
        arr = (ctypes.wintypes.DWORD*4096)()
        needed = ctypes.wintypes.DWORD()
        if not EnumProcesses(arr,ctypes.sizeof(arr),ctypes.byref(needed)):
            return []
        count = needed.value // ctypes.sizeof(ctypes.wintypes.DWORD)
        pids = arr[:count]
        match = []
        for pid in pids:
            path = get_exe_path(pid)
            if not path:
                continue
            exe = os.path.basename(path).lower()
            if exe == "robloxplayerbeta.exe":
                match.append(pid)
        return match
    pid = find_roblox_pid()
    roblox_exe = get_exe_path(pid=pid[0])
    subprocess.Popen([roblox_exe, f"roblox://placeId={16146832113}&linkCode={PRIVATE_SERVER_CODE}/"])
    time.sleep(10)
    try:
        window = None
        while window is None:
            find_title = next(filter(lambda p: "Roblox" in p, gw.getAllTitles()))
            window = gw.getWindowsWithTitle(find_title)[0]
            time.sleep(2)
        #<Win32Window left="200", top="161", width="1100", height="800", title="Roblox">
        window.left=200
        window.top=100
        window.width=1100
        window.height=800
    except Exception as e:
        print(f"error when resize: {e}")
    while not bt.does_exist("Winter\\AreaIcon.png",confidence=0.8,grayscale=False):
        if pyautogui.pixelMatchesColor(1085,321,(255,255,255),tolerance=5):  
            click(1083,321,delay=0.1)
        time.sleep(1)
    time.sleep(1)
    if pyautogui.pixelMatchesColor(1085,321,(255,255,255),tolerance=5):  
            click(1083,321,delay=0.1)
    bt.click_image("Winter\\AreaIcon.png",confidence=0.8,grayscale=False,offset=(0,0))
    time.sleep(3)
    open_menu = False
    def spam_e():
        #{(884, 266): (170, 232, 235)}
        while not open_menu:
            keyboard.press_and_release('e')
            time.sleep(0.2)
    while not open_menu:
        click(656,764,delay=0.1)
        time.sleep(1)
        keyboard.press('a')
        time.sleep(1)
        keyboard.release('a')
        Thread(target=spam_e).start()
        keyboard.press('a')
        time.sleep(1)
        keyboard.release('a')
        if pyautogui.pixelMatchesColor(888,269,(165, 232, 235),tolerance=30):
            open_menu = True
        if not open_menu:
            if pyautogui.pixelMatchesColor(1085,321,(255,255,255),tolerance=5):  
                click(1083,321,delay=0.1)
            bt.click_image("Winter\\AreaIcon.png",confidence=0.8,grayscale=False,offset=(0,0))
        time.sleep(3)
    # [(454, 703), (659, 509), (301, 676)]
    click(454, 703,delay=0.1)
    time.sleep(2)
    click(659, 509,delay=0.1)
    time.sleep(2)
    click(301, 676,delay=0.1)
    time.sleep(2)
    wait_start()
    wait_start()
    wait_start()
    keyboard.press('i')
    time.sleep(1)
    keyboard.release('i')
    ctypes.windll.user32.mouse_event(0x0001, 0, 1000, 0, 0)
    keyboard.press('o')
    time.sleep(1)
    keyboard.release('o')      
    click(488, 463,delay=0.2)

if "--restart" in sys.argv:
    on_disconnect()


       
    
Thread(target=disconnect_checker).start()
print(f"Launched with args {sys.argv}")
print(f"Running loxer's winter macro v{VERSION_N}")
if bt.does_exist("Winter\\Disconnected.png",confidence=0.9,grayscale=True,region=(525,353,972,646)) or  bt.does_exist("Winter\\Disconnect_Two.png",confidence=0.9,grayscale=True,region=(525,353,972,646)):
    on_disconnect()
    time.sleep(6)
if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=10) or pyautogui.pixelMatchesColor(690,270,(199, 45, 40),tolerance=5) or bt.does_exist("Winter\\DetectLoss.png",confidence=0.7,grayscale=True,region=(311, 295, 825, 428)):
    on_failure()
    time.sleep(6)
Thread(target=detect_loss).start()
try:
    window = None
    while window is None:
        find_title = next(filter(lambda p: "Roblox" in p, gw.getAllTitles()))
        window = gw.getWindowsWithTitle(find_title)[0]
    time.sleep(1)
    #<Win32Window left="200", top="100", width="1100", height="800", title="Roblox">
    if window.left == 200 and window.top == 100 and window.width == 1100 and window.height == 800:
        print("Roblox is positioned correctly")
    else:
        print("Roblox is not positioned correctly, please run position.py")
        sys.exit(0)
except Exception as e:
    print(f"error check window {e}")
if Settings.AUTO_START:
    if not "--stopped" in sys.argv:
        g_toggle = True
    else:
        print("Program was STOPPED, won't auto start")
for z in range(3):
    print(f"Starting in {3-z}")
    time.sleep(1)
if g_toggle:
    if avM.get_wave() >= 1:
        avM.restart_match()
    #release potential keys
    keyboard.press_and_release('w')
    keyboard.press_and_release('a')
    keyboard.press_and_release('s')
    keyboard.press_and_release('d')
    main()
else:
    while not g_toggle:
        time.sleep(1)
    if avM.get_wave() >= 1:
        avM.restart_match()
    #release potential keys
    keyboard.press_and_release('w')
    keyboard.press_and_release('a')
    keyboard.press_and_release('s')
    keyboard.press_and_release('d')
    main()
