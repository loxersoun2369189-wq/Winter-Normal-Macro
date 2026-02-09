

---

# Winter-Normal-Macro
An anime vanguards macro for the winter normal LTM mode
- Help guide: https://docs.google.com/document/d/1tDzx0MOSXvXefACTolxSwQxJZxrjvEqqECa1C2PsEs0/edit?tab=t.0

# What is this?
This just contains updated versions of the winter_event.py and the images.  
For the rest of the files download from:  
- [here](https://u.pcloud.link/publink/show?code=XZpt0l5ZkLubXliXPp0FbVB2nK7l4JbJzTRk)
### MAKE SURE TO REMOVE THIS IN Tools\avMethods.py
```
print(reset_match())
```
# Update Guide
https://youtu.be/E6ZZEhlJBC0
# Recent Updates

### Added Wave 140 reset toggle
### Added auto redo path if fail
### Added UI Navigation mode (if the upgrader doesnt work for you turn on)
### Added start button id mode (does image detection instead of pixel)

```python
START_BUTTON_ID = True # If true it uses image detection to search for start button
USE_UI_NAV = True # uses ui navigation for buying upgrades
WAVE_RESTART_150 = False # if false restarts on 140
```
---

## Common Fixes
Mega downloads can occasionally corrupt files, which breaks either **Python** or **Tesseract**.

### Tesseract issues
If Tesseract stops working or the macro can’t detect text:

- Re‑download the files and unzip again, **or**
- Install a clean version of Tesseract from:  
  https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0  
- Clear the old Tesseract folder before installing
- Optionally add the **Tesseract directory** (not the exe) to your system PATH

### Python issues
If Python fails to run or packages are missing:

- Install a clean Python **3.13.11**
- Install the required packages listed here:  
  https://pastebin.com/mS2xFd3m

---
