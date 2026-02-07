
---

# Winter-Normal-Macro
An anime vanguards macro for the winter normal LTM mode

# What is this?
This just contains updated versions of the winter event python files so I can release more QOL or updates easier.  
For the rest of the files download from:  
REMOVE THE print(restart_match()) IN AV METHODS (IN THE TOOLS FOLDER)
https://mega.nz/file/CphzFRiR#s5_-7hDLLsRpXCn5DjvZ6p9ZT-V0tVR8_sHXh21uiZM
MAKE SURE TO REPLACE THE OLD FILES IN THAT MEGA FILES WITH THE NEW ONES!!

# Common fixes
When downloading from mega data corruption can happen which can screw up the python executable or the tesseract. You can either try redownloading / unzipping again OR https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0 use the teseract installer to install tesseract (clear the folder first) with a clean version in the folder. You can also add the path to the tesseract (to the directory not the exe) in your PATH (enviromental variable).
For python, you can do a clean install of version 3.13.11 on your device and install these packages: https://pastebin.com/mS2xFd3m

# Recent updates
Added alot more failure detection to reset if it fails. Added CTM flags.  Roblox click to move (built in pathing, good for low-end devices / high ping users)
For `directions('1')` and `directions('2')`, you can add:

```python
directions('1', CTM = True) # or directions('1', 'rabbit', CTM = True) etc
```

to use the click‑to‑move version (good for low‑end / laggy machines).

Added support so you can use whatever unit you want from Caloric Stone.

```python
USE_WD = True          # use World Destroyer
USE_DIO = False        # built‑in DIO thing instead
USE_AINZ_UNIT = ""     # name of the unit

MONARCH_AINZ_PLACEMENT = False   # gets monarch for the unit you place with caloric stone
MAX_UPG_AINZ_PLACEMENT = False   # if True: presses Z for auto-upgrade
                                 # if False: upgrades until it finds a certain move (requires your own picture)

AINZ_PLACEMENT_MOVE_PNG = "Winter\\YOUR_MOVE.png"  
# name the screenshot YOUR_MOVE; it will upgrade the unit until it finds that image
```
