

---

# Winter-Normal-Macro
An anime vanguards macro for the winter normal LTM mode

# What is this?
This just contains updated versions of the winter event.  
For the rest of the files download from:  
https://mega.nz/file/C8p1nSpL#c_jFD9UViHjo4eYiVqW8Ep3nUB5L-e7x-f_rWsivvFA

# Recent updates
Added CTM flags.  
For `directions('1')` and `directions('2')`, you can add:

```python
CTM = True
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

