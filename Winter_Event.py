
from Tools import botTools as bt
from Tools import winTools as wt
from Tools import avMethods as avM
import webhook
import keyboard
import time
import pyautogui
from datetime import datetime
from threading import Thread
import ctypes


# Variables
STOP_START_HOTKEY = 'l'
USE_NIMBUS = True # Use the nimbus cloud instead of newsman (more consistent + better)
USE_WD = True # use world destroyer
USE_DIO = False # built in dio thing instead
USE_AINZ_UNIT = "" # name of the unit
MONARCH_AINZ_PLACEMENT = False # Gets monarch for the unit you place with caloric sone
MAX_UPG_AINZ_PLACEMENT = False # Will just press z for auto upgrade if true, else it goes untill it finds a certain move (you need your own picture of it)
AINZ_PLACEMENT_MOVE_PNG = "Winter\\YOUR_MOVE.png" # name the screenshot YOUR_MOVE, it will upgrade the unit untill it finds that image

Unit_Placements_Left = {
    "Ainz": 1,
    'Beni': 3,
    'Rukia': 3,
    'Mage': 3,
    'Escanor': 1,
    'Hero': 3,
    'Kuzan':4,
    'Kag':1
}   

Unit_Positions = {
        "Ainz": [(745, 470)],
        'Beni': [(873, 522),(843, 523), (807, 522)],
        'Rukia': [(784, 557),(827, 556),(867, 556)],
        'Mage': [(740, 557), (679, 583), (681, 498)],
        'Escanor':[(587, 519)],
        'Hero': [(916, 501),(927, 528),(916, 554)],
        'Kuzan':[(938, 477), (951, 570), (657, 521), (654, 559)],
        'Kag':[(643, 490)] 
        
}
Units_Placeable = ['Ainz','Beni','Rukia','Mage','Escanor','Hero','Kuzan','Kag']
# Mage = erza, Hero = trash gamer

# Failsafe key
g_toggle = False
def toggle():
    global g_toggle
    g_toggle = not g_toggle
4
keyboard.add_hotkey(STOP_START_HOTKEY, toggle) 

# Actions
def click(x,y, delay: int | None=None, right_click: bool | None = None) -> None:
    if delay is not None:
        delay=delay
    else:
        delay = 0.65
    pyautogui.moveTo(x,y)
    ctypes.windll.user32.mouse_event(0x0001, 0, 1, 0, 0)
    time.sleep(delay)
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
        
def directions(area: str, unit: str | None=None, CTM: bool | None = None): # This is for all the pathing
    '''
    This is the pathing for all the areas: 1 [rabbit, nami, hero (trash gamer)], 2 [speed, tak], 3: Mystery box, 4: Upgrader, 5: Monarch upgrader
    '''
    # All this does is set up camera whenever it's the first time running, disable if needed
        
    #Contains rabbit, nami, and hero
    if USE_NIMBUS:
        if area == '1':  
            #DIR_PATHING
            # Pathing
            if not CTM:
                keyboard.press('a')
                time.sleep(0.4)
                keyboard.release('a')
                keyboard.press_and_release('v')
                time.sleep(1)
                keyboard.press('w')
                time.sleep(1.5)
                keyboard.release('w')
                keyboard.press('a')
                time.sleep(1.1)
                keyboard.release('a')
            else:
                pos =  [(669, 287), (738, 188), (230, 312)]
                keyboard.press_and_release('v')
                time.sleep(1)
                for p in pos:
                    click(p[0],p[1],delay=0.2,right_click=True)
                    time.sleep(1.5)
                time.sleep(1.5)
            if unit == 'rabbit':
                click(596, 310, delay=0.2,right_click=True) # Click to move
                time.sleep(1)
            if unit == "nami":
                click(742, 219, delay=0.2,right_click=True)
                time.sleep(1)
            if unit == "hero":
                click(887, 305, delay=0.2,right_click=True)
                time.sleep(1)
            keyboard.press_and_release('v') 
            time.sleep(2)
        # Speed wagon + Tak
        if area == '2':
            if not CTM:
                keyboard.press('a')
                time.sleep(0.4)
                keyboard.release('a')
                keyboard.press_and_release('v')
                time.sleep(1)
                keyboard.press('w')
                time.sleep(1.5)
                keyboard.release('w')
            else:
                pos =  [(668, 292), (752, 182), (752, 348)]
                keyboard.press_and_release('v')
                time.sleep(1)
                for p in pos:
                    click(p[0],p[1],delay=0.2,right_click=True)
                    time.sleep(1.5)
                time.sleep(1.5)
            #(534, 706), (535, 546)
            if unit == 'speed':
                click(534, 706, delay=0.2,right_click=True)
                time.sleep(1)
            if unit == 'tak':
                click(535, 546, delay=0.2,right_click=True)
                time.sleep(1)
            keyboard.press_and_release('v')
            time.sleep(2)
        # Gambling time
        if area == '3': 
            
            keyboard.press_and_release('v')
            time.sleep(1)
            keyboard.press('a')
            time.sleep(3)
            keyboard.release('a')

            keyboard.press('s')
            time.sleep(1.65)
            keyboard.release('s')

            keyboard.press('d')
            time.sleep(1.6)
            keyboard.release('d')

            keyboard.press('s')
            time.sleep(0.5)
            keyboard.release('s')
            keyboard.press_and_release('v')
            time.sleep(2)

        if area == '4': #  Upgrader location
            keyboard.press_and_release('v')
            time.sleep(1)
            keyboard.press('a')
            time.sleep(3)
            keyboard.release('a')

            keyboard.press('s')
            time.sleep(1.85)
            keyboard.release('s')
            keyboard.press_and_release('v')
            time.sleep(2)
            
        if area == '5': # This is where it buys monarch
            keyboard.press_and_release('v')
            time.sleep(1)
            keyboard.press('a')
            time.sleep(3)
            keyboard.release('a')

            keyboard.press('w')
            time.sleep(1.85)
            keyboard.release('w')
            keyboard.press_and_release('v')
            time.sleep(2)
    else:
        #Contains rabbit, nami, and hero
        if area == '1':  
            #DIR_PATHING
            # Pathing
            if not CTM:
                keyboard.press('a')
                time.sleep(0.4)
                keyboard.release('a')
                keyboard.press_and_release('v')
                time.sleep(1)
                keyboard.press('w')
                time.sleep(1.5)
                keyboard.release('w')
                keyboard.press('a')
                time.sleep(1.1)
                keyboard.release('a')
            else:
                pos =  [(669, 287), (738, 188), (230, 312)]
                keyboard.press_and_release('v')
                time.sleep(1)
                for p in pos:
                    click(p[0],p[1],delay=0.2,right_click=True)
                    time.sleep(1.5)
                time.sleep(1.5)
            if unit == 'rabbit':
                click(596, 310, delay=0.2,right_click=True) # Click to move
                time.sleep(1)
            if unit == "nami":
                click(742, 219, delay=0.2,right_click=True)
                time.sleep(1)
            if unit == "hero":
                click(887, 305, delay=0.2,right_click=True)
                time.sleep(1)
            keyboard.press_and_release('v') 
            time.sleep(2)
        # Speed wagon + Tak
        if area == '2':
            if not CTM:
                keyboard.press('a')
                time.sleep(0.4)
                keyboard.release('a')
                keyboard.press_and_release('v')
                time.sleep(1)
                keyboard.press('w')
                time.sleep(1.5)
                keyboard.release('w')
            else:
                pos =  [(668, 292), (752, 182), (752, 348)]
                keyboard.press_and_release('v')
                time.sleep(1)
                for p in pos:
                    click(p[0],p[1],delay=0.2,right_click=True)
                    time.sleep(1.5)
                time.sleep(1.5)
            #(534, 706), (535, 546)
            if unit == 'speed':
                click(534, 706, delay=0.2,right_click=True)
                time.sleep(1)
            if unit == 'tak':
                click(535, 546, delay=0.2,right_click=True)
                time.sleep(1)
            keyboard.press_and_release('v')
            time.sleep(2)
        # Gambling time
        if area == '3': 
            
            keyboard.press_and_release('v')
            time.sleep(1)
            keyboard.press('a')
            time.sleep(2.8)
            keyboard.release('a')

            keyboard.press('s')
            time.sleep(1.65)
            keyboard.release('s')

            keyboard.press('d')
            time.sleep(1.6)
            keyboard.release('d')

            keyboard.press('s')
            time.sleep(0.4)
            keyboard.release('s')
            keyboard.press_and_release('v')
            time.sleep(2)

        if area == '4': #  Upgrader location
            keyboard.press_and_release('v')
            time.sleep(1)
            keyboard.press('a')
            time.sleep(3)
            keyboard.release('a')

            keyboard.press('s')
            time.sleep(1.65)
            keyboard.release('s')
            keyboard.press_and_release('v')
            time.sleep(2)
            
        if area == '5': # This is where it buys monarch
            keyboard.press_and_release('v')
            time.sleep(1)
            keyboard.press('a')
            time.sleep(3)
            keyboard.release('a')

            keyboard.press('w')
            time.sleep(1.65)
            keyboard.release('w')
            keyboard.press_and_release('v')
            time.sleep(2)
        
        
def upgrader(upgrade: str):
    '''
    Buys the upgrades for the winter event: fortune, range, damage, speed, armor
    '''
    keyboard.press_and_release('e')
    while not pyautogui.pixel(1111,310) == (255,255,255):
        keyboard.press_and_release('e')
        time.sleep(0.2)
    if upgrade == 'fortune':
        click(966, 471, delay=0.2)
        time.sleep(0.5)
        while not pyautogui.pixelMatchesColor(966, 471,expectedRGBColor=(24, 24, 24),tolerance=20):
            if not g_toggle:
                break
            click(966, 471, delay=0.2)
            time.sleep(0.8)
        click(1112, 309, delay=0.2)
    if upgrade == 'range':
        click(962, 621, delay=0.2)
        time.sleep(0.5)
        while not pyautogui.pixelMatchesColor(962, 621,expectedRGBColor=(24, 24, 24),tolerance=20):
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
        while not pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=20):
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
        while not pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=20):  
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
        while not  pyautogui.pixelMatchesColor(pos[0], pos[1],expectedRGBColor=(24, 24, 24),tolerance=20):
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
        click(pos[0],pos[1],delay=0.2)
        time.sleep(0.5)
    print(f"Selected unit at {pos}")


def place_unit(unit: str, pos : tuple[int,int], close: bool | None=None, region: tuple | None=None):
    '''
    Places a unit found in Winter\\UNIT_hb.png, at location given in pos. 
    '''
    time_out = 50
    # Click on the unit
    if region is None:
        while not bt.does_exist(f"Winter\\{unit}_hb.png", confidence=0.8, grayscale=False):
            time.sleep(0.3)
        bt.click_image(f'Winter\\{unit}_hb.png', confidence=0.8,grayscale=False,offset=(0,0))
    else:
        while not bt.does_exist(f"Winter\\{unit}_hb.png", confidence=0.8, grayscale=False,region=region):
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
        time.sleep(0.6)
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
    while not bt.does_exist('Winter\\Monarch.png',confidence=0.7,grayscale=False,region=monarch_region):
        if not g_toggle:
            break
        keyboard.press_and_release('e')
        time.sleep(0.8)
    print("got monarch")

def place_hotbar_units():
    global Unit_Placements_Left
    # Scans and places all units in your hotbar, tracking them too
    placing = True
    while placing:
        is_unit = False
        for unit in Units_Placeable:
            if bt.does_exist(f"Winter\\{unit}_hb.png", confidence=0.8, grayscale=False):
                is_unit = True
                unit_pos = Unit_Positions.get(unit)
                index = Unit_Placements_Left.get(unit)-1
                if index <0:
                    is_unit = False
                print(f"Placing unit {unit} {index+1} at {unit_pos}")
                place_unit(unit, unit_pos[index])
                if unit == 'Kag':
                    kag_ability = [(645, 444), (743, 817), (1091, 244)]
                    for cl in kag_ability:
                        if cl == (743, 817):
                            bt.click_image("Winter\\Kaguya_Auto.png", confidence=0.8, grayscale=False, offset=[0,0]) 
                        else:
                            click(cl[0],cl[1],delay=0.2)
                            time.sleep(1)
                Unit_Placements_Left[unit]-=1
                print(f"Placed {unit} | {unit} has {Unit_Placements_Left.get(unit)} placements left.")
        if is_unit == False:
            placing = False
            
def ainz_setup(unit:str): 
    '''
    Set's up ainz's abilities and places the unit given.
    '''
    pos  = [(646, 513), (526, 622), (779, 439), (779, 511), (503, 400), (524, 541), (781, 491), (506, 398), (681, 458), (778, 506), (959, 645), (750, 559), (649, 587), (690, 677), (503, 377), (495, 456), (618, 521)]
    for v,i in enumerate(pos):
        if v == 12:
            print("Selected Spells")
            click(Unit_Positions['Ainz'][0][0], Unit_Positions['Ainz'][0][1], delay=0.2)
            find = False
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
    click(771,703,delay=0.2)
    while pyautogui.pixelMatchesColor(771,703,expectedRGBColor=(198,158,0),tolerance=8):
        click(771,703,delay=0.2)
        print(pyautogui.pixel(771,703))
        time.sleep(0.4)
    

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
        

    
def main():
    first_run = True
    print("Starting Winter Event Macro")
    rabbit_pos = [(956, 543), (692, 524), (953, 512)]
    speed_pos =  [(851, 531), (892, 534), (932, 536)]
    start_of_run = datetime.now()
    num_runs = 0  
    while True:
        global g_toggle
        global Unit_Placements_Left
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
            global Unit_Placements_Left
            Unit_Placements_Left = Reset_Placements.copy()
            
            print("Starting new match")
            wait_start()
            quick_rts()
            # Set up first 2 rabbits
            directions('1', 'rabbit')
            keyboard.press_and_release('e')
            keyboard.press_and_release('e')
            quick_rts()
            click(835, 226, delay=0.2) # Start Match
            
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
            place_unit('Bunny', rabbit_pos[0], close=True)
            place_unit('Bunny', rabbit_pos[1], close=True)
            
            # get third
            directions('1', 'rabbit')
            keyboard.press_and_release('e')
            quick_rts()
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
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
                click(pos[0], pos[1], delay=0.2)
                keyboard.press_and_release('z')
                time.sleep(0.5)
            click(607, 381, delay=0.2)
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
            # Wait till max money on all speedwagon
            speed_max = [False, False, False]
            while not all(speed_max):
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
                if not g_toggle:
                    break
                for i, pos in enumerate(speed_pos):
                    if speed_max[i] != True:
                        click(pos[0],pos[1],delay=0.2)
                        time.sleep(0.6)
                        if bt.does_exist('Unit_Maxed.png',confidence=0.8,grayscale=True):
                            speed_max[i] = True
                        click(607, 381, delay=0.2)
                time.sleep(1)
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break  
            # Tak's placement + max
            keyboard.press('w')
            time.sleep(0.8)
            keyboard.release('w')
            # Press e untill tak is bought
            while not bt.does_exist('Winter\\Tak_hb.png', confidence=0.7, grayscale=False):
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
                keyboard.press_and_release('e')
                time.sleep(0.2)
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break    
            place_unit("Tak", (853, 604))
            keyboard.press_and_release('z')
            time.sleep(0.5)
            #DIR_NAMICARD
            click(382, 268, delay=0.2, right_click=True) # Goes to nami's card
            while not bt.does_exist('Unit_Maxed.png',confidence=0.8,grayscale=True): # Wait till tak is max
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
                time.sleep(0.5)
            click(607, 381, delay=0.2)
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
            
            #Nami
            while not bt.does_exist('Winter\\Nami_hb.png', confidence=0.7, grayscale=False, region=(528, 788, 749, 860)): # Buys nami's card
                keyboard.press_and_release('e')
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
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
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
                if avM.get_wave()>=19:
                    #DIR_BUYMAINLANES
                    keyboard.press('d')
                    time.sleep(1)
                    keyboard.release('d')
                    keyboard.press_and_release('e')
                    keyboard.press_and_release('e')
                    keyboard.press('w')
                    time.sleep(0.6)
                    keyboard.release('w')
                    keyboard.press_and_release('e')
                    keyboard.press_and_release('e')
                    wave_19=True
                if not g_toggle:
                    break
                time.sleep(0.5)
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
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
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
            upgrader('range')
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
            upgrader('speed')
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
            upgrader('armor')
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
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
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
                if bt.does_exist("Winter\\Full_Bar.png",confidence=0.7,grayscale=True, region=(493, 543, 1024, 785)) or bt.does_exist("Winter\\NO_YEN.png",confidence=0.7,grayscale=True,  region=(493, 543, 1024, 785)):
                    quick_rts()
                    time.sleep(3)
                    place_hotbar_units()
                    directions('3')
                if not Erza_Upgraded:
                    erza_buffer = Unit_Positions['Mage']
                    if Unit_Placements_Left['Mage'] == 0:
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
                    if Unit_Placements_Left['Beni'] == 0:
                        quick_rts()
                        time.sleep(1)
                        for ben in Unit_Positions['Beni']:
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
                    if Unit_Placements_Left['Ainz'] == 0: # Ainz thingy
                        ainzplaced = True
                        quick_rts()
                        time.sleep(1)
                        ainz_pos = Unit_Positions['Ainz']
                        pos = (876, 465)
                        secure_select((ainz_pos[0]))
                        time.sleep(0.5)
                        if USE_WD:
                            ainz_setup(unit="world des")
                        elif USE_DIO:
                            ainz_setup(unit="god")
                        else:
                            ainz_setup(unit=USE_AINZ_UNIT)
                        click(pos[0], pos[1], delay=0.67) # Place world destroyer + auto upgrade
                        time.sleep(0.5)
                        while not pyautogui.pixel(607, 381) == (255,255,255):
                            if g_toggle == False:
                                break
                            click(pos[0], pos[1], delay=0.67)
                            time.sleep(0.5)
                        time.sleep(1)
                        if USE_DIO:
                            ability_clicks = [(648, 448), (1010, 563), (1099, 309)]
                            for p in ability_clicks:
                                click(p[0], p[1], delay=0.2)
                                time.sleep(1.2)
                        if MAX_UPG_AINZ_PLACEMENT:
                            keyboard.press_and_release('z')
                        if MONARCH_AINZ_PLACEMENT:
                            directions('5')
                            buy_monarch()
                            quick_rts()
                            time.sleep(1)
                            click(pos[0], pos[1], delay=0.67) 
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
                for unit in Units_Placeable:
                    if Unit_Placements_Left[unit] > 0:
                        is_done = False
                        print(f"{unit} has {Unit_Placements_Left[unit]} placements left.")
                print("===============================")
                if is_done:
                    gamble_done = True
                time.sleep(0.1)
            print("Gambling done")
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
            # Auto upgrade + Monarch everything else
            
            # set up buffer erza
            
            quick_rts()
            time.sleep(1)
    
            # World destroyer
            if USE_WD:
                secure_select((876, 465))
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
            elif USE_DIO:
                secure_select((876, 465))
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
            elif MAX_UPG_AINZ_PLACEMENT == False:
                secure_select((876, 465))
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
            for ice in Unit_Positions['Rukia']:
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
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
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
                
            for gamer in Unit_Positions['Hero']:
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
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
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
            for kuzan in Unit_Positions['Kuzan']:
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
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
            for esc in Unit_Positions['Escanor']:
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
            
            wave_150 = False
            done_path = False   
            while not wave_150:
                if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                    break
                if avM.get_wave() == 149 and not done_path:       
                    def spam_e():
                        while not done_path:
                            keyboard.press_and_release('e')
                            time.sleep(0.2)
                        print("Done buying lanes")
                    quick_rts()
                    #DIR_BUYRESTLANES
                    keyboard.press('a')
                    time.sleep(0.4)
                    keyboard.release('a')
                    keyboard.press_and_release('v')
                    time.sleep(1)
                    Thread(target=spam_e).start()
                    keyboard.press('w')
                    time.sleep(1.5)
                    keyboard.release("w")
                    time.sleep(1)
                    keyboard.press('w')
                    time.sleep(0.5)
                    keyboard.release("w")
                    keyboard.press('s')
                    time.sleep(2.8)
                    keyboard.release('s')
                    time.sleep(1)
                    keyboard.press('s')
                    time.sleep(1)
                    keyboard.release('s')
                    keyboard.press_and_release('v')
                    quick_rts()
                    time.sleep(2)
                    done_path = True

                    # Buy all other lanes
                    pass
                if avM.get_wave()==150:
                    wave_150 = True
                else:
                    if avM.get_wave()%2==0:
                        repair_barricades()
                        quick_rts()
                time.sleep(2)
            if pyautogui.pixelMatchesColor(690,270,(242,25,28),tolerance=8):
                on_failure()
                break
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
                
                
            ainz_pos = Unit_Positions['Ainz']
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
                time.sleep(1)


main()
